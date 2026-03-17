# ⚙️ Setup & Installation

## 🐍 Install Python

Download Python from official website:
https://www.python.org/

Check installation:

```bash
python --version
```

## 💻 Install VS Code

Download VS Code:
https://code.visualstudio.com/

Install Python extension.

## 📦 Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

## 📥 Install FastAPI

```bash
pip install fastapi uvicorn
```

## ▶️ Run Server

```bash
uvicorn main:app --reload
```

## 🌐 Open in Browser

http://127.0.0.1:8000

Docs:
http://127.0.0.1:8000/docs
