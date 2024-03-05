from fastapi import FastAPI
from routes.user import user

#Implementar las operaciones CRUD en una API REST con FastAPI

app = FastAPI()


app.include_router(user)

#crear una ruta
@app.get("/")
def binvenida():
    return {"bienvenida": "Hola a fastapi"}


@app.get("/saludo")
def binvenida():
    return "Hola a fastapi"



    