# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->
Unofficial Guide to Striker-Fired Handgun Cleaning
This domain covers the community consensus on cleaning and lubricating striker-fired handguns. It provides valuable real-world context that manufacturer manuals omit, including the practical differences between cleaning solvents and specific advice on avoiding over-lubrication.
---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 |https://gunmagwarehouse.com/blog/beginners-guide-to-cleaning-and-maintaining-a-striker-fired-handgun/ |Step-by-step field strip and brush recommendations | |
| 2 | https://shoot-on.com/pistol-cleaning-fundamentals/|Detailed breakdown of using dedicated solvents and jags vs. loops. | |
| 3 | https://www.optics-trade.eu/blog/how-to-clean-your-glock-a-step-by-step-cleaning-guide/| Breakdown of specific cleaning points and avoiding aggressive solvent damage.| |
| 4 | https://americanhandgunner.com/gear/lubing-your-glock-in-3-2-1-easy-steps/| The community standard "3-2-1" oiling method.| |
| 5 |https://us.glock.com/en/owners-resources/education/caring-for-your-pistol | The official manufacturer baseline for lubrication points to contrast with community opinions.| |
| 6 |https://www.reddit.com/r/Glocks/comments/e045wk/how_to_keep_your_striker_channel_clean/?solution=dd1a6f426803d74edd1a6f426803d74e&js_challenge=1&jsc_token=7afd7253fec22262ff1c52b1703fe9ecacea58ccda7d70baeede7d4776bd460d&jsc_orig_r= |community knowledge on why you should never put oil in a striker channel and how to remove carbon buildup safely.| |
| 7 |https://www.reddit.com/r/guns/comments/cimu89/is_clp_all_i_need/ | Discussions on how high round counts dictate whether CLP is sufficient.| |
| 8 |https://seal1.com/blogs/news/gun-maintenance-schedule | Basic intervals for when cleaning is necessary based on range visits.| |
| 9 | https://www.reddit.com/r/guns/comments/1tjlxhe/gun_oil_cleaner_or_clp/| Community debate on using CLP (Clean, Lube, Protect) versus dedicated oils and heavy copper solvents.| |
| 10 | https://www.thehighroad.org/index.php?threads/gun-cleaning-field-vs-detail-stripping.359967/| forum thread detailing exactly when a standard field strip is enough versus when a complete detail strip/deep clean is required.| |

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:** 800 characters

**Overlap:** 150 characters

**Reasoning:** These numbers fit my documents because my corpus consists of detailed procedural guides and multi-paragraph forum debates about handgun maintenance. A chunk size of 800 characters is large enough to capture a complete step-by-step instruction or a full forum comment without diluting the specific topic. The 150-character overlap ensures that context is not lost if a step spans across a boundary. If my chunks were too small, retrieval would return useless fragments lacking context. If they were too large, the embeddings would become diluted with multiple unrelated cleaning steps, making precise retrieval difficult.

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:** sentence-transformers/all-MiniLM-L6-v2

**Top-k:** k = 4

**Production tradeoff reflection:** If deploying this system at production scale without cost constraints, several tradeoffs would be considered:
  - Context Window & Chunk Capacity: Larger embedding models (such as `text-embedding-3-large` or `bge-large-en-v1.5`) support longer chunk windows and denser vector representations, preserving broader semantic relationships at the cost of higher compute latency and storage.
  - Domain-Specific Terminology: Technical firearms terminology (e.g., "sear", "striker sleeve", "CLP", "extractor depressor plunger") benefits from specialized or fine-tuned embedding models rather than generic open-domain models.
  - Local vs. API Hosted: A local embedding model guarantees predictable zero-cost scaling and data privacy, whereas an API-hosted model offloads GPU infrastructure management at the cost of network latency and per-token charges.

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 |Where should oil NEVER be placed when cleaning a striker-fired handgun? | Expected Answer: Oil should never be applied inside the firing pin / striker channel. It must remain completely dry because oil attracts unburnt powder and carbon, causing light primer strikes.|
| 2 | What is the main community tradeoff between using a CLP product versus a dedicated bore solvent?| Expected Answer: CLP is convenient as an all-in-one cleaner, lubricant, and protectant for routine light cleaning, but dedicated bore solvents are significantly more effective at stripping heavy carbon, lead, and copper fouling after high round counts.|
| 3 | How many drops of oil are typically recommended for lubricating the slide rails of a Glock or similar striker-fired pistol?| Expected Answer: Exactly one drop of oil per slide rail groove (or one drop spread across both rail cuts), keeping lubrication minimal to avoid collecting debris.|
| 4 | Under what conditions is a full detail strip recommended instead of a routine field strip?| Expected Answer: A full detail strip is generally recommended only after thousands of rounds (5000–10,000 rounds), after dropping the firearm in water, mud, or sand, or when addressing internal mechanical malfunction.|
| 5 | What is the exact torque specification for mounting a red dot optic to an MOS slide plate?| Expected Answer: Refusal / "I do not have enough information in the provided documents to answer that question" (verifies that the LLM does not hallucinate specs not present in the cleaning corpus).|

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. Reddit and forum sources often contain signatures, upvote strings, emojis, formatting tags, and off-topic banter. If not cleaned properly, this noise degrades embedding quality and misleads vector search.

2. If document filenames or URLs are not rigidly bound to each chunk during ingestion, source citations in Milestone 5 will fail or attribute statements to the wrong source.



---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->
```mermaid
flowchart LR
    A[Raw Web / Forum Documents] --> B[Document Ingestion & Cleaning]
    B --> C[Fixed-Size Chunking<br/>800 chars / 150 overlap]
    C --> D[Embedding Model<br/>all-MiniLM-L6-v2]
    D --> E[(ChromaDB Vector Store)]
    F[User Query] --> G[Semantic Retrieval<br/>Top-k = 4]
    E --> G
    G --> H[Prompt Assembly with Grounding Constraints]
    H --> I[LLM Generation<br/>openai/gpt-oss-120b]
    I --> J[Grounded Response + Source Citations]

---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:** I will provide Gemini with the Documents and Chunking Strategy sections of this spec, along with raw document samples, and direct it to write a Python ingestion script using re and standard file operations to clean boilerplate text and split content into 800-character chunks with 150-character overlap.

**Milestone 4 — Embedding and retrieval:** I will feed the Retrieval Approach section and vector store requirements to Gemini to implement the ChromaDB collection creation, all-MiniLM-L6-v2 embedding generation, and a retrieval function returning top_k=4 chunks with full source metadata and distance scores.

**Milestone 5 — Generation and interface:**
I will provide Gemini with my strict grounding prompt specification, instruction to use the openai/gpt-oss-120b endpoint, and Gradio template requirements to build app.py. I will manually audit the generated code to ensure source attribution is appended programmatically rather than left to model discretion.