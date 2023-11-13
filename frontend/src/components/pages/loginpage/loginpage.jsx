import React,{useState} from 'react'
import './loginpage.css'
import { Form, Button} from 'react-bootstrap';
import { Link, Route } from 'react-router-dom';
import {useForm} from 'react-hook-form';
import {login} from "../../Auths/auth";
import { useNavigate } from 'react-router-dom';


const LoginPage = () => {

  const {register, handleSubmit, reset, formState:{errors}} = useForm()
  const navigate = useNavigate()
		
  const loginMe = (data)=> {
    console.log(data)
   const loginReqOption = {
    method: "POST",
    headers: {
      "content-type": "application/json"
    },
    body: JSON.stringify(data)
  };
  fetch("/users/login", loginReqOption)
  .then(resp=>resp.json())
  .then(data=>{
    console.log(data.access_token)
    login(data.access_token)
    if (data){
      login(data.access_token)

      navigate("/")
     }
     else{
         alert('Invalid username or password')
     }
    
  })
    reset()
    
  }

  return (
    <div className='container-signup'>
        <div className="form">
          <form>
            <Form.Group>
              <Form.Label htmlFor='username'>Username</Form.Label>
              <Form.Control type='text' id='username' placeholder='
              your name' autoComplete='off' {...register("username", {required: true, maxLength: 80})}></Form.Control>
            </Form.Group>
            {
             errors.username && <p style={{color: "red", fontSize: 12}}>Username is required.</p>
            }
            {
             errors.username?.type === "maxLength" && <p style={{color: "red", fontSize: 12}}>Username should be less than 81 characters.</p>
            }
           
            <br/>
            <Form.Group>
              <Form.Label htmlFor='password'>Password</Form.Label>
              <Form.Control type='password' id='password' placeholder='
              your password' autoComplete='off' {...register("password", {required: true, minLength: 8})}></Form.Control>
            </Form.Group>
            {
             errors.username && <p style={{color: "red", fontSize: 12}}>Password is required.</p>
            }
            {
             errors.password?.type === "minLength" && <p style={{color: "red", fontSize: 12}}>password should be at least 8 characters.</p>
            }
            <br/>
            <Form.Group>
              <small>Do not have an account? <Link to='/signup'>Create one</Link></small>
            </Form.Group>
            <Form.Group>
              <Button as='sub' variant='primary' onClick={handleSubmit(loginMe)}>Login</Button>
            </Form.Group>
                       
          </form>
        </div>
    </div>
  )
}

export default LoginPage