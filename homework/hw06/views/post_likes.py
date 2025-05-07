import json

from flask import Response, request
from flask_restful import Resource

from models import db
from models.like_post import LikePost
from models.post import Post
from views import get_authorized_user_ids

import flask_jwt_extended




class PostLikesListEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user

    @flask_jwt_extended.jwt_required()
    def post(self):

        '''
        error handing
        liking something you already have
        post not exits

        post_id
        user_id: self.current_user.id
        '''
        post_id = request.json.get("post_id")
        user_id = self.current_user.id

        #chedk if post id is integer
        try: 
            post_id = int(post_id)
        except:
            return Response(
            json.dumps({"message": "Invalid post_id"}),
            mimetype="application/json",
            status=404,
            )
        #does it exist
        post = Post.query.get(post_id)
        if post is None:
            return Response(
            json.dumps({"message": "Invalid post_id"}),
            mimetype="application/json",
            status=404,
            )
        # check if allowed ot like
        ids_for_me_and_my_friends = get_authorized_user_ids(self.current_user)
        if post.user_id not in ids_for_me_and_my_friends:
            return Response(
            json.dumps({"message": "Not authorized to like this post!"}),
            mimetype="application/json",
            status=404,
            )
        #check if weve liked it
        already_liked = LikePost.query.filter_by(
           user_id = user_id,post_id = post_id
           ).one_or_none()
        
        if already_liked is not None:
            return Response(
            json.dumps({"message": "Post already liked!"}),
            mimetype="application/json",
            status=400,
            )

        print(post_id, user_id)

        like = LikePost(
            post_id = post_id,
            user_id= user_id
        )

        db.session.add(like)
        db.session.commit()
        db.session.refresh(like)

        return Response(
            json.dumps(like.to_dict()),
            mimetype="application/json",
            status=201,
        )


class PostLikesDetailEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user

    @flask_jwt_extended.jwt_required()
    def delete(self, id):
        like = LikePost.query.get(id)
        if like is None:
               return Response(
                json.dumps({"Message": f"Post id not found"}),
                mimetype="application/json",
                status=404,
        )
        #check that user owns bookmark
        if like.user_id != self.current_user.id:
                return Response(
                json.dumps({"Message": f"You are not allowed to modify post id"}),
                mimetype="application/json",
                status=404,
        )

        #now the delete
        LikePost.query.filter_by(id=id).delete()
        db.session.commit()

        return Response(
            json.dumps(),
            mimetype="application/json",
            status=200,
        )


def initialize_routes(api, current_user):
    api.add_resource(
        PostLikesListEndpoint,
        "/api/likes",
        "/api/likes/",
        resource_class_kwargs={"current_user": current_user},
    )

    api.add_resource(
        PostLikesDetailEndpoint,
        "/api/likes/<int:id>",
        "/api/likes/<int:id>/",
        resource_class_kwargs={"current_user": current_user},
    )
