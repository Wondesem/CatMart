import React from 'react'
import './Navbar.css'
import { Link } from 'react-router-dom'
import logo from '../Assets/logo.svg'
import cartNew from '../Assets/cartNew.png'
import search_icon from "../Assets/search_icon.svg"
import {useAuth, logout} from "../Auths/auth"

const LoggedLinksTo = () =>{
  return(
    <>
      <div className="nav-menu">
          <p className='rule' >
            <Link style={{textDecoration: 'none', color: '#515151'}} to='/' > Cats on Market </Link>
          </p>
      </div>

      <div className="search">
            <form action="#">
                <input type="text"
                       placeholder=" Search Cats"
                       name="search"/>
                <button className='search-icon'>
                <img src={search_icon} alt='search'/>
                </button>
            </form>
      </div>

      <p className='login' > 
        <a className='active' style={{textDecoration: 'none', color: '#515151'}} href='/#' onClick={()=>{logout()}}> Logout </a>
      </p>
            
      <div className="cartblock">
          <Link to='/cart' style={{textDecoration: 'none', color: '#515151'}}><img src={cartNew} alt='cart'/>
            <div className='counter'> 0 </div>
            <div className="cart-text">Cart </div>
          </Link>
      </div>

    </>
  )
}

const LoggedOutLinks = () => {
  return (
  <div className="loggedout">
    <div className='menu'>
          
      <p className='market'>
          <Link style={{textDecoration: 'none', color: '#515151'}} to='/' > Cats on Market </Link>
      </p>

      <p className='singup'>
        <Link style={{textDecoration: 'none', color: '#515151'}} to='/signup' > Signup </Link>
      </p>
      <p className='login'>
        <Link style={{textDecoration: 'none', color: '#515151'}} to='/login' > Login </Link>
      </p>
            
    </div>               
  </div>
  )
}

const Navbar=()=> {
  const [logged] = useAuth()
  return (
    <nav className='navbar'>
        <div className="nav-logo">
          <Link style={{textDecoration: 'none'}} ><img src={logo} alt='Hello'/></Link>
          <Link style={{textDecoration: 'none'}} ><p className='catmart'>CatMart</p></Link>
        </div>
        {logged?<LoggedLinksTo/>:<LoggedOutLinks/>}
</nav>
  )
}

export default Navbar;