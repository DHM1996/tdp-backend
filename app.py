from fastapi import FastAPI

from routes.appointments import appointments_router
from routes.professions import professions_router
from routes.profile import profile_router
from routes.ratings import rating_router
from routes.test import test_router
from routes.access import access_router

from fastapi.middleware.cors import CORSMiddleware

from routes.works import work_router

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(test_router)
app.include_router(access_router)
app.include_router(profile_router)
app.include_router(appointments_router)
app.include_router(professions_router)
app.include_router(work_router)
app.include_router(rating_router)
