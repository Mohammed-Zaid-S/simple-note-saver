from fastapi import APIRouter, Request, Form, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from app.database import users_collection
from app.auth import get_password_hash, verify_password, create_access_token 

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/signup", response_class=HTMLResponse)
def signup_page(request: Request):
    return templates.TemplateResponse(request=request, name= "signup.html", context={})

@router.post("/signup")
def signup_user(username:str = Form(...), password:str = Form(...)):
    if users_collection.find_one({"username" :username}):
        return HTMLResponse(content="Username already exists", status_code=400)

    hashed_password = get_password_hash(password= password)
    users_collection.insert_one({"username" :username, "password": hashed_password})

    return RedirectResponse("/login", status_code=303)

@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(request= request, name="login.html", context={})

@router.post("/login")
def login_user(response= Response, username: str = Form(...), password: str = Form(...) ):
    user = users_collection.find_one({"username": username})
    if not user or verify_password(password, user["password"]):
        return HTMLResponse(content= "Invalid Credentials", status_code=400)

    token = create_access_token({"sub":str(user["_id"])})

    redirect_response = RedirectResponse(url= "/", status_code=303)
    redirect_response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        samesite='lax'
    )

    return redirect_response

@router.get("/logout")
def logout():
    response = RedirectResponse(url="/login", status_code=303)
    response.delete_cookie("access_token")

    return response








