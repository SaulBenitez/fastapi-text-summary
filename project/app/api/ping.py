# python imports

# fastapi imports
from fastapi import FastAPI, Depends, APIRouter

# app imports
from app.config import get_settings, Settings


router = APIRouter()


@router.get("/ping")
async def pong(settings: Settings=Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }