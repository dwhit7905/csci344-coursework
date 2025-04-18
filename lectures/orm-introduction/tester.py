# initializes flask app:
from models import Post, db, User, Comment, Following, Bookmark, LikePost
from utils import with_app_context
from sqlalchemy import func
from datetime import datetime

########################
# Function Definitions #
########################


# TASK 1
@with_app_context
def get_all_posts():
    # get all of the posts:
    posts = Post.query.filter_by(user_id=25).all()
    for post in posts:
        print(post.caption)
    return posts


# TASK 2
@with_app_context
def get_n_posts(count=10):
    # get all of the posts:
    if count > 50:
        count = 50
    posts = Post.query.limit(count).all()
    return posts


# TASK 3
@with_app_context
def get_posts_by_user_id(id):
    # get all of the posts:
    posts = Post.query.filter_by(user_id=id).all()
    return posts


# TASK 4
@with_app_context
def get_posts_by_username(uname):
    # get all of the posts:
    posts = Post.query.filter(Post.user.has(username=uname)).all()
    return posts


# TASK 5
@with_app_context
def get_post_by_id(id):
    post = db.session.get(Post, id)
    return post


# TASK 6
@with_app_context
def get_posts_liked_by_user(user_id):
    # get all posts liked by a specific user
    posts = Post.query.filter(Post.likes.any(user_id=user_id)).all()
    return posts


# TASK 7
@with_app_context
def get_posts_with_substring(substring):
    # get all posts where caption contains the substring
    posts = Post.query.filter(Post.caption.ilike(f"%{substring}%")).all()
    return posts


# TASK 8
@with_app_context
def get_posts_by_user_ids(user_ids):
    # get all posts from a list of user IDs
    posts = Post.query.filter(Post.user_id.in_(user_ids)).all()
    return posts


# TASK 9
@with_app_context
def get_posts_with_comment_counts():
    # get posts with their comment counts
    posts = (
        db.session.query(Post.id, Post.image_url, func.count(Comment.id))
        .join(User, User.id == Post.user_id)
        .outerjoin(Comment, Post.id == Comment.post_id)
        .group_by(Post.id)
        .all()
    )
    return posts


# TASK 10
@with_app_context
def get_user_feed_posts(user_id):
    # Get all posts from users that the current user is following
    # plus their own posts
    following = Following.query.filter(Following.user_id == user_id).all()
    user_ids = [f.following_id for f in following]
    user_ids.append(user_id)  # include user's own posts
    return Post.query.filter(Post.user_id.in_(user_ids)).all()


# TASK 11
@with_app_context
def get_bookmarked_posts(user_id):
    # Get all posts bookmarked by the user
    posts = Post.query.filter(Post.bookmarks.any(user_id=user_id)).all()
    return posts


# TASK 12
@with_app_context
def create_like(user_id, post_id):
    # Create a new like
    like = LikePost(user_id=user_id, post_id=post_id)
    db.session.add(like)
    db.session.commit()
    return like


# TASK 13
@with_app_context
def create_and_delete_bookmark(user_id, post_id):
    # Create a new bookmark
    bookmark = Bookmark(user_id=user_id, post_id=post_id)
    db.session.add(bookmark)
    db.session.commit()
    print("Bookmark created!")

    # Delete the bookmark
    db.session.delete(bookmark)
    db.session.commit()
    print("Bookmark deleted!")
    return True


# TASK 14
@with_app_context
def create_post(user_id, image_url, caption=None, alt_text=None):
    # Create a new post
    new_post = Post(
        user_id=user_id,
        image_url=image_url,
        caption=caption,
        alt_text=alt_text,
        pub_date=datetime.utcnow(),
    )
    db.session.add(new_post)
    db.session.commit()
    db.session.refresh(new_post)
    return new_post


def create_user():
    user = User(
        first_name='Walter',
        last_name='Goggons',
        username='wgogg',
        password='12345'
    )
    db.session.add(user)
    db.session.commit()
    db.session.refresh(user)
    print(user)
    return user

