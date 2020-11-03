from fastapi import APIRouter, Body, Depends
from loguru import logger
from typing import AsyncIterable, Dict
from app.dto.User import InputSignupForm,InputSigninForm
from app.services.AuthenticationService import signup
from marshmallow.exceptions import ValidationError
from starlette.responses import JSONResponse

router = APIRouter()

@router.post("/users/signup")
async def Signup(payload: InputSignupForm):
    try:
        await signup(payload)
    except ValidationError as e :
        return JSONResponse(e.normalized_messages(),status_code=400)


@router.post("/users/signin")
async def Signin(payload: InputSigninForm):
    pass
