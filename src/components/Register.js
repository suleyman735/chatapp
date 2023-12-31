import React, { useState } from "react";
import { TextField,Button } from "@mui/material";

export default function Register() {
  const BASE_URL = "http://127.0.0.1:8000/api/"
  const [formData,setFormData] = useState({
    "email":"",
    "first_name":"",
    "last_name":"",
    "password":""

  });
  const handleFormSubmit = ()=>{
    fetch(`${BASE_URL}register/`,{
      method:'POST',
      headers:{
        'Content-Type':'application/json'
      },
      body:JSON.stringify(formData)
    }).then(response=>response.json()).then(data =>{
      console.log(data);
    }).catch(error=>{
      console.log(error);
    })
  }
  return (
    <div className="container text-center">
      <div className="mt-3">
        <TextField id="email" type="email" onChange={e=>setFormData({...formData,email:e.target.value})} label="Email" variant="outlined" />
      </div>
      <div className="mt-3">
        <TextField id="first_name" type="text" onChange={e=>setFormData({...formData,first_name:e.target.value})} label="First name" variant="outlined" />
      </div>
      <div className="mt-3">
        <TextField id="last_name" type="text" onChange={e=>setFormData({...formData,last_name:e.target.value})} label="Last Name" variant="outlined" />
      </div>
      <div className="mt-3">
        <TextField id="password" type="password" onChange={e=>setFormData({...formData,password:e.target.value})} label="Password" variant="outlined" />
      </div>
      <div className="mt-3">
        <Button variant="contained" onClick={handleFormSubmit}>Save</Button>
      </div>
    </div>
  );
}
