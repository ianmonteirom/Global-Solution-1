function validar() {
    let user = document.querySelector('#userhtml').value; 
    let senha = document.querySelector('#senhahtml').value;
    
    if (user == 'user' && senha == 1234) {
        window.alert('Usuário validado!')
        window.location.href = "./quiz.html";
    } else if (user != 'user' || senha != 1234) {
        window.alert('Usuário ou senha inválidos! Preencha os dados e tente novamente.')
    }
}

function formulario() {
    let nome = document.querySelector('#nomehtml').value;
    let telefone = document.querySelector('#telhtml').value;
    let email = document.querySelector('#emailhtml').value;

    if (nome == '' || telefone == '' || email == '') {
        window.alert('Erro! Algum campo não foi preenchido. Verifique os dados e tente novamente.')
    } else {
        window.alert('Dados enviados com sucesso!')
    }
}
