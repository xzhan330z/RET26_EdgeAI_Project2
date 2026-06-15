import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

print("Loading the 0.5B Draft Model onto CPU...")
model_name = "Qwen/Qwen2.5-0.5B-Instruct"

# TODO: Load the tokenizer and the model
# Hint: Use AutoTokenizer.from_pretrained(model_name) and AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float32)
tokenizer = None
model = None

prompt = "The capital of Nevada is"

# Tokenize prompt to get model inputs
inputs = tokenizer(prompt, return_tensors="pt") if tokenizer else None

if inputs:
    print(f"Original Text Prompt: '{prompt}'")
    print(f"Converted into mathematical Token IDs: {inputs.input_ids.tolist()[0]}")

    # Instruct the small model to guess/draft the next 5 tokens
    # TODO: Complete the model.generate call to get next 5 tokens (max_new_tokens=5, min_new_tokens=5, do_sample=False)
    # Make sure to run inside 'with torch.no_grad():' to save CPU memory and speed up computation.
    with torch.no_grad():
        outputs = None # Replace with model.generate(...)

    if outputs:
        # TODO: Extract just the newly drafted tokens from the output sequences.
        # Hint:
        # 1. Access the sequences tensor: outputs.sequences[0]
        # 2. Extract the slice after inputs.input_ids.shape[1] to skip prompt tokens.
        # 3. Convert the tensor to a list: .tolist()
        draft_tokens = [] 

        print("\n--- RESULTS ---")
        print(f"Drafted Token IDs (Numbers to send over network): {draft_tokens}")
        print(f"Decoded Text: '{tokenizer.decode(draft_tokens)}'")
else:
    print("Please implement the tokenizer and model loading logic first.")
