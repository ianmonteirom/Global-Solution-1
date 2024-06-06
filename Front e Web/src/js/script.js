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

    let body = document.body;
    let header = document.querySelector('header');
    let links = document.querySelectorAll('a');
    let divs = document.querySelectorAll('div');
    let headingsAndParagraphs = document.querySelectorAll('h2, p');
    let footer = document.querySelector('footer');
    let burguer = document.querySelector('#burguer');

    let darkmode = document.querySelector('#darkmode');
    let lightmode = document.querySelector('#lightmode');

function darkMode() {
    links.forEach(function(link) {
        link.style.color = "#CBCDCC";
    });

    divs.forEach(function(div) {
        div.style.backgroundColor = "#001926";
    });

    headingsAndParagraphs.forEach(function(element) {
        element.style.color = "#ffffff";
    });


    body.style.backgroundColor = '#002444';
    header.style.backgroundColor = '#000D1D';
    footer.style.color = 'white';
    burguer.style.color = 'white';

    darkmode.style.display = 'none';
    lightmode.style.display = 'inline-block';
}

function lightMode() {
    let h1h2ap = document.querySelectorAll('h1, h2, a, p');

    divs.forEach(function(div) {
        div.style.backgroundColor = "#658896";
    });

    h1h2ap.forEach(function(element) {
        element.style.color = "black";
    });


    body.style.backgroundColor = '#84D4F4';
    header.style.backgroundColor = '#243C4C';
    footer.style.color = 'black';
    burguer.style.color = 'black';

    darkmode.style.display = 'inline-block';
    lightmode.style.display = 'none';
}