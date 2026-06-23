# NSF RET 2026 — Daily Lab Tasks

 Tasks are layered and chained — later steps depend on data produced in earlier steps, so you cannot skip ahead or fabricate results.

> **Non-negotiable ground rule:**
> - You can take help from your mentor, the internet, LLMs, or any resource, but you must fully understand what you are doing and how it works; you must be able to explain the diagrams and any work you do in the lab (no copy-pasting tasks or code without understanding).

---

## WEEK 2 — Research & Curriculum · Jun 22–26

---

### Monday Jun 22 — Morning (9:00 AM – 12:00 PM)
**Slot: Research work ✅ — TASK ASSIGNED**

#### Task: Token ID Deep Dive — From Text to Numbers and Back *(Part 1 of 2)*

**Concept:** Tokenization is the foundation of everything the model sees. Before you can understand why speculative decoding works or fails, you must understand how words become integers.

**Part 1 — Run and Record Your Baseline (60 min)**

1. Run `python edge_draft.py` using the default prompt. Write the 5 token IDs it prints into a hand-written log. Label this "Run 1 — Default Prompt."
2. Change the prompt to a sentence from your own classroom subject (a vocabulary term your students struggle with, a math word problem, a science concept). Run the script again. Record the token IDs. Label "Run 2 — My Prompt."
3. Run your custom prompt a third time immediately. Are the token IDs identical to Run 2? Record the answer and explain in one sentence why they are or are not deterministic at the draft stage.
4. Open the Hugging Face tokenizer playground in a browser. Select `Qwen/Qwen2.5-0.5B-Instruct`. Type your Run 2 prompt character by character — do not paste. Screenshot the token display after every 5 characters. You should have at least 4 intermediate screenshots. Label each with the character count at that point.

**Part 2 — Token Anatomy Table (60 min)**

5. For each of the 5 token IDs from Run 2, look them up individually in the tokenizer playground. Fill this table entirely by hand on paper — every cell must be filled:

| # | Token ID | Token Text (exact) | Char Count | Whole word? (Y/N) | Leading space? (Y/N) | Why did the tokenizer split here? |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |

6. Pick one token that surprised you. Change just that one word in your prompt and re-run. Did surrounding token IDs change even though you only changed one word? Record before-and-after IDs for all 5 positions and describe what you observe in 2 sentences.

**Part 3 — Substitution Experiment (60 min)**

7. Choose 5 forms of the same root word from your subject (e.g., "run / running / ran / runner / runs"). Look up each token ID in the playground. Hand-draw a tree diagram connecting the root to its variants with their token IDs labeled on each branch.
8. Tokenize the numbers "1", "10", "100", "1000", "10000" individually. Record their token IDs in a hand-drawn table. Are numbers single tokens or split?

**Deliverable Checklist (submit to shared folder before noon):**
- [ ] Hand-written run log (Run 1, Run 2, Run 3)
- [ ] 4+ intermediate tokenizer screenshots labeled with character counts
- [ ] Completed token anatomy table (paper, photographed)
- [ ] Before/after token comparison (2 sentences)
- [ ] Hand-drawn word-variant tree diagram (photographed)
- [ ] Hand-drawn number tokenization table (photographed)

---

### Monday Jun 22 — Afternoon (1:00 PM – 4:00 PM)
**Slot: Curriculum development with Dr. Chen ❌ — NO TASK ASSIGNED**

> This slot is reserved for curriculum development with Dr. Lily Chen. Attend that session.

---

### Tuesday Jun 23 — Morning (9:00 AM – 12:00 PM)
**Slot: Research work ✅ — TASK ASSIGNED**

#### Task: Token ID Deep Dive — Teach It Back *(Part 2 of 2, continues Jun 22 Morning)*

**This session requires your token anatomy table and tree diagram from yesterday morning.**

**Part 4 — Write the Explainer Sheet (75 min)**

1. Produce a one-page hand-written "Explainer Sheet" that you could give to a student who has never heard of tokenization. It must include:
   - A definition in your own words (no copying from the guide)
   - Your tree diagram from yesterday integrated as an illustration
   - One everyday-life analogy not from the build guide
   - Three "gotcha" facts that would surprise a student, each supported by a specific token ID you found yesterday

**Part 5 — Write the Teaching Paragraph (45 min)**

2. Write a typed paragraph (6–8 sentences) answering: *If you were teaching this to a 10th grader, how would you explain why "playing" and "play" might be different token IDs?* This paragraph must reference at least 2 specific token IDs from your own experiments — it cannot be written without your data from yesterday.

**Part 6 — Peer Exchange (60 min)**

3. Exchange your explainer sheet with a partner. Your partner reads it and writes — on a separate sheet — exactly 3 questions a curious student would still have after reading. Partner signs and dates the question sheet. You answer each question in writing (2–3 sentences per answer). Return both sheets.

**Oral Check-in (end of morning):** Show your token anatomy table. Explain why one specific split surprised you.

**Deliverable Checklist:**
- [ ] Hand-written explainer sheet with integrated tree diagram (photographed)
- [ ] Typed paragraph (6–8 sentences, citing 2 specific token IDs, word count at bottom)
- [ ] Partner's signed question sheet + your typed answers

---

### Tuesday Jun 23 — Afternoon (1:00 PM – 4:00 PM)
**Slot: Curriculum development with Dr. Chen ❌ — NO TASK ASSIGNED**

> This slot is reserved for curriculum development with Dr. Lily Chen. Attend that session.

---