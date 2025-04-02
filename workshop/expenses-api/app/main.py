from fastapi import FastAPI
from typing import List, Optional
from datetime import datetime
from fastapi.openapi.utils import get_openapi
from utils.expense_operations import ExpenseModel
from app.endpoints import expenses, users

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})

# Include routers from different modules
app.include_router(expenses.router)
app.include_router(users.router)
