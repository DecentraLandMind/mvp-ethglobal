# 🧠 DecentraMind MVP

A privacy-preserving decentralized AI system designed to demonstrate secure interaction between a user dApp and a local LLM inference node. This MVP encrypts all communication using modern cryptography and executes LLMs inside isolated containers to simulate privacy-first AI processing at the edge.

---

## 📦 Project Structure

```

decentramind-mvp/
├── llm-node/                  # Secure LLM inference node (FastAPI + Docker)
│   ├── app/
│   │   ├── main.py            # Entry point (FastAPI server)
│   │   ├── model\_runner.py    # Model execution (LLM or dummy)
│   │   ├── crypto\_utils.py    # AES & Curve25519 decryption utilities
│   │   └── config.py          # Constants (e.g., keys, model paths)
│   ├── Dockerfile             # Containerized LLM runtime
│   ├── requirements.txt       # Python dependencies
│   └── README.md              # Node-specific instructions

├── client-dapp/              # Frontend Web3 dApp (Next.js + Tailwind)
│   ├── src/
│   │   ├── components/        # Chat UI, input box, message list
│   │   └── lib/
│   │       ├── crypto.ts      # Curve25519 + AES-GCM encryption (client → node)
│   │       └── decrypt.ts     # Decryption for LLM responses
│   ├── public/                # Static assets
│   ├── tailwind.config.js
│   ├── package.json
│   └── README.md              # Frontend-specific instructions

├── .gitignore
└── README.md                  # You're here!

````

---

## 🚀 How It Works

1. User connects via MetaMask wallet in the dApp.
2. Message is encrypted using Curve25519 + AES-256-GCM.
3. Encrypted payload is sent via REST to a local or remote LLM node.
4. LLM Node decrypts payload, runs a model inside Docker sandbox, returns encrypted response.
5. Client decrypts and displays the output.

**✅ Fully encrypted**, **⛓️ On-chain identity (public key = wallet)**, **🧱 Edge-first private inference.**

---

## 🔐 Cryptography

- **Key Exchange:** X25519 (NaCl box sealing)
- **Symmetric Encryption:** AES-256-GCM
- **Transport:** REST (can be upgraded to HTTPS + gRPC)
- **Optional:** IPFS for encrypted chat log storage

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/DecentraLandMind/decentramind-mvp.git
cd decentramind-mvp
````

### 2. Backend – Secure LLM Node

```bash
cd llm-node
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 9000
```

### 3. Frontend – Web3 dApp

```bash
cd client-dapp
npm install
npm run dev
```

Open in browser: `http://localhost:3000`

---

## 🧪 Testing Flow

1. Connect MetaMask
2. Write a message (e.g., “Hello AI”)
3. Watch it get encrypted → securely sent → model replies back encrypted
4. Decrypt and display output in chat

---

## 🧱 Technologies Used

* 🔐 **PyNaCl / AES** for secure payloads
* ⚡ **FastAPI** for inference node
* 🧠 **llama.cpp** or dummy model runner (Docker)
* 🔗 **MetaMask + Ethers.js** for auth
* 💬 **Next.js + Tailwind CSS** frontend

---

## 📌 Security Notes

* Keys are never stored or logged in plaintext.
* AES session keys are ephemeral per message.
* The model runs in an isolated Docker container (optional Firecracker VM support).
* IPFS support is ready for encrypted output pinning.
* Node-level slashing/reputation not included in MVP but considered in full protocol.

---

## 📬 Contact

Want to collaborate or invest?
**Email:** `decentramind.info@gmail.com`
**Telegram:** `https://t.me/ArmanPayandeh`
**Site:** coming soon…

---

## Demo

[📹 Screencast.webm](./client-dapp//public/Screencast.webm)

---

Made with ❤️ for the decentralized AI future.
