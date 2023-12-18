import React from 'react'
import { Link } from 'react-router-dom'


export default function Navigation() {
  return (
    <div>
        <Link to='login/'>Login</Link>
        <br></br>
        <Link to='register/'>Register</Link>
        <br></br>
        <Link to='chat/'>Chat</Link>
        
    </div>
  )
}
