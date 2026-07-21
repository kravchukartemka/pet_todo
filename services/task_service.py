from core.logger import logger
from exeptions.task import InvalidTaskTitleError, InvalidTaskIdError
from repositories.task_repository import TaskRepository
from schemas.task import TaskCreate, TaskFilter, TaskUpdate


def validate_title(title: str) -> str:
    title = title.strip()

    if len(title) < 3:
        logger.warning("Invalid task title: '%s'", title)
        raise InvalidTaskTitleError()

    return title


class TaskService:

    def __init__(self, repository: TaskRepository):
        self.repository = repository

    async def create(
        self,
        task: TaskCreate,
        user_id: int,
    ):
        validate_title(task.title)

        logger.info(
            "User %s creates task '%s'",
            user_id,
            task.title,
        )

        return await self.repository.create(task, user_id)

    async def delete(
        self,
        task_id: int,
        user_id: int,
    ):
        if task_id <= 0:
            raise InvalidTaskIdError()

        logger.info(
            "User %s deletes task %s",
            user_id,
            task_id,
        )

        return await self.repository.delete(task_id, user_id)

    async def get_tasks(
        self,
        filters: TaskFilter,
        user_id: int,
    ):
        logger.info(
            "User %s requested task list",
            user_id,
        )

        return await self.repository.get_all(filters, user_id)

    async def get_task(
        self,
        task_id: int,
        user_id: int,
    ):
        logger.info(
            "User %s requested task %s",
            user_id,
            task_id,
        )

        return await self.repository.get_by_id(task_id, user_id)

    async def update(
        self,
        task: TaskUpdate,
        task_id: int,
        user_id: int,
    ):
        if task_id <= 0:
            raise InvalidTaskIdError()

        validate_title(task.title)

        logger.info(
            "User %s updates task %s",
            user_id,
            task_id,
        )

        return await self.repository.update(
            task,
            task_id,
            user_id,
        )