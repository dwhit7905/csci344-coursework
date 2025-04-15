import React from "react";

import {postDataToServer, deleteDataFromServer} from "../server-requests"

export default function Bookmark({ token,  bookmarkId, postId }) {
    console.log(bookmarkId); 


    async function createBookmark() {
        const sendData = {
            post_id: postId,
        }
        console.log("creating a bookmark...");
        const reponseData = await postDataToServer(
            token, 
            "/api/boookmarks/", 
            sendData
        );
        console.log(reponseData);
    }

    async function deleteBookmark() {
        console.log("deleting a bookmark...");
        const reponseData = await deleteDataFromServer;(
            token, 
            "/api/boookmarks/" + bookmarkId
        );
    }

    if (bookmarkId) {
        return (
            <button onClick={deleteBookmark}>
                <i class="fas fa-bookmark"></i>
            </button>
        );
    } else {
        return (
            <button onClick={createBookmark}>
                <i class="far fa-bookmark"></i>
            </button>
        );
    }
}