from fastapi import FastAPI
from routes.access import access
from routes.test import test
from routes.user import user
from routes.turn import turn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(access)
app.include_router(user)
app.include_router(turn)
app.include_router(test)
