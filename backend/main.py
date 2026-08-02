from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="ParsGuard")

# Static Files
app.mount("/static", StaticFiles(directory="backend/static"), name="static")

# Templates
templates = Jinja2Templates(directory="backend/templates")


# ---------------- Home ----------------

@app.get("/")
def home():
    return RedirectResponse(url="/login/")


# ---------------- Login ----------------

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
        return RedirectResponse(
            url="/panel/",
            status_code=303
        )

    return RedirectResponse(
        url="/login/",
        status_code=303
    )


# ---------------- Dashboard ----------------

@app.get("/panel/")
def panel(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="panel.html",
        context={
            "username": "Admin"
        }
    )


# ---------------- Users ----------------

@app.get("/users/")
def users(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="users.html",
        context={
            "username": "Admin"
        }
    )


# ---------------- Servers ----------------

@app.get("/servers/")
def servers(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="servers.html",
        context={
            "username": "Admin"
        }
    )


# ---------------- Logs ----------------

@app.get("/logs/")
def logs(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="logs.html",
        context={
            "username": "Admin"
        }
    )


# ---------------- Settings ----------------

@app.get("/settings/")
def settings(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="settings.html",
        context={
            "username": "Admin"
        }
    )
