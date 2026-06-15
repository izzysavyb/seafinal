from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.core.config import (
    SECRET_KEY,
    ALGORITHM
) 

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

def get_current_user(
        token: str = Depends(oauth2_scheme)
):
    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")
        role = payload.get("role")
        user_id = payload.get("id")

        if not username:

            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )
        
        return {
            "username": username,
            "role": role,
            "id": user_id
        }
    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
    

def require_role(
        required_role: str
):
    
    def checker(
            user=Depends(get_current_user)
    ):
        
        if user["role"] != required_role:
            
            raise HTTPException(
                status_code=403,
                detail="Permission denied"
            )
        
        return user
    
    return checker