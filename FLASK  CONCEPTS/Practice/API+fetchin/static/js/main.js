document.querySelector("#form").addEventListener('submit', async (e) => {
    e.preventDefault()
    const username = document.querySelector('#username').value
    let  pass= document.querySelector('#password')
    let password=pass.value
    try {
        const response = await fetch('/', {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            }, body: JSON.stringify({ username, password })
        })
        let data = await response.json()
        console.log(data)
        if (data.success) {
            window.location.href = "/home"
        }
        else {
            console.log(JSON.stringify({username,password}))
            pass.value=""
            alert(data.error)}
    }
    catch {
        pass.value=""
        alert("please check net")
    }
})