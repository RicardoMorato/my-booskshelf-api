from fastapi import FastAPI
from models.user import User
from random import randint

app = FastAPI()


@app.get('/')
async def root():
    info = {
        'App': 'Undefined',
        'Status': 'Development',
        'Author': 'Ricardo Morato <https://github.com/RicardoMorato>'
    }
    return info


@app.post('/users')
async def create_item(user: User):
    user_dict = user.dict()
    user_dict.update({"user_id": randint(1, 100000)})
    return user_dict
