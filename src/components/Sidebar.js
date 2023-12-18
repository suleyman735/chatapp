import React, { useEffect, useState } from 'react'
import withAuthentication from '../utils/withAuthentication'
import axios from 'axios'
import { Box, LinearProgress, List } from '@mui/material'
import UserItem from './UserItem'


 function Sidebar() {
  const BASE_URL= `http://127.0.0.1:8000/`
  const[userList,setUserList]=useState([])
  const[userLoader,setUserLoader]= useState(true)
  const getAuthTokenFromCookie =()=>{

    const cookies= document.cookie.split(';')
    for (let cookie in cookies) {
      const [name,value] = cookie.trim.split("=");
      if(name === "token"){
        console.log(value);
        return value
      }
      
    }
    return null
  }

  useEffect(()=>{
    const authToken =getAuthTokenFromCookie();
    if(authToken){
      axios.get(`${BASE_URL}api/users/`,{
        headers:{
          Authorization:`Bearer ${authToken}`
        }
      }).then(
        response=>{
          setUserList(response.data)
          setUserList(false)
          console.log(userList);
        }
      )
console.log(authToken);
    }
  },[])
  return (
    <div className='sidebar'>
      {userLoader? (
        <Box sx={{width:'100%'}}>
          <LinearProgress />
        </Box>
      ):(
        <List sx={{width:'100%',maxWidth:360,bgcolor:'background.paper'}}>
          {userList.map((user,index)=>(
            <UserItem key={index} email={user.email} name={`${user.first_name} ${user.last_name}`}id ={user.id}/> 
          ) )}
        </List>
      )
    }

    </div>
  )
}
export default withAuthentication(Sidebar)
