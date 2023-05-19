from fastapi import APIRouter
from fastapi import status
from app.models.user import User


router = APIRouter()


@router.post("/user", status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    del user.id
    return user
