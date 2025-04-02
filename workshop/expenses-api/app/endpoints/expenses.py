"""Expenses API endpoints."""
from fastapi import HTTPException, Path, APIRouter
from datetime import datetime
from models.schemas import ExpenseCreate, ExpenseOut, ExpenseUpdate
from models.errors import ErrorResponse
from utils.expense_operations import ExpenseModel

_BASE_URI = "http://localhost:9000/expenses"
router = APIRouter()


@router.post("/expenses/", response_model=dict)
async def create_expense(expense: ExpenseCreate):
    try:
       
        expense.created_date = datetime.now()   
        expense.expense_uri = f"{_BASE_URI}/{expense.expense_id}"     
        expense_id = await ExpenseModel.create(expense.dict())
        return {
            "status_code": 200,
            "id": expense_id,
            "created_expense": expense.dict()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating record: {str(e)}") from e



@router.get("/expenses/{record_id}", response_model=ExpenseOut, tags=["Expenses"])
async def get_expense(record_id: str = Path(title="Record ID", 
                                           description="The record ID to retrieve", example="1")):
    """
        Retrieves a record from collection using its ID.
    """
    try:
        record = await ExpenseModel.get(record_id)
        if not record:
            return ErrorResponse.create_error_response(404, "Record not found")
        return record
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving record: {str(e)}") from e


@router.put("/expenses/{record_id}", response_model=ExpenseOut)
async def update_expense(record_id: str, record: ExpenseUpdate):
    try:
        updated_expense = await ExpenseModel.get(record_id)
        if not updated_expense:
            return ErrorResponse.create_error_response(404, "Unable to update")
        
        await ExpenseModel.update(record_id, record.dict(exclude={"reason"}))
        
        return updated_expense
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating record: {str(e)}") from e
