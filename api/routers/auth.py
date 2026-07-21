from fastapi import APIRouter, Depends
from api.dependenciens import get_auth_service
from core.security import create_access_token
from schemas.auth import LoginRequest, Token
from services.auth_services import AuthService

router = APIRouter()


@router.post("/login")
async def auth(auth: LoginRequest, service: AuthService = Depends(get_auth_service)):
    user = await service.authenticate(auth)
    token = create_access_token(
        {"sub": str(user.id)}
    )

    return Token(
        access_token=token
    )
