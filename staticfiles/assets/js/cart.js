var updateCart = document.querySelectorAll(".update-cart")

for(let i=0; i<updateCart.length; i++){
    updateCart[i].addEventListener("click", ()=>{
        var productId = updateCart[i].dataset.product
        var action = updateCart[i].dataset.action
        console.log("productId:", productId, "Action:", action)


        if(user === 'AnonymousUser'){
            console.log('Not logged in')
            // alert("item added successfully")
            addCookieItem(productId, action)
        }
    })
}

function addCookieItem(productId, action){
    if(action == 'add'){
        if(cart[productId] == undefined){
            cart[productId] = {'quantity' : 1}
        }
        else{
            // cart[productId][quantity]++
            cart[productId]['quantity'] += 1
        }
    }
    else if(action == 'remove'){
        if(cart[productId] == undefined){
            alert("Item not found in cart")
        }
        else{
            cart[productId]['quantity'] -= 1
            if(cart[productId]['quantity'] == 0){
                delete cart[productId]
            }
        }
    }
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload()
}

function updateUserOrder (productId, action){
    console.log("user is logged in, sending data...")

    var url = 'update_item'

    fetch(url, {
        method: 'POST', 
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action}) 
    })
    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data', data)
        location.reload()
    })
}




