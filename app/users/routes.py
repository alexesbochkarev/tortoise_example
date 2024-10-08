from fastapi import APIRouter, HTTPException

from .schemas import User_Pydantic
from .models import User


router = APIRouter()


@router.post("/", response_model=User_Pydantic)
async def create_user(user: User_Pydantic):
    user_obj = await User.create(**user.dict())
    return await User_Pydantic.from_tortoise_orm(user_obj)


@router.get("/{user_id}", response_model=User_Pydantic)
async def get_user(user_id: int):
    
    user = await User.get_or_none(id=user_id)
    if not user:
        raise HTTPException(400, "Пользователь не найден")
    
    return user
