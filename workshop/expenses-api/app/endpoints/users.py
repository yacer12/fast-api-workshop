from fastapi import FastAPI, HTTPException, Query, Path, APIRouter, Depends
from models.schemas import User, UserCreate, UserOut, ResponseModelCreate
from datetime import datetime
from utils.user_operations import UserModel
from models.errors import ErrorResponse

_BASE_URI = "http://localhost:9000/expense"

router = APIRouter()


@router.post("/users/", response_model=ResponseModelCreate)
async def create_user(user: UserCreate):
    try:
        user_id = await UserModel.create(user.dict())
        if not user_id:
            return ErrorResponse.create_error_response(404, "Record not found")
        return {
            "status_code": 200,
            "timestamp": datetime.now(),
            "message": "Record created successfully",
            "created_record": user.dict()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating record: {str(e)}") from e


@router.get("/users/{user_id}", response_model=UserOut)
async def get_user( user_id: int = Path(..., title="User ID", description="The ID of the user to retrieve")):
    """
        Retrieves a record from collection using its ID.
    """
    try:
        user = UserOut(user_id=user_id,
                       status="Active",
                       request_time=datetime.now())
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving record: {str(e)}") from e

