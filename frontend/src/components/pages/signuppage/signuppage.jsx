import React, {useState} from 'react';
import { Link } from 'react-router-dom';
import { Form, Button, Alert} from 'react-bootstrap';
import {useForm} from "react-hook-form";
import './signuppage.css';


const SignupPage = () => {
  const {register, reset, handleSubmit, formState:{errors}} = useForm();
  const [show, setShow] = useState(true);
  const [servRespo, setServRespo] = useState('')

  const submitForm = (data)=> {
    if(data.password===data.confirmPassword){
      const body = {
        username: data.username,
        email: data.email,
        password: data.password
      };
      const requestOpt = {
        method: "POST",
        headers:{
          "content-type": "application/json"
        },
        body:JSON.stringify(body)
      };
      console.log(requestOpt.body)

      fetch('/users/signup', requestOpt)
      .then(resp=>resp.json())
      .then(data=>{
        setServRespo(data.message)
        setShow(true)
      }
      )
      .catch(err=>console.log(err))
      reset()
    }
    else{
      alert('The passwords do not match!')
    }
    
  }
  

  return (
    <div className='container-signup'>
        <div className="form">
        {show?
          <>
            <Alert variant="success" onClose={() => setShow(false)} dismissible>
              <p>
               {servRespo}
              </p>
            </Alert>
            <h1> Sign Up Page </h1>
          </>
            :
          <h1> Sign Up Page </h1>
         }
          <form action='' autoComplete='off'>
            <Form.Group>
              <Form.Label htmlFor="username">Username</Form.Label>
              <Form.Control type="text" placeholder="
              your name" autoComplete="off" id="username" {...register("username",{required:true,maxLength:80})}></Form.Control>
            </Form.Group>
            {errors.username && <span style={{color:"red", fontSize: 12, }}>username required</span>}
            {errors.username?.type==="maxLength" && <p style={{color:"red", fontSize: 12, }}>characters more than 80 are not allowed</p>}

            <br/>
            <Form.Group>
              <Form.Label htmlFor="email">Email</Form.Label>
              <Form.Control type="email" placeholder="your email" autoComplete="off" id="email"{...register("email",{required:true,maxLength:100})}></Form.Control>
            </Form.Group>
            {errors.email && <span style={{color:"red", fontSize:12}}>email required</span>}
            {errors.email?.type==="maxLength" && <p style={{color:"red", fontSize: 12, }}>characters more than 100 are not allowed</p>}
            <br/>
            <Form.Group>
              <Form.Label htmlFor="password">Password</Form.Label>
              <Form.Control type="password" placeholder="
              your password" autoComplete="off" id="password" {...register("password", {required:true,minLength:8})}></Form.Control>
            </Form.Group>
            {errors.password && <span style={{color:"red", fontSize:12}}>password required</span>}
            {errors.password?.type==="minLength" && <p style={{color:"red", fontSize: 12, }}>password should be at least 8 characters</p>}
            <br/>
            <Form.Group>
              <Form.Label htmlFor="passwordConfirm">Confirm Password</Form.Label>
              <Form.Control type="password" placeholder="
              your confirm password" autoComplete="off" id="passwordConfirm"{...register("confirmPassword",{required:true, minLength:8})}></Form.Control>
            </Form.Group>
            {errors.confirmPassword && <span style={{color:"red", fontSize:12}}>confirmation required</span>}
            {errors.confirmPassword?.type==="minLength" && <p style={{color:"red", fontSize: 12, }}>password should be at least 8 characters</p>}
            <br/>
            <Form.Group>
              <small>Do you have an account? <Link to="/login">Login</Link></small>
            </Form.Group>
          
            <Form.Group>
              <Button as="sub" variant="primary" onClick={handleSubmit(submitForm)}>Signup</Button>
            </Form.Group>
          </form>
        </div>
    </div>
  )
}

export default SignupPage