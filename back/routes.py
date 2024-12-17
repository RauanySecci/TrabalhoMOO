from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import SalaDeEstudo, Biblioteca
from log import logger

router = APIRouter()


# Cadastro de Salas de Estudo
@router.post("/salas")
async def cadastrar_sala(
    nome: str,
    numero: int,
    andar: int,
    capacidade: float,
    disponibilidade: bool,
    biblioteca_id: int,
    db: Session = Depends(get_db)
):
    """
    Endpoint para cadastrar uma nova sala de estudo.
    """
    try:
        # Verifica se a sala já existe
        sala_existente = db.query(SalaDeEstudo).filter_by(
            numero=numero, andar=andar, biblioteca=biblioteca_id
        ).first()

        if sala_existente:
            raise HTTPException(status_code=400, detail="Sala já cadastrada.")

        # Cria um novo objeto SalaDeEstudo
        nova_sala = SalaDeEstudo(
            nome=nome,
            numero=numero,
            andar=andar,
            capacidade=capacidade,
            disponibilidade=disponibilidade,
            biblioteca=biblioteca_id
        )

        # Adiciona ao banco de dados
        db.add(nova_sala)
        db.commit()
        db.refresh(nova_sala)

        return {"message": "Sala cadastrada com sucesso!", "sala_id": nova_sala.numero}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao cadastrar sala: {str(e)}")

# Pesquisa de 
@router.get("/salas-disponiveis")
async def buscar_salas_disponiveis(
    biblioteca_id: int,
    db: Session = Depends(get_db)
):
    """
    Endpoint para buscar salas disponíveis por biblioteca.
    """
    try:
        # Verificar se a biblioteca existe
        biblioteca = db.query(Biblioteca).filter(Biblioteca.idBiblioteca == biblioteca_id).first()
        if not biblioteca:
            raise HTTPException(
                status_code=404,
                detail="Biblioteca não encontrada."
            )

        # Buscar salas disponíveis
        salas_disponiveis = db.query(SalaDeEstudo).filter(
            SalaDeEstudo.biblioteca_id == biblioteca_id,
            SalaDeEstudo.disponibilidade == True
        ).all()

        # Verificar se há salas disponíveis
        if not salas_disponiveis:
            return {"message": "Nenhuma sala disponível nesta biblioteca."}

        # Retornar as salas encontradas
        salas = [
            {
                "nome": sala.nome,
                "numero": sala.numero,
                "andar": sala.andar,
                "capacidade": sala.capacidade,
                "disponibilidade": sala.disponibilidade,
            }
            for sala in salas_disponiveis
        ]

        return {"message": "Salas disponíveis encontradas.", "salas": salas}

    except Exception as err:
        logger.error(f"Erro ao buscar salas disponíveis: {err}")
        raise HTTPException(
            status_code=500,
            detail="Erro interno ao buscar salas disponíveis."
        )
    
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
