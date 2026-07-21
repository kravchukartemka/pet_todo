from fastapi import Request
from fastapi.responses import JSONResponse

from core.logger import logger
from exeptions.base import AppException


async def app_exception_handler(
    request: Request,
    exc: AppException,
):
    logger.warning(
        "%s %s -> %s",
        request.method,
        request.url.path,
        exc.detail,
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "detail": exc.detail,
        },
    )


async def internal_error_handler(
    request: Request,
    exc: AppException,
):
    logger.exception(
        "Unexpected error during %s %s",
        request.method,
        request.url.path,
    )

    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal server error",
        },
    )
