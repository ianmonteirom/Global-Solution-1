// alert('Seja bem-vindo!') 

// SlideShow Automático
let imagens=['./src/assets/pesca1.jpg','./src/assets/pesca2.jpg','./src/assets/pesca3.jpg'];
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

function clickMenu(){
    if(item.style.display == 'block') {
        item.style.display ='block'
    } else {
        item.style.display = 'block'

    }

}
