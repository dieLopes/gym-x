import asyncio
from uuid import uuid4
from motor.motor_asyncio import AsyncIOMotorClient

# Conexão com o MongoDB
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.gymx
user_collection = db.users

async def add_uuid_to_existing_users():
    async for user in user_collection.find({"id": {"$exists": False}}):
        new_id = str(uuid4())
        await user_collection.update_one(
            {"_id": user["_id"]},
            {"$set": {"id": new_id}}
        )
        print(f"Updated user {user['name']} with id {new_id}")

# Executa o script
asyncio.run(add_uuid_to_existing_users())
