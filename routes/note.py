from http.client import HTTPException
from typing import List, Any, Mapping
from fastapi import APIRouter, Form
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from config.db import client, DATABASE_NAME
from models.note import Note

note = APIRouter()

templates = Jinja2Templates(directory="templates")
db = client[DATABASE_NAME]


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    items_cursor = db.notes.find({})
    items: List[Mapping["_id", Any]] = await items_cursor.to_list(length=None)
    newDocs = []
    for item in items:
        newDocs.append({
            "id": item["_id"],
            "title": item["title"],
            "desc": item["desc"],
            "important": item["important"]
        })
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})


@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)
    formDict["important"] = True if formDict.get("important") == "on" else False
    print(formDict)
    note = db.notes.insert_one(formDict)
    return {"Success": True}