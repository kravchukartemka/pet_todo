from fastapi import FastAPI

from api.routers.tasks import router as task_router
from exeptions.base import AppException
from exeptions.handlers import app_exception_handler
from api.routers.user import router as user_router
from api.routers.auth import router as auth_router

app = FastAPI()

app.include_router(
    task_router,
    prefix="/tasks",
    tags=["Tasks"],
)
app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Auth"],
)
app.include_router(
    user_router,
    prefix="/users",
    tags=["Users"],
)


app.add_exception_handler(
    AppException,
    app_exception_handler,
)