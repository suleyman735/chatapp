
import './App.css';
import {ChatEngine} from 'react-chat-engine'
import Register from './components/Register';
import Login from './components/Login';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navigation from './components/Navigation';
import Sidebar from './components/Sidebar';
import Message from './components/Message';
import ChatArea from './components/ChatArea';


function App() {
  return (
    <div className="App">
      
      {/* <div className='chat-container'>
      <Sidebar/>
      <ChatArea />
      </div> */}
     
      

           <BrowserRouter >
      <Navigation />
      <Routes>
      
        <Route exact path='login/' element={<Login/>}/>
        <Route exact path='register/' element={<Register/>}/>
        <Route exact path='chat/' element={<ChatArea/>}/>
        <Route path='chat/' element={<><Sidebar/><ChatArea/></>}> </Route>

          
      
       </Routes>

   
      </BrowserRouter>

</div>
  );
}

export default App;
