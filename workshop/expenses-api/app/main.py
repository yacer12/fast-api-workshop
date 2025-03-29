from fastapi import FastAPI, HTTPException, Query, Path
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional
import uuid
from datetime import datetime
from fastapi.openapi.utils import get_openapi

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})


@app.get("/expenses/{record_id}")
async def get_record(record_id: str = Path(title="Record ID", description="The record ID to retrieve", example="1")):
    """
        Retrieves a record from collection using its ID.
    """
    try:
        
        record = {
            "id":int(record_id), 
            "user_id":str(uuid.uuid4()), 
            "amount": 100.0, 
            "category":"Groceries", 
            "description":"Groceries from PRIME Supermarket", 
            "date":datetime.utcnow(),
            "payment_method":"Credit Card", 
            "recurring":False
        }
        if not record:
            raise HTTPException(status_code=404, detail="Record not found")
        return record
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving record: {str(e)}")

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Expenses API",
        version="2.5.0",
        summary="This is a very custom OpenAPI schema",
        description="Here's a longer description of the custom **OpenAPI** schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi