from fastapi import FastAPI, HTTPException, Query, Path
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional
import uuid
from datetime import datetime
from fastapi.openapi.utils import get_openapi
from models.schemas import RecordCreate, RecordOut, RecordUpdate
from utils.expense_operations import ExpenseModel

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})


@app.get("/expenses/{record_id}", response_model=RecordOut, tags=["Expenses"])
async def get_record(record_id: str = Path(title="Record ID", 
                                           description="The record ID to retrieve", example="1")):
    """
        Retrieves a record from collection using its ID.
    """
    try:
        record = await ExpenseModel.get(record_id)
        if not record:
            raise HTTPException(status_code=404, detail="Record not found")
        return record
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving record: {str(e)}") from e


@app.put("/expenses/{record_id}", response_model=RecordOut)
async def update_record(record_id: str, record: RecordUpdate):
    try:
        await ExpenseModel.update(record_id, record.dict(exclude={"reason"}))
        updated_record = await ExpenseModel.get(record_id)
        if not updated_record:
            raise HTTPException(status_code=404, detail="Record not found after update")
        return updated_record
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating record: {str(e)}") from e
