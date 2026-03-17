# Pydantic Models

## 📌 What is Pydantic?

Used for data validation.

## 🔹 Example

```python
from pydantic import BaseModel

class Post(BaseModel):
    title: str
    content: str
```

## 🧠 Benefits

* Validates input
* Prevents errors
