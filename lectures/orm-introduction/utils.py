from functools import wraps
from app import app


def with_app_context(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        with app.app_context():
            return f(*args, **kwargs)

    return decorated_function
