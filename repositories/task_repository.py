from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from exeptions.task import TaskNotFoundError
from models.task import Task
from schemas.task import TaskCreate, TaskUpdate, TaskFilter


class TaskRepository:

    SORT_FIELDS = {
        "created_at": Task.created_at,
        "updated_at": Task.updated_at,
        "title": Task.title,
        "priority": Task.priority,
    }

    def __init__(self, session: AsyncSession):
        self.session = session

    async def _get_task(
        self,
        task_id: int,
        user_id: int,
    ) -> Task:
        query = (
            select(Task)
            .where(
                Task.id == task_id,
                Task.owner_id == user_id,
            )
        )

        result = await self.session.execute(query)

        task = result.scalars().one_or_none()

        if task is None:
            raise TaskNotFoundError()

        return task

    async def create(
        self,
        task: TaskCreate,
        user_id: int,
    ) -> Task:
        db_task = Task(
            **task.model_dump(),
            owner_id=user_id,
        )

        self.session.add(db_task)

        await self.session.commit()
        await self.session.refresh(db_task)

        return db_task

    async def get_all(
        self,
        filters: TaskFilter,
        user_id: int,
    ) -> list[Task]:

        query = select(Task).where(Task.owner_id == user_id)

        if filters.priority is not None:
            query = query.where(Task.priority == filters.priority)

        if filters.search:
            query = query.where(
                Task.title.ilike(f"%{filters.search}%")
            )

        if filters.sort_by:
            column = self.SORT_FIELDS[filters.sort_by]

            if filters.order_by == "desc":
                query = query.order_by(column.desc())
            else:
                query = query.order_by(column.asc())

        query = query.limit(filters.limit).offset(filters.offset)

        result = await self.session.execute(query)

        return result.scalars().all()

    async def get_by_id(
        self,
        task_id: int,
        user_id: int,
    ) -> Task:
        return await self._get_task(task_id, user_id)

    async def update(
        self,
        task: TaskUpdate,
        task_id: int,
        user_id: int,
    ) -> Task:

        db_task = await self._get_task(task_id, user_id)

        update_data = task.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(db_task, field, value)

        await self.session.commit()
        await self.session.refresh(db_task)

        return db_task

    async def delete(
        self,
        task_id: int,
        user_id: int,
    ) -> None:

        db_task = await self._get_task(task_id, user_id)

        await self.session.delete(db_task)
        await self.session.commit()