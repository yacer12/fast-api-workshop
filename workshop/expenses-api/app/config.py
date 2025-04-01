from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGODB_URL = os.getenv("MONGO_SERVER", "host.docker.internal:27017")
DATABASE_NAME = os.getenv("MONGO_DATABASE_NAME", "expensesDb")

client = AsyncIOMotorClient(MONGODB_URL)
database = client[DATABASE_NAME]