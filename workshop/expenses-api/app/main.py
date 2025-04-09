from datetime import datetime
from fastapi import HTTPException

from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
from utils.get_client_ip import get_client_ip
from models.errors import ErrorResponse


app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})

