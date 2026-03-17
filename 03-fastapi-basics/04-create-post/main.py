from fastapi import FastAPI, status
from models import Post
from random import randrange

app = FastAPI()

my_post = []

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(new_post: Post):
    post_dict = new_post.dict()
    post_dict["id"] = randrange(0, 1000)
    my_post.append(post_dict)
    return {"data": post_dict}