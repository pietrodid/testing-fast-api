from fastapi import FastAPI
from .users import Usuario
import json
import csv

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/items/{nombre}")
def read_nombre(nombre: str, q: str= None):
    return {"nombre": nombre}

@app.get("/get_name/{name}")
def get_name_by_string(name: str):
    return {"data": name}

@app.get("/get_perro/{name}")
def perro_de_agua_string(name: str):
    return {"data": name}

@app.get("/get_suma/{inta}/{intb}")
def get_suma(inta: int, intb: int):
    return {"total": inta + intb}

@app.get("/get_division/{inta}/{intb}")
def get_dividir(inta: int, intb: int):
    return {"total": inta // intb}

@app.get("/get_multiplicar/{inta}/{intb}")
def get_multiplicar(inta: int, intb: int):
    return{"total": inta * intb}

@app.post("/user/")
def get_usuario(user: Usuario):
    f = open("./db/db.txt", "a")
    json_user = json.dumps(user.__dict__)
    f.write(json_user + "\n")
    f.close()
    return user

@app.post("/new/")
def new_user(user: Usuario): 
    with open("./db/new.csv", "a") as csvfile:
        writer = csv.writer(csvfile)
        data = user.__dict__
        print(data.values())
        writer.writerow(data.values()) 
 
    return user     


