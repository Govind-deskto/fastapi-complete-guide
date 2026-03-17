# Basic FastAPI App

## 📌 What is FastAPI?

FastAPI is a modern Python framework to build APIs.

## 🔹 Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}
```

## 🧠 Key Concept

* `FastAPI()` creates app
* `@app.get()` creates route
