from pydantic import BaseModel


class User(BaseModel):
    name: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Luke Skywalker"
            }
        }
