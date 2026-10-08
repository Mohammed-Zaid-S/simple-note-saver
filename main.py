from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from app.router import notes, auth

app = FastAPI(title="Note Saver")

@app.exception_handler(303)
async def redirect_exception_handler(request: Request, exc):
    return RedirectResponse(url=exc.headers.get("Location", "/login"))

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(auth.router)
app.include_router(notes.router)


