# NSF RET 2026 — Daily Lab Deep-Dive Tasks

**Purpose:** These tasks are assigned into every **"Research work"** and **"Progress report"** slot in the official program schedule. Slots occupied by Dr. Chen's curriculum sessions, poster work, or microteaching preparation are marked clearly — no task is assigned to those slots. Every task is designed to fill its allocated slot (a half-day = ~3 hours, a full-day double slot = ~5–6 hours of active work). Tasks are layered and chained — later steps depend on data produced in earlier steps, so you cannot skip ahead or fabricate results.

> **Non-negotiable ground rules:**
> - Every written deliverable must cite your own measured numbers from that session. Writing without specific data will not be accepted.
> - Hand-drawn artifacts (diagrams, charts, tables) must be photographed and submitted. Typed substitutes are not accepted for hand-drawn items.
> - All peer-review items require the reviewer's **handwritten signature and the time of review**. Unsigned reviews are void.
> - Word counts are mandatory where specified. Write the count at the bottom of the document.
> - A **5-minute oral check-in** with the lab mentor occurs at the end of each afternoon session. You must be able to explain any number or diagram you produced. If you cannot, the deliverable does not count.

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
**Both slots: Research work ✅ — TASK ASSIGNED (full day)**

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

9. On a large sheet of paper (minimum A3 / 11×17 in), create a poster a school principal could read and understand. It must contain:
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
- [ ] Hand-made poster with scale calculation shown (photographed, min A3)
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

### Friday Jun 26 — Morning (9:00 AM – 12:00 PM)
**Slot: Research work ✅ — TASK ASSIGNED**

#### Task: The Edge AI Glossary — Definitions, Connections, and Teaching It Cold *(Part 1 of 2)*

**Concept:** Technical vocabulary is useless if you can recite definitions but cannot use them fluidly. Today you build your understanding of 12 core terms through three layers: define alone, self-assess against the guide, and map connections visually.

**Part 1 — First Draft Definitions, Alone and Unaided (90 min)**

All notes closed. No guide open. No browser. For each of the 12 terms below, write on paper:
- A definition in your own words (minimum 3 sentences)
- One concrete example from your own experience running the code this week (must name a specific file, output, or measurement)
- One analogy from your life outside technology

Terms: Autoregressive decoding · Token ID · Small Language Model (SLM) · Large Language Model (LLM) · Edge device · Inference · Model parameters (weights) · Virtual environment (`venv`) · Draft model · Target model · Acceptance bitmap · Network latency

If you finish in under 60 minutes, your definitions are too short.

**Part 2 — Self-Assessment Against the Build Guide (60 min)**

Open the build guide. For each definition:
- Underline every part that is accurate and consistent with the guide
- Put a "?" next to anything you are now unsure about
- Put a cross next to anything that was outright wrong
- Write a correction in a different ink color for every crossed item

Count how many definitions had at least one correction. Write this number prominently at the top — this is your "Round 1 accuracy score."

**Part 3 — Concept Map (30 min)**

On a large blank sheet of paper, arrange all 12 terms as nodes. Draw arrows between connected terms. Every arrow must be labeled with a verb phrase (e.g., "Token ID → [is consumed by] → Draft Model"). You must have at least 18 labeled arrows. No isolated nodes allowed. Photograph your map — you will reference it on Jun 29.

**Oral Check-in (end of morning):** The mentor will point to one arrow on your concept map and ask you to explain the relationship in 60 seconds without reading from the paper.

**Deliverable Checklist:**
- [ ] 12 hand-written first-draft definitions with examples and analogies (photographed)
- [ ] Self-assessed definitions with underlines, question marks, crosses, corrections in different ink (photographed)
- [ ] Round 1 accuracy score written at top
- [ ] Concept map with 18+ labeled arrows (photographed)

---

### Friday Jun 26 — Afternoon (1:00 PM – 4:00 PM)
**Slot: Research work ✅ — TASK ASSIGNED**

#### Task: The Edge AI Glossary — Peer Challenge and Teaching Cold *(Part 2 of 2, continues Jun 26 Morning)*

**This session requires your definition sheets and concept map from this morning.**

**Part 4 — Peer Definition Challenge (75 min)**

1. Exchange your definition sheets (before corrections) with a partner. Your partner reads each definition and writes for each one:
   - One sentence: "I think this is [correct / partially correct / incorrect] because…"
   - One follow-up question they still have about that term
   Partner signs and timestamps the review sheet.
2. For any term where your partner disagreed with your own self-assessment, write a 2-sentence justification or concession.

**Part 5 — Teach It Cold (75 min)**

3. Find someone who has not been your usual partner. You have 10 minutes to verbally explain "speculative decoding" using only your 12 terms and your concept map as a visual aid. Your listener rates you immediately after:

| Criterion | Score 1–5 |
|---|---|
| Used all key terms correctly | |
| Explanation was logically ordered | |
| Could follow it without the build guide | |
| Would be able to re-explain it to someone else | |

The listener writes one specific improvement suggestion and signs the rating sheet.

4. Rewrite your definition of "autoregressive decoding" incorporating all corrections and feedback from today. Final version must be at least 6 sentences and must cite your specific timing data from Jun 25 as a concrete example.

**Oral Check-in (3:30 PM):** The mentor reads one of your original wrong definitions (a crossed item) and asks you to state the correction and explain why you misunderstood it.

**Deliverable Checklist:**
- [ ] Partner's signed and timestamped review sheet
- [ ] Your typed justifications/concessions for disputed terms
- [ ] Listener's signed rating sheet
- [ ] Final rewritten "autoregressive decoding" definition (typed, 6+ sentences, citing Jun 25 data)

---

## WEEK 3 — Research · Jun 29 – Jul 3

---

### Monday Jun 29 — Morning (9:00 AM – 12:00 PM)
**Slot: Research work ✅ — TASK ASSIGNED**

#### Task: Bitmap Forensics — Tracing Verification Logic Across Seven Scenarios *(Part 1 of 2)*

**Concept:** Understanding the acceptance bitmap deeply means predicting, tracing, and explaining it for any input — not just the example in the guide.

**Part 1 — Run and Document the Baseline (30 min)**

1. Run `simulate_verify.py` as provided. Screenshot the output. Copy every printed line by hand into your log — do not just save the screenshot; copying forces you to read every character.
2. Read the source file top to bottom. On paper, list every variable the script declares, its initial value, and its data type. This is your "variable inventory."

**Part 2 — Hand-Trace Four Scenarios (2.5 hours)**

For each scenario: (a) trace through the verification loop step by step on paper, writing every variable's value at every iteration; (b) predict the output bitmap before running anything; (c) edit the script and run it; (d) screenshot the actual output; (e) compare your prediction to the actual result and explain any discrepancy in one sentence.

