# My Booskshelf API
API for the My Bookshelf app created in Python using FastAPI

## Installing the dependencies
- Install all dependencies using the following code:
```bash
pip install -r requirements.txt
```

## Running the project
- Enter the folder `/src` using `cd /src` and run `uvicorn main:app --reload`
- Add a file on the directory 'src' named config.py
- On the config.py add the following code:
```python
from pydantic import BaseSettings


class Settings(BaseSettings):
    api_key = 'YOUR_API_KEY_HERE'
```