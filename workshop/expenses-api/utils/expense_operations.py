from app.config import database
from bson.objectid import ObjectId
from datetime import datetime
import os

MONGO_DATABASE_NAME = os.getenv("MONGO_DATABASE_NAME", "expensesDb")

MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "expenseDetails")

class ExpenseModel:

    collection = database[MONGO_COLLECTION]
    deleted_collection = database["ACRONYMS_DELETED_COLLECTION_NAME"]

    @classmethod
    async def create(cls, record_data):
        record_data["_id"] = ObjectId()
        result = await cls.collection.insert_one(record_data)
        return str(result.inserted_id)

    @classmethod
    async def get(cls, record_id):        
        record = await cls.collection.find_one({"expense_id": record_id})
        return record

    @classmethod
    async def update(cls, record_id, update_data):
        update_data["updatedAt"] = datetime.now()
        await cls.collection.update_one({"expense_id": record_id}, {"$set": update_data})

    @classmethod
    async def delete(cls, record_id, reason):
        record = await cls.collection.find_one({"expense_id": record_id})
        if not record:
            return None

        # Move to deleted records collection
        deleted_record = {**record, "deletion_reason": reason}
        await cls.deleted_collection.insert_one(deleted_record)

        await cls.collection.delete_one({"_id": record_id})
        return record