import subprocess
import os
from app.config import MODEL_DIR, MODEL_FILE, DOCKER_IMAGE, EXECUTABLE

def run_model(prompt: str) -> str:
    result = subprocess.run([
        "docker", "run", "--rm",
        "-v", f"{MODEL_DIR}:/app/models",
        DOCKER_IMAGE,
        EXECUTABLE,
        f"file://models/{MODEL_FILE}",
        prompt
    ], capture_output=True, text=True)
