import os
import jwt
from datetime import datetime, timedelta, timezone
from pwdlib import PasswordHash
from fastapi import HTTPException, status, Request
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET_KEY", "super-secret-key-change-this")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24

password_hash = PasswordHash.recommended()

def get_password_hash(password: str) -> str:
    return password_hash.hash(password)

def verify_password(plain_password: str, hashed_password: str) ->bool:
    return password_hash.verify(plain_password, hashed_password)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm= ALGORITHM)

def get_current_user_from_cookie(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail= "Not Authorized")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None: 
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token")
        return user_id
    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token")


