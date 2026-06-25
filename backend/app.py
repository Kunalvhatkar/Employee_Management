from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from config import Config

from routes.auth import auth_routes
from routes.employee import employee_routes

app = Flask(__name__)

CORS(app)

client = MongoClient(Config.MONGO_URI)

db = client.employee_db

app.config["db"] = db

app.config["SECRET_KEY"] = Config.SECRET_KEY

app.register_blueprint(auth_routes)

app.register_blueprint(employee_routes)

@app.route("/")

def home():
    return {
        "message":"Employee Management API Running"
    }

if __name__=="__main__":
    app.run(debug=True)