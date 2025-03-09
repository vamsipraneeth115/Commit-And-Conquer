from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from prisma.models import User as PrismaUser
import jwt

class User(BaseModel):
    email: str
    password: str
    role: Optional[str] = None

router = APIRouter()

@router.post("/user/login")
async def login(user: User):
    prisma_user = await PrismaUser.prisma().find_unique(where={"email": user.email})
    if prisma_user is None:
        return {"error": "User not found"}
    else:
        if prisma_user.password == user.password:
            payload = {"id": prisma_user.id, "email": prisma_user.email, "role": prisma_user.role}
            token = jwt.encode(payload, 'jaidboss', algorithm='HS256')
            return {"fullName": prisma_user.fullName, "email": prisma_user.email, "role": prisma_user.role, "token": token}
        else:
            return {"error": "Incorrect password"}