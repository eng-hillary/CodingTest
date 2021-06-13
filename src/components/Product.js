import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container,Card, Row,Col} from 'react-bootstrap'

function Product({products}){
   
    return(
        <Container>
            <h1>products list</h1>
            {
                products.map(
                    product => (
                        <Row>
                            <Col>
                            <Card style={{ width: '18rem' }}>
                            
                            <Card.Img variant="top" src={product.image} style={{height:'100px'}} />
                            <Card.Body>
                            <Card.Title>product name: {product.name}</Card.Title>
                          
                            <Card.Text>
                                Price {product.price}
                            </Card.Text>
                            
                            </Card.Body>
                        </Card>
                            </Col>
                        </Row>
                        
                        
                    )
                    
                    
                )

            }
    
            
        </Container>
    )
}

export default Product;