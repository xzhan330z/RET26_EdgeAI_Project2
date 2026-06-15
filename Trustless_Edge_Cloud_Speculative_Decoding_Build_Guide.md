# **Trustless Edge-Cloud Speculative Decoding: A Step-by-Step Build Guide**

Build and analyze a collaborative, distributed Large Language Model (LLM) system across your laptop and a remote GPU server. Then, simulate how a malicious network middleman can exploit this design, and deploy cryptographic defenses to secure it.

**Mentors:** Dr. Xiaoxue Zhang and Mr. Md Omer Danish (PhD student)  
*Department of Computer Science & Engineering, University of Nevada, Reno*

---

## **1. Background Knowledge**

Before writing any code, let us understand how Large Language Models (LLMs) work and why we need a collaborative cloud-edge design.

### **1.1 The Bottleneck of Edge AI**
When you interact with a model like ChatGPT, the AI generates its answer **one word (token) at a time**. This is called **autoregressive decoding**.
* To generate each single word, the model must load billions of mathematical parameters into active memory.
* High-capability models (e.g., 7-Billion parameters or larger) are highly intelligent, but they are **too resource-heavy** to run on a normal school laptop or edge device. They would either run out of RAM or take minutes to print a single sentence.

### **1.2 What is Speculative Decoding?**
To bypass this limitation, engineers use **Speculative Decoding**. Instead of relying on a single large model, we pair two different models together to work as a team:

```
[ Edge: Your Laptop ]                            [ Cloud: GPU Server ]
Loads a tiny SLM                                 Loads a giant LLM
(Fast but guessing)                              (Slow but flawless)
       |                                                 |
  1. Drafts 5 tokens ------> [ Sent via Network ] ------>|
                                                         | 2. Checks all 5 in
                                                         |    ONE forward pass
       |                                                 |
  4. Accepts valid   <------ [ Returns Bitmap ] <------- 3. Generates Bitmap
     tokens & resets                                       (e.g., [1, 1, 1, 0, 0])
```

