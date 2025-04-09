"""Users API endpoints."""
from fastapi import FastAPI, HTTPException, Query, Path, APIRouter, Depends
from datetime import datetime
from models.schemas import UserCreate, UserOut, UserUpdate
from models.errors import ErrorResponse
from utils.user_operations import UserModel

router = APIRouter(tags=["Users"])

@router.post("/users/")
async def create_user(user: UserCreate):
    try:
        user_id = await UserModel.create(user.dict())
        if not user_id:
            raise HTTPException(status_code=400, detail="User creation failed")
        return {"status_code": 200, "user_id": user_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/users/{user_id}", response_model=UserOut)
async def get_user(user_id: int = Path(..., title="User ID", description="ID of the user to retrieve")):    
    try:
        user = await UserModel.get(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


@router.put("/users/{user_id}", response_model=UserOut)
async def update_user(user_id: int, user_record: UserUpdate):
    """
        Update a record from collection.
    """
    try:
        user = await UserModel.get(user_id)
        if not user:
            return ErrorResponse.create_error_response(404, "User Not found! Please try again!")
        await UserModel.update(user_id, user_record.dict(exclude={"reason"}))
        return user_record
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving record: {str(e)}") from e

@router.delete("/users/", status_code=204)
async def delete_user(user_id: str = Query(..., title="User ID", description="The ID of the user to be deleted"),
                      reason: str = Query(..., title="Reason", description="Reason of deletion"),
                      deleted_by: str = Query(..., title="Delete By", description="The username who has deleted the user id")
                      ):
    try:
        is_user_deleted = await UserModel.delete(user_id, reason, deleted_by)
        if is_user_deleted:
            print(f"UserID: {user_id} has been deleted by: {deleted_by} because of: {reason}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving record: {str(e)}") from e