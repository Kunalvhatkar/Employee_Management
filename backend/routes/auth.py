from flask import Blueprint,request,jsonify,current_app
import bcrypt
import jwt
import datetime

auth_routes=Blueprint("auth",__name__)

@auth_routes.route("/register",methods=["POST"])
def register():

    db=current_app.config["db"]

    data=request.json

    if db.users.find_one({"email":data["email"]}):

        return jsonify({"message":"Email already exists"}),400

    hashed=bcrypt.hashpw(
        data["password"].encode(),
        bcrypt.gensalt()
    )

    db.users.insert_one({

        "name":data["name"],

        "email":data["email"],

        "password":hashed

    })

    return jsonify({"message":"Registration Successful"})


@auth_routes.route("/login",methods=["POST"])
def login():

    db=current_app.config["db"]

    data=request.json

    user=db.users.find_one({"email":data["email"]})

    if not user:

        return jsonify({"message":"User not found"}),404

    if bcrypt.checkpw(
        data["password"].encode(),
        user["password"]
    ):

        token=jwt.encode({

            "email":user["email"],

            "exp":datetime.datetime.utcnow()+datetime.timedelta(hours=2)

        },
        current_app.config["SECRET_KEY"],
        algorithm="HS256")

        return jsonify({"token":token})

    return jsonify({"message":"Wrong Password"}),401