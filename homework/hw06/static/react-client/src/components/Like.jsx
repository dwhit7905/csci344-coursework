import React, {useState} from "react";

import {postDataToServer, deleteDataFromServer} from "../server-requests"


export default function Like({ likeId, postId, token }) {

    const [stateLikeId, setStateLikeId] = useState(likeId);
    console.log(likeId); 

    async function createLike() {
        const sendData = {
            post_id: postId,
        }
        console.log("creating a like...", sendData);
        const reponseData = await postDataToServer(
            token, 
            "/api/likes/", 
            sendData
        );
        console.log(reponseData);
        setStateLikeId(reponseData.id);
    }

    async function deleteLike() {
        console.log("deleting a like...");
        const reponseData = await deleteDataFromServer(
            token, 
            "/api/likes/" + stateLikeId
        );
        console.log(reponseData);
        setStateLikeId(null);
 
    }

    console.log(stateLikeId);


    if (stateLikeId) {
        return (
            <button ariaLabel="Unlike this post " ariaChecked="true" ariaRole="toggle" onClick={deleteLike}>
                <i className="fas text-red-700 fa-heart"></i>
            </button>
        );
    } else {
        return (
            <button ariaLabel="Like this post " ariaChecked="false" ariaRole="toggle" onClick={createLike}>
                <i className="far fa-heart"></i>
            </button>
        );
    }
    

}