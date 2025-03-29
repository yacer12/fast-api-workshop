from beanie import Document
from pydantic import Field
from datetime import datetime
from typing import Optional

class Expense(Document):
    user_id: str
    amount: float = Field(..., gt=0)
    category: str
    description: Optional[str] = None
    date: datetime = Field(default_factory=datetime.utcnow)
    payment_method: str  # e.g., "Credit Card", "Cash", "Bank Transfer"
    recurring: bool = False  # If true, this is a recurring expense

    class Settings:
        collection = "expenses"