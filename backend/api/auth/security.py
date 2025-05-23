import models
from typing import Optional
from jose import JWTError, jwt
from core.config import settings
from passlib.context import CryptContext
from datetime import datetime, timedelta
from api.auth.schemas import TokenPayload, Token


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token( user: models.User, expires_delta: Optional[timedelta] = None) -> Token:
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    payload = TokenPayload(
        sub=user.email,
        exp=expire,
        id=user.id,
        is_admin=user.is_admin,
        is_active=user.is_active,
    )
    # Convert Pydantic model to dict and encode datetime as timestamp
    to_encode = payload.dict()
    # If exp is datetime, convert to int timestamp for JWT compatibility
    if isinstance(to_encode["exp"], datetime):
        to_encode["exp"] = int(to_encode["exp"].timestamp())
    
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    return Token(
        access_token=encoded_jwt,
        token_type="bearer",
        expires_in=int(expires_delta.total_seconds()),
    )