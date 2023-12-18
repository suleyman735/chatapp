import React from 'react'

export default function ({text,sent}) {
  return (
    <div className={`message ${sent ? 'sent':'recieved'}`}>
        <div className='message-bubble'>{text}</div>
    </div>
  )
}
