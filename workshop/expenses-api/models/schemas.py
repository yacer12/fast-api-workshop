from pydantic import BaseModel, Field
from typing import List, Optional, Annotated
from bson.objectid import ObjectId
from datetime import datetime
from typing import Any
from enum import Enum
from bson import ObjectId
from uuid import uuid4
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

class UserType(str, Enum):
    admin = "admin"
    editor = "editor"
    viewer = "viewer"

class User(BaseModel):
    user_id: int
    user_name: str
    status: str
    user_type: UserType = Field(..., description="Type of the user (admin, editor, viewer)")
    request_time: datetime

class UserCreate(User):
    pass

class UserOut(User):
    id: Annotated[ObjectId, ObjectIdPydanticAnnotation] = Field(
        default="",
        alias="_id",
    )

class ResponseModelCreate(BaseModel):
    status_code: int
    message: str
    timestamp: datetime
    created_record: dict


class Expense(BaseModel):
    expense_id: str = Field(default_factory=lambda: str(uuid4()), description="Unique identifier for the expense")
    user_id: str = Field(..., description="The ID of the user associated with the expense")
    amount: float = Field(..., gt = 0, lt = 2500, description="The amount of the expense")
    category: str = Field(..., description="The category of the expense")
    description: Optional[str] = Field(None, description="A description of the expense")
    created_date: datetime = Field(default_factory=datetime.utcnow, description="The date of the expense")
    payment_method: str = Field(None, pattern="^(Credit Card|Cash|Mobile Payment|Bank Transfer)",
                                description="The payment method used for the expense")
    recurring: bool = Field(default=False, description="Whether the expense is recurring")
    expense_uri: str = Field(None, description="The url of the expense")


class ExpenseCreate(Expense):
    pass

class ExpenseUpdate(Expense):
    reason: str

class ExpenseOut(Expense):
    id: Annotated[ObjectId, ObjectIdPydanticAnnotation] = Field(
        default="",
        alias="_id",
    )

