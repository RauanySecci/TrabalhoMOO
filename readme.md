# 🏛️ Aplicação de Gestão Bibliotecária

Este projeto é uma aplicação web simples que permite cadastrar salas de estudo e buscar salas usando filtros personalizados. O backend é desenvolvido em Python com FastAPI e banco de dados PostgreSQL, enquanto o frontend utiliza HTML, CSS e JavaScript.

## 🚀 Passo a Passo para Rodar a Aplicação


1.  Instalar o Docker e o Docker Compose

    🐧 Linux (Ubuntu/Debian)
    
    1. Instalar o Docker:

        Execute os comandos no terminal:

        ```console
        sudo apt update
        sudo apt install apt-transport-https ca-certificates curl software-properties-common

        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
        sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

        sudo apt update
        sudo apt install docker-ce
        ```

        Verificar a instalação:

       ```console
       docker --version
       ```

        Adicionar o usuário ao grupo Docker (para rodar sem sudo):
        ```console
        sudo usermod -aG docker $USER
        ```

        Reinicie a sessão do terminal para aplicar.

    2. Instalar o Docker Compose:

        Execute os comandos:
        ```console
        sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
        sudo chmod +x /usr/local/bin/docker-compose
        ```

     Verificar a instalação:

    ```console
    docker-compose --version
    ```

 🪟 Windows

 1. Instalar o Docker Desktop:

     a. Acesse o site oficial e baixe o Docker Desktop: Download Docker Desktop.
     
     b. Siga o assistente de instalação.
     
     c. Reinicie o computador, se necessário.

     d. Habilitar WSL 2 (caso solicitado durante a instalação):
     
     e. Baixe e instale o WSL 2: Instruções para WSL.

     f. Verificar a instalação:

     g. Abra o terminal (PowerShell ou CMD) e execute:

    ```console
    docker --version
    docker-compose --version
    ```

1. Clonar o Repositório

   1. Clone o projeto do GitHub:
    ```console
    git clone https://github.com/RauanySecci/TrabalhoMOO.git
    ```

   2. Acessar a Pasta do Projeto

        Navegue até a pasta do projeto:
        ```console
        cd TrabalhoMOO
        ```

   3. Configurar o Backend com Docker

       Acesse a pasta back:
        ```console
        cd back
        ```

    Rode o Docker Compose para inicializar o backend e o banco de dados:
    ```console
    docker compose up --build
    ```

    O comando docker compose up --build irá:
    
    a. Configurar o servidor FastAPI na porta 8000.
    
    b. Configurar o banco de dados PostgreSQL na porta 5432.

2. Configurar o Frontend

    Abra a pasta do projeto no Visual Studio Code:

    ```console
    code ..
    ```

    Caso não tenha o VS Code, baixe aqui: [Visual Studio Code](https://code.visualstudio.com/)

    Instale a extensão Live Server no VS Code:
    
    Abra o VS Code.
    
    Acesse a aba Extensões (ícone de quadrado no menu lateral esquerdo).
        Procure por "Live Server" e instale.

    Após instalar o Live Server:
        Acesse a pasta front.
        Clique com o botão direito no arquivo index.html.
        Selecione "Open with Live Server".

3. Utilizar a Aplicação
    
    A página inicial será aberta no navegador (geralmente em http://127.0.0.1:5501).

    Funcionalidades Disponíveis:

    ### Cadastrar Sala de Estudo:
    -> Navegue até a aba "Cadastrar Sala".
    
    -> Preencha os campos obrigatórios e cadastre a sala.

    ### Buscar Salas de Estudo:
    -> Navegue até a aba "Buscar Sala".
    
    -> Use o campo número ou os filtros adicionais (andar, capacidade, disponibilidade) para pesquisar.


## 🛠️ Tecnologias Utilizadas

**Backend**: Python (FastAPI), PostgreSQL, Docker.

**Frontend**: HTML, CSS, JavaScript.

**Ferramentas**: Visual Studio Code, Live Server, Docker Compose.


## 🐳 Observação sobre o Docker

Se necessário, reinicie os containers com:
```console
docker compose down
docker compose up --build
```


## 🤝 Contribuidores

**Agnes Bressan**

**Carol Elias**

**Rauany Secci**

**Rhayna Casado**


Seguindo esses passos, você terá a aplicação funcionando corretamente e poderá explorar todas as funcionalidades disponíveis. 🚀