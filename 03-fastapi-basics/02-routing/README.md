# Routing in FastAPI

## 📌 What is Routing?

Routing defines how your API responds to different URLs.

## 🔹 Example

```python
@app.get("/posts")
def get_posts():
    return {"data": "All posts"}
```

## 🧠 Key Concepts

* Each route handles a request
* URL defines behavior
