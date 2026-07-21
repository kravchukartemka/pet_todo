from core.security import hash_password
from models.user import User
from repositories.user_repository import UserRepository
from schemas.user import UserCreate, UserUpdate


class UserService:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def create(self, user: UserCreate):
        data = user.model_dump()

        data["password_hash"] = hash_password(
            data.pop("password")
        )

        return await self.repository.create(data)

    async def delete(self, user_id: int):
        return await self.repository.delete(user_id)

    async def get_user(self, user_id: int) -> User:
        return await self.repository.get_user(user_id)

    async def update(self, user: UserUpdate, user_id: int):
        return await self.repository.update(user, user_id)
