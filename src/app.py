from fastapi import FastAPI
from src.api.account import post_account

app = FastAPI()

app.include_router(post_account.router)