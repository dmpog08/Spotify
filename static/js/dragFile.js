const dragArea = document.querySelector("#dragArea");
let file;
const inputFile = document.querySelector("#input_file") 
let buttonFile = document.querySelector("#button_file")
const buttonSend = document.querySelector("#send")

function showFile(){
    const fileType = file.type;
    const valid = ["image/jpeg", "image/jpg", "image/png"]
    if(valid.includes(fileType)){
        const fileReader = new FileReader();
        fileReader.onload = () => {
            const fileURL = fileReader.result
            const img = `<img src="${fileURL}" alt="">
            <div class="delite_file"><span class="material-icons">close</span></div>`
            dragArea.innerHTML = img
            const div = document.querySelector(".delite_file") 
            div.addEventListener("click", delite)
        };
        fileReader.readAsDataURL(file);
    }else{
        dragArea.classList.remove("active");
    }
}

function delite(){
    file = null
    dragArea.innerHTML = '<span class="material-icons">backup</span><label for="img">Обложка</label><button class="button button_form", id="button_file",  type="button">Загрузить</button>'
    buttonFile = document.querySelector("#button_file")
    buttonFile.onclick = ()=>{
        inputFile.click();
        
    };
}

buttonFile.onclick = ()=>{
    inputFile.click();
};

inputFile.addEventListener("change", function(){
    file = this.files[0];
    showFile()
    dragArea.classList.remove("active");
});

dragArea.addEventListener("dragover", (e)=>{
    e.preventDefault()
    dragArea.classList.add("pulse")
});

dragArea.addEventListener("dragleave", ()=>{
    dragArea.classList.remove("pulse")
})

dragArea.addEventListener("drop", (e)=>{
    e.preventDefault()
    file = e.dataTransfer.files[0];
    dragArea.classList.remove("pulse")
    showFile()
})