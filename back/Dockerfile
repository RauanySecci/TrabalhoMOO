# Use uma imagem Python para rodar a aplicação
FROM python:3.10

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos da aplicação para o container
COPY . /app

# Instala as dependências necessárias
RUN pip install --no-cache-dir -r requirements.txt

# Define variáveis de ambiente
ENV DB_USER=postgres \
    DB_PASSWORD=123456789 \
    DB_DNS=db:5432/banco

# Expõe a porta 8000 para acesso externo
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
