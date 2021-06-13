import React from 'react'
import ReactDom from 'react-bootstrap'
import Product from '../components/Product'

// writing a test case for the Product component
const products = [
    {
        id: '1',
        name: 'radio',
        price: 2000
    },
    {
        id: '2',
        name: 'smart phone',
        price: 50000
    }
]
it("renders without crashing", () => {
    const dev = document.createElement("div");
    ReactDom.render(<Product products={products}></Product>, dev);

})

