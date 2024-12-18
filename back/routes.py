from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import SalaDeEstudo, Biblioteca
from log import logger
from schemas import SalaBase
from fastapi import Query

router = APIRouter()


router = APIRouter()

# Cadastro de Salas de Estudo
@router.post("/salas")
async def cadastrar_sala(sala: SalaBase, db: Session = Depends(get_db)):
    """
    Endpoint para cadastrar uma nova sala de estudo.
    """
    try:
        # Verifica se a sala já existe
        sala_existente = db.query(SalaDeEstudo).filter_by(
            numero=sala.numero, andar=sala.andar, biblioteca_id=sala.biblioteca_id
        ).first()

        if sala_existente:
            raise HTTPException(status_code=400, detail="Sala já cadastrada.")

        # Cria um novo objeto SalaDeEstudo
        nova_sala = SalaDeEstudo(
            nome=sala.nome,
            numero=sala.numero,
            andar=sala.andar,
            capacidade=sala.capacidade,
            disponibilidade=sala.disponibilidade,
            biblioteca_id=sala.biblioteca_id
        )

        # Adiciona ao banco de dados
        db.add(nova_sala)
        db.commit()
        db.refresh(nova_sala)

        return {"message": "Sala cadastrada com sucesso!", "sala_id": nova_sala.numero}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao cadastrar sala: {str(e)}")

# Pesquisa de Salas de Estudos
@router.get("/busca-sala")
def buscar_sala(
    numero: int,
    andar: int = Query(None),
    biblioteca_id: int = Query(None),
    capacidade: float = Query(None),
    disponibilidade: bool = Query(None),
    db: Session = Depends(get_db)
):
    """
    Busca por salas baseadas nos filtros fornecidos.
    """
    try:
        query = db.query(SalaDeEstudo).filter(SalaDeEstudo.numero == numero)

        if andar:
            query = query.filter(SalaDeEstudo.andar == andar)
        if biblioteca_id:
            query = query.filter(SalaDeEstudo.biblioteca_id == biblioteca_id)
        if capacidade:
            query = query.filter(SalaDeEstudo.capacidade >= capacidade)
        if disponibilidade is not None:
            query = query.filter(SalaDeEstudo.disponibilidade == disponibilidade)

        salas = query.all()

        if not salas:
            raise HTTPException(status_code=404, detail="Nenhuma sala encontrada.")

        return {"salas": [sala.__dict__ for sala in salas]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")
    
# Pesquisa de bibliotecas presentes no banco
@router.get("/bibliotecas")
async def listar_bibliotecas(db: Session = Depends(get_db)):
    """
    Endpoint para listar todas as bibliotecas.
    """
    try:
        # Consultar todas as bibliotecas no banco de dados
        bibliotecas = db.query(Biblioteca).all()

        # Retornar os dados em formato JSON
        return {"bibliotecas": [{"idBiblioteca": b.idBiblioteca, "nome": b.nome} for b in bibliotecas]}
    except Exception as err:
        logger.error(f"Erro ao listar bibliotecas: {err}")
        raise HTTPException(
            status_code=500,
            detail="Erro interno ao buscar bibliotecas."
        )
