from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://localhost:27017"
DATABASE_NAME = "notes"

client = AsyncIOMotorClient(MONGO_URL)
