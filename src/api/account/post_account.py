from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from src.services.account_service import create_account
from src.api.account.schemas import (
    PostAccountSuccess,
    PostAccountExists,
    PostAccountRequest,
)

router = APIRouter()

response_model = {
    200: {
        "description": "Successfully registered account",
        "model": PostAccountSuccess,
    },
    409: {"description": "Account already exists", "model": PostAccountExists},
}


@router.post(
    "/register",
    responses=response_model,
    summary="Register a new account",
    description="This endpoint allows you to register a new account",
)
async def post_account(account: PostAccountRequest):
    try:
        new_account = create_account(account)
        return JSONResponse(status_code=200, content=new_account.model_dump_json())

    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"detail": e.detail})
