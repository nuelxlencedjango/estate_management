

let menuInfo = false;
let main_menu = document.getElementById("menu");
let mainRow  = document.getElementById("overall");
//let checkMenu = document.getElementById("want_buy");
//let logo = document.getElementById("logo");

function checkToggle(){
if(menuInfo===false){

    
    //checkMenu.style.paddingTop ="360px";
    main_menu.style.display = "block";
    mainRow.style.marginTop ="400px";
   
    menuInfo =true;
}
else{
    //checkMenu.style.marginTop ="30px";
    main_menu.style.display = "none";
    mainRow.style.marginTop ="30px";
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





let popup = false;
let messenger = document.getElementById("messenger");
let chatPop  = document.getElementById("popupChat");
//let checkMenu = document.getElementById("want_buy");
//let logo = document.getElementById("logo");

function openMessenger(){
if(popup===false){
    chatPop.style.display = "block"; 
    popup =true;
}
else{
   
    chatPop.style.display = "none";
    popup =false;

}
}