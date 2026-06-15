from fastapi import FastAPI
import uvicorn
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import crypto_auth  # Import the cryptographic module

app = FastAPI()

MODEL_NAME = "Qwen/Qwen2.5-7B-Instruct"
device = "cuda" if torch.cuda.is_available() else "cpu"

print(f"Loading Target Model '{MODEL_NAME}' onto {device}...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16 if device == "cuda" else torch.float32,
    device_map="auto" if device == "cuda" else None
)
print("Target Model loaded successfully! Secure server is ready.")

@app.post("/verify")
def secure_verify_handler(payload: dict):
    tokens = payload.get("draft_tokens", [])
    client_signature = payload.get("signature")
    prompt_text = payload.get("prompt", "")
    
    print(f"\nReceived incoming request!")
    print(f"Client Prompt: {prompt_text}")
    print(f"Draft IDs to verify: {tokens}")
    print(f"Client Signature: {client_signature}")
    
    # TODO: Implement the security verification steps
    # Hint:
    # Step 1: Check if signature is provided.
    #         If client_signature is None or empty, log a security alert and return a Rejected response dict:
    #         { "bitmap": [], "status": "Rejected", "message": "SECURITY ALERT: Request rejected. Cryptographic signature is missing." }
    #
    # Step 2: Verify signature integrity.
    #         Call crypto_auth.verify_signature(tokens, client_signature).
    #         If it returns False, print a security exploit message and return a Rejected response dict:
    #         { "bitmap": [], "status": "Rejected", "message": "SECURITY ALERT: Data payload tampering detected in transit. Inference aborted." }
    #
    # If both steps pass, print a verified success message and run speculative decoding inference.
    
    # [Write your security check logic here]
        
    print("[SECURITY VERIFIED]: Proceeding to inference...")
    
    # --- SPECULATIVE DECODING VERIFICATION ---
    prompt_inputs = tokenizer(prompt_text, return_tensors="pt")
    prompt_ids = prompt_inputs.input_ids[0].tolist()
    
    input_ids_list = prompt_ids + tokens
    input_ids = torch.tensor([input_ids_list]).to(device)
    
    with torch.no_grad():
        outputs = model(input_ids)
        logits = outputs.logits[0]
        
    acceptance_bitmap = []
    start_idx = len(prompt_ids) - 1
    
    for idx, draft_token in enumerate(tokens):
        logit_pos = start_idx + idx
        next_token_logits = logits[logit_pos]
        predicted_token = torch.argmax(next_token_logits).item()
        
        if draft_token == predicted_token:
            acceptance_bitmap.append(1)
        else:
            acceptance_bitmap.append(0)
            break
            
    print(f"Generated Acceptance Bitmap: {acceptance_bitmap}")
    return {
        "bitmap": acceptance_bitmap,
        "status": "Success",
        "message": "Target model verification completed."
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
