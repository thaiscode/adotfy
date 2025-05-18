let msg = document.querySelector('.mensagem-envio');
let send2 = document.querySelector('.main')
let btn = document.querySelector('.enviar');

btn.addEventListener('click', envio);

function envio() {
            send2.style.display = 'none';
            msg.style.display = 'block'; 
}