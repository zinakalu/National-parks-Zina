import React, { useState } from 'react'

function SignupComponent(){
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    function handleSignup(){
        const data = { username, password}

        fetch('/signup', {
            method: 'POST',
            headers:{
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(res => res.json)
        .then(data => {
            console.log(data)
        })
        .catch(error => {
            console.error(error)
        })
    }

    return (
        <div>
            <h2>Signup</h2>
            <input
            type= "text"
            placeholder="Username"
            value={username}
            onchange = {e => setUsername(e.target.value)}
            />
            <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={e => setPassword(e.target.value)}
            />

            <button  onClick={handleSignup} >Signup</button>
        </div>

    );

}


function LoginComponent(){
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');


    function handleLogin(){
        const data = { username, password}

        fetch('/login', {
            method: 'POST',
            headers:{
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(res => res.json())
        .then(data => {
            console.log(data)
        })
        .catch(error =>{
            console.error(error)
        })
    }

    return (
        <div>
            <h2>Login</h2>
            <input 
                type="text"
                placeholder="Username"
                value={username}
                onchange={e => setUsername(e.target.value)}
            />
            <input 
                type="password"
                placeholder="Password"
                value={password}
                onchange={e => setPassword(e.target.value)}
            />
            <button onClick={handleLogin}>Login</button>
        </div>
    )

}


function LogoutComponent(){

    function handleLogout(){
        fetch('/logout', {
            method: 'DELETE',
        })
        .then(res => res.json())
        .then(data => {
            console.log(data)
        })
        .catch(error => {
            console.error(error)
        })
    }

    return (
        <div>
            <h2>Logout</h2>
            <button onClick={handleLogout}>Logout</button>
        </div>
    )

}

export{
    SignupComponent,
    LoginComponent,
    LogoutComponent
}