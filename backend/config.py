import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()


class Config:
    """
    Application Configuration
    """

    # Flask
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "change-this-secret-key"
    )

    DEBUG = os.getenv(
        "DEBUG",
        "True"
    ) == "True"

    # MongoDB
    MONGO_URI = os.getenv(
        "MONGO_URI",
        "mongodb://localhost:27017/employee_db"
    )

    DATABASE_NAME = os.getenv(
        "DATABASE_NAME",
        "employee_db"
    )

    # JWT
    JWT_SECRET = os.getenv(
        "JWT_SECRET",
        "jwt-secret-key"
    )

    JWT_EXPIRE_HOURS = int(
        os.getenv(
            "JWT_EXPIRE_HOURS",
            24
        )
    )

    # CORS
    CORS_HEADERS = "Content-Type"

    # Upload Folder (Optional)
    UPLOAD_FOLDER = "uploads"

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024