from pydantic import BaseModel

class Usuario(BaseModel):
    nombre:str
    apellido: str
    edad: int
    sexo: str