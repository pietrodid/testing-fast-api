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

@app.get("/get_suma/{inta}/{intb}")
def get_suma(inta: int, intb: int):
    return {"total": inta + intb}

@app.get("/get_division/{inta}/{intb}")
def get_dividir(inta: int, intb: int):
    return {"total": inta // intb}

@app.get("/get_multiplicar/{inta}/{intb}")
def get_multiplicar(inta: int, intb: int):
    return{"total": inta * intb}