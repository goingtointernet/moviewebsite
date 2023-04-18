/*==dark-mode============================*/
var icon = document.getElementById("nav-modes");
    /*on click add dark-theme class to body element*/
    icon.onclick = function(){
        document.body.classList.toggle("light-theme");

        var theme;

        /* if dark-theme class avaliable in body element do this js code*/
        if(document.body.classList.contains("light-theme")){
            icon.classList.add("fa-moon")
            icon.classList.remove("fa-sun")
            theme = "LIGHT"
        }
        /* if not do this*/
        else{
            icon.classList.add("fa-sun")
            icon.classList.remove("fa-moon")
            theme = "DARK"
        }
        /*save to localstorage beacuse we need the selected theme even user refresh the page or move to next page or open the page again after some time*/
        localStorage.setItem("PageTheme", JSON.stringify(theme));
}

    /* get value of theme varibale which we save in localStorage*/
    let GetTheme = JSON.parse(localStorage.getItem("PageTheme"));
 
    /* if "theme" varibale value is DARK do this js code*/
    if(GetTheme === "LIGHT"){
        document.body.classList = "light-theme";
        icon.classList.add("fa-moon")
        icon.classList.remove("fa-sun")
    }
    /*If "theme" Value is Not DARK Value Do This*/
    else{
        document.body.classList = "";
        icon.classList.add("fa-sun")
        icon.classList.remove("fa-moon")
    }

