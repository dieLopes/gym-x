from app.config.database import database
from app.users.model import User

class UserRepository:
    
    def __init__(self):
        self.collection = database.get_collection("users")

    async def create_user(self, user: User):
        user_dict = user.model_dump()
        await self.collection.insert_one(user_dict)
        return user

    async def get_user_by_id(self, user_id: str):
        user = await self.collection.find_one({"id": user_id})
        return user

    async def delete_user(self, user_id: str):
        result = await self.collection.delete_one({"id": user_id})
        return result.deleted_count > 0

    async def list_users(self):
        users = await self.collection.find().to_list(100)
        return users
