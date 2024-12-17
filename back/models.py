from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
from db import Base

# Modelo Biblioteca
class Biblioteca(Base):
    __tablename__ = 'biblioteca'

    idBiblioteca = Column("idbiblioteca", Integer, primary_key=True, autoincrement=True)
    nome = Column(String(30), nullable=False)
    departamento = Column(String(30), nullable=False)
    horarioFuncionamento = Column("horariofuncionamento", String(30))

    # Relacionamentos
    salas = relationship("SalaDeEstudo", back_populates="biblioteca_rel")
    usuarios = relationship("Usuario", back_populates="biblioteca_rel")



# Modelo SalaDeEstudo
class SalaDeEstudo(Base):
    __tablename__ = 'saladeestudo'

    numero = Column(Integer, primary_key=True)
    andar = Column(Integer, primary_key=True)
    biblioteca_id = Column(Integer, ForeignKey('biblioteca.idbiblioteca'), primary_key=True)
    nome = Column(String(30), nullable=False)
    capacidade = Column(Float)
    disponibilidade = Column(Boolean, nullable=False)

    # Relacionamentos
    biblioteca_rel = relationship("Biblioteca", back_populates="salas")

    equipamentos = relationship(
        "Equipamento",
        back_populates="sala",
        primaryjoin="and_(SalaDeEstudo.numero == foreign(Equipamento.numero), "
                    "SalaDeEstudo.andar == foreign(Equipamento.andar), "
                    "SalaDeEstudo.biblioteca_id == foreign(Equipamento.biblioteca_id))"
    )

    reservas = relationship(
        "Reserva",
        back_populates="sala",
        primaryjoin="and_(SalaDeEstudo.numero == Reserva.numero, "
                    "SalaDeEstudo.andar == Reserva.andar, "
                    "SalaDeEstudo.biblioteca_id == Reserva.biblioteca_id)"
    )


# Modelo Equipamento
class Equipamento(Base):
    __tablename__ = 'equipamento'

    idequipamento = Column("idequipamento", Integer, primary_key=True, autoincrement=True)
    nome = Column(String(30), nullable=False)
    statusdisponibilidades = Column("statusdisponibilidades", Boolean, nullable=False)
    dataaquisicao = Column("dataaquisicao", Date)
    biblioteca_id = Column(Integer, ForeignKey('saladeestudo.biblioteca_id'))
    numero = Column(Integer, ForeignKey('saladeestudo.numero'))
    andar = Column(Integer, ForeignKey('saladeestudo.andar'))

    sala = relationship(
        "SalaDeEstudo",
        back_populates="equipamentos",
        primaryjoin="and_(foreign(Equipamento.numero) == SalaDeEstudo.numero, "
                    "foreign(Equipamento.andar) == SalaDeEstudo.andar, "
                    "foreign(Equipamento.biblioteca_id) == SalaDeEstudo.biblioteca_id)"
    )


# Modelo Usuario
class Usuario(Base):
    __tablename__ = 'usuario'

    cpf = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    biblioteca_id = Column(Integer, ForeignKey('biblioteca.idbiblioteca'))

    # Relacionamentos
    biblioteca_rel = relationship("Biblioteca", back_populates="usuarios")
    membro_usp = relationship("MembroComunidadeUSP", back_populates="usuario")
    reservas = relationship("Reserva", back_populates="usuario_rel")
    bibliotecario = relationship("Bibliotecario", back_populates="usuario")


# Modelo MembroComunidadeUSP
class MembroComunidadeUSP(Base):
    __tablename__ = 'membrocomunidadeusp'

    cpf = Column(Integer, ForeignKey('usuario.cpf'), primary_key=True)
    tipomembro = Column("tipomembro", String(50))

    usuario = relationship("Usuario", back_populates="membro_usp")


# Modelo Bibliotecario
class Bibliotecario(Base):
    __tablename__ = 'bibliotecario'

    cpf = Column(Integer, ForeignKey('usuario.cpf'), primary_key=True)
    nivelpermissao = Column("nivelpermissao", String(50))
    datacontratacao = Column("datacontratacao", Date)
    salario = Column(Float)

    usuario = relationship("Usuario", back_populates="bibliotecario")


# Modelo Notificacao
class Notificacao(Base):
    __tablename__ = 'notificacao'

    idnotificacao = Column("idnotificacao", Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(255), nullable=False)
    descricao = Column(String(255))
    dataenvio = Column("dataenvio", Date)


# Modelo Reserva
class Reserva(Base):
    __tablename__ = 'reserva'

    idreserva = Column("idreserva", Integer, primary_key=True, autoincrement=True)
    datareserva = Column("datareserva", Date, nullable=False)
    biblioteca_id = Column(Integer, ForeignKey('saladeestudo.biblioteca_id'))
    numero = Column(Integer, ForeignKey('saladeestudo.numero'))
    andar = Column(Integer, ForeignKey('saladeestudo.andar'))
    horarioreserva = Column("horarioreserva", String(50))
    usuario_id = Column(Integer, ForeignKey('usuario.cpf'))

    # Relacionamentos
    sala = relationship(
        "SalaDeEstudo",
        back_populates="reservas",
        primaryjoin="and_(Reserva.numero == SalaDeEstudo.numero, "
                    "Reserva.andar == SalaDeEstudo.andar, "
                    "Reserva.biblioteca_id == SalaDeEstudo.biblioteca_id)"
    )
    usuario_rel = relationship("Usuario", back_populates="reservas")
