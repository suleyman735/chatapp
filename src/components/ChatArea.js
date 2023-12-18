import React from 'react'
import Message from './Message'
import MessageInput from './MessageInput'
import withAuthentication from '../utils/withAuthentication'

 function ChatArea() {
  return (
    <div className='chat-area'>
        <div className='chat-header'></div>
        <div className='messages'>
            <Message text="Hey how is it going" sent/>
            <Message text="I am good" received/>
        </div>
        <MessageInput />
    </div>
  )
}
export default withAuthentication(ChatArea)
