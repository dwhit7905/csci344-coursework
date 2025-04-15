import React from "react";

import {postDataToServer, deleteDataFromServer} from "../server-requests"

export default function Bookmark({ bookmarkId }) {
    console.log(bookmarkId); 


    async function createBookmark() {
        console.log("creating a bookmark...");
    }

    async function deleteBookmark() {
        console.log("deleting a bookmark...");
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