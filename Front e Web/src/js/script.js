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
let imagens=['./src/assets/img/bike1.png','./src/assets/img/bike2.jpg','./src/assets/img/bike3.jpg', './src/assets/img/bike4.jpg'];
let index = 0;
let time = 3000;

function slideShow(){
    document.getElementById('imgBanner').src=imagens[index];
    index++;

    if(index == imagens.length){
        index = 0;
    }
    setTimeout('slideShow()', time);
}
slideShow();

