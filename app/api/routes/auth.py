from fastapi import APIRouter, Depends
from app.schemas.user import UserCreate, UserLogin, Token
from app.services.auth import AuthService, get_auth_service

router = APIRouter()


@router.post("/signup", response_model=Token)
def signup(user: UserCreate, auth_service: AuthService = Depends(get_auth_service)):
    return auth_service.signup(user)


@router.post("/login", response_model=Token)
def login(user: UserLogin, auth_service: AuthService = Depends(get_auth_service)):
    return auth_service.login(user)
