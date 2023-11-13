
import './App.css';
import { BrowserRouter, Route, Routes,} from 'react-router-dom';
import Navbar from './components/Navbar/Navbar';
import LogoutPage from './components/pages/logoutpage/logoutpage';
import Homepage from './components/pages/homepage/homepage';
import SignupPage from './components/pages/signuppage/signuppage';
import Cart from './components/pages/cartpage/cartpage';
import LoginPage from'./components/pages/loginpage/loginpage'

function App() {
  return (
    <div>
      <BrowserRouter>
      <Navbar/>
      <Routes>
        <Route path='/' element={<Homepage/>}/>
        <Route path='/signup' element={<SignupPage/>}/>
        <Route path='/login' element={<LoginPage/>}/>
        <Route path='/logout' element={<LogoutPage/>}/>
        <Route path='/cart' element={<Cart/>}/>
      </Routes>
      </BrowserRouter>
    </div>      
  );
}

export default App;
