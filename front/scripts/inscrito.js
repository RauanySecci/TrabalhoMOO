let btnVerificar = document.querySelector("#ba2");

btnVerificar.addEventListener("click", async function () {
    // Capturar o valor do campo número
    let numero = document.querySelector("#numero").value.trim();

    // Validação: número não pode ser vazio
    if (!numero) {
        alert("O campo número não pode estar vazio.");
        return;
    }

    // Validação: verificar se o valor é um número válido e contém apenas dígitos
    if (!/^\d+$/.test(numero)) {
        alert("Número inválido. Certifique-se de que contém apenas dígitos numéricos.");
        return;
    }

    try {
        // Enviar requisição para o backend
        let response = await fetch("http://127.0.0.1:2000/salas-disponiveis", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ numero: numero }) // Envia o número no corpo da requisição
        });

        // Verificar se a resposta do servidor é válida
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || "Erro na requisição ao servidor.");
        }

        // Ler a resposta do backend
        let data = await response.json();

        if (data.exists) {
            // Número encontrado no banco de dados
            sessionStorage.setItem("numero", numero);

            // Redirecionar para a página de pesquisa
            window.location.href = "pesquisa.html";
        } else {
            // Número não encontrado no banco de dados
            alert("Número não encontrado no banco de dados.");
        }
    } catch (error) {
        // Exibir a mensagem de erro no console para depuração
        console.error("Erro ao conectar ao servidor:", error);

        // Exibir uma mensagem de erro detalhada ao usuário
        alert(`Erro ao conectar ao servidor: ${error.message}`);
    }
});


document.addEventListener("DOMContentLoaded", function() {
    const filterButton = document.getElementById("filter-button");
    const filterForm = document.getElementById("filter-form");
  
    filterButton.addEventListener("click", function() {
      if (filterForm.style.display === "none" || filterForm.classList.contains("hidden")) {
        filterForm.style.display = "flex"; // Mostra o formulário
        filterForm.classList.remove("hidden");
        filterButton.textContent = "Filtros";
      } else {
        filterForm.reset(); // Limpa os inputs do formulário
        filterForm.style.display = "none"; // Oculta o formulário
        filterForm.classList.add("hidden");
        filterButton.textContent = "Filtros";
      }
    });
  
    // Inicializa o formulário oculto
    filterForm.style.display = "none";
  });

  document.addEventListener("DOMContentLoaded", async function () {
    const bibliotecaSelect = document.getElementById("biblioteca");

    try {
        // Enviar requisição ao backend para buscar bibliotecas
        let response = await fetch("http://127.0.0.1:2000/bibliotecas", {
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

