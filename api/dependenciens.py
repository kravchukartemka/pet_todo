import jwt
from jwt import InvalidTokenError

from core.config import settings

from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from models.user import User
from repositories.task_repository import TaskRepository
from repositories.user_repository import UserRepository
from services.auth_services import AuthService
from services.task_service import TaskService
from db.session import get_db
from services.user_service import UserService
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login",
)


async def get_task_repository(session: AsyncSession = Depends(get_db)) -> TaskRepository:
    return TaskRepository(session)


async def get_task_service(repository: TaskRepository = Depends(get_task_repository)) -> TaskService:
    return TaskService(repository)


async def get_user_repository(session: AsyncSession = Depends(get_db)) -> UserRepository:
    return UserRepository(session)


async def get_user_service(repository: UserRepository = Depends(get_user_repository)) -> UserService:
    return UserService(repository)


async def get_auth_service(repository: UserRepository = Depends(get_user_repository)) -> AuthService:
    return AuthService(repository)


async def get_current_user(token: str = Depends(oauth2_scheme), repository: UserRepository = Depends(get_user_repository)) -> int:
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )
    except InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
        )
    user_id = payload.get("sub")
    user = await repository.get_by_id(user_id)
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials",
        )
    return user.id
