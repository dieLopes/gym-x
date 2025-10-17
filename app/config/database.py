import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from bson.codec_options import CodecOptions, UuidRepresentation

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("MONGO_DB_NAME", "gymx")

client = AsyncIOMotorClient(MONGO_URI, uuidRepresentation="standard")
database = client.get_database(
    DB_NAME,
    codec_options=CodecOptions(uuid_representation=UuidRepresentation.STANDARD)
)
