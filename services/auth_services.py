from fastapi import HTTPException, status

from core.security import verify_password
from repositories.user_repository import UserRepository
from schemas.auth import LoginRequest


class AuthService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def authenticate(
        self,
        auth: LoginRequest
    ):
        user = await self.repository.get_by_email(auth.email)

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )

        if not verify_password(
                auth.password,
                user.password_hash,
        ):
            return None
        return user
