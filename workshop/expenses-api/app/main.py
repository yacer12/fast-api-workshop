from datetime import datetime
from fastapi import FastAPI, Request
from utils.get_client_ip import get_client_ip
from app.endpoints import users, expenses

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})

