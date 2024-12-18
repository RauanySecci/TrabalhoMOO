document.addEventListener("DOMContentLoaded", function () {
    const tabelaBody = document.querySelector("#tabela-times tbody");
    const resultadoSalas = JSON.parse(localStorage.getItem("resultado_salas"));

    if (resultadoSalas && resultadoSalas.length > 0) {
        resultadoSalas.forEach(sala => {
            const row = `
                <tr>
                    <td>${sala.nome}</td>
                    <td>${sala.numero}</td>
                    <td>${sala.andar}</td>
                    <td>${sala.capacidade}</td>
                    <td>${sala.disponibilidade ? "Disponível" : "Indisponível"}</td>
                    <td>${sala.biblioteca_id}</td>
                </tr>
            `;
            tabelaBody.insertAdjacentHTML("beforeend", row);
        });
    } else {
        tabelaBody.innerHTML = `<tr><td colspan="6">Nenhuma sala encontrada.</td></tr>`;
    }
});