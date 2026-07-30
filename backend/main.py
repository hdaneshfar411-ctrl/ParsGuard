from fastapi import FastAPI

app = FastAPI(title="ParsGuard")

@app.get("/")
def home():
    return {
        "message": "ParsGuard is running!"
    }
