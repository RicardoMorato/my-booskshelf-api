from pydantic import BaseModel, EmailStr


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr

    class Config:
        schema_extra = {
            "example": {
                "username": "LukeSkywalker",
                "password": "deathStar@123",
                "email": "luke@tatooine.com"
            }
        }


class UserOut(BaseModel):
    username: str
    email: EmailStr
