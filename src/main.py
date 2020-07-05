from fastapi import FastAPI
import requests
from models.user import UserIn, UserOut
from config import Settings

settings = Settings()
print(settings.api_key)

app = FastAPI()


@app.get('/')
async def root():
    info = {
        'App': 'Undefined',
        'Status': 'Development',
        'Author': 'Ricardo Morato <https://github.com/RicardoMorato>'
    }
    return info


@app.post('/user', response_model=UserOut)
async def create_user(user: UserIn):
    return user


@app.get('/search/{search_param}')
async def search_google(search_param):
    url = f'https://www.googleapis.com/books/v1/volumes?q={search_param}'
    res = requests.get(url)
    volume_info = res.json()["items"][0]["volumeInfo"]
    return volume_info
