const send_response = (message) => {
    message_editted = message.split(' ').join('+');
    fetch(`http://localhost:5000/conv?sentence=${message_editted}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("chat").innerHTML += `<div class="bot-message">${data}</div>`
        });
    space_for_new_message();
}

const space_for_new_message = () => {
    var children = document.getElementById("chat").childNodes;
    children.forEach(function(item){
        let position = parseInt(item.style.bottom) || 0;
        if(position == 0){
            item.style.bottom = "40px"
        }else{
            item.style.bottom = `${40+position}px`
        }
    });
}

const send_message = (side_message) => {
    let message = document.getElementById("message").value || side_message;
    document.getElementById("message").value = "";

    if(message != ""){
        space_for_new_message();
        document.getElementById("chat").innerHTML += `<div class="my-message">${message}</div>`
        setTimeout(() => send_response(message), Math.floor((Math.random()*10000))/4);
    }
}