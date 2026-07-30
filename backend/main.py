from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI(title="ParsGuard")

BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


@app.get("/")
def home():
    return {"message": "ParsGuard is running!"}


@app.get("/login/")
def login_page(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {
            "request": request
        }
    )


@app.post("/login/")
def login(username: str = Form(...), password: str = Form(...)):
    if username == "admin" and password == "admin":
        return {"message": "Login successful"}

    return {"message": "Wrong username or password"}
