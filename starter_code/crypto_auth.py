import hashlib
import json

# Pre-shared secret key for calculating the signature
SECRET_KEY = "UNR_speculative_decoding_secret_key"

def generate_signature(tokens):
    """
    Converts a list of token IDs into a JSON string, combines it with the secret key,
    and returns its SHA-256 hash.
    """
    # TODO: Implement this function.
    # Hint:
    # 1. Convert the 'tokens' list into a string using json.dumps(tokens)
    # 2. Concatenate the token string, a colon ':', and the SECRET_KEY (e.g. f"{token_string}:{SECRET_KEY}")
    # 3. Encode the concatenated message to bytes using .encode('utf-8')
    # 4. Use hashlib.sha256(message).hexdigest() to calculate and return the SHA-256 fingerprint.
    pass

def verify_signature(tokens, signature):
    """
    Recomputes the signature for the given tokens and compares it with the client-supplied signature.
    """
    # TODO: Implement this function.
    # Hint:
    # 1. Generate the expected signature by calling generate_signature(tokens)
    # 2. Compare the expected signature with the client's signature.
    # 3. Return True if they match, and False otherwise.
    pass
