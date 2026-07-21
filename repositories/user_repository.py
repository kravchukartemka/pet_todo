from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.user import User


class UserRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: dict) -> User:
        db_user = User(**data)

        self.session.add(db_user)

        await self.session.commit()

        await self.session.refresh(db_user)

        return db_user

    async def delete(self, user_id: int):
        query = select(User).where(User.id == user_id)
        result = await self.session.execute(query)
        task = result.scalars().one_or_none()
        await self.session.delete(task)
        await self.session.commit()

    async def get_user(self, user_id) -> User:
        query = select(User).where(User.id == user_id)
        result = await self.session.execute(query)
        return result.scalars().one_or_none()

    async def update(self, user, user_id):
        query = select(User).where(User.id == user_id)
        result = await self.session.execute(query)
        user = result.scalars().one_or_none()
        update_data = user.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(user, field, value)

        await self.session.commit()

        await self.session.refresh(user)

        return user

    async def get_by_email(
            self,
            email: str,
    ) -> User | None:
        query = select(User).where(User.email == email)

        result = await self.session.execute(query)

        return result.scalar_one_or_none()

    async def get_by_id(
            self,
            id: int,
    ) -> User | None:
        query = select(User).where(User.id == id)

        result = await self.session.execute(query)

        return result.scalar_one_or_none()