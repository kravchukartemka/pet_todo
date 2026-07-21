from api.dependenciens import get_user_service
from schemas.user import UserCreate, UserResponse, UserUpdate
from fastapi import APIRouter, Depends

from services.user_service import UserService

router = APIRouter()


@router.post("/")
async def create_user(user: UserCreate, service: UserService = Depends(get_user_service)):
    return await service.create(user)


@router.delete("/{user_id}")
async def delete_user(user_id: int, service: UserService = Depends(get_user_service)):
    return await service.delete(user_id)


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, service: UserService = Depends(get_user_service)):
    return await service.get_user(user_id)


@router.patch("/{user_id}")
async def update_user(user: UserUpdate, user_id: int, service: UserService = Depends(get_user_service)):
    return await service.update(user, user_id)