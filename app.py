from fastapi import FastAPI
from routes.routes_users import user


app = FastAPI(
    title= 'Documentacion de Doc Sentinel BackEnd',
    description= 'Esta es la primera version del BackEnd de Doc Sentinel'
)

app.include_router(user)