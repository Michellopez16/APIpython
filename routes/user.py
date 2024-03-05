from fastapi import APIRouter
from pydantic import BaseModel
from uuid import uuid4 as uuid
from cryptography.fernet import Fernet


user = APIRouter()

key = Fernet.generate_key()
fernet = Fernet(key)

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

@user.get("/posts/{user_id}")
def get_posts(user_id: str):
    for post in posts:
        if post["id"] == user_id:
            return post
    return "No se encontro el usuario"

@user.post("/posts")
def create_posts(post: Post):
    post.id = str(uuid())
    encrypted_password = fernet.encrypt(post.password.encode())
    post.password = encrypted_password
    posts.append(dict(post))
    return posts[-1]


@user.delete("/posts/{user_id}")
def delete_posts(user_id: str):
    for index,post in enumerate(posts):
        if post["id"] == user_id:
            posts.pop(index)
            return "Usuario correctamente eliminado"
    return "No se encontro el usuario"


@user.put("/posts/{user_id}")
def update_posts(user_id: str,updatePost: Post):
    for index,post in enumerate(posts):
        if post["id"] == user_id:
            posts[index]["username"] = updatePost.username
            posts[index]["email"] = updatePost.email
            encrypted_password = fernet.encrypt(post.password.encode())
            posts[index]["password"] = encrypted_password
            #posts[index]["password"] = updatePost.password
            posts[index]["active"] = updatePost.active
            return "Usuario correctamente actualizado"
    return "No se encontro el usuario"