from fastapi import FastAPI
from models.user import UserIn, UserOut

app = FastAPI()


@app.get('/')
async def root():
    info = {
        'App': 'Undefined',
        'Status': 'Development',
        'Author': 'Ricardo Morato <https://github.com/RicardoMorato>'
    }
    return info


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user
