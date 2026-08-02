from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="ParsGuard")

# Static Files
app.mount("/static", StaticFiles(directory="backend/static"), name="static")

# Templates
templates = Jinja2Templates(directory="backend/templates")


@app.get("/")
def home():
    return {"message": "ParsGuard is running!"}


# ---------------- Login Page ----------------

@app.get("/login/")
def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html"
    )


@app.post("/login/")
def login(
    username: str = Form(...),
    password: str = Form(...)
):
    if username == "admin" and password == "admin":
        return RedirectResponse("/panel/", status_code=303)

    return {"message": "Wrong username or password"}


# ---------------- Panel ----------------

@app.get("/panel/")
def panel(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="panel.html",
        context={
            "username": "Admin"
        }
    )