**Scenario 1 (Warm-up):**
- Draft: `[42, 17, 99, 55, 23]` | Target: `[42, 17, 88, 55, 23]`

**Scenario 2 (First token wrong):**
- Draft: `[42, 17, 99, 55, 23]` | Target: `[99, 17, 99, 55, 23]`

**Scenario 3 (All correct):**
- Draft: `[10, 20, 30, 40, 50]` | Target: `[10, 20, 30, 40, 50]`

**Scenario 4 (All wrong):**
- Draft: `[10, 20, 30, 40, 50]` | Target: `[99, 99, 99, 99, 99]`

**Oral Check-in (end of morning):** The mentor gives you a new scenario not listed above and asks you to predict the bitmap verbally in 90 seconds.

**Deliverable Checklist:**
- [ ] Screenshot of baseline `simulate_verify.py` output
- [ ] Hand-written variable inventory (photographed)
- [ ] 4 hand-traced scenario tables with predicted and actual bitmaps (photographed)
- [ ] 4 comparison sentences
- [ ] 4 screenshots of modified script outputs (labeled)

---

### Monday Jun 29 — Afternoon (1:00 PM – 4:00 PM)
**Slot: Research work ✅ — TASK ASSIGNED**

#### Task: Bitmap Forensics — Pattern Analysis, Cost, and Flowchart *(Part 2 of 2, continues Jun 29 Morning)*

**This session requires your 4 traced scenario tables from this morning.**

**Part 3 — Three More Scenarios (75 min)**

Continue the same trace-predict-run-compare process for three more scenarios:

**Scenario 5 (Last token only wrong):**
- Draft: `[10, 20, 30, 40, 50]` | Target: `[10, 20, 30, 40, 99]`

**Scenario 6 (Alternating correct/wrong):**
- Draft: `[10, 20, 30, 40, 50]` | Target: `[10, 99, 30, 99, 50]`

**Scenario 7 (Design your own — exactly 3 accepted):**
- Choose draft and target tokens yourself such that the output is exactly `[1, 1, 1, 0, 0]`. Explain in writing: how did you choose these values? Could there be multiple valid answers?

**Part 4 — Pattern Summary and Cost Analysis (75 min)**

1. Lay out all 7 scenario results side by side. Fill in this summary table by hand:

| Scenario | # Tokens Accepted | Position of First Rejection | Later tokens checked? | Efficient? (Y/N) |
|---|---|---|---|---|

2. Write a general rule paragraph: one paragraph that could replace reading the code. Someone reading it should be able to predict the output bitmap for any scenario without seeing the script. It must account for cascade rejection.
3. Using Scenarios 2 vs. 5: if the GPU server charges $0.001 per forward pass token and runs 100 requests/hour, how much does cascade rejection cost per hour in each scenario? Show all arithmetic on paper.

**Part 5 — Flowchart and Peer Trace (30 min)**

4. Draw a formal flowchart of the verification loop: start node, input box, loop counter, decision diamond (accept/reject), cascade stop branch, end node with output bitmap.
5. Give your flowchart to a partner — without showing them the code. They trace Scenario 6 through your flowchart and write down the bitmap they predict. If their prediction is wrong, identify which box confused them and redraw that section. Partner signs.

**Oral Check-in (3:30 PM):** The mentor picks one cell from your summary table and asks you to explain what it means for system efficiency.

**Deliverable Checklist:**
- [ ] 3 more hand-traced scenario tables (Scenarios 5–7) with predictions and actuals (photographed)
- [ ] 3 more screenshots of modified script outputs
- [ ] Scenario 7 design explanation (typed)
- [ ] Hand-written 7-row summary table (photographed)
- [ ] Typed general rule paragraph
- [ ] GPU cost arithmetic on paper (photographed)
- [ ] Hand-drawn flowchart (photographed)
- [ ] Partner's signed trace result on your flowchart

---

### Tuesday Jun 30 — Morning (9:00 AM – 12:00 PM)
**Slot: Research work ✅ — TASK ASSIGNED**

#### Task: Server Archaeology — Mapping a Machine You Have Never Touched Before *(Part 1 of 2)*

**Concept:** Professionals read a machine before they write to it. Today you document what the server is, what is running on it, and how the project files fit into it — before running a single project script.

**Part 1 — First Contact and System Profile (90 min)**

1. SSH into the GPU server. Run each command below one at a time. For each, write the exact command, the full output (by hand or screenshot), and one sentence explaining what it tells you:
   - `uname -a` | `lscpu | head -20` | `free -h` | `df -h` | `who` | `uptime` | `nvidia-smi`

2. From the `nvidia-smi` output, fill in this hand-written table:

| Property | Value |
|---|---|
| GPU Model | |
| Total VRAM | |
| VRAM Currently Used | |
| GPU Utilization % | |
| Driver Version | |
| CUDA Version | |

**Part 2 — Process and File Archaeology (90 min)**

3. Run `ps aux | grep python`. Screenshot. Are any Python processes already running? Write down their PIDs and what you think they are doing.
4. Navigate to the project directory. Run `ls -lh`. Record the file sizes and last-modified timestamps of every `.py` file in a hand-written table.
5. Run `which python3` and `python3 --version`. Record both.
6. Run `pip3 show torch`. Record the "Location" line. Navigate there and run `ls | wc -l`. Record the package count.

**Oral Check-in (end of morning):** The mentor asks: "What is the current VRAM usage on the server and why?"

**Deliverable Checklist:**
- [ ] 7 command outputs with one-sentence explanations (hand-written or screenshot)
- [ ] Hand-written `nvidia-smi` table (photographed)
- [ ] `ps aux` screenshot + written process notes
- [ ] Hand-written `ls -lh` file table (photographed)
- [ ] Python path and version recorded

---

### Tuesday Jun 30 — Afternoon (1:00 PM – 4:00 PM)
**Slot: Research work ✅ — TASK ASSIGNED**

#### Task: Server Archaeology — Reading the Script, Starting the Server, Reflecting *(Part 2 of 2, continues Jun 30 Morning)*

**This session requires your system profile data from this morning.**

**Part 3 — Read the Server Script Before Running It (75 min)**

1. Open `server.py` in `nano` or `vim` (terminal only — no VS Code remote). Read it top to bottom. Answer on paper in full sentences:
   - What Python libraries does it import? List every import.
   - What port does it listen on? What variable stores this?
   - What is the name of the route it exposes, and what HTTP method does it accept?
   - What fields does it expect in the incoming JSON body?
   - What does it return on success?
   - What would happen if the JSON is missing a required field?

2. Draw a sequence diagram on paper: your laptop terminal → network → server port → FastAPI route → model → response → back to laptop. Label every arrow with: (a) direction, (b) data type/format, (c) estimated time for that step.

