from fastapi import APIRouter, Depends, HTTPException, Request, Form
from sqlalchemy.orm import Session
from .. import models, database
from ..schemas import ChatRoomCreate, ChatRoomSearch
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/chat", response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

@router.post("/create-room")
async def create_room(room_name: str = Form(...), db: Session = Depends(get_db)):
    db_room = models.ChatRoom(name=room_name)
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return RedirectResponse(url="/chat", status_code=303)

@router.get("/search-rooms", response_class=HTMLResponse)
async def search_rooms(search_query: str, request: Request, db: Session = Depends(get_db)):
    rooms = db.query(models.ChatRoom).filter(models.ChatRoom.name.contains(search_query)).all()
    return templates.TemplateResponse("chat.html", {"request": request, "rooms": rooms})
