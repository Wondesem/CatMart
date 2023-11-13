import React from 'react'
import './logoutpage.css'
import { Link } from 'react-router-dom'

const LogoutPage = () => {
  return (
    <div className='logout'><h1>
      To leave the site click on logout
      </h1>
      <Link to='/login'> Login
      </Link></div>
  )
}

export default LogoutPage