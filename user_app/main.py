from fastapi import FastAPI
from user_app.routers import user
from user_app import models, database

app = FastAPI()

models.user.Base.metadata.create_all(database.engine)

app.include_router(user.router)
