## 🚀 Run
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 9000
````
## ⚙️ Configuration
Edit system paths and runtime variables in:
```
config.py
```
This file contains all constants such as model path, Docker image name, and executable location.
