from fastapi import APIRouter, HTTPException
from app.users.model import User
from app.users.services import UserService

router = APIRouter(prefix="/users", tags=["users"])
service = UserService()

@router.post("/", response_model=User)
async def create_user(user: User):
    created = await service.create_user(user)
    return created

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: str):
    user = await service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}")
async def delete_user(user_id: str):
    deleted = await service.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"deleted": True}

@router.get("/", response_model=list[User])
async def list_users():
    return await service.list_users()
