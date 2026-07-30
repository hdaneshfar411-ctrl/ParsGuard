from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI(title="ParsGuard")

templates = Jinja2Templates(directory="backend/templates")


@app.get("/")
def home():
    return {
        "message": "ParsGuard is running!"
    }


@app.get("/login/")
def login_page(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {
            "request": request
        }
    )


@app.post("/login/")
def login(
    username: str = Form(...),
    password: str = Form(...)
):
    if username == "admin" and password == "admin":
        return {
            "message": "Login successful"
        }

    return {
        "message": "Wrong username or password"
    }


@app.get("/panel/")
def panel(request: Request):
    return templates.TemplateResponse(
        "panel.html",
        {
            "request": request
        }
    )
