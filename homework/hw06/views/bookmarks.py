import json

from flask import Response, request
from flask_restful import Resource

from models import db
from models.bookmark import Bookmark
from models.post import Post
from views import get_authorized_user_ids
import flask_jwt_extended




class BookmarksListEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user

    @flask_jwt_extended.jwt_required()
    def get(self):
       
        bookmarks = Bookmark.query.filter_by(user_id=self.current_user.id).all()
        data = [item.to_dict() for item in bookmarks]

        return Response(
            json.dumps(data),
            mimetype="application/json",
            status=200,
        )
    
    @flask_jwt_extended.jwt_required()
    def post(self):

        body = request.get_json()
        post_id = body.get('post_id') if body else None

        if post_id is None:
            return Response(
                json.dumps({"message": "post id=is a required field"}),
                mimetype="application/json",
                status=400,
            )
        
        print(post_id)
    #check if post id is an integer
        try: 
            post_id = int(post_id)
        except:
            return Response(
            json.dumps({"message": "Invalid post_id"}),
            mimetype="application/json",
            status=400,
            )
       
        #does post exists
        post = Post.query.get(post_id)
        if post is None:
            return Response(
                json.dumps({"message": f"post id not found"}),
                mimetype="application/json",
                status=404,
            )
        
        # check if allowed ot like
        ids_for_me_and_my_friends = get_authorized_user_ids(self.current_user)
        if post.user_id not in ids_for_me_and_my_friends:
            return Response(
            json.dumps({"message": "Not authorized to bookmark this post!"}),
            mimetype="application/json",
            status=404,
            )
        
        #check if already bookmarked
        already_bookmarked = Bookmark.query.filter_by(
           user_id = self.current_user.id,
           post_id = post_id
           ).one_or_none()
        
        if already_bookmarked is not None:
            return Response(
            json.dumps({"message": "ALready bookmarked!"}),
            mimetype="application/json",
            status=400,
            )
        
        

        new_bookmark = Bookmark(
            post_id=post_id,
            user_id=self.current_user.id,
        )

        db.session.add(new_bookmark)
        db.session.commit()
        db.session.refresh(new_bookmark)
        

        return Response(
            json.dumps(new_bookmark.to_dict()),
            mimetype="application/json",
            status=201,
        )


class BookmarkDetailEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user

    @flask_jwt_extended.jwt_required()
    def delete(self, id):
       
        bookmark = Bookmark.query.get(id)
        if bookmark is None:
               return Response(
                json.dumps({"Message": f"Post id not found"}),
                mimetype="application/json",
                status=404,
        )
        #check that user owns bookmark
        if bookmark.user_id != self.current_user.id:
                return Response(
                json.dumps({"Message": f"You are not allowed to modify post id"}),
                mimetype="application/json",
                status=404,
        )

        #now the delete
        Bookmark.query.filter_by(id=id).delete()
        db.session.commit()
        serialized_data = {"message": "Bookmark {0} successfully deleted".format(id)}
        return Response(
            json.dumps(serialized_data),
            mimetype="application/json",
            status=200,
        )


def initialize_routes(api, current_user):
    api.add_resource(
        BookmarksListEndpoint,
        "/api/bookmarks",
        "/api/bookmarks/",
        resource_class_kwargs={"current_user": current_user},
    )

    api.add_resource(
        BookmarkDetailEndpoint,
        "/api/bookmarks/<int:id>",
        "/api/bookmarks/<int:id>",
        resource_class_kwargs={"current_user": current_user},
    )
