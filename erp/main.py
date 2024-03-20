# main.py

from fastapi import FastAPI
from app.routers import user_router as user
from app.routers import customer_routers as customer

app = FastAPI()

app.include_router(user.router)

app.include_router(customer.router)
