from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
from db import Base

# Modelo para a tabela Biblioteca
class Biblioteca(Base):
    __tablename__ = 'biblioteca'

    idBiblioteca = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(30), nullable=False)
    departamento = Column(String(30), nullable=False)
    horarioFuncionamento = Column(String(30))

    # Relacionamento com SalaDeEstudo
    salas = relationship("SalaDeEstudo", back_populates="biblioteca_rel")

    # Relacionamento com Usuario
    usuarios = relationship("Usuario", back_populates="biblioteca_rel")




class SalaDeEstudo(Base):
    __tablename__ = 'saladeestudo'

    numero = Column(Integer, primary_key=True)
    andar = Column(Integer, primary_key=True)
    biblioteca = Column(Integer, ForeignKey('biblioteca.idBiblioteca'), primary_key=True)
    nome = Column(String(30), nullable=False)
    capacidade = Column(Float)
    disponibilidade = Column(Boolean, nullable=False)

    # Relacionamento com Biblioteca
    biblioteca_rel = relationship("Biblioteca", back_populates="salas")

    # Relacionamento com Equipamento
    equipamentos = relationship(
        "Equipamento",
        back_populates="sala",
        primaryjoin="and_(SalaDeEstudo.numero == foreign(Equipamento.numero), "
                    "SalaDeEstudo.andar == foreign(Equipamento.andar), "
                    "SalaDeEstudo.biblioteca == foreign(Equipamento.biblioteca))"
    )

    # Relacionamento com Reserva
    reservas = relationship(
        "Reserva",
        back_populates="sala",
        primaryjoin="and_(SalaDeEstudo.numero == Reserva.numero, "
                    "SalaDeEstudo.andar == Reserva.andar, "
                    "SalaDeEstudo.biblioteca == Reserva.biblioteca)",
        foreign_keys="[Reserva.numero, Reserva.andar, Reserva.biblioteca]"
    )




class Equipamento(Base):
    __tablename__ = 'equipamento'

    idEquipamento = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(30), nullable=False)
    statusDisponibilidades = Column(Boolean, nullable=False)
    dataAquisicao = Column(Date)
    biblioteca = Column(Integer, ForeignKey('saladeestudo.biblioteca'))
    numero = Column(Integer, ForeignKey('saladeestudo.numero'))
    andar = Column(Integer, ForeignKey('saladeestudo.andar'))

    # Relacionamento com SalaDeEstudo
    sala = relationship(
        "SalaDeEstudo",
        back_populates="equipamentos",
        primaryjoin="and_(foreign(Equipamento.numero) == SalaDeEstudo.numero, "
                    "foreign(Equipamento.andar) == SalaDeEstudo.andar, "
                    "foreign(Equipamento.biblioteca) == SalaDeEstudo.biblioteca)"
    )




class Usuario(Base):
    __tablename__ = 'usuario'

    cpf = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    biblioteca = Column(Integer, ForeignKey('biblioteca.idBiblioteca'))

    # Relacionamento com Biblioteca
    biblioteca_rel = relationship("Biblioteca", back_populates="usuarios")

    # Relacionamento com MembroComunidadeUSP
    membro_usp = relationship("MembroComunidadeUSP", back_populates="usuario")

    # Relacionamento com Reserva
    reservas = relationship("Reserva", back_populates="usuario_rel")

    # Relacionamento com Bibliotecario
    bibliotecario = relationship("Bibliotecario", back_populates="usuario")




class MembroComunidadeUSP(Base):
    __tablename__ = 'membrocomunidadeusp'

    cpf = Column(Integer, ForeignKey('usuario.cpf'), primary_key=True)  # Chave estrangeira para Usuario
    tipoMembro = Column(String(50))

    # Relacionamento com Usuario
    usuario = relationship(
        "Usuario",
        back_populates="membro_usp",
        primaryjoin="MembroComunidadeUSP.cpf == Usuario.cpf"
    )


class Bibliotecario(Base):
    __tablename__ = 'bibliotecario'

    cpf = Column(Integer, ForeignKey('usuario.cpf'), primary_key=True)  # Chave estrangeira para Usuario
    nivelPermissao = Column(String(50))
    dataContratacao = Column(Date)
    salario = Column(Float)

    # Relacionamento com Usuario
    usuario = relationship(
        "Usuario",
        back_populates="bibliotecario",
        primaryjoin="Bibliotecario.cpf == Usuario.cpf"
    )



# Modelo para a tabela Notificacao
class Notificacao(Base):
    __tablename__ = 'notificacao'

    idNotificacao = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False)
    descricao = Column(String(255))
    dataEnvio = Column(Date)


class Reserva(Base):
    __tablename__ = 'reserva'

    idReserva = Column(Integer, primary_key=True, autoincrement=True)
    dataReserva = Column(Date, nullable=False)
    biblioteca = Column(Integer, ForeignKey('saladeestudo.biblioteca'))
    numero = Column(Integer, ForeignKey('saladeestudo.numero'))
    andar = Column(Integer, ForeignKey('saladeestudo.andar'))
    horarioReserva = Column(String(50))
    usuario = Column(Integer, ForeignKey('usuario.cpf'))

    # Relacionamento com SalaDeEstudo
    sala = relationship(
        "SalaDeEstudo",
        back_populates="reservas",
        primaryjoin="and_(Reserva.numero == SalaDeEstudo.numero, "
                    "Reserva.andar == SalaDeEstudo.andar, "
                    "Reserva.biblioteca == SalaDeEstudo.biblioteca)",
        foreign_keys="[Reserva.numero, Reserva.andar, Reserva.biblioteca]"
    )

    # Relacionamento com Usuario
    usuario_rel = relationship("Usuario", back_populates="reservas")