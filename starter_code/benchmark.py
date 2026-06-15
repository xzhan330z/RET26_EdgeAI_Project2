import requests
import time
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# 1. Initialize local draft model
print("Loading local draft model...")
DRAFT_MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(DRAFT_MODEL_NAME)
draft_model = AutoModelForCausalLM.from_pretrained(DRAFT_MODEL_NAME, torch_dtype=torch.float32)

# Server address configuration (change "localhost" to your server's IP if needed)
SERVER_IP = "localhost"
SERVER_URL = f"http://{SERVER_IP}:8000/verify"

# Load dataset prompts (ShareGPT subset)
import json
import sys

try:
    with open("sharegpt_subset.json", "r", encoding="utf-8") as dataset_file:
        dataset = json.load(dataset_file)
    PROMPTS = [item["conversations"][0]["value"] for item in dataset]
    print(f"Successfully loaded {len(PROMPTS)} prompts from sharegpt_subset.json")
except Exception as e:
    print(f"CRITICAL ERROR: Could not load sharegpt_subset.json ({e}).")
    print("Please ensure 'sharegpt_subset.json' is in the same directory as this script.")
    sys.exit(1)



print(f"\nStarting benchmark on {len(PROMPTS)} prompts...")

# Prepare headers for printing
header_line = f"{'Prompt':<45} | {'Latency (s)':<12} | {'Acceptance Rate':<15} | {'Bitmap':<15}"
separator_line = "-" * 95

print(header_line)
print(separator_line)

output_file_path = "benchmark_results.txt"
with open(output_file_path, "w", encoding="utf-8") as f:
    f.write("===============================================================================================\n")
    f.write("                       SPECULATIVE DECODING SYSTEM BENCHMARK RESULTS                           \n")
    f.write("===============================================================================================\n")
    f.write(header_line + "\n")
    f.write(separator_line + "\n")
    
    total_latency = 0
    total_accepted = 0
    total_drafted = 0
    success_count = 0
    
    for prompt in PROMPTS:
        # TODO: Implement the benchmark logic for this prompt
        # Hint:
        # 1. Tokenize prompt: inputs = tokenizer(prompt, return_tensors="pt")
        # 2. Get prompt length: prompt_len = inputs.input_ids.shape[1]
        # 3. Generate exactly 5 tokens with draft_model:
        #    outputs = draft_model.generate(**inputs, max_new_tokens=5, min_new_tokens=5, do_sample=False)
        # 4. Slice outputs to get draft_tokens: outputs[0][prompt_len:].tolist()
        # 5. Package as payload: payload = {"prompt": prompt, "draft_tokens": draft_tokens}
        # 6. Record start time, POST payload to SERVER_URL, parse JSON response, and record latency.
        # 7. Extract 'bitmap' from response. Calculate accepted_count = sum(bitmap) and drafted_count = len(draft_tokens).
        # 8. Compute acceptance_rate = (accepted_count / drafted_count) * 100
        
        # [Write your implementation here]
        
        # Once you have the data, you can log it by uncommenting and adjusting the following lines:
        """
        latency = 0.0 # Change me
        acceptance_rate = 0.0 # Change me
        bitmap = [] # Change me
        accepted_count = 0 # Change me
        drafted_count = 5 # Change me
        
        total_latency += latency
        total_accepted += accepted_count
        total_drafted += drafted_count
        success_count += 1
        
        short_prompt = prompt if len(prompt) < 42 else prompt[:40] + "..."
        row_data = f"{short_prompt:<45} | {latency:<12.4f} | {acceptance_rate:<13.1f}% | {str(bitmap):<15}"
        print(row_data)
        f.write(row_data + "\n")
        """
        pass
            
    # 4. Print Summary Statistics
    if success_count > 0:
        avg_latency = total_latency / success_count
        overall_acceptance_rate = (total_accepted / total_drafted) * 100 if total_drafted > 0 else 0.0
        summary_line = f"{'AVERAGES / TOTALS':<45} | {avg_latency:<12.4f} | {overall_acceptance_rate:<13.1f}%"
        
        print(separator_line)
        print(summary_line)
        
        f.write(separator_line + "\n")
        f.write(summary_line + "\n")
        f.write("===============================================================================================\n")
    else:
        print("\nAll benchmark queries failed. Please check server status.")

print(f"\n[BENCHMARK COMPLETE] Results successfully saved to: {output_file_path}")
