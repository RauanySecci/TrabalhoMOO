from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import SalaDeEstudo, Biblioteca
from log import logger

router = APIRouter()

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
    Endpoint para cadastrar uma nova sala.
    """
    try:
        # Verificar se a biblioteca existe
        biblioteca = db.query(Biblioteca).filter(Biblioteca.idBiblioteca == biblioteca_id).first()
        if not biblioteca:
            raise HTTPException(
                status_code=404,
                detail="Biblioteca não encontrada."
            )

        # Criar nova sala
        nova_sala = SalaDeEstudo(
            nome=nome,
            numero=numero,
            andar=andar,
            capacidade=capacidade,
            disponibilidade=disponibilidade,
            biblioteca_id=biblioteca_id
        )

        # Adicionar ao banco de dados
        db.add(nova_sala)
        db.commit()
        db.refresh(nova_sala)

        return {"message": "Sala cadastrada com sucesso.", "sala": nova_sala.id}

    except Exception as err:
        logger.error(f"Erro ao cadastrar sala: {err}")
        raise HTTPException(
            status_code=500,
            detail="Erro interno ao cadastrar sala."
        )


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
