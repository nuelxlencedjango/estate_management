

let menuInfo = false;
let main_menu = document.getElementById("menu");
//let checkMenu = document.getElementById("want_buy");
//let logo = document.getElementById("logo");

function checkToggle(){
if(menuInfo===false){

    //checkMenu.style.marginTop ="380px";
    //checkMenu.style.paddingTop ="360px";
    main_menu.style.display = "block";
    //main_menu.style.marginBottom="400px";
    $("#menu").css({"margin-bottonr":"600px"});

   
    menuInfo =true;
}
else{
    //checkMenu.style.marginTop ="30px";
    main_menu.style.display = "none";
    menuInfo =false;

}
}




window.onscroll = function() {myFunction()};
            
var header = document.getElementById("myHeader");
var sticky = header.offsetTop;


function myFunction() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
    $(".header").css({"background-color":"whitesmoke"});
   
  } else {
    header.classList.remove("sticky");
    $(".header").css({"background-color":"whitesmoke"});
  }
}

