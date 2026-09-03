import os
from groq import Groq
from config import LLM_MODEL, N_RESULTS
from retriever import retrieve

# Initialize the Groq client using the API key from your .env field
_groq_client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# The exact phrase the model is instructed to use when the context falls short.
# Defined once so the prompt and the refusal check can never drift apart.
REFUSAL_PHRASE = "I don't have enough information on that."


def _is_refusal(answer):
    """
    True if the model declined to answer entirely. Chroma always returns the top N
    nearest chunks no matter how weak the match, so a refusal still arrives with
    sources attached — we detect it here and drop them rather than cite documents
    that did not support an answer.

    Anchored to the start of the answer, not a substring search: a partial answer
    that mentions the phrase somewhere in its body is a real answer and must keep
    its sources.
    """
    # Normalize curly apostrophes, which the model sometimes emits instead of ASCII '
    normalized = answer.replace("’", "'").strip().lstrip("*#> ").lower()
    return normalized.startswith("i don't have enough information")


def generate_answer(query):
    """
    Given a user query, retrieve relevant chunks, format them into a strict 
    grounding prompt, and call the Groq LLM to generate an answer with source attribution.
    """
    # 1. Fetch relevant chunks using our semantic retriever
    retrieved_chunks = retrieve(query, n_results=N_RESULTS)

    # 2. Handle edge case: empty database or no matching chunks
    if not retrieved_chunks:
        return {
            "answer": REFUSAL_PHRASE,
            "sources": []
        }

    # 3. Format the retrieved text and collect unique sources for attribution
    context_blocks = []
    sources = set()
    
    for chunk in retrieved_chunks:
        context_blocks.append(f"Content: {chunk['text']}\nSource: {chunk['source']}")
        sources.add(chunk['source'])

    combined_context = "\n\n---\n\n".join(context_blocks)

    # 4. Construct a strict system prompt enforcing grounding & refusals
    system_prompt = (
        "You are an expert technical assistant providing answers based *only* on the provided documents. "
        "Your task is to answer the user's question using the provided context. "
        "Strictly adhere to the following rules:\n"
        "1. Use *only* the information contained in the provided context chunks.\n"
        "2. Do not use any outside knowledge or general assumptions. In particular, do not "
        "generalize instructions written for a different firearm type into instructions for "
        "the one being asked about, and do not fill gaps in a procedure by inference.\n"
        f"3. If the context cannot answer the question at all, reply with exactly "
        f"'{REFUSAL_PHRASE}' and nothing else. Use that phrase ONLY for a complete refusal. "
        "If the context answers part of the question, answer that part and plainly state "
        "which part the documents do not cover — without using the refusal phrase.\n"
        "4. Draw on every provided chunk that bears on the question, including informal "
        "sources such as forum discussions — they often contain practical caveats the "
        "formal guides omit.\n"
        "5. Include relevant warnings and 'do not do this' guidance *that appear in the "
        "context*, not just affirmative steps. Never invent a caution, step, or tip that "
        "is not stated in the chunks — rule 1 outranks this one.\n"
        "6. Be clear and well-organized. Completeness means covering what the context "
        "actually says, not padding the answer to look thorough."
    )

    user_prompt = (
        f"Context information:\n{combined_context}\n\n"
        f"User Question: {query}"
    )

    try:
        # 5. Call the Groq API using LLM_MODEL from config.py
        completion = _groq_client.chat.completions.create(
            model=LLM_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.1,  # Low temperature minimizes hallucinations
        )
        
        answer = completion.choices[0].message.content
        return {
            "answer": answer,
            # Suppress attribution on a refusal — nothing was actually used
            "sources": [] if _is_refusal(answer) else list(sources)
        }

    except Exception as e:
        print(f"Error calling Groq API: {e}")
        return {
            "answer": f"An error occurred while generating the response: {str(e)}",
            "sources": []
        }