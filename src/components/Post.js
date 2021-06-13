import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container,Card, Row,Col} from 'react-bootstrap'

function Post({posts}){
  
    return(
        <Container>
            <h1>posts list</h1>
            
                {
                    posts.map(
                        post => (
                                                  
                            <Row>
                                <Col>
                                <Card style={{ width: '18rem' }}>
                            
                                    <Card.Body>
                                    <Card.Title>{post.title}</Card.Title>
                                    
                                    <Card.Text>
                                        {post.content}
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

export default Post;