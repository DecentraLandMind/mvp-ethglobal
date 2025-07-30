import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from nacl.public import PrivateKey, SealedBox
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_DIR, "..", "logs", "encryption_logs.txt")
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

def log_message(action: str, data: dict):
    with open(LOG_PATH, "a") as log_file:
        timestamp = datetime.utcnow().isoformat()
        log_file.write(f"[{timestamp}] {action.upper()} - {data}\n")

def decrypt_payload(encrypted_key: str, encrypted_payload: str, nonce: str) -> str:
    PRIVATE_KEY_BASE64 = "IF+alcQWuNRx5ZIEUspk0C4rDMuMJ4xxfRkS6xH56BI="
    private_key = PrivateKey(base64.b64decode(PRIVATE_KEY_BASE64))
    sealed_box = SealedBox(private_key)

    aes_key = sealed_box.decrypt(base64.b64decode(encrypted_key))

    nonce_bytes = base64.b64decode(nonce)
    ciphertext = base64.b64decode(encrypted_payload)

    cipher = AES.new(aes_key, AES.MODE_GCM, nonce=nonce_bytes)
    decrypted = cipher.decrypt_and_verify(ciphertext[:-16], ciphertext[-16:])
   
    # log just for debug
    # decrypted_text = decrypted.decode("utf-8")
    # log_message("decrypt", {
    #         "encrypted_key": encrypted_key,
    #         "encrypted_payload": encrypted_payload,
    #         "nonce": nonce,
    #         "decrypted_text": decrypted_text
    #     })

    return decrypted.decode("utf-8"), aes_key, nonce_bytes


def encrypt_response(response_text: str, key: bytes, nonce: bytes) -> str:
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    encrypted, tag = cipher.encrypt_and_digest(response_text.encode("utf-8"))
    payload = encrypted + tag

    encrypted_data = {
        "payload": base64.b64encode(encrypted).decode(),
        "key": base64.b64encode(key).decode(),
        "nonce": base64.b64encode(nonce).decode()
    }
    # log just for debug
    # log_message("encrypt", {
    #     "response_text": response_text,
    #     **encrypted_data
    # })
    return base64.b64encode(payload).decode()
