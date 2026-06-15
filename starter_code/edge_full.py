import requests
import time

# Set default to localhost for testing. During camp, change this to match your server's IP address.
SERVER_IP = "localhost" 
URL = f"http://{SERVER_IP}:8000/verify"

# Setup the data packet (Payload) containing our text and guesses
payload = {
    "prompt": "The capital of Nevada is",
    "draft_tokens": [279, 1584, 748, 7772, 3283]
}

print(f"Sending 5 Draft Tokens to Cloud Server at: {URL}")
start = time.time()

try:
    # TODO: Send an HTTP POST request carrying our JSON data payload
    # Hint: Use requests.post(URL, json=payload) and extract the JSON dict using .json()
    response = {} # Replace with requests.post(...)
    
    latency = time.time() - start

    if response:
        print("\n--- NETWORK RESPONSE ---")
        print(f"Returned Acceptance Bitmap: {response.get('bitmap', [])}")
        print(f"Server Message: {response.get('message', '')}")
        print(f"Total Network Round-Trip Time: {latency:.4f} seconds")
except Exception as e:
    print(f"Connection error: {e}")
    print("Please make sure the server script is running and your SERVER_IP is set correctly.")
