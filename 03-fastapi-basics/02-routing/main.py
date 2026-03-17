from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI"}

@app.get("/posts")
def get_posts():
    return {"data": "All posts"}

@app.get("/posts/{id}")
def get_post(id: int):
    return {"data": f"Post {id}"}