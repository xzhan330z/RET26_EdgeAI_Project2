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


### Wednesday Jun 24 — Full Day (9:00 AM – 12:00 PM + 1:00 PM – 4:00 PM)


#### Task: Model Scale Reality Check — Measuring What "7 Billion Parameters" Actually Means

**Concept:** The numbers in AI headlines (0.5B, 7B parameters) are abstract until you measure what they cost in RAM, time, and disk space on real hardware.

**Morning Block (9:00 AM – 12:00 PM)**

**Part 1 — Hardware Profiling (90 min)**

1. Before running anything, open Task Manager / Activity Monitor / `htop`. Screenshot baseline RAM and CPU. Label "Baseline — Nothing Running."
2. Open VS Code. Screenshot again. Label "With Editor Open."
3. Run `python edge_draft.py`. While it loads, screenshot. Label "During Model Load." The moment it finishes printing, screenshot again. Label "Post-Inference." You now have 4 screenshots at 4 distinct moments.
4. Extract RAM values from all 4 screenshots into this hand-written table:

| State | RAM Used (GB) | CPU % | Notes |
|---|---|---|---|
| Baseline | | | |
| Editor Open | | | |
| During Load | | | |
| Post-Inference | | | |

5. Calculate by hand: how much RAM did the 0.5B model consume at peak? (Post-Inference minus Baseline.) Show subtraction on paper.

**Part 2 — Spec Sheet Research (90 min)**

6. Go to the Hugging Face model card for `Qwen/Qwen2.5-0.5B-Instruct`. Without using AI, find and record: number of parameters (exact), total disk size (sum the `.safetensors` files on the Files tab), architecture type, context window length, and training data cutoff. Record the URL for each finding.
7. Do the same for `Qwen/Qwen2.5-7B-Instruct`.
8. Build a comparison table on paper (both models side by side). Add a third column: the ratio (7B ÷ 0.5B) for each row. Calculate all ratios by hand. Show arithmetic.

**Afternoon Block (1:00 PM – 4:00 PM)**

**Part 3 — Physical Analogy Poster (90 min)**

9. On a sheet of paper or white board, create a poster that a school principal could read and understand. It must contain:
   - Side-by-side scale drawings of both models (make the 7B model visually 14× larger in area — calculate the correct dimensions and show that calculation on the poster)
   - Your actual RAM measurements from Part 1, integrated into the diagram
   - Your ratio calculations from Part 2 displayed prominently
   - One real-world size analogy of your own invention for each model (not from the build guide)
   - One sentence at the bottom explaining why this size difference matters for classrooms
   Photograph your poster.

**Part 4 — Discussion Questions and Peer Critique (90 min)**

10. Write 5 discussion questions about model size and edge AI limitations suitable for the grade level you teach. For each question, also write: the expected student response, a common wrong answer you anticipate, and a follow-up question to redirect the wrong answer.
11. Exchange your 5 questions with a partner who teaches a different grade level. Your partner answers your questions as if they were a student (written answers). You read their answers and write a 3-sentence response: did their answers reveal misunderstandings you did not anticipate? What would you change?

**Oral Check-in (3:30 PM):** Point to any number on your poster and explain exactly where it came from — which screenshot, which calculation.

**Deliverable Checklist:**
- [ ] 4 labeled hardware screenshots
- [ ] Hand-written RAM/CPU table with subtraction shown (photographed)
- [ ] Spec comparison table with ratios calculated by hand (photographed)
- [ ] Hand-made poster with scale calculation shown (photographed)
- [ ] 5 discussion questions with expected answers, wrong answers, follow-ups (typed)
- [ ] Partner's written student-role answers + your 3-sentence response

---




### Thursday Jun 25 — Morning (9:00 AM – 12:00 PM)
**Slot: Progress report ✅ — TASK ASSIGNED**

#### Task: Latency Laboratory — Rigorous Timing on Real Hardware *(Part 1 of 2)*

**Concept:** Performance is not a single number — it is a distribution with variance and environmental dependencies. Today you run a proper timing experiment under two conditions and begin your statistical analysis.

