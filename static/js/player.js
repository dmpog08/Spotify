let audio = new Audio();
let typeVolume = '<span class="material-icons">volume_up</span>'
let seekto
const playBtn = document.querySelector("#now_sound")
const nextBtn = document.querySelector("#next_sound")
const pregBtn = document.querySelector("#preg_sound")
const muteBtn = document.querySelector("#mute_sound")
const seekSlider = document.querySelector("#slider")
const volumeSlider = document.querySelector("#volume_slider")
let seeking = false
const curTimeText = document.querySelector("#current_time")
const durTimeText = document.querySelector("#time_sound")
const volumeText = document.querySelector("#volume_text")

let defaultPlayList = []
playList = ["lol", "pop", "info"]
let currentPlayList = []
let currentSound

audio.onloadedmetadata = function(){
    durTimeText.innerHTML = timeSoundView(audio.duration)
}

playBtn.addEventListener("click", playPause);
nextBtn.addEventListener("click", nextSound);
pregBtn.addEventListener("click", pregSound);
muteBtn.addEventListener("click", muteSound);
seekSlider.addEventListener("mousedown", (e)=>{
    seeking = true;
    audio.muted = true
    seek(e);
});
seekSlider.addEventListener("mousemove", (e)=>{seek(e)});
seekSlider.addEventListener("mouseup", ()=>{
    seeking = false
    audio.muted = false});
volumeSlider.addEventListener("mousemove", setVolume)
audio.addEventListener("timeupdate", ()=>{seekTimeUpdate()});
audio.addEventListener("ended", ()=>{nextSound()});

function loadSound(soundFile, imgFile, nameMusic, nameAuter, id){
    currentSound = id
    audio.src = soundFile
    audio.loop = false
    audio.preload = "metadata"
    const player = document.querySelector(".player")

    const img = player.querySelector(".player_info_img").childNodes[0]
    const name_music = player.querySelector(".player_info_text").childNodes[1]
    const name_auter = player.querySelector(".player_info_text").childNodes[3]

    img.src = imgFile

    name_music.innerHTML = nameMusic
    name_auter.innerHTML = nameAuter

    seekSlider.value = 0

    player.classList.add("player_active")
    playPause()
}

function timeSoundView(time){
    const min = Math.floor(time / 60)
    let second = Math.floor(time - min * 60)
    if(second < 10)
        second = `0${second}`
    
    return `${min}:${second}`
}

function updateIconVolume(type){
    muteBtn.childNodes[1].innerHTML = type
    menuVolume.childNodes[5].innerHTML = type
}

function playPause(){
    if(audio.paused){
        audio.play();
        playBtn.innerHTML = '<span class="material-icons">pause</span>'
    }else{
        audio.pause();
        playBtn.innerHTML = '<span class="material-icons">play_arrow</span>'
    }
    durTimeText.innerHTML = timeSoundView(audio.duration)
}

function nextSound(){
    let info = 0
    for(let i = 0; i < currentPlayList.length; i++){
        if(currentPlayList[i].id == currentSound){
            info = i
        } 
    }
    if(info + 1 > currentPlayList.length - 1){
        sound = currentPlayList[0]
    }else {
        sound = currentPlayList[info + 1]
    }
    loadSound(sound.file_name, sound.img, sound.name, sound.id_user, sound.id)
}

function pregSound(){
    let info = 0
    for(let i = 0; i < currentPlayList.length; i++){
        if(currentPlayList[i].id == currentSound){
            info = i
        } 
    }
    if(info - 1 < 0){
        sound = currentPlayList[currentPlayList.length - 1]
    }else {
        sound = currentPlayList[info - 1]
    }
    loadSound(sound.file_name, sound.img, sound.name, sound.id_user, sound.id)
}

function setVolume(){
    audio.volume = volumeSlider.value / 100
    volumeText.innerHTML = volumeSlider.value
    if(50 < volumeSlider.value && volumeSlider.value <= 100){
        typeVolume = "volume_up"
    }else if(0 < volumeSlider.value && volumeSlider.value <= 50){
        typeVolume = "volume_down"
    }else{
        typeVolume = "volume_mute"
    }
    updateIconVolume(typeVolume)
}

function muteSound(){
    if(audio.muted){
        audio.muted = false
        updateIconVolume(typeVolume)
    }else{
        audio.muted = true
        updateIconVolume('volume_off')
    }
}


