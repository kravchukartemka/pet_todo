import pytest

from exeptions.task import InvalidTaskTitleError
from schemas.enums import TaskPriority
from schemas.task import TaskCreate


@pytest.mark.asyncio
async def test_create_task(task_service, task_repository):

    task = TaskCreate(
        title="Buy milk",
        description="Go to shop",
        priority=TaskPriority.high,
    )

    await task_service.create(task, user_id=1)

    task_repository.create.assert_awaited_once_with(
        task,
        1,
    )

@pytest.mark.asyncio
async def test_create_invalid_title(task_service):

    task = TaskCreate(
        title="ab",
        description="test",
        priority=TaskPriority.low,
    )

    with pytest.raises(InvalidTaskTitleError):
        await task_service.create(task, 1)

@pytest.mark.asyncio
async def test_get_tasks(task_service, task_repository):

    filters = AsyncMock()

    await task_service.get_tasks(
        filters,
        user_id=5,
    )

    task_repository.get_all.assert_awaited_once_with(
        filters,
        5,
    )

@pytest.mark.asyncio
async def test_get_task(task_service, task_repository):

    await task_service.get_task(
        10,
        3,
    )

    task_repository.get_by_id.assert_awaited_once_with(
        10,
        3,
    )

from exeptions.task import InvalidTaskIdError


@pytest.mark.asyncio
async def test_delete_invalid_id(task_service):

    with pytest.raises(InvalidTaskIdError):
        await task_service.delete(
            -1,
            2,
        )

@pytest.mark.asyncio
async def test_delete_task(task_service, task_repository):

    await task_service.delete(
        7,
        4,
    )

    task_repository.delete.assert_awaited_once_with(
        7,
        4,
    )

from schemas.task import TaskUpdate


@pytest.mark.asyncio
async def test_update_task(task_service, task_repository):

    task_repository.get_by_id.return_value = AsyncMock()

    task = TaskUpdate(
        title="Updated",
    )

    await task_service.update(
        task,
        5,
        2,
    )

    task_repository.update.assert_awaited_once()

