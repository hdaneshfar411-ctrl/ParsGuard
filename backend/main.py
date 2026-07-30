from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI(title="ParsGuard")

templates = Jinja2Templates(directory="backend/templates")


@app.get("/")
def home():
    return {
        "message": "ParsGuard is running!"
    }


@app.get("/login/")
def login(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {"request": request}
    )
