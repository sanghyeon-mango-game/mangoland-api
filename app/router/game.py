from fastapi import APIRouter, Depends, Request
from fastapi_restful.cbv import cbv

from app.core.response import APIResponse

router = APIRouter(
    prefix="/game",
    tags=["Game"],
    responses={404: {"description": "Not found"}},
)


@cbv(router)
class Ranking:

    @router.get("/home")
    async def get_home(self, request: Request) -> APIResponse[]
        return {"message": "Hello, MangoLand!"}
