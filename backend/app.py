from flask import Flask, jsonify
from flask_cors import CORS

from config import Config
from database.mongo import init_db

# Import Blueprints
from routes.auth import auth_bp
from routes.employee import employee_bp

app = Flask(__name__)

# Load configuration
app.config.from_object(Config)

# Enable CORS
CORS(app)

# Initialize MongoDB
init_db(app)


@app.route("/")
def home():
    return jsonify({
        "success": True,
        "message": "Employee Management System API",
        "version": "1.0"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "database": "Connected"
    })


# Register Blueprints
app.register_blueprint(auth_bp, url_prefix="/api")
app.register_blueprint(employee_bp, url_prefix="/api")


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "message": "API endpoint not found"
    }), 404


@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "success": False,
        "message": "Internal Server Error"
    }), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )