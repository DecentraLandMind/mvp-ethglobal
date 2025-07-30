FROM ubuntu:22.04

RUN apt update && apt install -y \
  git build-essential cmake curl \
  libopenblas-dev pkg-config libcurl4-openssl-dev

WORKDIR /app

RUN git clone https://github.com/ggml-org/llama.cpp . && \
    cmake -B build -DGGML_BLAS=ON -DGGML_BLAS_VENDOR=OpenBLAS \
      -DLLAMA_CURL=ON \
      && cmake --build build --config Release

COPY models/ ./models/

CMD ["./build/bin/main", "-m", "models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf", "-p", "Hello!"]
