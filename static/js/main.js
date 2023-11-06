const menu_up = document.querySelector(".header_menu")
const menu_down = document.querySelector(".button_close")


menu_up.addEventListener("click", (e)=>{
    const body_menu = document.querySelector(".menu_back") 
    body_menu.style.display = "flex"
    body_menu.style.opacity = "1"
})

menu_down.addEventListener("click", (e)=>{
    const body_menu = document.querySelector(".menu_back") 
    body_menu.style.opacity = "0"
    body_menu.style.display = "none"
})




const model_wind_button = document.querySelector("#button_model")
const model_wind = document.querySelector("#model")

try {
    model_wind_button.addEventListener("click", (e)=>{
        model_wind.classList.add("model_activ");
    })
    
    model_wind.addEventListener("click", (e)=>{
        if(e.target == model_wind){
            model_wind.classList.remove("model_activ");
        }
    })
  } catch (err) {}



setTimeout(()=>{
    const acc = document.getElementsByClassName("accordion")

    for(let i = 0; acc.length > i; i++){
        acc[i].onclick = function(){
            this.classList.toggle("active")
    
            const panel = this.nextElementSibling
    
            if(panel.style.maxHeight){
                panel.style.maxHeight = null
                panel.style.padding = null
            }else{
                panel.style.padding = "18px"     
                panel.style.maxHeight = panel.scrollHeight + "px"       
            }
        }
    }
}, 100)


const commentsVal = document.querySelector("#comments")
const btnComment = document.querySelector("#submit_comment")
btnComment.addEventListener("click", ()=>{
    
    const url = new URL(window.location.href.replace("#", "?"))
    const params = url.searchParams

    const message = {
        text: commentsVal.value,
        id: params.get("id") 
    }

    fetch(`${window.origin}/upload_comment`, {
        method:"POST",
        credentials: "include",
        body: JSON.stringify(message),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    })
    .then((response)=>{
        if(response.status !== 200){
            console.log("lol")
            return;
        }
        response.json().then((data)=>{
            console.log(data)
            commentsVal.value = null
        })
    })
})