1. **The Draft Model (Edge / Laptop):** We load an ultra-lightweight **Small Language Model (SLM)** locally. It is fast but error-prone. It takes your prompt and quickly "guesses" or "drafts" a batch of upcoming tokens (let's say $\gamma = 5$ tokens).
2. **The Target Model (Cloud / Server):** Your laptop packages these 5 drafted tokens and sends them over the network to a remote GPU server running a larger, highly accurate **LLM**.
3. **Single-Pass Verification:** Instead of checking the tokens one by one, the large Cloud model verifies all 5 drafted tokens **simultaneously in a single forward pass**.

### **1.3 What is an Acceptance Bitmap?**
The Cloud server compares the Edge's guesses with its own logits. It returns a list of 1s and 0s called an **Acceptance Bitmap**:
* `1` means the guess was correct and accepted.
* `0` means the guess was incorrect and rejected.

For example, if your laptop drafts: `["Carson", "City", "is", "a", "desert"]`, and the Cloud server determines that the first three words are correct but the fourth should be different, it returns `[1, 1, 1, 0, 0]`.

> [!TIP]
> **Why does this save time?**
> The laptop gets **3 correct tokens** in the time of a single network round-trip! This converts slow network round-trips into a highly efficient speculative handshake.

---

## **2. How the System Works & The Threat Model**

While this collaborative architecture is incredibly fast, it introduces a critical vulnerability when deployed across decentralized or public networks:

* **The Security Threat:** The draft tokens travel over the network as integers (Token IDs). If a malicious router or an attacker intercepts the connection, they can silently alter these integers. This is a **Man-in-the-Middle (MitM) attack**.
* **The Consequences:** A tiny change (even just 10% to 20% of the numbers) will cause the Cloud server to misinterpret the draft completely, leading to corrupted, nonsensical answers and wasting expensive GPU memory (VRAM) processing garbage data.

In this project, you will build the complete collaborative system, write a proxy program that acts as the network attacker to see how it breaks, and then deploy a **Cryptographic Attestation Module** (using SHA-256 secure hashing) to detect tampering and instantly protect the system.

---

## **3. What You Need**

### **3.1 Hardware & Network Connections**
* **Edge Device (Your Laptop):** Your local machine acts as the local "Edge" node running the small draft model.
* **Cloud Device (The Lab Server):** A remote Linux server equipped with a GPU.
* **Network Path:** Both machines must be connected to the same network so they can talk via IP addresses.

### **3.2 Models We Will Use**
* **On Laptop:** `Qwen/Qwen2.5-0.5B-Instruct` (An ultra-small model with 0.5 billion parameters. It requires very little memory and runs comfortably on standard laptop CPUs).
* **On Server:** `Qwen/Qwen2.5-7B-Instruct` (A much larger model with 7 billion parameters. It requires GPU power but acts as our master validation engine).

---

## **4. Build It, Step by Step**

We have provided a starter template package in the `starter_code/` directory, and the complete reference solution in `reference_code/`. Follow these steps in order.

### **Step 0 — Prepare Your Virtual Environment**
Create an isolated Python environment on both your laptop and the GPU server.

```bash
# Create a new virtual environment named 'ret_env'
python3 -m venv ret_env

# Activate the virtual environment
# On Mac/Linux:
source ret_env/bin/activate
# On Windows (PowerShell):
.\ret_env\Scripts\activate

# Install the necessary libraries
pip install torch transformers accelerate numpy requests fastapi uvicorn
```

> [!NOTE]
> Verify your environment is set up by running:
> ```bash
> python -c "import torch, transformers, fastapi; print('Setup Success')"
> ```

---

### **Step 1 — Local Speculative Drafting**
Load the 0.5B model on your laptop and generate a list of draft tokens.

* **Task:** Open `starter_code/edge_draft.py` and complete the `# TODO` sections to load the model and extract the newly drafted token IDs.
* **Command to Run:**
  ```bash
  python edge_draft.py
  ```
* **Checkpoint:** The script prints out the prompt, 5 integer Token IDs, and their decoded text (e.g., `Carson City, which is`).

---

### **Step 2 — Simulating the Verification Process (Laptop Local Mock)**
* **Goal:** Understand the speculative decoding verification rule on your laptop without loading heavy models or writing network code.
* **Concept:** In speculative decoding, if the cloud model rejects a token, it rejects all subsequent tokens in that batch. This step simulates this check using a simple Python list comparison: we mock a mismatch when the token value is `11`.
* **Task:** Open `starter_code/simulate_verify.py` and complete the `# TODO` loop. If a token ID is not equal to `11`, append `1` (accept) to the bitmap. If it is `11`, append `0` (reject) and halt verification (the autoregressive rule).
* **Command to Run:**
  ```bash
  python simulate_verify.py
  ```
* **Checkpoint:** You should see a terminal output showing `Final Generated Acceptance Bitmap: [1, 1, 0]`.

---

### **Intermission — Accessing the GPU Server & Transferring Code**
Before moving to Step 3, we need to run code on the remote GPU server. Since you will be developing code on your laptop, we need to connect to the server and copy your files over:

1. **Access:** Connect to the GPU server using your terminal via SSH:
   ```bash
   ssh username@server-ip-address

   ```



> [!IMPORTANT]
> **Server Setup Requirement**
> Once connected to the server terminal, you must prepare the server virtual environment as shown in **Step 0**:
> ```bash
> # Create folder for your code on the server and enter it
> mkdir -p RET_2026 && cd RET_2026
> 
> # Create and activate the virtual environment
> python3 -m venv ret_env
> source ret_env/bin/activate
> 
> # Install the packages needed on the server
> pip install torch transformers accelerate numpy fastapi uvicorn
> ```



2. **Transfer Code (Create Files on Server):** You can copy the code from your laptop and create the files directly on the server using the `nano` editor:
   * Open the file on the server (e.g., `nano server.py`).
   * Paste the code from the matching file on your laptop.
   * Save and exit: Press `Ctrl + O` to write the file, hit `Enter` to confirm, and press `Ctrl + X` to close the editor.
   * Repeat this process to create `server_secure.py` and `crypto_auth.py` on the server.


---

### **Step 3 — Turning the Cloud Server into a Service (Server Code Execution)**
* **Goal:** Load the actual 7B model on the GPU server, wrap speculative verification in a web API using **FastAPI**, and run the service.
* **Concept:** We will make the server run a web server using `uvicorn` on port `8000`. It will listen for incoming HTTP POST requests containing draft tokens from your laptop and evaluate them using the real `Qwen/Qwen2.5-7B-Instruct` model.
* **Task:** Transfer your code to the server (following the Intermission guide). Open `server.py` on the server, implement the speculative decoding verification logic inside the `/verify` route handler, and start the service.
* **Command to Run (Execute in the GPU Server Terminal):**
  ```bash
  python server.py
  ```
* **Checkpoint:** The terminal prints `INFO: Uvicorn running on http://0.0.0.0:8000` and does not crash. This confirms the 7B model loaded successfully into GPU memory and the server is waiting for network requests. (Note: We will not query the server from the laptop until Step 4).

---

### **Step 4 — Connect Laptop to Server & Test Connection**
* **Goal:** Verify that your laptop and the remote GPU server can talk to each other over the network, and run the distributed system end-to-end for the first time.
* **Concept:** We will run the target model service on the server first, configure our laptop client with the server's IP address, send the hardcoded testing payload, and inspect the logs on both sides.
* **Testing Procedure:**
  1. **Start the Server:** On your remote GPU server terminal (connected via SSH), start the server script and keep it running:
     ```bash
     # [On GPU Server Terminal]
     python server.py
     ```
     *Do not close this terminal window! The server must stay active to receive requests.*
  2. **Configure Client IP:** On your laptop, open `starter_code/edge_full.py`. Find the line `SERVER_IP = "localhost"` and replace `"localhost"` with the actual IP address of the GPU server (e.g., `"192.168.1.55"`).
  3. **Complete Request Code:** Complete the `# TODO` inside `starter_code/edge_full.py` to send the HTTP POST request to the server URL.
  4. **Run the Client:** Open a terminal on your laptop, activate your local environment, and execute the client:
     ```bash
     # [On Laptop Terminal]
     python edge_full.py
     ```
* **Checkpoint:** 
  * **On your Laptop Console:** You should see a successful network response printing the network round-trip time (latency) and the returned acceptance bitmap from the cloud model (e.g., `[1, 1, 1, 1, 1]` or similar).
  * **On the GPU Server Console:** You should see active connection logs:
    ```
    Received incoming request!
    Client Prompt: The capital of Nevada is
    Draft IDs to verify: [1243, 4322, 11, 432, 99]
    Generated Acceptance Bitmap: [1, 1, 1, 1, 1]
    ```

---

### **Step 5 — Measure System Performance (Your Research Baseline)**
* **Goal:** Instead of manually testing prompts, in actual LLM research we evaluate performance on benchmark datasets. In this step, we will load prompts from `sharegpt_subset.json` (a small representative subset of the **ShareGPT** dataset, a common dataset used to evaluate and train large language models) and run an automated benchmark to measure key performance metrics.
* **Benchmark Metrics to Measure:**
  1. **Network Latency (seconds):** The total round-trip time from when your laptop client sends the HTTP verification request containing local draft tokens until it receives and parses the response from the GPU server.
  2. **Token Acceptance Rate (%):** The percentage of draft tokens verified as correct and accepted by the cloud model out of the total drafted tokens (calculated as `sum(bitmap) / len(draft_tokens) * 100`). A higher acceptance rate means the tiny model's guesses align better with the giant model, saving more time.
  3. **Average System Statistics:** The cumulative averages computed across all 15 prompts in the dataset, providing a baseline comparison to evaluate system performance.
* **Task:** 
  1. Open `sharegpt_subset.json` in your local `starter_code/` folder to see how prompt datasets are structured in JSON list format.
  2. Open `starter_code/benchmark.py` on your laptop. Set the `SERVER_IP` to your server's IP address.
  3. Complete the `# TODO` sections to load prompts from the dataset, generate drafts locally, query the server, and calculate average metrics.
  4. Make sure both `benchmark.py` and `sharegpt_subset.json` are in the same folder on your laptop.
* **Command to Run on Laptop:**
  ```bash
  # Ensure server.py is still running on the GPU server!
  # [On Laptop Terminal]
  python benchmark.py
  ```
* **Checkpoint:** The script successfully loads the dataset prompts, runs all queries sequentially, prints a formatted table of results to your console, and outputs a summary file named `benchmark_results.txt`. Record your average latency and acceptance rate; this is your clean, benign research baseline.



---

### **Step 6 — Implement the Man-in-the-Middle Attack**
* **Goal:** Simulate a **Man-in-the-Middle (MitM) Attack** where a malicious router intercepts your network packet, inspects the draft tokens, and modifies them in transit to break the AI's response.
* **What is the Attacker script?**
  * The file `attacker_mitm.py` represents the malicious actor. It is a FastAPI server that runs on a separate port (**port 8001**).
  * It intercepts incoming payload packets, tampers with them, and then forwards the corrupted payload to the real server on **port 8000**.
* **How is Interception Simulated?**
  * In a real cyberattack, an attacker would hijack network routing (e.g., via DNS spoofing or ARP poisoning) to force your laptop's traffic to go through their machine. 
  * In this lab, we simulate this routing hijack simply by changing the client URL on our laptop to point to the attacker's port (**8001**) instead of the server's port (**8000**).
* **Task:** Open `starter_code/attacker_mitm.py` on your laptop. Complete the attack logic to intercept the payload, overwrite a random draft token with the junk value `99999`, print an alert message, and forward the tampered payload to the server.
* **Commands to Run:**
  1. Open a **new terminal window** on your laptop, activate your environment, and run the attacker script:
     ```bash
     # [On Laptop Terminal 2]
     python attacker_mitm.py
     ```
  2. Open your local `starter_code/edge_full.py` and modify the server URL port from `8000` to `8001` (routing traffic through the attacker):
     ```python
     URL = f"http://{SERVER_IP}:8001/verify"
     ```
  3. Execute the client script on your laptop:
     ```bash
     # [On Laptop Terminal 1]
     python edge_full.py
     ```
* **Checkpoint:** 
  * **On the Attacker Console (Terminal 2):** You should see an alert log indicating that a token index was overwritten with bad data.
  * **On the Client Console (Terminal 1):** You will see the server's response. Because the token was corrupted, the server rejects subsequent tokens, resulting in a zero acceptance rate or garbled outputs. You have successfully simulated a live cyber exploit!

---

### **Step 7 — Deploy Cryptographic Attestation Defense**
Protect the system from payload tampering by signing the token package with a secure digital signature.

```
[ edge_secure.py ]                     [ attacker_mitm.py ]                 [ server_secure.py ]
Signs tokens with key                  Tampers with tokens                  Verifies signature
and sends payload                      and forwards payload                 using pre-shared key
       |                                        |                                     |
(Tokens, Signature) ------------------> (Corrupted, Signature) ------------>  Re-computes signature;
                                                                            Mismatch detected!
                                                                            Inference rejected.
```

* **Task:**
  1. Open `starter_code/crypto_auth.py` and implement `generate_signature` and `verify_signature` using the SHA-256 algorithm and the pre-shared secret key.
  2. Open `starter_code/edge_secure.py`. Complete the logic to generate a signature for the tokens and include it in the request payload.
  3. Open `starter_code/server_secure.py`. Complete the security check logic to verify the incoming signature. If the signature is missing or fails authentication, reject the request.
* **Commands to Run:**
  1. Terminate the previous server and launch the secure version on the server (port 8000):
     ```bash
     python server_secure.py
     ```
  2. Keep the attacker running on your laptop (port 8001).
  3. Run the secure client script on your laptop:
     ```bash
     python edge_secure.py
     ```
* **Checkpoint:** The server detects the signature mismatch caused by the attacker's token tampering, aborts inference immediately, and returns a `SECURITY ALERT: Data payload tampering detected` status message.

---


## **5. Security & Defense Concepts Covered**

* **Token Splicing & Tampering:** How network intermediaries can silently modify token arrays to disrupt distributed context windows.
* **Cryptographic Attestation (HMAC-like):** Running hash functions with a shared secret key to generate digital signatures that verify data integrity.
* **Fail-Secure System Design:** Forcing distributed clusters to reject requests and abort operations (saving GPU VRAM) when validating bad credentials or tampered data.

---

## **6. Troubleshooting Guide**

| Issue | Root Cause & Resolution |
| :--- | :--- |
| `ModuleNotFoundError: No module named 'transformers'` | Your virtual environment is not active or you forgot to install packages. Run `source ret_env/bin/activate` and try again. |
| Laptop runs extremely slowly during Step 1 | Ensure you loaded the small `0.5B` model locally. Loading the heavy `7B` model on CPU will exhaust RAM. |
| `Connection refused` error | Ensure `server.py` is actively running on the target machine and check your IP addresses/port configurations. |
| Attack proxy does not change the bitmap | Ensure `edge_full.py` is pointing to port `8001` (the proxy) rather than port `8000` (the direct server). |
