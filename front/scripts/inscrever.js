// Capturar o botão de cadastro
let btnCadastrar = document.querySelector("#ba1");

// Função para cadastrar uma nova sala
btnCadastrar.addEventListener("click", async function () {
    // Capturando os valores dos campos do formulário
    let nome = document.querySelector("#nome").value.trim();
    let numero = document.querySelector("#numero").value.trim();
    let andar = document.querySelector("#andar").value.trim();
    let capacidade = document.querySelector("#capacidade").value.trim();
    let disponibilidade = document.querySelector("#disponibilidade").value;
    let biblioteca = document.querySelector("#biblioteca").value;

    // Validações básicas
    if (!nome || !numero || !andar || !capacidade || !biblioteca) {
        alert("Por favor, preencha todos os campos obrigatórios.");
        return;
    }

    if (capacidade <= 0) {
        alert("A capacidade deve ser maior que zero.");
        return;
    }

    if (andar < 0) {
        alert("O andar não pode ser negativo.");
        return;
    }

    // Montando o objeto sala
    let sala = {
        nome,
        numero: parseInt(numero),
        andar: parseInt(andar),
        capacidade: parseFloat(capacidade),
        disponibilidade: disponibilidade === "True",
        biblioteca_id: parseInt(biblioteca)
    };

    // Enviando os dados ao backend via POST
    try {
        const response = await fetch("http://localhost:8000/salas", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(sala),
        });

        if (!response.ok) {
            const errorData = await response.json();
            // Tratando erros do backend
            if (Array.isArray(errorData.detail)) {
                alert(`Erro ao cadastrar sala: ${errorData.detail.map(e => e.msg).join(", ")}`);
            } else {
                alert(`Erro ao cadastrar sala: ${JSON.stringify(errorData.detail)}`);
            }
            return;
        }

        alert("Sala cadastrada com sucesso!");

        // Limpando os campos do formulário
        document.querySelectorAll(".form-control").forEach(input => input.value = "");
    } catch (error) {
        alert(`Erro inesperado: ${error.message}`);
        console.error("Erro:", error);
    }
});

document.addEventListener("DOMContentLoaded", async function () {
    const bibliotecaSelect = document.getElementById("biblioteca");

    try {
        // Enviar requisição ao backend para buscar bibliotecas
        let response = await fetch("http://localhost:8000/bibliotecas", {
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            }
        });

        // Verificar se a resposta é válida
        if (!response.ok) {
            throw new Error("Erro ao buscar bibliotecas.");
        }

        // Ler os dados do backend
        let data = await response.json();

        // Preencher o select com os nomes das bibliotecas
        data.bibliotecas.forEach(biblioteca => {
            let option = document.createElement("option");
            option.value = biblioteca.idBiblioteca;
            option.textContent = biblioteca.nome;
            bibliotecaSelect.appendChild(option);
        });
    } catch (error) {
        console.error("Erro ao carregar bibliotecas:", error);
        alert("Erro ao carregar bibliotecas. Tente novamente.");
    }
});