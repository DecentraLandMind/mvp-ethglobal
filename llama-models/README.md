# LLaMA Server (TinyLlama + Docker)
This project provides a simple setup to run the [TinyLlama 1.1B Chat](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF) model inside a Docker container using `llama.cpp`.

---

## 📁 Project Structure

```

llama-server/
├── Dockerfile
├── models/
│   └── tinyllama-1.1b-chat-v1.0.Q4\_K\_M.gguf

````

---

## ⚙️ Step-by-step Setup

### 1. Install dependencies

Make sure your system has Python 3, Docker, and the required build tools:

```bash
sudo apt update && sudo apt install -y python3-pip git curl build-essential cmake
pip3 install huggingface-hub hf_transfer
export HF_HUB_ENABLE_HF_TRANSFER=1
````

---

### 2. Download the model

Create the project directory and download the model using `huggingface-cli`:

```bash
mkdir -p llama-server/models
cd llama-server

huggingface-cli download TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF \
  tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf \
  --local-dir ./models \
  --local-dir-use-symlinks False
```

---

### 3. Dockerfile

Here's the `Dockerfile` used to build the image:

```Dockerfile
FROM ubuntu:22.04

RUN apt update && apt install -y \
  git build-essential cmake curl \
  libopenblas-dev pkg-config libcurl4-openssl-dev

WORKDIR /app

RUN git clone https://github.com/ggml-org/llama.cpp . && \
    cmake -B build -DGGML_BLAS=ON -DGGML_BLAS_VENDOR=OpenBLAS \
      -DLLAMA_CURL=ON && \
    cmake --build build --config Release

COPY models/ ./models/

CMD ["./build/bin/main", "-m", "models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf", "-p", "Hello!"]
```

---

### 4. Build the Docker image

In the same directory as the `Dockerfile`, run:

```bash
docker build -t llama-runner .
```

---

### 5. Test the model

Once built, test the model using:

```bash
docker run --rm llama-runner ./build/bin/llama-run file://models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf "What is decentralization?"
```

---

## 🧠 Notes

* You can mount external models via `-v` if needed.
* For custom prompts or batch processing, edit the CMD or use `subprocess` in Python.

---

## 📜 License

This project uses [`llama.cpp`](https://github.com/ggml-org/llama.cpp), licensed under MIT.
