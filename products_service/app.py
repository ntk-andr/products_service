from fastapi import FastAPI, APIRouter
from .db import init_db

from .models import Product
from .router import router
app = FastAPI()



@app.on_event('startup')
def on_startup():
    init_db()
    
app.include_router(router)

    
