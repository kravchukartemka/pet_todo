from unittest.mock import AsyncMock, patch

from schemas.user import LoginRequest


@pytest.mark.asyncio
async def test_login_success(auth_service, user_repository):

    user = AsyncMock()
    user.password_hash = "hash"

    user_repository.get_by_email.return_value = user

    with patch(
        "services.auth_services.verify_password",
        return_value=True,
    ):

        result = await auth_service.authenticate(
            LoginRequest(
                email="user@mail.ru",
                password="123456",
            )
        )

    assert result == user

@pytest.mark.asyncio
async def test_login_user_not_found(auth_service, user_repository):

    user_repository.get_by_email.return_value = None

    result = await auth_service.authenticate(
        LoginRequest(
            email="test@test.ru",
            password="123",
        )
    )

    assert result is None

@pytest.mark.asyncio
async def test_login_invalid_password(auth_service, user_repository):

    user = AsyncMock()

    user_repository.get_by_email.return_value = user

    with patch(
        "services.auth_services.verify_password",
        return_value=False,
    ):

        result = await auth_service.authenticate(
            LoginRequest(
                email="user@mail.ru",
                password="wrong",
            )
        )

    assert result is None