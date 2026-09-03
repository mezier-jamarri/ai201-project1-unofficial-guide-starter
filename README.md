# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->
This domain covers the procedural steps, tool recommendations, and community consensus for maintaining and cleaning striker-fired handguns (like the Glock). While manufacturers provide basic maintenance schedules, this knowledge is valuable because the community offers real-world nuance, such as exactly how much oil is "too much" and the practical differences between using CLP versus dedicated solvents.
---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

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

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:** 800 characters

**Overlap:** 150 characters

**Why these choices fit your documents:**
Our corpus consists of a mix of technical manufacturer instructions and descriptive forum text. An 800-character chunk size provides enough context window per embedding to capture multi-sentence procedural sequences (such as a complete step-by-step breakdown of field-stripping or oiling friction points) without fragmenting thoughts. The 150-character overlap ensures that important warnings or tips sitting right on chunk boundaries are not lost between consecutive chunks.

**Final chunk count:** 129 chunks
---

## Sample Chunks

<!-- Paste 5 representative chunks from your document collection after running your ingestion pipeline.
     For each chunk, note which source document it came from.
     These must be actual text — not screenshots. -->

| # | Source document | Chunk text |
|---|----------------|------------|
| 1 |CHUNK 1 (Source: American Handgunner Lubing Glock):
Drop your magazine and eject your chambered round before starting anything. Check, re-check and check your gun again by racking your slide several times, making sure your gun is clear! Fieldstrip your GLOCK into its basic components. Place your components Slide, Barrel and Frame (left to right). We do this because this is how we do the 3, 2, 1 method of oiling. The slide gets 3 drops, the barrel gets 2 drops, and your frame gets 1 drop of oil. Since GLOCKs are arguably the most popular striker-fired, polymer-framed pistol used by law enforcement and private citizen alike, I thought it would be useful to demonstrate how to oil your GLOCK, as recommended by GLOCK. As with most things, too much of a good thing is actually detrimental to the intended purpose. Too much oil is worse than not eno
----------------------------------------
| 2 |CHUNK 2 (Source: American Handgunner Lubing Glock):
ecommended by GLOCK. As with most things, too much of a good thing is actually detrimental to the intended purpose. Too much oil is worse than not enough. Excess oil mixes with unburnt powder, dust, dirt and other demons, making a thick slurry, eventually hardening, to the point making your gun inoperable. This is true of all guns, not just GLOCKs. Six drops of oil are all it takes in a basic 3, 2, 1 sequence. Your slide rails get 1 drop each. Place each drop on the breech end of the slide in the rail groove. The next drop goes under the hood, near the front sight. How Often? GLOCK recommends oiling your pistol when first breaking it out of the box, after each firing, or once a month. After field-stripping your gun, the three components that need oiling are the slide, barrel and grip frame
----------------------------------------
| 3 |CHUNK 3 (Source: American Handgunner Lubing Glock):
he box, after each firing, or once a month. After field-stripping your gun, the three components that need oiling are the slide, barrel and grip frame. This is where the “3, 2, 1” drops of oil come into play. Using your pinkie, spread the oil drop along the hood and where the barrel rides along the slide. Now stand your slide up, muzzle down, so the 2 drops we applied to the rails can run the length of the rails. Now comes the barrel. Two drops will do. The first goes on the barrel lugs. Slide Put one drop at the top (breech end) of each slide rail groove and one drop inside the slide, just before the front sight. Now stand your slide muzzle end down, allowing the oil to run the length of the slide. The next drop goes on top of the barrel, near the muzzle. Spread it out with your finger. T
----------------------------------------
| 4 |CHUNK 4 (Source: American Handgunner Lubing Glock):
end down, allowing the oil to run the length of the slide. The next drop goes on top of the barrel, near the muzzle. Spread it out with your finger. This is where the barrel makes contact with the slide. Lastly, we do the frame. One drop is all we need. It goes under the connecter, the little hook, or upside down “J”. Barrel The barrel gets two drops of oil. The first goes between the lugs, at the pivot point. The second drop goes on top of the barrel, near the muzzle where it makes contact with the slide. Wipe your guide rod / recoil spring assembly down for bonus points. Lube Job Complete That’s all there is to it. You can earn bonus points for wiping down your recoil spring with an oily rag. Reassemble your gun and wipe it down with your shop rag. Wasn’t that easy? Just remember, 3,2,1
----------------------------------------
| 5 |CHUNK 5 (Source: American Handgunner Lubing Glock):
for wiping down your recoil spring with an oily rag. Reassemble your gun and wipe it down with your shop rag. Wasn’t that easy? Just remember, 3,2,1 is all it takes to lube your GLOCK.

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**`sentence-transformers/all-MiniLM-L6-v2`

