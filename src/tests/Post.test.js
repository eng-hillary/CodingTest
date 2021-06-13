import React from 'react'
import ReactDom from 'react-bootstrap'
import Post from '../components/Post'

// writing a test case for the Product component
const posts = [
    {
        id: '1',
        title: 'job advert',
        content: 'first post'
    },
    {
        id: '2',
        name: 'sales promotion',
        content: 'second post'
    }
]
it("renders without crashing", () => {
    const dev = document.createElement("div");
    ReactDom.render(<Post posts={posts}></Post>, dev);

})
