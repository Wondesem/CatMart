import React from 'react'
import './homepage.css'
import { Link } from 'react-router-dom'
import { useAuth } from '../../Auths/auth'

const LoggedHome = ()=>{
  return (
    <div className="cats-market">
      <h1>
        List of available cats on market
      </h1>
    </div>
  )
}
const LoggedOutHome = () =>{
  return (
    <div className='homepage'><h1>Welcome to CatMart cat market site </h1><Link to='/signup'>Get started</Link>
    </div>
  )
}

const Homepage = () => {
  const [logged] = useAuth()
  return (
    <>
    {logged? <LoggedHome/>:<LoggedOutHome/>}
    </>    
  )
}

export default Homepage