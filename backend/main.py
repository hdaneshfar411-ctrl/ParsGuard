from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="ParsGuard")

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
        context={
            "request": request
        }
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
        return RedirectResponse(
            url="/panel",
            status_code=303
        )

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
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "request": request,
            "username": "Admin",
            "users": 0,
            "servers": 1,
            "traffic": "0 GB",
            "status": "Online"
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
        context={
            "request": request,
            "users": [
                {
                    "id": 1,
                    "username": "admin",
                    "status": "Active"
                }
            ]
        }
    )


# ===========================
# Servers
# ===========================

@app.get("/servers")
def servers(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="servers.html",
        context={
            "request": request
        }
    )


# ===========================
# Configs
# ===========================

@app.get("/configs")
def configs(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="configs.html",
        context={
            "request": request
        }
    )


# ===========================
# Logs
# ===========================

@app.get("/logs")
def logs(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="logs.html",
        context={
            "request": request
        }
    )


# ===========================
# Settings
# ===========================

@app.get("/settings")
def settings(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="settings.html",
        context={
            "request": request
        }
    )


# ===========================
# Logout
# ===========================

@app.get("/logout")
def logout():
    return RedirectResponse(
        url="/login",
        status_code=303)
