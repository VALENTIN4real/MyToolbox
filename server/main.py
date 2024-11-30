from fastapi import FastAPI
from .routers import user_router, operation_router
from .database import config
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    config.create_db_and_tables()

app.include_router(
    user_router.router,
    prefix="/api",)

app.include_router(
    operation_router.router,
    prefix="/api"
)
@app.get("/")
def read_root():
    return {"Hello": "World"}