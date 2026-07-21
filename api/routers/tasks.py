from api.dependenciens import get_task_service, get_current_user
from models.user import User
from schemas.task import TaskUpdate, TaskCreate, TaskResponse, TaskFilter
from fastapi import APIRouter, Depends

from services.task_service import TaskService

router = APIRouter()


@router.post("/")
async def create_task(task: TaskCreate, service: TaskService = Depends(get_task_service), current_user: int = Depends(get_current_user),):
    return await service.create(task, current_user)


@router.delete("/{task_id}")
async def delete_task(task_id: int, service: TaskService = Depends(get_task_service), current_user: int = Depends(get_current_user),):
    return await service.delete(task_id, current_user)


@router.get("/", response_model=list[TaskResponse],)
async def get_tasks(service: TaskService = Depends(get_task_service), filters: TaskFilter = Depends(), current_user: User = Depends(get_current_user),):
    return await service.get_tasks(filters, current_user.id)


@router.get("/{task_id}", response_model=TaskResponse, )
async def get_task(task_id: int, service: TaskService = Depends(get_task_service), current_user: User = Depends(get_current_user),):
    return await service.get_task(task_id, current_user.id)


@router.patch("/{task_id}")
async def update_task(task: TaskUpdate, task_id: int, service: TaskService = Depends(get_task_service), current_user: User = Depends(get_current_user),):
    return await service.update(task, task_id, current_user.id)