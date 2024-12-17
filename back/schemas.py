from pydantic import BaseModel

# Modelo Pydantic para validação ao cadastrar uma sala
class SalaBase(BaseModel):
    nome: str
    numero: int
    andar: int
    capacidade: float
    disponibilidade: bool
    biblioteca_id: int