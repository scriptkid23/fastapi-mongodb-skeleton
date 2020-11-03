from fastapi import APIRouter, Body, Depends
from loguru import logger
from typing import AsyncIterable, Dict
from app.dto.User import InputSignupForm,InputSigninForm
from app.services.AuthenticationService import signup

router = APIRouter()


@router.post("/users/signup")
async def Signup(payload: InputSignupForm):
    await signup(payload)
    pass

@router.post("/users/signin")
async def Signin(payload: InputSigninForm):
    pass
