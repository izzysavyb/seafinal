from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./assets.db"
)

ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv(
        "ACCESS_TOKEN_EXPIRE_MINUTES",
        "60"
    )
)


ALGORITHM = os.getenv("ALGORITHM")
