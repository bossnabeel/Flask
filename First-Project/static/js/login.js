let button = document.querySelector('.show')
button.addEventListener('click', (e) => {
    e.preventDefault()
    let show = document.querySelector('#password')
    if (show.type == "password") {
        show.type = 'text';
        button.innerText = 'hide'
    } else if (show.type == 'text') {
        show.type = 'password'
        button.innerText = 'show'
    }
})
let login=document.querySelector('#login')
login.addEventListener('submit',async function (e) {
    e.preventDefault()
    let pass = document.querySelector('#password').value
    let username = document.querySelector('#username').value
    try {
        let response = await fetch('/login', ({
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username:username,
                password:pass
            })
        }));
        
        let data = await response.json()
        console.log(data)
        if(data.success){
            window.location.href="/"
        }else{
            alert(data.message)
        }
    } catch(err){
        alert("pleas check your network")
    }
})