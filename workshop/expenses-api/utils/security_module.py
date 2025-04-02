import os

from fastapi import FastAPI, APIRouter, HTTPException, Depends
from fastapi.security.api_key import APIKeyHeader
from typing import List


# Define the API key header
API_KEY_NAME = "X-API-Key"
API_KEY = os.getenv("API_KEY", None) # Replace with your actual API key or load from environment variable
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)

# Dependency to validate the API key
def validate_api_key(api_key: str = Depends(api_key_header)):
    """Validates API Key, sample method

    Args:
        api_key (str, optional): _description_. Defaults to Depends(api_key_header).

    Raises:
        HTTPException: _description_
    """
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
