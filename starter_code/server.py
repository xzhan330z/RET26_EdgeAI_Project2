from fastapi import FastAPI
import uvicorn
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

app = FastAPI()

print("Initializing Server Backend Context...")
MODEL_NAME = "Qwen/Qwen2.5-7B-Instruct"
device = "cuda" if torch.cuda.is_available() else "cpu"

print(f"Loading Target Model '{MODEL_NAME}' onto {device}...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16 if device == "cuda" else torch.float32,
    device_map="auto" if device == "cuda" else None
)
print("Target Model loaded successfully! Server is ready.")

@app.post("/verify")
def verify_endpoint(payload: dict):
    # Extract the data sent by the laptop over the network
    prompt_text = payload.get("prompt", "")
    received_drafts = payload.get("draft_tokens", [])
    
    print(f"\nReceived incoming request!")
    print(f"Client Prompt: {prompt_text}")
    print(f"Draft IDs to verify: {received_drafts}")
    
    if not prompt_text or not received_drafts:
        return {
            "bitmap": [],
            "status": "Error",
            "message": "Missing 'prompt' or 'draft_tokens' in request payload."
        }
    
    # --- SPECULATIVE DECODING VERIFICATION ---
    # Convert prompt text into Token IDs
    prompt_inputs = tokenizer(prompt_text, return_tensors="pt")
    prompt_ids = prompt_inputs.input_ids[0].tolist()
    
    # TODO: Implement verification
    # Hint:
    # 1. Combine prompt_ids and received_drafts into a single list 'input_ids_list'.
    # 2. Convert to a 2D tensor: input_ids = torch.tensor([input_ids_list]).to(device)
    # 3. Get the logits in a torch.no_grad() block: model(input_ids).logits[0]
    # 4. Initialize acceptance_bitmap as empty list.
    # 5. Set start_idx = len(prompt_ids) - 1
    # 6. Loop over received_drafts (enumerate):
    #    - Find logits position: logit_pos = start_idx + idx
    #    - Get next token logits: next_token_logits = logits[logit_pos]
    #    - Find predicted token: predicted_token = torch.argmax(next_token_logits).item()
    #    - If draft_token == predicted_token, append 1 to acceptance_bitmap.
    #    - Else, append 0 and break.
    
    acceptance_bitmap = [] # Implement logic and fill this list
    
    # [Write your verification logic here]
            
    print(f"Generated Acceptance Bitmap: {acceptance_bitmap}")
    
    return {
        "bitmap": acceptance_bitmap,
        "status": "Success",
        "message": "Cloud inference pass completed successfully."
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
