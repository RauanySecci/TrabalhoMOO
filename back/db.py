from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from pydantic_settings import BaseSettings

# Carregar as configurações do arquivo .env
class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_DNS: str

    class Config:
        env_file = ".env"

settings = Settings()

# Construir a URL do banco de dados
database_url = f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_DNS}"

# Configurar o SQLAlchemy
engine = create_engine(database_url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()

# Dependência para os controladores do FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
