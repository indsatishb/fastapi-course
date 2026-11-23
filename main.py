from fastapi import FastAPI

app = FastAPI(
    title="My First API",
    description="FastAPI hosted on Render",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Hello Satish!",
        "status": "success"
    }

@app.get("/about")
def about():
    return {
        "framework": "FastAPI",
        "hosting": "Render"
    }