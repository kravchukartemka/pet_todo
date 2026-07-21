import pytest

from unittest.mock import patch

from schemas.user import UserCreate


@pytest.mark.asyncio
async def test_create_user(user_service, user_repository):

    user = UserCreate(
        username="sergey",
        email="test@mail.ru",
        password="123456",
    )

    with patch(
        "services.user_service.hash_password",
        return_value="HASH",
    ):

        await user_service.create(user)

    user_repository.create.assert_awaited_once()