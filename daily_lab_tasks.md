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
