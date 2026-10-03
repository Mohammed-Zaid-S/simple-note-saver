from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from bson import ObjectId
from app.database import note_collection

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/")
def read_root(request: Request):
    notes = list(note_collection.find({}))
    for note in notes:
        note["_id"] = str(note['_id'])
    return templates.TemplateResponse(request=request, name="index.html", context={"note" : notes})

@router.get("/newNote", response_class=HTMLResponse)
def create_note_form(request : Request):
    return templates.TemplateResponse(request=request, name="new_note.html", context={})

@router.post("/newNote")
def create_note(title: str = Form(...), note_content: str = Form(...), important: bool = Form(False)):
    new_note = {
        "title" : title,
        "Note" : note_content,
        "important" : important
    }
    note_collection.insert_one(new_note)
    return RedirectResponse(url = "/", status_code= 303)

@router.get("/note/{note_id}", response_class=HTMLResponse)
def read_note(request: Request, note_id : str):
    if not ObjectId.is_valid(note_id):
        raise HTTPException(status_code=400, detail="Invalid Note ID format")

    note = note_collection.find_one({"_id" : ObjectId(note_id)})
    if not note: 
        raise HTTPException(status_code=404, detail="Note not found")
    return templates.TemplateResponse(request=request, name="view_note.html", context={"Note" : note})

@router.post("/delete/{note_id}")
def delete_note(note_id : str):
    if ObjectId.is_valid:
        note_collection.delete_one({"_id" : ObjectId(note_id)})
    return RedirectResponse(url="/", status_code=303)


    

