/*!
 * SlickNav Responsive Mobile Menu v1.0.10
 * (c) 2016 Josh Cope
 * licensed under MIT
 */



/*let navbar_menu = document.getElementById("nav_menu");
let menu_list = document.getElementById("nav_menu_list");

window.onscroll =function(){
    if(window.pageYOffset >= menu_list.offsetTop){
        navbar_menu.classList.add("sticky");
    }
    else{
        navbar_menu.classList.remove("sticky");
    }
}*/


//sticky navbar

/*let timV = document.getElementById("tim-vine");
let navbar_new = document.getElementById("navbar");

let navPoss = navbar.getBoundingClientRect().top;

window.addEventListener("scroll", e => {
  let scrollPoss = window.scrollY;
  if (scrollPoss > navPoss) {
    navbar_new.classList.add('sticky');
    main_menu.classList.add('navbarOffsetMargin');
  } else {
    navbar_new.classList.remove('sticky');
    main_menu.classList.remove('navbarOffsetMargin');
  }
});*/




let menuInfo = false;
let main_menu = document.getElementById("menu")
let checkMenu = document.getElementById("want_buy");

function checkToggle(){
if(menuInfo===false){

    checkMenu.style.marginTop ="380px";
    //checkMenu.style.paddingTop ="360px";
    main_menu.style.display = "block";
    menuInfo =true;
}
else{
    checkMenu.style.marginTop ="30px";
    main_menu.style.display = "none";
    menuInfo =false;

}
}



