from fastapi import FastAPI
from routes import router

from database import engine
from models import Base

app = FastAPI()

app.include_router(router)