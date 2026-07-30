from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import os

app = FastAPI(title="ParsGuard")

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home():
    return {"message": "ParsGuard is running!"}


@app.get("/login/")
def login_page(request: Request):
    return templates.TemplateResponse(
    name="login.html",
    context={
        "request": request
    }
)


@app.post("/login/")
def login(username: str = Form(...), password: str = Form(...)):
    if username == "admin" and password == "admin":
        return {"message": "Login successful"}

    return {"message": "Wrong username or password"}
