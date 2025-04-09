from datetime import datetime
from fastapi import FastAPI, Request
from utils.get_client_ip import get_client_ip
from app.endpoints import users, expenses

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})

app.include_router(users.router)
app.include_router(expenses.router)
@app.get("/ping")
async def ping(request: Request):
    """
    Health check endpoint.
    """
    try:
        client_ip = get_client_ip(request)
        result = {
            "client_ip": client_ip,
            "timestamp": datetime.now().isoformat(),
            "api_status": "ok",
            "api_version": "1.0.0"
        }
        return result
    except Exception as e:
        return {"error":True, "message": str(e)}
    