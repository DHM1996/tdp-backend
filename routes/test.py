from fastapi import APIRouter

test_router = APIRouter()


@test_router.get("/test", status_code=200)
def test():
    return "ok"
