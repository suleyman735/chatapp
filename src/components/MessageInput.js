import React, { useState } from 'react'

export default function () {
    const [inpuValue,setInpuValue]=useState('')
    const handleSendMessage=()=>{
        console.log('Message send');
    }
  return (
    <div className='message-input'>
        <textarea 
        placeholder='Type your message'
        value={inpuValue}
        // onChange={handleInputChange}
        />
        <button onClick={handleSendMessage}>Send</button>
    </div>
  )
}
