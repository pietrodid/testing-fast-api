from fastapi import FastAPI

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

@app.get("/get_suma/{suma}")
def get_suma_int(suma: int):
    return{"total": suma, "a+b"}