import React from 'react'
import { BrowserRouter as Router,Link, NavLink } from 'react-router-dom'
import Route from 'react-router-dom/Route'
import Home from './Home'
import Product from './Product'
import Post from './Post'

const Navigation = () => { 
    return(
        <div>
        <Router>
          <Link to="/home" component={Home} activeStyle={{color: 'green'}}>Home</Link>
          <NavLink to="/products" component={Product} activeStyle={{color: 'green'}}>Products</NavLink>
          <NavLink to="/posts" component={Post} activeStyle={{color: 'green'}}>Posts</NavLink>

          
        
          <Route path="/home"/>
          <Route path="/products"/>
          <Route path="/posts" />
        </Router>
    </div>
    )
}

export default Navigation;