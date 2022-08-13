document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#email_signup').onsubmit = () =>{
        var email = document.querySelector("#email_input").value;
        console.log(email)
        fetch('/emails', {
            method: 'POST',
            body: JSON.stringify({
                correo: email
            })
        })
        .then(response => response.json())
        .then(result => {
            console.log(result)
        })
        thanks = document.querySelector("#thanks")
        thanks.style.display = "block"
        return false;
    }
})