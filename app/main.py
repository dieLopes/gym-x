from fastapi import FastAPI
from app.users import router

app = FastAPI()

app.include_router(router.router)
