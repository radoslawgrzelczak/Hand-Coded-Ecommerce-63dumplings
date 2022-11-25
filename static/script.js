document.querySelector("#checkout-button")

function grabUserData(){
    let name = document.querySelector("#name").value
    let quantity = document.querySelector("#quantity").value
    localStorage.setItem("name", name)
    localStorage.setItem("quantity", quantity)
}
