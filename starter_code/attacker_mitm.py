from fastapi import FastAPI
import requests
import random
import uvicorn

app = FastAPI()

# Target server URL (change 'localhost' to the server's IP address if running across different hosts)
REAL_SERVER_URL = "http://localhost:8000/verify"

@app.post("/verify")
def intercept_and_tamper(payload: dict):
    corrupted_tokens = list(payload.get("draft_tokens", []))
    
    # TODO: Implement the token tampering attack
    # Hint:
    # 1. Check if the corrupted_tokens list is not empty.
    # 2. Pick a random index: malicious_index = random.randint(0, len(corrupted_tokens) - 1)
    # 3. Overwrite the token at that index with an invalid token ID like 99999 to simulate a payload corrupting attack.
    # 4. Print a message indicating that the attacker has overwritten the token.
    
    # [Write your attack tampering here]

    # Substitute the clean draft tokens with the tampered ones
    payload["draft_tokens"] = corrupted_tokens
    
    # Forward the compromised payload onwards to the real server
    try:
        response = requests.post(REAL_SERVER_URL, json=payload)
        return response.json()
    except Exception as e:
        return {
            "bitmap": [],
            "status": "Error",
            "message": f"Attacker failed to forward request to real server at {REAL_SERVER_URL}: {e}"
        }

if __name__ == "__main__":
    # Runs on port 8001 to sit in the middle of client (pointing to 8001) and server (running on 8000)
    uvicorn.run(app, host="0.0.0.0", port=8001)
