from fastapi import APIRouter

from app.router.game import router as game_router

router = APIRouter(
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def root():
    return {"message": "Hello, MangoLand!"}


router.include_router(game_router)
