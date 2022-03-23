$(document).ready(function(){
    if ($('.owl-carousel').length){
    $('.owl-carousel').owlCarousel({
        loop:true,
        //margin:10,
        nav:true,

       // autoplayTimeout: 2000,
        autoplay:true,
    //autoplayTimeout:10000,
    //autoPlayHoverPause:false,
        //animateOut: 'slideOutDown',
        //animateIn: 'flipInX',
        responsiveClass:true,
        responsive:{
            0:{
                items:1,
                
            },
            600:{
                items:2,
               
            },
            1000:{
                items:3,
               
                loop:true,
            }
        }
    })
}
})




