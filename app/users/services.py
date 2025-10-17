from app.users.repository import UserRepository
from app.users.model import User

class UserService:
    
    def __init__(self):
        self.repository = UserRepository()

    async def create_user(self, user: User):
        return await self.repository.create_user(user)

    async def get_user(self, user_id: str):
        return await self.repository.get_user_by_id(user_id)

    async def delete_user(self, user_id: str):
        return await self.repository.delete_user(user_id)

    async def list_users(self):
        return await self.repository.list_users()
