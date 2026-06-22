from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import ( routes_assets, routes_auth)
from app.database.database import ( engine ,Base)
app = FastAPI()
from app.database import models

Base.metadata.create_all(
    bind=engine
)

app = FastAPI(
    title="The IT LTD API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(
    routes_auth.router,
    prefix="/auth",
    tags=["Authentication"]
)

app.include_router(
    routes_assets.router,
    prefix="/assets",
    tags=["Assets"]
)


