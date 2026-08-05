from .database import init_db

from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="ParsGuard")

init_db()

# Static Files
app.mount("/static", StaticFiles(directory="backend/static"), name="static")

# Templates
templates = Jinja2Templates(directory="backend/templates")

# ===========================
# Home
# ===========================

@app.get("/")
def home():
    return RedirectResponse(url="/login")


# ===========================
# Login Page
# ===========================

@app.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={"request": request}
    )


# ===========================
# Login
# ===========================

@app.post("/login")
def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    if username == "admin" and password == "admin":
        return RedirectResponse(url="/panel", status_code=303)

    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={
            "request": request,
            "error": "Wrong username or password"
        }
    )


# ===========================
# Dashboard
# ===========================

@app.get("/panel")
def panel(request: Request):

    client_ip = request.client.host

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "request": request,
            "username": "Admin",
            "users": 0,
            "servers": 1,
            "traffic": "0 GB",
            "status": "Online",
            "client_ip": client_ip
        }
    )


# ===========================
# Users
# ===========================

@app.get("/users")
def users(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="users.html",
        context={"request": request}
    )


@app.get("/servers")
def servers(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="servers.html",
        context={"request": request}
    )


@app.get("/configs")
def configs(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="configs.html",
        context={"request": request}
    )


@app.get("/logs")
def logs(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="logs.html",
        context={"request": request}
    )


@app.get("/settings")
def settings(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="settings.html",
        context={"request": request}
    )


# ===========================
# Users Add
# ===========================

from .database import get_db


@app.get("/users/add")
def add_user_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="add_user.html",
        context={"request": request}
    )


@app.post("/users/add")
def add_user(
    username: str = Form(...),
    password: str = Form(...),
    protocol: str = Form(...),
    traffic: int = Form(...),
    expire: int = Form(...)
):
    db = get_db()

    db.execute(
        """
        INSERT INTO users
        (username,password,protocol,traffic,expire,status)
        VALUES(?,?,?,?,?,?)
        """,
        (
            username,
            password,
            protocol,
            traffic,
            expire,
            "Active"
        )
    )

    db.commit()
    db.close()

    return RedirectResponse("/users", status_code=303)


@app.get("/logout")
def logout():
    return RedirectResponse(url="/login", status_code=303)
