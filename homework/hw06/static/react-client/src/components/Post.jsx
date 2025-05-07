import React from "react";
import Bookmark from "./Bookmark";
import Like from "./Like";

export default function Post({ token, postObj }) {

    function outputComment() { 
        if (postObj.comments.length === 0) {
            return "";
        } 
        if (postObj.comments.length === 1 ) {
            const comment= postObj.comments[0];
            return (
                <div> 
                <p className="text-sm mb-3">
                        <strong>{comment.user.username}</strong>
                    {comment.text}
                </p>
                </div>
            )
        } 
        if (postObj.comments.length > 1) {
            const comment = postObj.comments[postObj.comments.length - 1];
            return (
                <div> 
                
                <button>
                    View All {postObj.comments.length} comments
                </button>
                <p className="text-sm mb-3">
                        <strong>{comment.user.username}</strong>
                    {comment.text}
                </p>                
                </div>
            )
        }
        
        return (
            <div>
            <p className="text-sm mb-3">
                    <strong>vanek97</strong>
                Hello
            </p>
            <p className="uppercase text-gray-500 text-xs">{postObj.display_time}</p>
            </div>
        )
    }


    return (
        <section className="bg-white border mb-10">
            <div className="p-4 flex justify-between">
                <h3 className="text-lg font-Comfortaa font-bold">{postObj.user.username}</h3>
                <button className="icon-button"><i className="fas fa-ellipsis-h"></i></button>
            </div>
            <img src={postObj.image_url} alt={postObj.alt_txt} width="300" height="300"
                className="w-full bg-cover"/>
            <div className="p-4">
                <div className="flex justify-between text-2xl mb-3">
                    <div>
                        <Like likeId={postObj.current_user_like_id} 
                        postId={postObj.id}
                        token={token}/>

                        <button><i className="far fa-comment"></i></button>
                        <button><i className="far fa-paper-plane"></i></button>
                    </div>
                    <div>
                        <Bookmark 
                        bookmarkId={postObj.current_user_bookmark_id} 
                        postId={postObj.id}
                        token={token}
                        />
                    </div>
                </div>
                <p className="font-bold mb-3">{postObj.likes.length}</p>
                <div className="text-sm mb-3">
                    <p>
                        <strong>{postObj.user.username}</strong> 
                       {postObj.caption}
                       <button className="button"> more</button>
                    </p>
                </div>
                
            {outputComment()}

            <p className="uppercase text-gray-500 text-xs">{postObj.display_time}</p>
                
            </div>
            <div className="flex justify-between items-center p-3">
                <div className="flex items-center gap-3 min-w-[80%]">
                    <i className="far fa-smile text-lg"></i>
                    <input type="text" className="min-w-[80%] focus:outline-none" placeholder="Add a comment..."/>
                </div>
                <button className="text-blue-500 py-2">Post</button>
            </div>
        </section>
    );
}