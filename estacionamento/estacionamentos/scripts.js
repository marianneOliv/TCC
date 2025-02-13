console.log('scripts.js foi carregado');

function mudarCampoDocumento(tipo) {

    let campoDocumento = document.getElementById("documento");
    if (tipo === "CPF") {
        campoDocumento.placeholder = "CPF";
    } else {
        campoDocumento.placeholder = "CNPJ";
    }

}

function buscarEstacionamento() {
    const cep = document.getElementById('cep').value;
    
    if (!cep) {
        alert("Por favor, informe um CEP.");
        return;
    }

    fetch(`https://viacep.com.br/ws/${cep}/json/`)
        .then(response => response.json())
        .then(data => {
            if (data.erro) {
                alert("CEP não encontrado.");
                return;
            }

            const endereco = `${data.logradouro}, ${data.bairro}, ${data.localidade} - ${data.uf}`;
            console.log( endereco);

            fetch(`/api/estacionamentos?cep=${cep}`)
                .then(response => response.json())
                .then(estacionamentos => {
                    if (estacionamentos.length > 0) {
                        exibirEstacionamentos(estacionamentos);
                    } else {
                        exibirMensagemSemEstacionamento();
                    }
                });
        })
        .catch(error => {
            console.error("Erro ao buscar o CEP:", error);
            alert("Erro ao buscar os dados.");
        });
}

function exibirEstacionamentos(estacionamentos) {
    const resultado = document.getElementById('resultado');
    resultado.innerHTML = ''; // Limpa o resultado anterior

    estacionamentos.forEach(estacionamento => {
        const div = document.createElement('div');
        div.classList.add('estacionamento');
        div.innerHTML = `
            <h3>${estacionamento.nome}</h3>
            <p>CEP: ${estacionamento.cep}</p>
            <p>Endereço: ${estacionamento.endereco}</p>
        `;
        resultado.appendChild(div);
    });

    document.getElementById('semEstacionamento').style.display = 'none';
}

function exibirMensagemSemEstacionamento() {
    document.getElementById('resultado').innerHTML = '';    
    document.getElementById('semEstacionamento').style.display = 'block';
}

function toggleMenu() {
    var menu = document.getElementById('menu');
    console.log('Menu foi clicado!');  // Depuração
    menu.classList.toggle('show');
}

document.getElementById('cep').addEventListener('blur', function() {
    var cep = this.value.replace(/\D/g, ''); // Remove caracteres não numéricos
    if (cep.length === 8) {
        fetch(`https://viacep.com.br/ws/${cep}/json/`)
            .then(response => response.json())
            .then(data => {
                if (data.erro) {
                    alert('CEP não encontrado.');
                } else {
                    document.getElementById('rua').value = data.logradouro;
                    document.getElementById('cidade').value = data.localidade;
                    document.getElementById('estado').value = data.uf;
                }
            })
            .catch(error => alert('Erro ao buscar o CEP: ' + error));
    } else {
        alert('CEP inválido.');
    }
});


$(document).ready(function() {
    $('#comodidades').on('change', function() {
        var selectedOptions = $(this).val(); // Obtém as opções selecionadas
        var displayComodidades = $('#selected-comodidades');
        displayComodidades.empty(); // Limpa a lista antes de adicionar

        selectedOptions.forEach(function(optionValue) {
            var optionText = $('#comodidades option[value="' + optionValue + '"]').text();
            var listItem = $('<li class="selected-comodidade-item"></li>');
            listItem.text(optionText);
            var removeButton = $('<button type="button" class="remove-comodidade" onclick="removeComodidade(this)">×</button>');
            listItem.append(removeButton);
            displayComodidades.append(listItem);
        });
    });
});

function removeComodidade(button) {
    var item = button.parentElement;
    var optionValue = item.textContent.replace('×', '').trim();
    $('#comodidades option').each(function() {
        if ($(this).text().trim() === optionValue) {
            $(this).prop('selected', false);
        }
    });
    item.remove(); 
}

$(document).ready(function() {
    $('#comodidades').select2();
});

$('#vagas').select2({
    placeholder: 'Selecione a quantidade de vagas'
});

function atualizarVagas() {
    fetch('/atualizar_vagas/')
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            let vagasElement = document.getElementById('vagas-count-11');
            if (vagasElement) {
                vagasElement.textContent = data.vagas;  // Atualiza o HTML com o novo número de vagas
            } else {
                console.error("Elemento vagas-count-11 não encontrado no DOM.");
            }
        } else {
            console.error("Erro ao atualizar vagas:", data.error);
        }
    })
    .catch(error => console.error("Erro na requisição AJAX:", error));
}

function iniciarAtualizacaoVagas() {
    setInterval(() => atualizarVagas(), 5000); // Atualiza a cada 5 segundos
}

document.addEventListener("DOMContentLoaded", iniciarAtualizacaoVagas);
