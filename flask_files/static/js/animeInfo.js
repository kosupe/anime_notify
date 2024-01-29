//曜日選択の処理
const list = document.querySelectorAll(".list");
function activeLink(){
    list.forEach((item) =>
    item.classList.remove("active"));
    this.classList.add("active")
}
list.forEach((item) =>{
    item.children[0].addEventListener("click", event => {
        event.preventDefault()
    })
    item.addEventListener("click", activeLink)
})

//時間のselectの初期化
let selects = document.querySelectorAll("select")
for (let i=23; i >= 0; i--){
    if (i < 10){
        time = "0" + String(i)    
    }else{
        time = String(i)
    }
    let option = `<option value="${time}"  >${time}</option>`
    selects[0].firstElementChild.insertAdjacentHTML("afterend", option)
}
for (let i=55; i >= 0; i-=5){
    if (i < 10){
        time = "0" + String(i)    
    }else{
        time = String(i)
    }
    let option = `<option value="${time}"  >${time}</option>`
    selects[1].firstElementChild.insertAdjacentHTML("afterend", option)
}




let editButton   = document.getElementById("editButton")
let deleteButton = document.getElementById("deleteButton")

editButton.addEventListener("click",()=>{
    
})