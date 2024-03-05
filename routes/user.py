from fastapi import APIRouter
from pydantic import BaseModel
from uuid import uuid4 as uuid

user = APIRouter()

@user.get("/users")
def binvenida():
    return {"bienvenida": "Hola a fastapi en users"}


#Base de datos posts
posts = []

class Post(BaseModel):
    id: str = str(uuid())
    username: str
    email: str
    password: str
    active: bool = True

@user.get("/posts")
def get_posts():
    return posts

@user.post("/posts")
def create_posts(post: Post):
    post.id = str(uuid())
    posts.append(dict(post))
    return posts[-1]