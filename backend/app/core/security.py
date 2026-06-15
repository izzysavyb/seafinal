from datetime import datetime, timedelta, timezone
from app.core.config import (SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES)
from dotenv import load_dotenv
import os
from jose import jwt
from pwdlib import PasswordHash

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

password_hash = PasswordHash.recommended()

def hash_password(password: str) -> str:
    return password_hash.hash(password)

def verify_password(
        plain_password: str,
        hashed_password: str
) -> bool:
    return password_hash.verify(
        plain_password,
        hashed_password
    )

def create_access_token(
        data: dict,
       

) -> str:
    
   

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = data.copy()

    payload.update({
        "exp": expire
    })


    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )