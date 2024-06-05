// alert('Seja bem-vindo!') 

// SlideShow da Sessão do Problema
let imagensProblema=['./src/assets/problemapesca.jpg','./src/assets/problemapesca2.jpg','./src/assets/problemapesca3.jpg'];
let indexProblema = 0;
let timeProblema = 3000;

function slideShowProblema(){
    document.getElementById('imgProblema').src=imagensProblema[indexProblema];
    indexProblema++;

    if(indexProblema == imagensProblema.length){
        indexProblema = 0;
    }
    setTimeout('slideShowProblema()', timeProblema);
}
slideShowProblema();

// SlideShow da Sessão da Tecnologia
let imagensTecnologia=['./src/assets/database.jpg','./src/assets/database2.jpg','./src/assets/database3.jpg'];
let indexTecnologia = 0;
let timeTecnologia = 3000;

function slideShowTecnologia(){
    document.getElementById('imgTecnologia').src=imagensTecnologia[indexTecnologia];
    indexTecnologia++;

    if(indexTecnologia == imagensTecnologia.length){
        indexTecnologia = 0;
    }
    setTimeout('slideShowTecnologia()', timeTecnologia);
}
slideShowTecnologia();

// SlideShow da Sessão dos Objetivos
let imagensObjetivos=['./src/assets/objetivos.jpg','./src/assets/objetivos2.jpg','./src/assets/objetivos3.jpg'];
let indexObjetivos = 0;
let timeObjetivos = 3000;

function slideShowObjetivos(){
    document.getElementById('imgObjetivos').src=imagensObjetivos[indexObjetivos];
    indexObjetivos++;

    if(indexObjetivos == imagensObjetivos.length){
        indexObjetivos = 0;
    }
    setTimeout('slideShowObjetivos()', timeObjetivos);
}
slideShowObjetivos();

// SlideShow da Sessão do Público-Alvo
let imagensPublicoAlvo=['./src/assets/publico.jpg','./src/assets/publico2.jpg','./src/assets/publico3.jpg'];
let indexPublicoAlvo = 0;
let timePublicoAlvo = 3000;

function slideShowPublicoAlvo(){
    document.getElementById('imgPublicoAlvo').src=imagensPublicoAlvo[indexPublicoAlvo];
    indexPublicoAlvo++;

    if(indexPublicoAlvo == imagensPublicoAlvo.length){
        indexPublicoAlvo = 0;
    }
    setTimeout('slideShowPublicoAlvo()', timePublicoAlvo);
}
slideShowPublicoAlvo();

// SlideShow da Sessão dos Benefícios
let imagensBeneficios=['./src/assets/beneficios.jpg','./src/assets/beneficios2.jpg','./src/assets/beneficios3.jpg'];
let indexBeneficios = 0;
let timeBeneficios = 3000;

function slideShowBeneficios(){
    document.getElementById('imgBeneficios').src=imagensBeneficios[indexBeneficios];
    indexBeneficios++;

    if(indexBeneficios == imagensBeneficios.length){
        indexBeneficios = 0;
    }
    setTimeout('slideShowBeneficios()', timeBeneficios);
}
slideShowBeneficios();

// Efeito de rolagem suave quando o usuário clica em algum item do menu
document.querySelectorAll('#menu .opcao').forEach(item => {
    item.addEventListener('click', function(event) {
        event.preventDefault();
        
        const targetId = this.getAttribute('href').substring(1);
        const targetElement = document.getElementById(targetId);
        
        targetElement.scrollIntoView({ behavior: 'smooth' });
    });
});



function clickMenu() {
    let menu = document.getElementById('menu');
    let itemsMenu = document.querySelectorAll('#menu a');

    if (menu.style.display == 'block') {
        menu.style.display = 'none';
        itemsMenu.forEach(function(item) {
            item.style.display = 'block';
        });
    } else {
        menu.style.display = 'block';
        itemsMenu.forEach(function(item) {
            item.style.display = 'block';
        });
    }    
}
