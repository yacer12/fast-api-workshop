from pydantic import BaseModel, Field
from typing import List, Optional, Annotated
from bson.objectid import ObjectId
from datetime import datetime
from typing import Any

from bson import ObjectId
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import core_schema


class ObjectIdPydanticAnnotation:
    """Defines a wrapper class around the mongodb ObjectID class adding serialization."""

    @classmethod
    def validate_object_id(cls, v: Any, handler) -> ObjectId:
        if isinstance(v, ObjectId):
            return v

        s = handler(v)
        if ObjectId.is_valid(s):
            return ObjectId(s)
        else:
            msg = "Invalid ObjectId"
            raise ValueError(msg)

    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        source_type,
        _handler,
    ) -> core_schema.CoreSchema:
        assert source_type is ObjectId  # noqa: S101
        return core_schema.no_info_wrap_validator_function(
            cls.validate_object_id,
            core_schema.str_schema(),
            serialization=core_schema.to_string_ser_schema(),
        )

    @classmethod
    def __get_pydantic_json_schema__(cls, _core_schema, handler) -> JsonSchemaValue:
        return handler(core_schema.str_schema())

class ExpenseBase(BaseModel):
    expense_id: str
    user_id: str
    amount: float = Field(..., gt=0)
    category: str
    description: Optional[str] = None
    date: datetime = Field(default_factory=datetime.utcnow)
    payment_method: str  # e.g., "Credit Card", "Cash", "Bank Transfer"
    recurring: bool = False  # If true, this is a recurring expense

class RecordCreate(ExpenseBase):
    pass

class RecordUpdate(ExpenseBase):
    reason: str

class RecordOut(ExpenseBase):
    id: Annotated[ObjectId, ObjectIdPydanticAnnotation] = Field(
        default="",
        alias="_id",
    )