from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
from db import Base

# Modelo para a tabela Biblioteca
class Biblioteca(Base):
    __tablename__ = 'biblioteca'

    idBiblioteca = Column(Integer, primary_key=True, index=True)
    nome = Column(String(30), nullable=False)
    departamento = Column(String(30), nullable=False)
    horarioFuncionamento = Column(String(30))

    # Relacionamento com outras tabelas
    salas = relationship("SalaDeEstudo", back_populates="biblioteca")
    usuarios = relationship("Usuario", back_populates="biblioteca")


# Modelo para a tabela SalaDeEstudo
class SalaDeEstudo(Base):
    __tablename__ = 'saladeestudo'

    numero = Column(Integer, primary_key=True)
    andar = Column(Integer, primary_key=True)
    capacidade = Column(Float)
    disponibilidade = Column(Boolean, nullable=False)
    biblioteca_id = Column(Integer, ForeignKey('biblioteca.idBiblioteca'), primary_key=True)

    # Relacionamento reverso
    biblioteca = relationship("Biblioteca", back_populates="salas")
    equipamentos = relationship("Equipamento", back_populates="sala")
    reservas = relationship("Reserva", back_populates="sala")


# Modelo para a tabela Equipamento
class Equipamento(Base):
    __tablename__ = 'equipamento'

    idEquipamento = Column(Integer, primary_key=True, index=True)
    nome = Column(String(30), nullable=False)
    statusDisponibilidades = Column(Boolean, nullable=False)
    dataAquisicao = Column(Date)
    biblioteca_id = Column(Integer)
    sala_numero = Column(Integer)
    sala_andar = Column(Integer)

    # Relacionamento com SalaDeEstudo
    sala = relationship("SalaDeEstudo", back_populates="equipamentos")


# Modelo para a tabela Usuario
class Usuario(Base):
    __tablename__ = 'usuario'

    cpf = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    biblioteca_id = Column(Integer, ForeignKey('biblioteca.idBiblioteca'))

    # Relacionamento reverso
    biblioteca = relationship("Biblioteca", back_populates="usuarios")
    reservas = relationship("Reserva", back_populates="usuario")


# Modelo para a tabela MembroComunidadeUSP
class MembroComunidadeUSP(Base):
    __tablename__ = 'membrocomunidadeusp'

    cpf = Column(Integer, primary_key=True)
    tipoMembro = Column(String(50))

    # Relacionamento com Usuario
    usuario = relationship("Usuario", back_populates="membro_usp")


# Modelo para a tabela Bibliotecario
class Bibliotecario(Base):
    __tablename__ = 'bibliotecario'

    cpf = Column(Integer, primary_key=True)
    nivelPermissao = Column(String(50))
    dataContratacao = Column(Date)
    salario = Column(Float)

    # Relacionamento com Usuario
    usuario = relationship("Usuario", back_populates="bibliotecario")


# Modelo para a tabela Notificacao
class Notificacao(Base):
    __tablename__ = 'notificacao'

    idNotificacao = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False)
    descricao = Column(String(255))
    dataEnvio = Column(Date)


# Modelo para a tabela Reserva
class Reserva(Base):
    __tablename__ = 'reserva'

    idReserva = Column(Integer, primary_key=True, index=True)
    dataReserva = Column(Date, nullable=False)
    biblioteca_id = Column(Integer)
    sala_numero = Column(Integer)
    sala_andar = Column(Integer)
    horarioReserva = Column(String(50))
    usuario_id = Column(Integer, ForeignKey('usuario.cpf'))

    # Relacionamentos
    sala = relationship("SalaDeEstudo", back_populates="reservas")
    usuario = relationship("Usuario", back_populates="reservas")
