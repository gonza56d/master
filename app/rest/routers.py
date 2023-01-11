from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app import business
from app.schemas import UserSchema
from exceptions import BusinessException

users_router = APIRouter(
    prefix='/users',
    tags=['users'],
)


@users_router.post('/')
async def create_user(payload: UserSchema):
    user = payload.get_model()
    response = JSONResponse(content=payload.dict(), status_code=201)
    try:
        business.Users.create_user(user)
    except BusinessException as e:
        response = JSONResponse(content=e.payload, status_code=e.status_code)
    return response