**Part 1 — Controlled Timing Experiment, Condition A: Normal Load (60 min)**

Keep all your usual applications open (browser with multiple tabs, editor, background apps). This is "Condition A."

1. Run `edge_draft.py` 20 times. Before each run, write the run number and current time in a hand-written log. Use a physical stopwatch: start when you press Enter, stop when the last token ID appears. Record to the nearest tenth of a second. If you missed the timing on a run, mark it void and repeat.
2. After 20 runs, circle any outliers (runs that took more than 2× the typical time). Note beside each what was happening on screen at that moment.

**Part 2 — Condition B: Minimal Load (60 min)**

3. Close every application except the terminal. Disable WiFi. This is "Condition B." Repeat the exact same 20-run experiment. Record in a separate hand-written log.

**Part 3 — Statistical Analysis by Hand (60 min)**

4. For Condition A, order your 20 measurements smallest to largest on a new sheet of paper.
5. Calculate for Condition A (show all arithmetic):
   - Mean, Median, Minimum, Maximum, Range
   - Standard deviation: √(Σ(xᵢ − mean)² / n) — calculate every term individually on paper
6. Calculate the same 5 statistics for Condition B. Show all arithmetic.
7. Draw a hand-made stem-and-leaf plot for Condition A. Label stems and leaves correctly.

**Oral Check-in (end of morning):** Explain your standard deviation calculation for Condition A by pointing to the arithmetic on your paper.

**Deliverable Checklist:**
- [ ] Hand-written timing log for Condition A (20 runs, circled outliers with notes)
- [ ] Hand-written timing log for Condition B (20 runs)
- [ ] Full statistical calculations for both conditions (paper, photographed)
- [ ] Hand-drawn stem-and-leaf plot for Condition A (photographed)

---

### Thursday Jun 25 — Afternoon (1:00 PM – 4:00 PM)
**Slot: Research work ✅ — TASK ASSIGNED**

#### Task: Latency Laboratory — Graphing, Analysis, and Peer Comparison *(Part 2 of 2, continues Jun 25 Morning)*

**This session requires your two timing logs and statistical calculations from this morning.**

**Part 4 — Comparative Graphing (60 min)**

1. On a single sheet of graph paper, draw two overlapping box-and-whisker plots — one for Condition A and one for Condition B. Label every component: minimum whisker, Q1, median line, Q3, maximum whisker, and outlier dots. Use different colors or patterns to distinguish the two.

**Part 5 — Written Analysis (90 min)**

2. Write a typed analysis paragraph (200–250 words) that must include:
   - Your actual mean and standard deviation for both conditions (use your numbers from this morning)
   - Whether the difference between conditions is meaningful or within noise (your judgment, justified)
   - One sentence explaining what "variance" means for a classroom AI tool that students are waiting on
   - One prediction: if 30 students all ran this simultaneously on the same network, what would happen to the distribution and why?
   This paragraph cannot be written without your specific numbers. Word count at bottom.
3. Write a second paragraph (100–150 words) predicting what the distribution would look like on: (a) a 5-year-old budget laptop, (b) a new MacBook Pro M3. Ground your prediction in the RAM and CPU specs you researched on Jun 24. Reference that data explicitly ("From my Jun 24 spec table…").

**Part 6 — Peer Data Comparison (30 min)**

4. Find a partner with different hardware. Share your mean and standard deviation only (not your raw data). Together, calculate the difference in means and discuss: how many extra seconds per inference does the slower machine add? Write a 4-sentence joint conclusion that you both sign.

**Oral Check-in (3:30 PM):** The mentor picks one number from your box-and-whisker plot and asks where it came from in your raw data.

**Deliverable Checklist:**
- [ ] Hand-drawn dual box-and-whisker plot (labeled, both conditions) (photographed)
- [ ] Typed analysis paragraph (200–250 words, word count at bottom)
- [ ] Typed prediction paragraph referencing Jun 24 spec data (100–150 words)
- [ ] Jointly signed 4-sentence peer comparison conclusion

---