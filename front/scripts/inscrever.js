let btnCadastrar = document.querySelector("#ba1");

// Função para cadastrar uma nova sala
btnCadastrar.addEventListener("click", async function () {
    // Capturando os valores dos campos do formulário
    let nome = document.querySelector("#nome").value.trim();
    let numero = document.querySelector("#numero").value.trim();
    let andar = document.querySelector("#andar").value.trim();
    let capacidade = document.querySelector("#capacidade").value.trim();
    let disponibilidade = document.querySelector("#disponibilidade").value;
    let biblioteca = document.querySelector("#bilbioteca").value;

    // Validações básicas
    if (!nome || !numero || !andar || !capacidade || !biblioteca) {
        alert("Por favor, preencha todos os campos obrigatórios.");
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
            alert(`Erro ao cadastrar sala: ${errorData.detail}`);
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

// Função para carregar as bibliotecas no select ao carregar a página
document.addEventListener("DOMContentLoaded", async function () {
    const selectBiblioteca = document.querySelector("#biblioteca");
    try {
        // Fazendo um GET para buscar as bibliotecas do backend
        let response = await fetch("http://localhost:8000/bibliotecas");
        if (!response.ok) throw new Error("Erro ao buscar bibliotecas.");

        const bibliotecas = await response.json();
        
        // Preencher o select com as bibliotecas
        bibliotecas.forEach(bib => {
            let option = document.createElement("option");
            option.value = bib.idBiblioteca;
            option.textContent = bib.nome;
            selectBiblioteca.appendChild(option);
        });
    } catch (error) {
        alert(`Erro ao carregar bibliotecas: ${error.message}`);
        console.error(error);
    }
});