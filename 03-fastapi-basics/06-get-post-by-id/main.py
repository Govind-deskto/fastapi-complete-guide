from fastapi import FastAPI, HTTPException

app = FastAPI()

my_post = [
    {"title": "title 1", "content": "content 1", "id": 1},
    {"title": "title 2", "content": "content 2", "id": 2}
]

def find_post(id):
    for p in my_post:
        if p["id"] == id:
            return p

@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"data": post}