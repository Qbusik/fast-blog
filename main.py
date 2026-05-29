from fastapi import FastAPI
from user.routes import router as user_router

app = FastAPI(title="Fast-Blog", version="1.0.0")

app.include_router(user_router)
