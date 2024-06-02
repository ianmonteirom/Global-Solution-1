// alert('Seja bem-vindo!') 

// SlideShow da Sessão do Problema
let imagensProblema=['./src/assets/problemapesca.jpg','./src/assets/problemapesca2.png','./src/assets/problemapesca3.jpg'];
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
let imagensTecnologia=['./src/assets/img/','./src/assets/img/','./src/assets/img/', './src/assets/img/'];
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
let imagensObjetivos=['./src/assets/','./src/assets/','./src/assets/', './src/assets/'];
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
let imagensPublicoAlvo=['./src/assets/','./src/assets/i','./src/assets/', './src/assets/'];
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
let imagensBeneficios=['./src/assets/','./src/assets/','./src/assets/', './src/assets/'];
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

// SlideShow da Sessão do Dia a Dia
let imagenDiaadia=['./src/assets/','./src/assets/','./src/assets/', './src/assets/'];
let indexDiaadia = 0;
let timeDiaadia = 3000;

function slideShowDiaadia(){
    document.getElementById('imgDiaadia').src=imagensDiaadia[indexDiaadia];
    indexDiaadia++;

    if(indexDiaadia == imagensDiaadia.length){
        indexDiaadia = 0;
    }
    setTimeout('slideShowDiaadia()', timeDiaadia);
}
slideShowDiaadia();
