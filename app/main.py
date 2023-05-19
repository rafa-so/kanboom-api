from fastapi import FastAPI

from app.routers import users_router

app = FastAPI()
app.include_router(users_router.router, tags=['usuario'])
