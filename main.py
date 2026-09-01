from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

Templates = Jinja2Templates(directory="template")
db_conn = MongoClient("mongodb+srv://Zaid_1:jGnx4aVs5st%3AZMm@notes-app.bodljud.mongodb.net/")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    noteRef = list(db_conn.Master_Note.Notes.find({}))
    return Templates.TemplateResponse(request=request, name="index.html", context={"note": noteRef})

# 1. Render the create note form
@app.get("/newNote", response_class=HTMLResponse)
async def create_note_form(request: Request):
    return Templates.TemplateResponse(request=request, name="new_note.html", context={})

# 2. Handle the form submission
@app.post("/newNote")
async def create_note(title: str = Form(...), note_content: str = Form(...), important: bool = Form(False)):
    new_note_data = {
        "title": title,
        "Note": note_content, 
        "important": important
    }
    db_conn.Master_Note.Notes.insert_one(new_note_data)
    # Redirect back to the home page after saving
    return RedirectResponse(url="/", status_code=303)

# 3. Handle note deletion
@app.post("/delete/{title}")
async def delete_note(title: str):
    db_conn.Master_Note.Notes.delete_one({"title": title})
    return RedirectResponse(url="/", status_code=303)

# MUST BE LAST: The dynamic title route
@app.get("/{title}", response_class=HTMLResponse)
async def read_note(request: Request, title: str):
    userNote = db_conn.Master_Note.Notes.find_one({"title": title})
    return Templates.TemplateResponse(request=request, name="note_Template.html", context={"Note": userNote})