function seek(e){
    if(audio.duration == 0){
        null
    }else{
        if(seeking){
            seekSlider.value = (e.clientX - seekSlider.offsetLeft) / (seekSlider.offsetWidth - 0)
            seekto = seekSlider.value * audio.duration
            audio.currentTime = seekto
            curTimeText.innerHTML = timeSoundView(audio.currentTime)
        }
    }
}

function seekTimeUpdate(){
    if(audio.duration){
        if(seeking == false){
            seekSlider.value = audio.currentTime * (100 / audio.duration);
            curTimeText.innerHTML = timeSoundView(audio.currentTime)
        }
    }
}

//*************************************************************/
const menuVolume = document.querySelector(".menu_right_volume")

muteBtn.addEventListener("contextmenu", (e)=>{
    e.preventDefault();
    menuVolume.classList.toggle("active_music")
    let mod = (menuVolume.offsetWidth - muteBtn.offsetWidth) / 2
    menuVolume.style.left = `${muteBtn.offsetLeft - mod}px`
    menuVolume.style.top = `${muteBtn.getBoundingClientRect().y - menuVolume.offsetHeight}px`
    updateIconVolume(typeVolume)
})

menuVolume.addEventListener("click", (e)=>{
    e.stopPropagation();
})

//************************************************************ */
const menuListSound = document.querySelector(".list_sound_menu")

function viewListSound(data, where, id){
    for(music of data){
        const card = `<div class="music_card">
        <div class="music_card_img list">
            <img src="${music.img}">
            <div class="music_card_play list_play">
                <a href="#type=play&id=${music.id}&list_sound=${id}"><span class="material-icons">play_arrow</span></a>
                <a href="#type=add_list&id=${music.id}"><span class="material-icons">playlist_add</span></a>
            </div>
        </div>
        <div class="music_card_text">
            <div class="card_text_listener list_listener">
                <h1>${music.name}</h1>
                <h3>${music.listening}<span class="material-icons">headset</span></h3>
            </div>
            <div class="card_text_info list_info">
                <h3><span class="material-icons">thumb_up</span>${music.like}</h3>
                <h3><span class="material-icons">thumb_down</span>${music.dislike}</h3>
                <a href="#id=${music.id}" id="commens_button"><h3><span class="material-icons">question_answer</span>${music.comments}</h3></a>
            </div>
        </div>
    </div>`
        where.insertAdjacentHTML("beforeEnd", card);
    }    
}

function viewList(data, where){
    for(let i = 0 ; i < data.length; i++){
        const listView = `
        <div class="wrapper">
            <button class="accordion" type="button">${data[i].name}</button>
            <div class="panel">
            </div>
        </div>`
        where.insertAdjacentHTML("beforeEnd", listView);
        const info_panel = where.querySelector(".panel")
        viewListSound(data[i].sounds, info_panel, i)
    }
}


fetch(`${window.origin}/list_sound_view`, {
    method:"POST",
    credentials: "include",
    body: JSON.stringify({}),
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
        playList = data.data
        viewList(data.data, menuListSound)
    })
})

const butMenuListSound = document.querySelector("#list_sound")

butMenuListSound.addEventListener("click", ()=>{
    menuListSound.classList.toggle("active_menu")
    const player = document.querySelector(".player")
    menuListSound.style.left = `${player.offsetWidth - menuListSound.offsetWidth}px`
    menuListSound.style.top = `${butMenuListSound.getBoundingClientRect().y - menuListSound.offsetHeight}px`
})

//*************************************************/
window.addEventListener('popstate', function(e){
    const url = new URL(window.location.href.replace("#", "?"))
    const params = url.searchParams

    if(params.get("type") == "play"){
        const mass = {
            id: params.get("id")
        }
    
        fetch(`${window.origin}/get_music`, {
            method:"POST",
            credentials: "include",
            body: JSON.stringify(mass),
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
                loadSound(data.data.file_name, data.data.img, data.data.name, data.data.id_user, data.data.id)
                try{
                    idList = params.get("list_sound")
                    currentPlayList = playList[idList].sounds
                }catch (err) {
                    currentPlayList = defaultPlayList
                }
            })
        })
    }
    else if(params.get("type") == "add_list"){
        const mass = {
            id: params.get("id")
        }
    
        fetch(`${window.origin}/add_list_music`, {
            method:"POST",
            credentials: "include",
            body: JSON.stringify(mass),
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
                console.log(data.data)
            })
        })
    }
});

