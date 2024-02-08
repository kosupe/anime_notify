//Editの処理---------------------------------------------------
let modalFilter = document.getElementById("modalFilter")
//Text
let editWeekText = document.getElementById("editWeekText")
let editTimeHourText = document.getElementById("editTimeHourText")
let editTimeMinText  = document.getElementById("editTimeMinText")

//modal
let modalEdit = document.getElementsByName("modalEdit")[0]

//button
let editButton   = document.getElementById("editButton")
editButton.addEventListener("click",()=>{
    modalEdit.classList.add("activePop")
    modalFilter.classList.add("activePop")
})
let editCloceButton = document.getElementsByName("editClose")[0]
editCloceButton.addEventListener("click", ()=>{
    modalEdit.classList.remove("activePop")
    modalFilter.classList.remove("activePop")
})

let deleteButton = document.getElementById("deleteButton")



//曜日選択の処理--------------------------------------------
const list = document.querySelectorAll(".list");
function activeLink(){
    list.forEach((item) =>{
        item.classList.remove("active")
        item.textContent.r
    });
    this.classList.add("active")
    editWeekText.textContent = this.children[0].textContent[37]+"曜日"
}
list.forEach((item) =>{
    item.children[0].addEventListener("click", event => {
        event.preventDefault()
    })
    item.addEventListener("click", activeLink)
})



//時間のselectの初期化--------------------------------------
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
selects[0].addEventListener("change", ()=>{
    console.log(selects[0].value)
    editTimeHourText.textContent = selects[0].value
})
selects[1].addEventListener("change", ()=>{
    console.log(selects[1].value)
    editTimeMinText.textContent = selects[1].value
})