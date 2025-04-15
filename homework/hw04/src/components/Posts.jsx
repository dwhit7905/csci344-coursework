import React, { useState, useEffect } from "react";
import { getDataFromServer } from "../server-requests";
import Post from "./Post.jsx";

export default function Posts({ token }) {
    // when useState is invloked in returns and array with 2 values
    // 1. state variable
    //2. function whos job is to set the state variable
    // & then redraw teh screen after the variable is set
    const [posts, setPosts] = useState([]);
    

    async function getPosts() {
        const data = await getDataFromServer(token, "/api/posts");
        console.log(data);
        setPosts(data);
    }

    useEffect(() => {
        getPosts();
    }, []);

  function outputPosts(post, idx) {
    return (
        <Post token={token} key={idx} postObj={post}/>

    )
  }

    return <div>
        TODO: output all of the posts: {posts.length}
        {posts.map(outputPosts)}
        <br />
        </div>;
}
