from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI(title="ParsGuard")

templates = Jinja2Templates(directory="backend/templates")


@app.get("/")
def home():
    return {"message": "ParsGuard is running!"}


@app.get("/login/")
def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={}
    )


from fastapi.responses import RedirectResponse


@app.post("/login/")
def login(username: str = Form(...), password: str = Form(...)):
    if username == "admin" and password == "admin":
        return RedirectResponse("/panel/", status_code=303)

    return {"message": "Wrong username or password"}
