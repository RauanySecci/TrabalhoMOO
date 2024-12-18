-- Tabela biblioteca
CREATE TABLE biblioteca (
    idbiblioteca SERIAL PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    departamento VARCHAR(30) NOT NULL,
    horariofuncionamento VARCHAR(30)
);

-- Tabela saladeestudo
CREATE TABLE saladeestudo (
    nome VARCHAR(30) NOT NULL,
    numero INT NOT NULL,
    andar INT NOT NULL,
    capacidade DOUBLE PRECISION,
    disponibilidade BOOLEAN NOT NULL,
    biblioteca_id INT REFERENCES biblioteca(idbiblioteca) ON DELETE CASCADE,
    PRIMARY KEY (numero, andar, biblioteca_id)
);

-- Tabela equipamento
CREATE TABLE equipamento (
    idequipamento SERIAL PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    statusdisponibilidades BOOLEAN NOT NULL,
    dataaquisicao DATE,
    biblioteca_id INT,
    numero INT,
    andar INT,
    FOREIGN KEY (numero, andar, biblioteca_id) 
        REFERENCES saladeestudo(numero, andar, biblioteca_id) ON DELETE CASCADE
);

-- Tabela usuario
CREATE TABLE usuario (
    cpf INT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    biblioteca_id INT REFERENCES biblioteca(idbiblioteca) ON DELETE CASCADE
);

-- Tabela membrocomunidadeusp
CREATE TABLE membrocomunidadeusp (
    cpf INT PRIMARY KEY,
    tipomembro VARCHAR(50),
    FOREIGN KEY (cpf) REFERENCES usuario(cpf)
);

-- Tabela bibliotecario
CREATE TABLE bibliotecario (
    cpf INT PRIMARY KEY,
    nivelpermissao VARCHAR(50),
    datacontratacao DATE,
    salario DOUBLE PRECISION,
    FOREIGN KEY (cpf) REFERENCES usuario(cpf)
);

-- Tabela notificacao
CREATE TABLE notificacao (
    idnotificacao SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    descricao VARCHAR(255),
    dataenvio DATE NOT NULL
);

-- Tabela reserva
CREATE TABLE reserva (
    idreserva SERIAL PRIMARY KEY,
    datareserva DATE NOT NULL,
    biblioteca_id INT,
    numero INT,
    andar INT,
    horarioreserva VARCHAR(50),
    usuario_cpf INT,
    FOREIGN KEY (numero, andar, biblioteca_id) 
        REFERENCES saladeestudo(numero, andar, biblioteca_id) ON DELETE CASCADE,
    FOREIGN KEY (usuario_cpf) REFERENCES usuario(cpf) ON DELETE CASCADE,
    UNIQUE(datareserva, biblioteca_id, numero, andar, horarioreserva, usuario_cpf)
);




-- Inserir dados na tabela Biblioteca
INSERT INTO Biblioteca (idBiblioteca, nome, departamento, horarioFuncionamento)
VALUES 
    (1, 'Biblioteca Central', 'Administração', '08:00-20:00'),
    (2, 'Biblioteca Ciências', 'Ciências', '09:00-18:00'),
    (3, 'Biblioteca Saúde', 'Saúde', '08:30-17:30'),
    (4, 'Biblioteca Engenharia', 'Engenharia', '08:00-19:00'),
    (5, 'Biblioteca Humanas', 'Humanas', '09:00-18:00');

-- Inserir dados na tabela SalaDeEstudo
INSERT INTO SalaDeEstudo (nome, numero, andar, capacidade, disponibilidade, biblioteca_id)
VALUES 
    ('Sala A', 101, 1, 25.0, TRUE, 1),
    ('Sala B', 102, 1, 30.0, TRUE, 1),
    ('Sala C', 201, 2, 15.0, FALSE, 2),
    ('Sala D', 202, 2, 20.0, TRUE, 2),
    ('Sala E', 301, 3, 50.0, FALSE, 3);

-- Inserir dados na tabela Equipamento
INSERT INTO Equipamento (idEquipamento, nome, statusDisponibilidades, dataAquisicao, biblioteca_id, numero, andar)
VALUES 
    (1, 'Projetor', TRUE, '2022-01-15', 1, 101, 1),
    (2, 'Quadro', TRUE, '2023-03-10', 1, 102, 1),
    (3, 'Notebook', FALSE, '2021-05-20', 2, 201, 2),
    (4, 'Mesa', TRUE, '2020-10-05', 2, 202, 2),
    (5, 'Cadeira', TRUE, '2023-07-01', 3, 301, 3);

-- Inserir dados na tabela Usuario
INSERT INTO Usuario (cpf, nome, email, biblioteca_id)
VALUES 
    (123456789, 'João Silva', 'joao.silva@example.com', 1),
    (987654321, 'Maria Oliveira', 'maria.oliveira@example.com', 2),
    (456789123, 'Carlos Souza', 'carlos.souza@example.com', 3),
    (321654987, 'Ana Pereira', 'ana.pereira@example.com', 4),
    (789123456, 'Paulo Lima', 'paulo.lima@example.com', 5);

-- Inserir dados na tabela MembroComunidadeUSP
INSERT INTO MembroComunidadeUSP (cpf, tipoMembro)
VALUES 
    (123456789, 'Aluno'),
    (987654321, 'Professor'),
    (456789123, 'Funcionário'),
    (321654987, 'Aluno'),
    (789123456, 'Professor');

-- Inserir dados na tabela Bibliotecario
INSERT INTO Bibliotecario (cpf, nivelPermissao, dataContratacao, salario)
VALUES 
    (123456789, 'Administrador', '2020-06-01', 3500.0),
    (987654321, 'Auxiliar', '2021-09-15', 2500.0),
    (456789123, 'Gerente', '2019-04-10', 4000.0),
    (321654987, 'Assistente', '2022-01-20', 2000.0),
    (789123456, 'Supervisor', '2018-08-25', 4500.0);

-- Inserir dados na tabela Notificacao
INSERT INTO Notificacao (idNotificacao, titulo, descricao, dataEnvio)
VALUES 
    (1, 'Aviso de Reunião', 'Reunião dia 20/12', '2023-12-10'),
    (2, 'Manutenção', 'Sala 101 em manutenção', '2023-12-05'),
    (3, 'Novo Livro', 'Livro disponível', '2023-12-12'),
    (4, 'Atualização de Sistema', 'Manutenção programada', '2023-11-30'),
    (5, 'Férias Coletivas', 'Encerramento de atividades em janeiro', '2023-12-01');

-- Inserir dados na tabela Reserva
INSERT INTO Reserva (idReserva, dataReserva, biblioteca_id, numero, andar, horarioReserva, usuario_cpf)
VALUES 
    (1, '2023-12-15', 1, 101, 1, '10:00-12:00', 123456789),
    (2, '2023-12-16', 2, 201, 2, '13:00-15:00', 987654321),
    (3, '2023-12-17', 1, 102, 1, '09:00-11:00', 456789123),
    (4, '2023-12-18', 3, 301, 3, '14:00-16:00', 321654987),
    (5, '2023-12-19', 2, 202, 2, '11:00-13:00', 789123456);
