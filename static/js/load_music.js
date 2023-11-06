let start = 0

window.onload = ()=>{
    const message = {
        start: start,
        end: start + 20 
    }
    fetch(`${window.origin}/load_music_view`, {
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
            view(data.data)
            defaultPlayList = data.data
        })
    })
}


function view(data){
    const mainBody = document.querySelector(".list_music")
    for(music of data){
        const card = `<div class="music_card">
        <div class="music_card_img">
            <img src="${music.img}">
            <div class="music_card_play">
                <a href="#type=play&id=${music.id}"><span class="material-icons">play_arrow</span></a>
                <a href="#type=add_list&id=${music.id}"><span class="material-icons">playlist_add</span></a>
            </div>
        </div>
        <div class="music_card_text">
            <div class="card_text_listener">
                <h1>${music.name}</h1>
                <h3>${music.listening}<span class="material-icons">headset</span></h3>
            </div>
            <div class="card_text_info">
                <h3><span class="material-icons">thumb_up</span>${music.like}</h3>
                <h3><span class="material-icons">thumb_down</span>${music.dislike}</h3>
                <a href="#id=${music.id}" id="commens_button"><h3><span class="material-icons">question_answer</span>${music.comments}</h3></a>
            </div>
        </div>
    </div>`
        mainBody.insertAdjacentHTML("beforeEnd", card);
    }    
}

setTimeout(()=>{
    const buttonModel = document.querySelectorAll("#commens_button")
    const model_wind_info = document.querySelector("#model_commens")
    
    try {
        for(button of buttonModel){
            button.addEventListener("click", (e)=>{
                model_wind_info.classList.add("model_activ");
                loadComments()
            })
        }
        model_wind_info.addEventListener("click", (e)=>{
            if(e.target == model_wind_info){
                model_wind_info.classList.remove("model_activ");
            }
        })
      } catch (err) {}
}, 1000)


function viewCommends(data){
    const mainBody = document.querySelector(".comments_list")
    mainBody.innerHTML = ""
    for(comments of data){
        const card = `<div class="comment">
        <div class="img_menu"><img src="/static/${comments.user.icon}"></div>
        <div class="comments_text">
            <h2>${comments.user.nickname}</h2>
            <p>${comments.comment.text}</p>
        </div>
    </div>`
        mainBody.insertAdjacentHTML("beforeEnd", card);
    }    
}

function loadComments(){

    const url = new URL(window.location.href.replace("#", "?"))
    const params = url.searchParams
    const message = {
        id: params.get("id"),
    }
    console.log(message)
    fetch(`${window.origin}/load_view_comments`, {
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
            viewCommends(data.data)
        })
    })
}