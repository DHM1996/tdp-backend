from fastapi import APIRouter

test = APIRouter()


@test.get("/test", status_code=200)
def request_turn():
    return "ok"