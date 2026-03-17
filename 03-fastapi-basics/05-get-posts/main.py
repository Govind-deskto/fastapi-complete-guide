from fastapi import FastAPI

app = FastAPI()

my_post = [
    {"title": "title 1", "content": "content 1", "id": 1},
    {"title": "title 2", "content": "content 2", "id": 2}
]

@app.get("/posts")
def get_posts():
    return {"data": my_post}