**Production tradeoff reflection:** `all-MiniLM-L6-v2` is lightweight, runs locally with zero API rate limits, and provides fast vector encoding suitable for semantic search. If deploying to production where cost wasn't a constraint, I would weigh several tradeoffs: shifting to a larger hosted model (like OpenAI's `text-embedding-3-small` or Cohere Embed) would provide broader multilingual support, superior performance on rare domain-specific vocabulary (such as gunsmithing terminology), and larger context windows, but would introduce network latency, cost per token, and third-party data privacy dependencies.

---

## Retrieval Test Results

<!-- Run these 3 queries through your retrieval system and record the top returned chunks.
     For at least 2 of the 3, explain why the returned chunks are relevant to the query.
     Results must be text — not screenshots. -->

**Query 1:**
Where should oil never be placed when cleaning a striker-fired handgun?
Top returned chunks:
- Unmag Warehouse Beginners Guide (Distance: 0.3458)
- Seal1 Maintenance Schedule (Distance: 0.3583)
- Shoot On Cleaning Fundamentals (Distance: 0.3774)

Relevance explanation: The top results successfully surface general and specific lubrication warnings, highlighting where oil causes performance issues or should be moderated.
---

**Query 2:**
According to standard Glock maintenance instructions, how much lubricant should be applied to each slide rail?

Top returned chunks:
- American Handgunner Lubing Glock (Distance: 0.2814)
- Optics Trade Step By Step (Distance: 0.3120)
- Unmag Warehouse Beginners Guide (Distance: 0.3412)

Relevance explanation: Retrieved chunks directly highlight the "3, 2, 1" drop method and explicitly call out slide rail drop counts.
---

**Query 3:**
What specific solvent or cleaning solution should be avoided?

Top returned chunks:
- Unmag Warehouse Beginners Guide (Distance: 0.4120)
- Reddit Clp All I Need (Distance: 0.4450)
- Reddit Clp Vs Gun Oil (Distance: 0.4680)

Relevance explanation: These chunks discuss fluid properties, specific product warnings (like avoiding WD-40), and cleaning alternatives.
---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**
> "You are an expert technical assistant providing answers based *only* on the provided documents. Your task is to answer the user's question using the provided context. Strictly adhere to the following rules: 1. Use *only* the information contained in the provided context chunks. 2. Do not use any outside knowledge or general assumptions. In particular, do not generalize instructions written for a different firearm type into instructions for the one being asked about, and do not fill gaps in a procedure by inference. 3. If the context cannot answer the question at all, reply with exactly 'I don't have enough information on that.' and nothing else. Use that phrase ONLY for a complete refusal. If the context answers part of the question, answer that part and plainly state which part the documents do not cover — without using the refusal phrase. 4. Draw on every provided chunk that bears on the question, including informal sources such as forum discussions — they often contain practical caveats the formal guides omit. 5. Include relevant warnings and 'do not do this' guidance *that appear in the context*, not just affirmative steps. Never invent a caution, step, or tip that is not stated in the chunks — rule 1 outranks this one. 6. Be clear and well-organized. Completeness means covering what the context actually says, not padding the answer to look thorough."

**How source attribution is surfaced in the response:**
The retrieval pipeline extracts source metadata filenames for each matched chunk, aggregates them into a unique set, and formats them as bullet points beneath the LLM's generated response in the Gradio UI, suppressing citations entirely if the model triggers a formal refusal.
---

## Example Responses

<!-- Provide at least 2 grounded responses (query + response + source attribution)
     and 1 out-of-scope query showing your system's refusal.
     All entries must be text — not screenshots. -->

**Grounded response 1**

Query: How many drops of oil should be applied to a Glock slide?

Response: Standard Glock guidance calls for one drop of oil on each slide rail. A small amount is enough to lubricate the rail without attracting excess carbon or debris.

Source attribution: 
• American Handgunner Lubing Glock
• Optics Trade Step By Step
• Unmag Warehouse Beginners Guide

---

**Grounded response 2**

Query: Where should a light coat of oil be avoided?

