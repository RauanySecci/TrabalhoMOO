document.addEventListener("DOMContentLoaded", function () {
    const btnBuscar = document.getElementById("ba2"); // Botão de buscar
    const filterButton = document.getElementById("filter-button"); // Botão de filtros
    const filterForm = document.getElementById("filter-form"); // Formulário de filtros

    // Toggle para mostrar/ocultar o formulário de filtros
    filterButton.addEventListener("click", function () {
        if (filterForm.classList.contains("hidden")) {
            filterForm.classList.remove("hidden");
            filterForm.style.display = "block";
        } else {
            filterForm.classList.add("hidden");
            filterForm.style.display = "none";
        }
    });

    // Função para validar campos
    function validarCampos(numero, andar, capacidade) {
        const erros = [];

        // Validação do número da sala
        if (!numero) {
            erros.push("O número da sala é obrigatório.");
        } else if (isNaN(numero) || parseInt(numero) < 0) {
            erros.push("O número da sala deve ser um número inteiro positivo.");
        }

        // Validação do andar (se fornecido)
        if (andar) {
            if (isNaN(andar) || parseInt(andar) < 0) {
                erros.push("O andar deve ser um número inteiro positivo.");
            }
        }

        // Validação da capacidade (se fornecida)
        if (capacidade) {
            if (isNaN(capacidade) || parseFloat(capacidade) <= 0) {
                erros.push("A capacidade deve ser um número positivo maior que zero.");
            }
        }

        return erros;
    }

    // Evento de busca
    btnBuscar.addEventListener("click", function () {
        const numero = document.getElementById("numero").value.trim();
        const andar = document.getElementById("andar").value.trim();
        const biblioteca = document.getElementById("biblioteca").value.trim();
        const capacidade = document.getElementById("capacidade").value.trim();
        const disponibilidade = document.getElementById("disponibilidade").value.trim();

        // Validação dos campos
        const erros = validarCampos(numero, andar, capacidade);

        if (erros.length > 0) {
            alert("Erros encontrados:\n- " + erros.join("\n- "));
            return;
        }

        // Montar os parâmetros de consulta (query string)
        const params = new URLSearchParams();
        params.append("numero", numero);

        if (andar) params.append("andar", andar);
        if (biblioteca) params.append("biblioteca_id", biblioteca);
        if (capacidade) params.append("capacidade", capacidade);
        if (disponibilidade) params.append("disponibilidade", disponibilidade);

        // URL do backend com os parâmetros montados
        const url = `http://localhost:8000/busca-sala?${params.toString()}`;

        // Fazer a requisição para verificar os dados e redirecionar
        fetch(url, { method: "GET" })
            .then(response => {
                if (!response.ok) {
                    return response.json().then(err => { throw new Error(err.detail); });
                }
                return response.json();
            })
            .then(data => {
                // Armazenar o resultado no localStorage para a página de pesquisa
                localStorage.setItem("resultado_salas", JSON.stringify(data.salas));

                // Redirecionar para a página de pesquisa
                window.location.href = "pesquisa.html";
            })
            .catch(error => {
                console.error("Erro ao buscar dados:", error.message);
                alert(`Erro ao buscar salas: ${error.message}`);
            });
    });
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

