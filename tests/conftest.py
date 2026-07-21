import pytest

from unittest.mock import AsyncMock

from services.task_service import TaskService
from services.user_service import UserService
from services.auth_services import AuthService


@pytest.fixture
def task_repository():
    return AsyncMock()


@pytest.fixture
def user_repository():
    return AsyncMock()


@pytest.fixture
def task_service(task_repository):
    return TaskService(task_repository)


@pytest.fixture
def user_service(user_repository):
    return UserService(user_repository)


@pytest.fixture
def auth_service(user_repository):
    return AuthService(user_repository)