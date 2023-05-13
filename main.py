import fastapi from FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "api de pé"
