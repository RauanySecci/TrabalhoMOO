from psycopg2 import DatabaseError, IntegrityError
from fastapi import HTTPException
from log import logger

def postgres_select_errors(err: DatabaseError):
    """
    Função para tratar erros de SELECT no PostgreSQL.
    """
    error_code = err.pgcode  # Código do erro (SQLState)
    error_message = str(err)

    if error_code == "42P01":  # Undefined table (Table does not exist)
        raise HTTPException(
            status_code=400,
            detail=f"Tabela ou view não encontrada. Verifique a configuração do banco. Mensagem do erro: {error_message}"
        )
    elif error_code == "42703":  # Undefined column (Invalid column name)
        raise HTTPException(
            status_code=400,
            detail=f"Coluna inválida especificada na consulta. Mensagem do erro: {error_message}"
        )
    elif error_code == "42601":  # Syntax error
        raise HTTPException(
            status_code=400,
            detail=f"Erro de sintaxe na consulta SQL. Mensagem do erro: {error_message}"
        )
    elif error_code == "22001":  # String data right truncation
        raise HTTPException(
            status_code=500,
            detail=f"Valor truncado durante a execução da consulta. Mensagem do erro: {error_message}"
        )
    elif error_code == "42P10":  # Ambiguous column
        raise HTTPException(
            status_code=400,
            detail=f"Coluna definida de forma ambígua na consulta. Mensagem do erro: {error_message}"
        )
    elif error_code == "02000":  # No data found
        raise HTTPException(
            status_code=404,
            detail="Nenhum dado encontrado para a consulta especificada."
        )
    else:
        # Log para erros desconhecidos
        logger.error(f"Código {error_code} - {error_message}")
        raise HTTPException(
            status_code=500,
            detail=f"Código: {error_code}. Mensagem: {error_message}"
        )

def postgres_insert_errors(err: IntegrityError):
    """
    Função para tratar erros de INSERT no PostgreSQL.
    """
    error_code = err.pgcode  # Código do erro (SQLState)
    error_message = str(err)

    if error_code == "23505":  # Unique violation
        raise HTTPException(
            status_code=400,
            detail=f"Um registro com esses dados já existe. Mensagem do erro: {error_message}"
        )
    elif error_code == "23502":  # Not null violation
        raise HTTPException(
            status_code=400,
            detail=f"Um campo obrigatório está ausente. Mensagem do erro: {error_message}"
        )
    elif error_code == "22001":  # String data right truncation
        raise HTTPException(
            status_code=400,
            detail=f"Valor excede o tamanho permitido para uma coluna. Mensagem do erro: {error_message}"
        )
    elif error_code == "23503":  # Foreign key violation
        raise HTTPException(
            status_code=400,
            detail=f"Valor fornecido não existe na tabela relacionada. Mensagem do erro: {error_message}"
        )
    elif error_code == "23504":  # Check constraint violation
        raise HTTPException(
            status_code=400,
            detail=f"Violação de regra de integridade definida no banco. Mensagem do erro: {error_message}"
        )
    else:
        # Log para erros desconhecidos
        logger.error(f"Código {error_code} - {error_message}")
        raise HTTPException(
            status_code=500,
            detail=f"Código: {error_code}. Mensagem: {error_message}"
        )
