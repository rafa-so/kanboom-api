from fastapi import FastAPI
from fastapi import status

from app.models.user import User

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Projeto do kanboom-api (studywise)"}

@app.post("/user", status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    del user.id
    return user
