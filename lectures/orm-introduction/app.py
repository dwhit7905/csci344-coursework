from flask import Flask, Response, request
import json
from flask_restful import Api
from models import User, db, Bookmark, Post, LikePost, Following
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

# initializes flask app:
app = Flask(__name__)


cors = CORS(
    app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True
)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)
api = Api(app)


# pretend that user #12 is logged into the system
with app.app_context():
    current_user = User.query.filter_by(id=12).one()


#############################
# For Grading (do not edit) #
#############################
@app.route("/")
def home():
    return """
        <html>
        <body>
            <h1>ORM Demo</h1>
            <p>Some demo queries...</p>
            <ul>
                <li>Get bookmarks for the current user: <a href="/api/bookmarks">/api/bookmarks</a></li>
                <li>Retrieve or create a post: <a href="/api/bookmarks">/api/bookmarks</a></li>
            </ul>
        </body>
        """


@app.route("/api/bookmarks")
@app.route("/api/bookmarks/")
def get_bookmarks():
    query = Bookmark.query.filter_by(user_id=current_user.id)
    print(query)
    bookmarks = query.all()
    print(bookmarks)
    return Response(
        json.dumps([bookmark.to_dict() for bookmark in bookmarks]),
        mimetype="application/json",
        status=200,
    )


def get_posts_by_user():
    # Handle GET request - return all posts
    query = Post.query.filter_by(user_id=current_user.id)
    print(query)
    posts = query.all()
    print(posts)
    return Response(
        json.dumps([posts.to_dict(user=current_user) for posts in posts]),
        mimetype="application/json",
        status=200,
    )


def create_post():
    # Handle POST request - create new post
    data = request.json
    try:
        new_post = Post(
            user_id=current_user.id,
            image_url=data.get("image_url"),
            caption=data.get("caption"),
            alt_text=data.get("alt_text"),
        )
        db.session.add(new_post)
        db.session.commit()

        return Response(
            json.dumps(new_post.to_dict()),
            mimetype="application/json",
            status=201,
        )
    except Exception as e:
        return Response(
            json.dumps({"message": "Could not create post", "error": str(e)}),
            mimetype="application/json",
            status=400,
        )


@app.route("/api/posts", methods=["GET", "POST"])
def posts():
    if request.method == "GET":
        return get_posts_by_user()

    elif request.method == "POST":
        return create_post()
