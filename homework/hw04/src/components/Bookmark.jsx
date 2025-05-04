import React, {useState} from "react";

import {postDataToServer, deleteDataFromServer} from "../server-requests"

export default function Bookmark({ token,  bookmarkId, postId }) {

    const [stateBookmarkId, setStateBookmarkId] = useState(bookmarkId);
    console.log(bookmarkId); 

    async function createBookmark() {
        const sendData = {
            post_id: postId,
        }
        console.log("creating a bookmark...", sendData);
        const reponseData = await postDataToServer(
            token, 
            "/api/bookmarks/", 
            sendData
        );
        console.log(reponseData);
        setStateBookmarkId(reponseData.id);
    }

    async function deleteBookmark() {
        console.log("deleting a bookmark...");
        const reponseData = await deleteDataFromServer(
            token, 
            "/api/bookmarks/" + stateBookmarkId
        );
        console.log(reponseData);
        setStateBookmarkId(null);
 
    }

    console.log(stateBookmarkId);


    if (stateBookmarkId) {
        return (
            <button ariaLabel="Unbookmark this post " ariaChecked="true" ariaRole="toggle" onClick={deleteBookmark}>
                <i class="fas fa-bookmark"></i>
            </button>
        );
    } else {
        return (
            <button ariaLabel="Bookmark this post " ariaChecked="false" ariaRole="toggle" onClick={createBookmark}>
                <i class="far fa-bookmark"></i>
            </button>
        );
    }
}