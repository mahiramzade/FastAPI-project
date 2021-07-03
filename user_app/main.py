from fastapi import FastAPI
from user_app.routers import user, authentication
from user_app import models, database

app = FastAPI()

# creation of db models
models.user.Base.metadata.create_all(database.engine)

# connection of main file and router files (which are connected with other files)
app.include_router(authentication.router)
app.include_router(user.router)
