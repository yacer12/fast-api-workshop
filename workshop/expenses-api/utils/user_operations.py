from http.client import HTTPException
from app.config import database
from bson.objectid import ObjectId
from datetime import datetime
import os

MONGO_DATABASE_NAME = os.getenv("MONGO_DATABASE_NAME", "financeDB")

MONGO_COLLECTION = os.getenv("MONGO_COLLECTION_USERS", "users")


class UserModel:
    collection = database[MONGO_COLLECTION]

    @classmethod
    async def create(cls, user_data):
        user_data["_id"] = ObjectId()
        result = await cls.collection.insert_one(user_data)
        return str(result.inserted_id)

    @classmethod
    async def get(cls, user_id):
        user = await cls.collection.find_one({"user_id": user_id})
        return user

    @classmethod
    async def update(cls, user_id, update_data):
        update_data["updatedAt"] = datetime.now()
        await cls.collection.update_one({"expense_id": user_id}, {"$set": update_data})

    @classmethod
    async def delete(cls, user_id, reason):
        if not reason:
            raise HTTPException(status_code=400, detail="Reason is required for deletion")

        user = await cls.collection.find_one({"user_id": user_id})
        if not user:
            return None

        await cls.collection.delete_one({"_id": user_id})
        return user