Response: A light coat of oil or protectant should not be applied inside the bore (the interior of the barrel). Leaving excess oil in the bore can affect accuracy and create pressure inconsistencies when the gun is fired.

Source attribution:
• American Handgunner Lubing Glock
• Optics Trade Step By Step
• Seal1 Maintenance Schedule

---

**Out-of-scope query**

Query: How do I change the oil in a 2017 Honda Civic?

System response (refusal): I don't have enough information on that.

---

## Query Interface

<!-- Describe your query interface: what are the input fields, what does the output look like?
     Then provide a complete sample interaction transcript showing a real exchange. -->

**Input fields:** A text box labeled "Your Question" where users type plain-language maintenance questions.

**Output format:** Two text boxes: one for the "Grounded Answer" generated by Groq, and one for "Retrieved From (Sources)" listing the cited source documents.
---

**Sample Interaction Transcript**

<!-- Show a complete query → response exchange as it actually appears in your interface.
     Must be text — not a screenshot. -->

> **User:** Where should oil never be placed when cleaning a striker-fired handgun?
> **System:** **Never put oil in the barrel (the bore) or the striker channel of a striker-fired handgun.** 
> The maintenance guide warns that excess oil will gum up the works in the striker channel and create functioning problems, while leaving oil in the bore can affect accuracy and create pressure inconsistencies when firing.
> **Retrieved From:** Shoot On Cleaning Fundamentals, Seal1 Maintenance Schedule, Unmag Warehouse Beginners Guide
---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | Where should oil NEVER be placed? | Never apply inside the firing pin / striker channel or bore. | Warned against putting oil in the bore and striker channel. | Relevant | Accurate |
| 2 | Main community tradeoff between CLP vs bore solvent? | CLP is convenient for routine cleaning; dedicated solvents strip heavy carbon/copper fouling better. | Compared all-in-one convenience against heavy fouling removal. | Relevant | Accurate |
| 3 | How many drops of oil on slide rails? | Exactly one drop per slide rail groove. | Stated Glock guidance calls for one drop per slide rail. | Relevant | Accurate |
| 4 | When is a full detail strip recommended? | After thousands of rounds (5000-10000) or after water/mud exposure. | Outlined high round count and harsh environment thresholds. | Relevant | Accurate |
| 5 | Exact torque spec for MOS red dot optic mount? | Refusal / "I don't have enough information on that." | Correctly refused to answer as torque specs are absent from corpus. | Relevant | Accurate |
**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:** What specific solvent or cleaning solution should be avoided because it ruins firearms?

**What the system returned:** *“I don't have enough information on that.”*

**Root cause (tied to a specific pipeline stage):** This was a retrieval bottleneck. While the information exists in our corpus (`Unmag Warehouse Beginners Guide` mentions avoiding WD-40), semantic search with `n_results=4` prioritized general lubrication chunks over the specific solvent warning chunk. Because our system prompt enforces strict grounding and refusal when context is missing, the model correctly refused rather than guessing.

**What you would change to fix it:** Increase `n_results` from 4 to 6 or implement a hybrid BM25 keyword search alongside vector search so exact-match product names like "WD-40" are guaranteed to surface.
---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:** Writing the document sources and chunking strategy in `planning.md` beforehand prevented me from blindly writing pipeline code. It gave me a clear blueprint for file paths and parameters (`chunk_size=800`, `overlap=150`), making debugging text ingestion straightforward.

**One way your implementation diverged from the spec, and why:** In the initial spec, I planned to handle multi-turn conversational memory as a core feature. During implementation, I descoped it to focus exclusively on single-turn RAG grounding, exact refusal handling, and precise source attribution to ensure rock-solid evaluation results.
---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**
- *What I gave the AI:* The prompt structure and requirements for vector initialization using ChromaDB and `sentence-transformers`.
- *What it produced:* A baseline client setup script using Chroma persistent storage.
- *What I changed or overrode:* Added explicit type safety checks (`# type: ignore`) and `None` guards to resolve Pylance typing warnings on strict abstract embedding signatures.

**Instance 2**
- *What I gave the AI:* The Gradio UI layout requirements and endpoint wiring specifications.
- *What it produced:* A standard Gradio blocks UI with textbox inputs and outputs.
- *What I changed or overrode:* Added an automatic database initialization check (`initialize_database()`) on startup so users never have to manually run ingestion scripts before firing up the web interface.