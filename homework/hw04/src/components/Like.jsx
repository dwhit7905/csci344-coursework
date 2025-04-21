import React from "react";

import {postDataToServer, deleteDataFromServer} from "../server-requests"


export default function Like({ likeId, postId, token }) {
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
        // setStateBookmarkId(reponseData.id);
    }

    if (likeId) {
        return (
            <button>
                <i className="fas text-red-700 fa-heart"></i>
            </button>
        );
    } else {
        return (
            <button onClick={createLike}>
                <i className="far fa-heart"></i>
            </button>
        );
    }
    

}