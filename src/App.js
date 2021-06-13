
import './App.css';
import React ,{ useState, useEffect }from 'react'
import Product from './components/Product'
import Post from './components/Post'
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Row, Col } from 'react-bootstrap'
import axios from 'axios'



function App() {

//defining state
const [products, setProducts] = useState([])
const [posts, setPosts] = useState([])

// fetching products from API     
useEffect(() => {
    axios
    .get('http://127.0.0.1:8000/api/products/')
    .then(res => {
      
       setProducts(res.data)
    })
    .catch(
        err => {
            console.log(err)
        }
    )
},[products])

// fetching posts from API
  useEffect(() => {
    axios
    .get('http://127.0.0.1:8000/api/posts/')
    .then(res => {
       
       setPosts(res.data)
    })
    .catch(
        err => {
            console.log(err)
        }
    )
},[posts])


  return (
    <Container>
  
        <div className="App" style={{background:'#00CED1'}}>
        
          
       
            <Row>
              <Col> 
                <Product products={products}/>
              </Col>
              <Col>
                 <Post posts={posts}/>
              </Col>
            </Row>
            
          
     </div>

     </Container>  
    
  );
}

export default App;