**Part 4 — Start the Server and Observe (75 min)**

3. Start `server.py`. While it loads, copy every terminal output line by hand. Stopwatch the startup time. Record it.
4. Run `nvidia-smi` immediately after ready. Fill in the `nvidia-smi` table again. Calculate VRAM delta (now minus your baseline from Jun 29 Morning's table).
5. From your laptop, send one manual `curl` request. Record: exact command, exact raw JSON response, and round-trip time (stopwatch).

**Part 5 — Reflection Journal (30 min)**

6. Write a structured journal entry (250–300 words) covering:
   - What was most disorienting about working on a machine you cannot see?
   - What information from today would you include in a student SSH-lab handout?
   - If two students tried to load the 7B model simultaneously, what would happen? Use your VRAM numbers.
   Word count at bottom.

**Oral Check-in (3:30 PM):** Point to your sequence diagram. The mentor asks you to explain one specific arrow.

**Deliverable Checklist:**
- [ ] Written answers to 6 server script questions (full sentences, paper)
- [ ] Hand-drawn sequence diagram with labeled arrows (photographed)
- [ ] Hand-written startup log lines + startup time
- [ ] Second `nvidia-smi` table + VRAM delta calculation (paper)
- [ ] `curl` command + raw response + round-trip time
- [ ] Typed journal entry (250–300 words, word count at bottom)

---

### Wednesday Jul 1 — Morning (9:00 AM – 12:00 PM)
**Slot: Research work ✅ — TASK ASSIGNED**

#### Task: HTTP Anatomy Lab — Every Byte Between Your Laptop and the Server *(Part 1 of 2)*

**Concept:** Every request has a precise structure — headers, body, status codes — and every byte can be read, modified, or blocked by anyone in between.

**Part 1 — Manual curl Experiments (90 min)**

Ensure `server.py` is running on the GPU server.

1. Construct and send a valid POST request using `curl` only (no Python). Record the exact command. Screenshot the response. This is your "golden request."
2. Send 6 deliberately broken requests. For each one, record: the modified command, the full response, and one sentence explaining why it broke:
   - Missing `Content-Type: application/json` header
   - Empty body `{}`
   - Correct field name but string value: `{"draft_tokens": "hello"}`
   - Correct field with empty list: `{"draft_tokens": []}`
   - Wrong port (try port 8002)
   - GET request instead of POST to the same URL
3. After all 6, write a one-paragraph "API contract" in plain English — the exact requirements a request must satisfy to receive a valid response.

**Part 2 — Request Anatomy Diagram (90 min)**

4. On a large sheet of paper, draw the full anatomy of your "golden request": HTTP method, URL broken into protocol/host/port/path, all headers with what each means, body with format/field name/field value/data type.
5. Draw the full anatomy of the response: status code and meaning, response headers, response body with all fields.
Both diagrams must use your actual values, not placeholders.

**Oral Check-in (end of morning):** The mentor gives you a `curl` command with a deliberate error. You identify the error and explain what the server will return.

**Deliverable Checklist:**
- [ ] 7 `curl` commands (1 golden + 6 broken) with screenshots and explanations
- [ ] Typed "API contract" paragraph
- [ ] Hand-drawn request anatomy diagram (photographed)
- [ ] Hand-drawn response anatomy diagram (photographed)

---

### Wednesday Jul 1 — Afternoon (1:00 PM – 4:00 PM)
**Slot: Research work ✅ — TASK ASSIGNED**

#### Task: HTTP Anatomy Lab — Comparison Table, Security Connection, Field Guide *(Part 2 of 2, continues Jul 1 Morning)*

**This session requires your golden request, broken request log, and anatomy diagrams from this morning.**

**Part 3 — GET vs. POST Comparison and Security Connection (90 min)**

1. Research HTTP GET vs. POST using MDN Web Docs or RFC 7231 (not AI). Fill in this comparison table on paper with at least 2 sentences per cell:

| Property | HTTP GET | HTTP POST |
|---|---|---|
| Where is the data? | | |
| Length limit? | | |
| Cached by browser? | | |
| Visible in server logs? | | |
| Safe for sensitive data? | | |
| Our project uses which? Why? | | |

2. Write a paragraph (150–200 words): *If an attacker was sitting on the same WiFi network as a student sending requests to the GPU server, exactly what could they read from the traffic? What could they change? What could they not change without detection (in the current non-secure system)?* Reference specific fields from your anatomy diagrams. Word count at bottom.

**Part 4 — HTTP Field Guide and Partner Test (90 min)**

3. Create a 1-page hand-drawn "HTTP Field Guide" — a reference card a student could keep at their desk — containing:
   - A miniature anatomy diagram (condensed from this morning)
   - The 6 broken-request scenarios as a "common mistakes" list with the error each causes
   - Your API contract paragraph condensed to bullet points
   - One "why this matters for security" callout box

4. Exchange your Field Guide with a partner. Your partner attempts to construct a valid `curl` request from scratch using only your Field Guide — no other documentation, no previous notes. Screenshot their terminal showing whether it worked. If it failed, identify which part of your Field Guide was unclear. Write a correction.

**Oral Check-in (3:30 PM):** The mentor asks: "What would an attacker see if they intercepted your golden request on the network right now?"

**Deliverable Checklist:**
- [ ] Hand-written GET vs. POST comparison table (photographed)
- [ ] Typed security paragraph (150–200 words, word count at bottom)
- [ ] Hand-drawn HTTP Field Guide (photographed)
- [ ] Partner's `curl` test screenshot + your written correction if needed

---

### Thursday Jul 2 — Morning (9:00 AM – 12:00 PM)
**Slot: Progress report ✅ — TASK ASSIGNED**

#### Task: GPU Memory Observatory — Tracking the True Cost of Model Inference *(Part 1 of 2)*

**Concept:** VRAM is the scarcest resource in AI systems. Today you measure, calculate, and project VRAM consumption to answer a real question: how many simultaneous users can this server actually support?

**Part 1 — Controlled Loading Experiment (90 min)**

1. Confirm the server is stopped. Run `nvidia-smi`. Record baseline VRAM.
2. Start `server.py`. Stopwatch from first output line to "ready." Run `nvidia-smi` the moment it says ready. Calculate VRAM consumed (current − baseline).
3. Send 1 `curl` request. During the response (within 1 second of sending — use a helper), run `nvidia-smi`. Does VRAM spike during inference or is it constant? Record and describe.
4. Kill the server. Wait 10 seconds. Run `nvidia-smi`. Has it returned to baseline? Measure how long it takes with your stopwatch.
5. Restart the server 3 more times (4 restarts total). Record startup time and post-load VRAM each time:

| Restart # | Time Since Kill (sec) | Startup Time (sec) | VRAM After Load (GB) |
|---|---|---|---|
| 1 | N/A | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |

Is startup time faster on subsequent runs? Write a 3-sentence hypothesis.

**Part 2 — Disk-to-VRAM Transfer Analysis (90 min)**

6. Navigate to the model weights directory on the server. Run `ls -lh *.safetensors`. Record each file size and sum the total by hand. Show the addition.
7. Compare total disk size to VRAM consumption. Write a paragraph explaining why they may differ — look this up in the Hugging Face model card or documentation, not AI. Cite your source.
8. Draw a diagram on paper: SSD → RAM → GPU VRAM. Label each stage with the file format, approximate size from your measurements, and the bottleneck at each transfer.

**Oral Check-in (end of morning):** "If a student ran two inference requests simultaneously, what would happen to VRAM? Show me the arithmetic."

**Deliverable Checklist:**
- [ ] 4 `nvidia-smi` screenshots (baseline, post-load, during inference, after kill)
- [ ] 4-row startup timing table with 3-sentence hypothesis (paper, photographed)
- [ ] `ls -lh` output with total disk size summed by hand (paper)
- [ ] Typed disk-vs-VRAM explanation paragraph (with source cited)
- [ ] Hand-drawn SSD → RAM → VRAM diagram with sizes labeled (photographed)

---

### Thursday Jul 2 — Afternoon (1:00 PM – 4:00 PM)
**Slot: Draft lessons (section 4) + section 5 (independent) + Mid-program survey ❌ — NO TASK ASSIGNED**

> This slot is reserved for drafting lesson sections 4 and 5 (independent) and completing the mid-program survey. Complete those program requirements.

---

### Friday Jul 3 — Full Day
**Slot: No program — Independence Day (UNR closed) ❌ — NO TASK ASSIGNED**

> UNR is closed. No lab today.

---

## WEEK 4 — Research · Jul 6–10

---

### Monday Jul 6 — Morning (9:00 AM – 12:00 PM)
**Slot: Research work ✅ — TASK ASSIGNED**

#### Task: GPU Memory Observatory — Capacity Planning and Comparison *(Part 2 of 2, continues Jul 2 Morning)*

**This session requires your VRAM measurements and disk-size data from Jul 2 Morning.**

**Part 3 — Capacity Planning Calculation (90 min)**

1. Using your measured VRAM consumption per model load, calculate (show all arithmetic on paper):
   - How many simultaneous 7B model instances could this GPU support? (Total VRAM ÷ VRAM per instance)
   - If a school district deployed this system for 30 teachers simultaneously, how many GPU servers would they need?
   - If each GPU server costs $3.50/hour on a cloud provider, what is the monthly cost for that district assuming 6 hours/school day, 20 days/month?

2. Write a 1-paragraph "Budget Memo" (150–200 words) addressed to a fictional school district CTO explaining the infrastructure cost to run this system at scale. Use your actual calculated numbers. Word count at bottom.

**Part 4 — Full Comparison Table (90 min)**

3. Go back to your Jun 24 RAM measurements for the 0.5B model. Build a final side-by-side comparison table on paper using real data from Jun 24 and today:

| Metric | 0.5B on Laptop | 7B on GPU Server | Ratio |
|---|---|---|---|
| Load time (seconds) | | | |
| Memory consumed (GB) | | | |
| Memory available on device (GB) | | | |
| % of device memory used | | | |
| Cost per hour (estimate) | | | |

Calculate all ratios by hand.

4. Write a typed 4-sentence conclusion: *What did these measurements teach you about why speculative decoding is architecturally necessary, rather than just a nice optimization?* Reference at least 3 specific numbers from your table.

**Oral Check-in (end of morning):** Point to any ratio in your comparison table and trace it back to the two raw measurements that produced it.

**Deliverable Checklist:**
- [ ] 3 capacity planning calculations shown on paper (photographed)
- [ ] Typed Budget Memo (150–200 words, word count at bottom)
- [ ] Final 5-row comparison table from real data (paper, photographed)
- [ ] Typed 4-sentence conclusion citing 3 specific numbers

---

### Monday Jul 6 — Afternoon (1:00 PM – 4:00 PM)
**Slot: Research work ✅ — TASK ASSIGNED**

#### Task: Dataset Archaeology — Reading, Auditing, and Extending ShareGPT *(Part 1 of 2)*

**Concept:** A benchmark is only as good as its data. Today you read the dataset the way a researcher would — by hand, counting, reading, and critiquing — not by running it.

**Part 1 — Raw File Census (90 min)**

Open `sharegpt_subset.json` in a plain text editor only. No code.

1. Count by hand: how many top-level conversations are in the file? Write your counting method.
2. For each conversation, count the message turns. Total turns across all conversations? Average turns per conversation? Show the division.
3. For each conversation, hand-write the first 20 words of the human prompt into your log. Do not paste — write it out.
4. Fill in this table for every conversation:

| # | First 5 Words | Your Topic Label | Length (S/M/L) | Conversational or Factual? |
|---|---|---|---|---|

**Part 2 — Depth Analysis of Three Conversations (90 min)**

5. Choose the longest, shortest, and one in the middle. For each, write a paragraph (100–150 words) describing: what the human was trying to accomplish, how the AI response would typically be structured, and whether this is the kind of question a K-12 student or teacher would realistically ask.

**Oral Check-in (end of afternoon):** The mentor picks one conversation from your table. You explain its topic and why you labeled its length as S, M, or L.

**Deliverable Checklist:**
- [ ] Hand-written conversation count with method shown
- [ ] Turn tally with total and average calculated (paper)
- [ ] Hand-written first 20 words of each prompt
- [ ] Full 15-row table (paper, photographed)
- [ ] 3 typed conversation-analysis paragraphs (100–150 words each)

---

### Tuesday Jul 7 — Morning (9:00 AM – 12:00 PM)
**Slot: Research work ✅ — TASK ASSIGNED**

#### Task: Dataset Archaeology — Critical Audit and Benchmark Extension *(Part 2 of 2, continues Jul 6 Afternoon)*

**This session requires your 15-row table and conversation analyses from yesterday afternoon.**

**Part 3 — Critical Audit (60 min)**

1. Write a structured critique (250–300 words) of the dataset addressing:
   - What subjects or domains are over-represented?
   - What subjects are missing entirely?
   - What grade levels does the language suit?
   - Could any prompt cause a problem if an AI gave a wrong answer to a student?
   - Is 15 prompts sufficient for a production classroom AI benchmark? What number would you use and why?
   Word count at bottom.

**Part 4 — Design Your Own Benchmark Extension (120 min)**

2. Write 10 original prompts to extend this benchmark for K-12 classroom AI use. Rules:
   - Each prompt must come from a subject or grade level you actually teach
   - No two prompts from the same topic
   - At least 3 must involve numbers, data, or calculations
   - At least 2 must be ambiguous (the "right" answer depends on context)
   - At least 2 must be the kind a struggling student might write (incomplete, vague, or imperfect grammar — real students write like that)

3. Write each prompt on paper first, then type in valid JSON format matching the file's exact structure. For each prompt, write in a separate section: why you chose it, what a correct AI response would include, and what a dangerously wrong response might look like.

4. Exchange your 10 prompts with a partner. They write for each: "Accepted as-is" or "Needs revision: [reason]." Partner signs and timestamps. Revise any flagged prompt and note what you changed.

**Oral Check-in (end of morning):** The mentor picks one of your 10 prompts and asks: "Why would a wrong AI response to this specific prompt be harmful in a classroom?"

**Deliverable Checklist:**
- [ ] Typed critical audit (250–300 words, word count at bottom)
- [ ] 10 prompts hand-written first, then typed in JSON format
- [ ] Typed justification + correct answer + wrong answer for each prompt
- [ ] Partner's signed and timestamped review
- [ ] Your revision notes for any flagged prompts

---

### Tuesday Jul 7 — Afternoon (1:00 PM – 4:00 PM)
**Slot: Research work ✅ — TASK ASSIGNED**

#### Task: Benchmark Interpretation Lab — Making Numbers Tell a Story *(Part 1 of 2)*

**Concept:** Running a benchmark is easy. Interpreting the output rigorously — with appropriate uncertainty — is a professional skill.

**Part 1 — Three Benchmark Runs (90 min)**

1. Run `benchmark.py` to completion. Save output as `benchmark_results_run1.txt`. Screenshot terminal and file.
2. Run again immediately, save as `run2.txt`. Screenshot.
3. Wait 10 minutes (let server idle). Run again, save as `run3.txt`. Screenshot.
4. For all 15 prompts, extract latency and acceptance rate from all 3 runs into a hand-written table (45 rows: 15 prompts × 3 runs):

| Prompt # | Run1 Latency | Run2 Latency | Run3 Latency | Run1 Acc. | Run2 Acc. | Run3 Acc. |
|---|---|---|---|---|---|---|

**Part 2 — Statistical Summary (90 min)**

5. For each of the 15 prompts, calculate by hand (show arithmetic):
   - Mean latency across 3 runs
   - Mean acceptance rate across 3 runs
   - Range of acceptance rate (max − min)

6. Which prompt has the highest variance in acceptance rate? Which has the lowest? Write one sentence about each explaining why.

**Oral Check-in (end of afternoon):** The mentor picks one row from your 45-row table and asks you to locate it in the saved benchmark text file.

**Deliverable Checklist:**
- [ ] 3 benchmark run screenshots and saved text files
- [ ] 45-row hand-written data table (photographed)
- [ ] Mean and range calculations for all 15 prompts (paper, arithmetic shown)
- [ ] 2 typed sentences on highest/lowest variance prompts

---

### Wednesday Jul 8 — Morning (9:00 AM – 12:00 PM)
**Slot: Research work ✅ — TASK ASSIGNED**

#### Task: Benchmark Interpretation Lab — Visualization and Honest Reporting *(Part 2 of 2, continues Jul 7 Afternoon)*

**This session requires your 45-row data table and statistical calculations from yesterday afternoon.**

**Part 3 — Hand-Drawn Visualizations (90 min)**

1. Draw a scatter plot on graph paper: X-axis = mean latency, Y-axis = mean acceptance rate. Plot all 15 data points using your calculated means. Label each point with a 3-word prompt label. Use a ruler.
2. Draw a horizontal bar chart showing the acceptance rate range (max − min) for each of the 15 prompts, ordered from most variable to least variable.
3. Write a 3-sentence observation: do prompts with higher latency tend to have higher or lower acceptance rates? Is there a cluster?

**Part 4 — Results Section and Peer Cross-Examination (90 min)**

4. Write a typed "Results Section" (300–400 words) as if this were a research paper. It must:
   - Report key statistics with actual numbers
   - Acknowledge limitations (only 3 runs, 15 prompts, one hardware configuration)
   - Avoid over-claiming ("the system is fast" → "for these 15 prompts on this hardware, median latency was X seconds")
   - Include one finding that surprised you and one that confirmed your hypothesis
   Word count at bottom.

5. Exchange with a partner. Your partner circles every claim not supported by a specific number, and every number not traceable to a specific table row. You do the same for theirs. Return and revise.

**Oral Check-in (end of morning):** The mentor points to one data point on your scatter plot and asks you to trace it back to the raw benchmark run that produced it.

**Deliverable Checklist:**
- [ ] Hand-drawn scatter plot (labeled, ruler used) (photographed)
- [ ] Hand-drawn horizontal bar chart (labeled) (photographed)
- [ ] Typed 3-sentence observation
- [ ] Typed Results Section (300–400 words, word count at bottom)
- [ ] Partner's markup of your Results Section + your revision

---

### Wednesday Jul 8 — Afternoon (1:00 PM – 4:00 PM)
**Slot: Research work ✅ — TASK ASSIGNED**

#### Task: Network Path Forensics — Tracing Every Hop Between Your Laptop and the Server

**Concept:** The network between your laptop and the GPU server is a chain of routers, switches, and firewalls, each adding delay. Today you map that chain and connect it to your benchmark numbers.

**Part 1 — Traceroute and Hop Table (75 min)**

1. Run `traceroute <server-IP>` from your laptop 3 times. Screenshot all 3 outputs.
2. For every hop across all 3 runs, fill in a hand-written table:

| Hop # | IP Address | Avg RTT (ms) | In all 3 runs? | Hypothesized device type |
|---|---|---|---|---|

3. Which hop has the highest RTT? Which has the most variance across runs? One sentence each.

**Part 2 — Ping Statistics (45 min)**

4. Run `ping <server-IP> -c 50`. Screenshot the full output including the summary. Record min, avg, max, mdev. Calculate the coefficient of variation (mdev ÷ avg × 100) by hand.
5. Run the same test at a second time of day. Record both sets and compare coefficients of variation.

**Part 3 — Network Map and Latency Gap Analysis (60 min)**

6. Draw a physical network map on paper: your laptop → each hop → GPU server. Label each link with measured RTT, hypothesized device type, and IP address. Mark where the campus network ends and the internet begins.
7. For each of your 15 prompts, calculate the "unexplained gap": mean benchmark latency − (ping avg RTT ÷ 1000). Hand-write these 15 values.
8. Write a typed paragraph (200–250 words) breaking the gap into at least 4 distinct factors with estimated time contributions specific to this system (e.g., "FastAPI parsing," "model tokenization," "GPU forward pass"). Factors must roughly sum to the gap. Word count at bottom.

**Oral Check-in (3:30 PM):** The mentor points to one hop on your network map and asks: "What is this device and how do you know?"

**Deliverable Checklist:**
- [ ] 3 `traceroute` screenshots
- [ ] Hand-written hop table (photographed)
- [ ] 2 ping run screenshots with coefficient of variation calculations
- [ ] Physical network map (hand-drawn, labeled) (photographed)
- [ ] 15 latency gap calculations (paper)
- [ ] Typed latency gap explanation (200–250 words, word count at bottom)

---

### Thursday Jul 9 — Morning (9:00 AM – 12:00 PM)
**Slot: Progress report ✅ — TASK ASSIGNED**

#### Task: The Performance Report — Writing for a Principal, Defending to a Peer *(Part 1 of 2)*

**Concept:** Research has no value unless it can be communicated. You synthesize two days of data into a written report, then defend every number in a structured peer cross-examination.

**Part 1 — Data Audit (60 min)**

1. Lay out all your data from Jul 7 and Jul 8. Before writing, fill in a "data audit" table — every statistic you plan to cite must have a source:

| Statistic | Exact Value | Source (which day, which table, which row) |
|---|---|---|

List at least 12 statistics. Any number whose source column you cannot fill in cannot appear in your report.

2. Write a hand-written report outline: at least 4 sections with at least 3 sub-points each.

**Part 2 — First Draft (120 min)**

3. Write the first draft by hand on paper. Target 450–550 words. Addressed to a school principal: *"Should our district pay to deploy this AI system for classroom use? Is it fast and reliable enough?"*

Must include:
- One paragraph summarizing system performance (cite 3+ specific numbers)
- One paragraph on network reliability (cite ping results and variance)
- One paragraph on evaluation limitations (what you could not measure)
- One paragraph with your recommendation (yes/no/maybe, justified by data)
- One hand-drawn chart attached to the report

**Oral Check-in (end of morning):** The mentor reads one sentence from your draft and asks: "Which specific row in which table did this sentence come from?"

**Deliverable Checklist:**
- [ ] Data audit table (12+ statistics with sources) (paper, photographed)
- [ ] Hand-written report outline (photographed)
- [ ] Hand-written first draft (photographed)
- [ ] Hand-drawn chart attached to draft (photographed)

---

### Thursday Jul 9 — Afternoon (1:00 PM – 4:00 PM)
**Slot: Research work ✅ — TASK ASSIGNED**

#### Task: The Performance Report — Cross-Examination and Final Revision *(Part 2 of 2, continues Jul 9 Morning)*

**This session requires your hand-written draft from this morning.**

**Part 3 — Type and Peer Cross-Examination (120 min)**

1. Type your report. Word count must appear at the bottom. Must be 450–550 words — revise until in range.
2. Structured peer cross-examination: find a partner. Take turns as "author" and "examiner." The examiner challenges every number:
   - "Where does this number come from? Show me in your raw data."
   - "What evidence supports this claim? Could the opposite be true?"
   - "What would change your recommendation? What is the weakest assumption here?"
   The examiner writes every question asked and every answer given (brief notes). This is a deliverable. Both sign it.

**Part 4 — Revision Memo and Final Visual (60 min)**

3. Write a revision memo (100–150 words): what did the cross-examination reveal as weak? What did you change and why? What did you defend and why?
4. Create a clean hand-drawn one-page summary visual suitable for a slide — key findings displayed visually, not as text bullets. Label everything. This is what a principal could understand in 30 seconds.

**Oral Check-in (3:30 PM):** "Read me one finding from your report. Now explain it without looking at your slides or notes."

**Deliverable Checklist:**
- [ ] Typed final report (450–550 words, word count at bottom)
- [ ] Cross-examination record (questions + answers, both signed)
- [ ] Typed revision memo (100–150 words)
- [ ] Hand-drawn one-page summary visual (photographed)

---

### Friday Jul 10 — Morning (9:00 AM – 12:00 PM)
**Slot: Research work ✅ — TASK ASSIGNED**

#### Task: Threat Model Construction — Finding Every Hole Before the Attacker Does *(Part 1 of 2)*

**Concept:** Professional threat modeling is systematic. Today you apply the STRIDE framework to identify, classify, and prioritize every vulnerability in the system before running a single exploit.

**Part 1 — STRIDE Framework Study (60 min)**

1. Look up STRIDE using OWASP or Microsoft's documentation (no AI). Write on paper what each letter stands for and a 2-sentence explanation with one everyday-technology example (not from this project):
   S · T · R · I · D · E

2. Look up the DREAD scoring model (Damage, Reproducibility, Exploitability, Affected Users, Discoverability). Record all 5 dimensions and their scoring scale.

**Part 2 — Component Inventory and STRIDE Analysis (120 min)**

3. List every distinct component in the current non-secure system (minimum 6). For each: what it does, what data it holds, what happens if compromised.
4. For each component, go through all 6 STRIDE categories. Fill in a large table on paper (minimum 20 rows total). Vague entries like "could be hacked" are not acceptable — each threat must be specific (e.g., "Attacker intercepts JSON on port 8000 and changes `draft_tokens[2]` from 412 to 9999").

**Oral Check-in (end of morning):** The mentor picks one row from your STRIDE table and asks you to explain the specific threat in detail.

**Deliverable Checklist:**
- [ ] Hand-written STRIDE definitions with examples (photographed)
- [ ] DREAD dimensions and scale (paper)
- [ ] 6+ component inventory (paper)
- [ ] STRIDE table (20+ rows, paper, photographed)

---

### Friday Jul 10 — Afternoon (1:00 PM – 4:00 PM)
**Slot: Finalize section 4 + section 5 (independent) ❌ — NO TASK ASSIGNED**

> This slot is reserved for finalizing your lesson sections 4 and 5 independently as specified in the program schedule. Complete that program requirement.

---

## WEEK 5 — Research & Course Materials · Jul 13–17

---

### Monday Jul 13 — Morning (9:00 AM – 12:00 PM)
**Slot: Research work ✅ — TASK ASSIGNED**

#### Task: Threat Model — DREAD Scoring, Priority Matrix, Code Read, and Attack Prediction *(Part 2 of 2, continues Jul 10 Morning)*

**This session requires your STRIDE table from Jul 10 Morning.**

**Part 3 — DREAD Scoring and Priority Matrix (90 min)**

1. Select your 10 most credible threats from the STRIDE table. For each, score all 5 DREAD dimensions (1–10 each) and calculate a total score. Show all scoring on paper.
2. Plot these 10 threats on a 2×2 priority matrix: X-axis = Exploitability, Y-axis = Damage Potential. Label each dot. High-right quadrant = fix immediately.

**Part 4 — Code Read and Prediction (90 min)**

3. Open `attacker_mitm.py`. Read it completely without running it. Answer on paper:
   - Which STRIDE category does this attack fall under?
   - What is the exact mathematical operation applied to token IDs? Write the formula.
   - At the default tampering rate, how many of the 5 draft tokens will be modified per request on average? Show the calculation.
   - Which row in your STRIDE table does this attack correspond to? Write the row number.

4. Write your prediction: *At the default tampering rate, what acceptance rate do you expect, and why?* Sign and date this — you will verify it in the next session.

**Oral Check-in (end of morning):** "Which cell in your priority matrix has the highest combined score? Why?"

**Deliverable Checklist:**
- [ ] DREAD scoring table for 10 threats (paper, photographed)
- [ ] 2×2 priority matrix (paper, photographed)
- [ ] Written answers to 4 code-read questions (paper)
- [ ] Signed and dated acceptance rate prediction

---

### Monday Jul 13 — Afternoon (1:00 PM – 4:00 PM)
**Slot: Research work ✅ — TASK ASSIGNED**

#### Task: Execute, Measure, and Explain the Attack *(Part 1 of 2)*

**This session requires your signed prediction from this morning.**

**Part 1 — Baseline Re-run (30 min)**

1. Run `benchmark.py` directly to the server (no attacker). Record results. Screenshot. This is today's clean baseline — yesterday's data cannot substitute.

**Part 2 — Attack at Three Intensity Levels (150 min)**

For tampering percentages **10%, 50%, 100%** (three levels this afternoon, two tomorrow morning):

For each level:
- Set the tampering rate in `attacker_mitm.py`
- Start attacker on port 8001
- Point client at port 8001
- Run full `benchmark.py`
- Screenshot results
- Stop attacker
- Run `nvidia-smi` and screenshot

Record in a master hand-written table:

| Tampering % | Mean Latency | Mean Acc. Rate | # Prompts with 0% Acc. | GPU Util. % |
|---|---|---|---|---|
| 0% (baseline) | | | | |
| 10% | | | | |
| 50% | | | | |
| 100% | | | | |

**Oral Check-in (3:30 PM):** "What acceptance rate did you observe at 50% tampering, and how does that compare to your prediction from this morning?"

**Deliverable Checklist:**
- [ ] Clean baseline screenshot
- [ ] 3 benchmark screenshots (10%, 50%, 100%)
- [ ] 3 `nvidia-smi` screenshots
- [ ] Partial master table (4 rows filled) (paper, photographed)

---

### Tuesday Jul 14 — Morning (9:00 AM – 12:00 PM)
**Slot: Research work ✅ — TASK ASSIGNED**

#### Task: Execute the Attack — Complete Data, Graphing, and Analysis *(Part 2 of 2, continues Jul 13 Afternoon)*

**This session requires your partial master table from yesterday afternoon.**

**Part 3 — Two Remaining Intensity Levels (60 min)**

1. Run the attack at **0% (verify)** and **25%** tampering using the same process as yesterday. Add these rows to your master table (now 6 rows: 0%, 10%, 25%, 50%, 100%, and your re-verified 0%).

**Part 4 — Graphing and Cost Analysis (90 min)**

2. Hand-draw a line graph: X-axis = tampering % (0, 10, 25, 50, 100), Y-axis = mean acceptance rate. Describe the curve shape in one sentence.
3. Calculate the "cost per attack hour" for each tampering level:
   - (1 − acceptance rate) × 100 requests/hour × 2 seconds/rejected request = wasted GPU seconds/hour
   - ÷ 3600 = wasted GPU hours/hour
   - × $3.50 = cost to server operator per hour
   Show all arithmetic. Add a cost column to your master table.

**Part 5 — Prediction Comparison and Server Log Analysis (30 min)**

4. Pull out your signed prediction from yesterday morning. Compare to your actual results. Write a 3-paragraph formal response:
   - What you predicted and why
   - What actually happened (quote specific numbers)
   - Why there was a discrepancy, or what reasoning led you to the correct answer

5. Write down every line the server printed during one attack run. Does the server know it is being attacked? Describe what information the server has vs. what it does not have.

**Oral Check-in (end of morning):** "Walk me through the cost calculation at 25% tampering, step by step."

**Deliverable Checklist:**
- [ ] 2 more benchmark screenshots (25% + re-verified 0%)
- [ ] Completed 6-row master table with cost column (paper, photographed)
- [ ] Hand-drawn line graph (photographed)
- [ ] Cost arithmetic shown on paper (photographed)
- [ ] Typed 3-paragraph prediction comparison
- [ ] Hand-written server log lines + analysis paragraph

---

### Tuesday Jul 14 — Afternoon (1:00 PM – 4:00 PM)
**Slot: Lesson teaching materials / refine your module design (with Dr. Chen) ❌ — NO TASK ASSIGNED**

> This slot is reserved for lesson teaching materials and module design refinement with Dr. Chen. Attend that session.

---

### Wednesday Jul 15 — Morning (9:00 AM – 12:00 PM)
**Slot: Research work ✅ — TASK ASSIGNED**

#### Task: Hash Functions by Hand — Building Cryptographic Intuition from Scratch *(Part 1 of 2)*

**Concept:** Cryptographic functions seem magical until you understand the mathematical intuition behind them. Today you build that intuition by constructing and breaking a toy hash function by hand.

**Part 1 — Toy Hash Construction and Avalanche Testing (90 min)**

**Toy Hash Algorithm (paper arithmetic only — no computer):**
1. Convert each character in your input to its ASCII decimal value (use a printed ASCII table)
2. Multiply each value by its 1-indexed position: char 1 × 1, char 2 × 2, etc.
3. Sum all the products
4. Divide by 97 (prime) and record the remainder — this is your hash

Apply this to: (a) your full name, (b) your name with one character changed, (c) your name with only the first character changed to a space, (d) your name with the first and second characters swapped. Show every arithmetic step on paper.

Fill in the table:

| Input | Full calculation (every step) | Final Hash | Δ from original |
|---|---|---|---|

Write a 4-sentence analysis: Does your toy hash exhibit the avalanche effect? How easily could an attacker find two inputs with the same hash?

**Part 2 — Breaking the Toy Hash (60 min)**

5. Find two different strings that produce the same hash (a "collision"). Try by hand or with simple arithmetic. Record both strings and show that they produce the same output.
6. Explain in 3 sentences why this collision is easy to find and why it would be catastrophic in a security system.

**Part 3 — SHA-256 Properties Research (30 min)**

7. Look up SHA-256 using NIST FIPS 180-4 or a university cryptography lecture (not AI). Record: output size in bits, block size, number of rounds, whether collisions have been found, estimated brute-force time at 10¹⁵ hashes/second.

**Oral Check-in (end of morning):** Show your two collision strings. Explain why this breaks this project's security.

**Deliverable Checklist:**
- [ ] Toy hash arithmetic for all 4 experiments (paper, every step, photographed)
- [ ] 4-row experiment table (photographed)
- [ ] Typed 4-sentence avalanche analysis
- [ ] Two collision strings with proof (paper, photographed)
- [ ] Typed 3-sentence collision danger explanation
- [ ] SHA-256 properties recorded with source cited

---

### Wednesday Jul 15 — Afternoon (1:00 PM – 4:00 PM)
**Slot: Lesson teaching materials / refine your module design (with Dr. Chen) ❌ — NO TASK ASSIGNED**

> This slot is reserved for lesson teaching materials and module design refinement with Dr. Chen. Attend that session.

---

### Thursday Jul 16 — Morning (9:00 AM – 12:00 PM)
**Slot: Research work ✅ — TASK ASSIGNED**

#### Task: Hash Functions — HMAC Code Reading and Plain-English Translation *(Part 2 of 2, continues Jul 15 Morning)*

**This session requires your SHA-256 properties and toy-hash findings from yesterday morning.**

**Part 4 — SHA-256 vs. Toy Hash Comparison (30 min)**

1. For each of your 4 toy-hash experiments, write one sentence comparing how SHA-256 would behave differently (stronger avalanche? harder collision? more position-sensitive?).

**Part 5 — HMAC Code Reading and Annotation (75 min)**

2. Open `crypto_auth.py`. Read every line. For each line involving HMAC generation, verification, or key handling, copy the line on paper and write a plain-English annotation: what it does and why it is necessary — as if explaining to a 10th grader.
3. Write a 5-step English recipe for how `crypto_auth.py` signs a message and how `server_secure.py` verifies it. No code — prose only. A student who reads your recipe should understand HMAC without seeing the script.

**Part 6 — Security Connection (45 min)**

4. Write a 5-sentence analogy explaining HMAC to a high school student using an everyday object (wax seals, tamper-evident packaging, notarized documents — your choice).
5. Connect your avalanche finding to this system: *Why does HMAC need the avalanche property? What would happen if the hash function had easy collisions like your toy hash?* Write 4 sentences.

**Oral Check-in (end of morning):** "Walk me through your 5-step HMAC recipe without looking at your notes."

**Deliverable Checklist:**
- [ ] Typed SHA-256 vs. toy hash comparison (4 sentences)
- [ ] Hand-written annotated code lines from `crypto_auth.py` (photographed)
- [ ] Typed 5-step HMAC recipe in plain English
- [ ] Typed 5-sentence everyday-life analogy
- [ ] Typed 4-sentence avalanche-to-security connection

---

### Thursday Jul 16 — Afternoon (1:00 PM – 4:00 PM)
**Slot: Lesson teaching materials / refine your module design (with Dr. Chen) ❌ — NO TASK ASSIGNED**

> This slot is reserved for lesson teaching materials and module design refinement with Dr. Chen. Attend that session.

---

### Friday Jul 17 — Morning (9:00 AM – 12:00 PM)
**Slot: Research work ✅ — TASK ASSIGNED**

#### Task: Defense Verification — Six Scenarios and Fail-Secure Analysis *(Part 1 of 2)*

**Concept:** A defense that works in one scenario may not work in all scenarios. Today you test the cryptographic defense systematically across 6 conditions and read the source code to understand exactly how it blocks attacks.

**Part 1 — Six Test Scenarios (90 min)**

For each scenario, write your prediction before running, then run, screenshot, and compare.

- **Scenario A:** `edge_secure.py` → `server_secure.py` directly (correct key, no attacker)
- **Scenario B:** `edge_secure.py` → attacker port 8001 → `server_secure.py`
- **Scenario C:** `edge_secure.py` with one character changed in the key → `server_secure.py` directly
- **Scenario D:** `edge_secure.py` with no HMAC field at all (remove signature from JSON) → `server_secure.py`
- **Scenario E:** Attacker with token tampering commented out (proxy only, signature untouched) → `server_secure.py`
- **Scenario F:** Fully valid correctly-signed request but with one extra unexpected JSON field added

Fill in the master table:

| Scenario | Your Prediction | Actual Result | Match? | Explanation of discrepancy |
|---|---|---|---|---|

**Part 2 — Source Code Annotation (90 min)**

2. Open `server_secure.py`. Read every line. For each line in the HMAC verification logic, copy it on paper and write: (a) what it does, (b) what would happen if this line were deleted, (c) which scenario it blocks.

**Oral Check-in (end of morning):** "Point to Scenario D in your table. Why does the server behave this way? Show me the specific lines."

**Deliverable Checklist:**
- [ ] 6 labeled screenshots (one per scenario)
- [ ] Master 6-row prediction vs. actual table (paper, photographed)
- [ ] Hand-written annotated code lines from `server_secure.py` (photographed)

---

### Friday Jul 17 — Afternoon (1:00 PM – 4:00 PM)
**Slot: Lesson teaching materials / refine your module design (with Dr. Chen) ❌ — NO TASK ASSIGNED**

> This slot is reserved for lesson teaching materials and module design refinement with Dr. Chen. Attend that session.

---

## WEEK 6 — Finalize, Poster & Microteaching · Jul 20–24

> **Note:** All of Week 6 is occupied by program-required activities — RET poster completion, course material finalization with Dr. Chen, microteaching preparation, and microteaching presentations. **No research tasks are assigned this week.** The sessions below describe what each slot is for so you know where to be.

---

### Monday Jul 20
- **Morning:** Complete your RET poster (one per teacher/group) ❌
- **Afternoon:** Finalize course materials & module design with Dr. Chen ❌

### Tuesday Jul 21
- **Morning:** Complete your RET poster (one per teacher/group) ❌
- **Afternoon:** Finalize course materials & module design with Dr. Chen ❌

### Wednesday Jul 22
- **Morning:** Prepare your microteaching presentation ❌
- **Afternoon:** Prepare your microteaching presentation with Dr. Chen ❌

### Thursday Jul 23
- **Morning:** Prepare your microteaching presentation with Dr. Chen ❌
- **Afternoon:** Prepare your microteaching presentation with Dr. Chen ❌

### Friday Jul 24
- **Morning:** Microteaching presentations (30 + 10 min Q&A per teacher) ❌
- **Afternoon:** Microteaching presentations (cont.) + lunch & closing + group photo ❌
  - Submit: Module design + course materials + poster
  - Submit: Post-program survey

---

*Tasks designed for NSF RET 2026 — EdgeAI Site, University of Nevada, Reno.*
*Mentors: Dr. Xiaoxue Zhang and Mr. Md Omer Danish*
*Program Dates: June 15 – July 24, 2026*
