let btnVerificar = document.querySelector("#ba2");

btnVerificar.addEventListener("click", async function () {
    // Capturar o valor do campo CPF
    let numero = document.querySelector("#numero").value.trim();

    // Validação: numero não pode ser vazio e deve ter exatamente 11 dígitos
    if (!numero) {
        alert("O campo número não pode estar vazio.");
        return;
    }

    // if (numero.length !== 11 || isNaN(numero)) {
    //     alert("Numero inválido. Certifique-se de que possui exatamente 11 dígitos numéricos.");
    //     return;
    // }

    try {
        // Enviar requisição para o backend
        let response = await fetch("http://127.0.0.1:2000/verify-numero", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ numero: numero }) // Envia o numero no corpo da requisição
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || "Erro na requisição ao servidor");
        }

        // Ler a resposta do backend
        let data = await response.json();

        if (data.message) {
            // Armazena o numero no Session Storage
            sessionStorage.setItem("numero", numero);

            // Redirecionar para a página de pesquisa
            window.location.href = "pesquisa.html";
        } else {
            // numero não encontrado no banco de dados
            alert("Numero não encontrado no banco de dados.");
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


