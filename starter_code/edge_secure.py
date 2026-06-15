import requests
import crypto_auth  # Import the cryptographic library we created

# Pointing to the attacker's port (port 8001) to verify if the attack is detected and blocked
SERVER_URL = "http://localhost:8001/verify" 

tokens = [1243, 4322, 11, 432, 99]

# TODO: Create a secure mathematical signature of our draft tokens using the secret key
# Hint: Call crypto_auth.generate_signature(tokens)
secure_signature = "" # Replace this

payload = {
    "prompt": "The capital of Nevada is",
    "draft_tokens": tokens,
    # TODO: Add the secure signature to the payload JSON so the server can verify it.
    "signature": secure_signature 
}

print(f"Sending signed payload to {SERVER_URL}...")
try:
    response = requests.post(SERVER_URL, json=payload).json()
    print(f"\n--- SERVER SECURITY RESPONSE ---")
    print(f"Status: {response.get('status', 'Unknown')}")
    print(f"Message: {response.get('message', '')}")
    print(f"Returned Bitmap: {response.get('bitmap', [])}")
except Exception as e:
    print(f"Error communicating with server: {e}")
