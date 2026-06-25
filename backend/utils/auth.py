import jwt
from functools import wraps
from flask import request,jsonify,current_app

def token_required(f):

    @wraps(f)

    def decorated(*args,**kwargs):

        token=request.headers.get("Authorization")

        if not token:

            return jsonify({"message":"Token missing"}),401

        try:

            jwt.decode(
                token,
                current_app.config["SECRET_KEY"],
                algorithms=["HS256"]
            )

        except:

            return jsonify({"message":"Invalid Token"}),401

        return f(*args,**kwargs)

    return decorated