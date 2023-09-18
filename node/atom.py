# This file contains all helper function and Nylas related functions

from flask import jsonify, session, json
from functools import wraps

def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return jsonify({"message":"Failure", "status_code": 403,  "meta": "Please revist the login route"})
        
        return f(*args, **kwargs)
    return decorated_function