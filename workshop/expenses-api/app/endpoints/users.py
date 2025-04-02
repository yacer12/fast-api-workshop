from fastapi import FastAPI, HTTPException, Query, Path, APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional
import uuid
from datetime import datetime
from utils.security_module import validate_api_key

router = APIRouter(dependencies=[Depends(validate_api_key)])

@router.get("/users/{user_id}")
async def get_user( user_id: int = Path(..., title="User ID", description="The ID of the user to retrieve")):
    """
        Retrieves a record from collection using its ID.
    """
    try:
        print(user_id)
        return {
            "user_id": user_id,
            "status": "Active",
            "request_time": datetime.now(),
            

        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving record: {str(e)}") from e

