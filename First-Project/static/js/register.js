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
let button2 = document.querySelector('#show2')
button2.addEventListener('click', (e) => {
    e.preventDefault()
    let show = document.querySelector('#set-password')
    if (show.type == "password") {
        show.type = 'text';
        button2.innerText = 'hide'
    } else if (show.type == 'text') {
        show.type = 'password'
        button2.innerText = 'show'
    }
})
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}  
let login=document.querySelector('#login')
login.addEventListener('submit',async function (e) {
    e.preventDefault()
    let pass = document.querySelector('#password').value.trim()
    let conPass= document.querySelector('#set-password').value.trim()
    let username = document.querySelector('#username').value
    let email=document.querySelector('#email').value
    let name=document.querySelector('#first_name').value
    let lname=document.querySelector('#last_name').value

    if(pass!=="" && conPass!=="" && isValidEmail(email) && username && name){
    try{
        let response = await fetch('/register', ({
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name:name,
                lname:lname,
                email:email,
                username:username,
                password:pass
            })
        }));
        
        let data = await response.json()
        console.log(data)
        if(data.success){
            console.log(data)
            window.location.href="/login"
            console.log(
                "pass"
            )
        }else{
            alert(data.message)
        }
    } catch(error){
        console.log(error)
        alert(error)
    }}else{
        document.querySelector('#password').value = ''
        document.querySelector('#set-password').value = ''
        document.querySelector('#email').value = ""
        alert("Please check your fields")
    }
})