######################
# Test the functions #
######################
@with_app_context
def tester():
    print("\n----------------------")
    print("Test 1: Get all posts")
    print("----------------------")
    posts = get_all_posts()
    print(posts)

    # print("\n-------------------------")
    # print("Test 2: Get first n posts")
    # print("-------------------------")
    # posts = get_n_posts()
    # print(posts)

    # print("\n--------------------------")
    # print("Test 3: Get posts by user_id")
    # print("---------------------------")
    # posts = get_posts_by_user_id(12)
    # print(posts)

    # print("\n---------------------------")
    # print("Test 4: Get posts by username")
    # print("----------------------------")
    # posts = get_posts_by_username("webdev")
    # print(posts)
    # # for post in posts:
    # #     print(f"{post.user.username}: {post.image_url}")

    # print("\n-----------------------------")
    # print("Test 5: Get single post by id")
    # print("-----------------------------")
    # post = get_post_by_id(20)
    # print(post)
    # print(f"{post.user.username}: {post.image_url}")
    # print(post.comments)
    # print(post.likes)

    # print("\n---------------------------------")
    # print("Test 6: Get posts liked by user 3")
    # print("---------------------------------")
    # posts = get_posts_liked_by_user(3)
    # print(posts)

    # print("\n----------------------------------------")
    # print("Test 7: Get posts with 'tree' in caption")
    # print("----------------------------------------")
    # posts = get_posts_with_substring("tree")
    # print(posts)

    # print("\n----------------------------------------")
    # print("Test 8: Get posts from users 3, 4, and 5")
    # print("----------------------------------------")
    # posts = get_posts_by_user_ids([3, 4, 5])
    # print(posts)

    # print("\n-------------------------------------")
    # print("Test 9: Get posts with comment counts")
    # print("-------------------------------------")
    # results = get_posts_with_comment_counts()
    # for post_id, image_url, comment_count in results:
    #     print(f"Post {post_id}: {comment_count} comments")

    # print("\n-----------------------------------------------")
    # print("Test 10: Get user's feed (following + own posts)")
    # print("-----------------------------------------------")
    # feed_posts = get_user_feed_posts(1)  # get feed for user 1
    # print(f"Number of posts in feed: {len(feed_posts)}")
    # for post in feed_posts[:3]:  # show first 3 posts
    #     print(f"Post {post.id} by {post.user.username}")

    # print("\n---------------------------------------")
    # print("Test 11: Get posts bookmarked by user 3")
    # print("---------------------------------------")
    # bookmarked = get_bookmarked_posts(3)
    # print(f"Number of bookmarked posts: {len(bookmarked)}")
    # for post in bookmarked[:3]:  # show first 3 bookmarks
    #     print(f"Bookmarked post {post.id} by {post.user.username}")

    # print("\n-------------------------------------------------")
    # print("Test 12: Create a new like (user 3 likes post 10)")
    # print("-------------------------------------------------")
    # try:
    #     new_like = create_like(3, 10)
    #     print(
    #         f"Created like: user_id={new_like.user_id}, post_id={new_like.post_id}"
    #     )
    # except Exception as e:
    #     print(f"Could not create like (might already exist): {str(e)}")

    # print("\n-------------------------------------")
    # print("Test 13: Create and delete a bookmark")
    # print("-------------------------------------")
    # result = create_and_delete_bookmark(3, 10)
    # if result:
    #     print("Successfully demonstrated bookmark creation and deletion!")

    # print("\n----------------------------------------")
    # print("Test 14: Create a new post")
    # print("----------------------------------------")
    # new_post = create_post(
    #     user_id=1,
    #     image_url="https://example.com/image.jpg",
    #     caption="My new test post!",
    #     alt_text="A test image",
    # )
    # print(f"Created new post: ID={new_post.id}")
    # print(f"Posted by: {new_post.user.username}")
    # print(f"Caption: {new_post.caption}")


if __name__ == "__main__":
    # Invoke the tester:
    tester()
