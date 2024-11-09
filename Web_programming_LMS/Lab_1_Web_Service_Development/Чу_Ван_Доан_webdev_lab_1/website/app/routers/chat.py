# Импортируем необходимые модули из FastAPI и других библиотек
import jwt  # Импортируем библиотеку для работы с JWT
from fastapi import APIRouter, Depends, HTTPException, WebSocket, WebSocketDisconnect, Request, Form  # Импортируем классы и функции для работы с API
from sqlalchemy.orm import Session  # Импортируем класс для работы с сессиями SQLAlchemy
from fastapi.responses import HTMLResponse, RedirectResponse  # Импортируем классы для ответа HTML и перенаправления
from .. import models, database  # Импортируем модели и базу данных из текущего пакета
from .websocket_handler import ConnectionManager  # Импортируем класс для управления соединениями WebSocket
from fastapi.templating import Jinja2Templates  # Импортируем класс для работы с шаблонами Jinja2
import os

# Khởi tạo router và manager cho WebSocket
router = APIRouter()  # Создаем объект маршрутизатора
templates = Jinja2Templates(directory="app/templates")  # Указываем директорию для шаблонов
manager = ConnectionManager()  # Создаем менеджер соединений WebSocket

SECRET_KEY = "chuvandoan"
ALGORITHM = "HS256"


# Функция для получения сессии базы данных
def get_db():
    db = database.SessionLocal()  # Создаем новую сессию
    try:
        yield db  # Возвращаем сессию для использования
    finally:
        db.close()  # Закрываем сессию после использования

# Функция для декодирования JWT
def decode_jwt(token: str):
    if token is None:  # Если токен не предоставлен
        return None
    try:
        token = token.split(" ")[1]  # Удаляем префикс "Bearer"
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])  # Декодируем токен
        return payload.get("sub")  # Возвращаем значение "sub" из полезной нагрузки
    except jwt.PyJWTError:
        return None  # Возвращаем None в случае ошибки декодирования

# Обработка GET-запроса для страницы чата
@router.get("/chat", response_class=HTMLResponse)
async def chat_page(request: Request, db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")  # Получаем токен из cookie
    if not token:  # Если токен отсутствует
        return RedirectResponse(url="/login")  # Перенаправляем на страницу входа

    user_email = decode_jwt(token)  # Декодируем токен для получения email пользователя
    if not user_email:  # Если декодирование не удалось
        return RedirectResponse(url="/login")  # Перенаправляем на страницу входа

    user = db.query(models.User).filter(models.User.email == user_email).first()  # Находим пользователя в базе данных
    if not user:  # Если пользователь не найден
        return RedirectResponse(url="/login")  # Перенаправляем на страницу входа

    user_rooms = db.query(models.ChatRoom).filter(models.ChatRoom.owner_id == user.id).all()  # Получаем все комнаты пользователя
    return templates.TemplateResponse("chat.html", {"request": request, "rooms": user_rooms, "user": user})  # Возвращаем страницу чата с комнатами

# Обработка POST-запроса для создания новой комнаты
@router.post("/create-room", response_class=HTMLResponse)
async def create_room(request: Request, room_name: str = Form(...), db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")  # Получаем токен из cookie
    user_email = decode_jwt(token)  # Декодируем токен
    user = db.query(models.User).filter(models.User.email == user_email).first()  # Находим пользователя

    existing_room = db.query(models.ChatRoom).filter(models.ChatRoom.name == room_name).first()  # Проверяем, существует ли комната
    if existing_room:  # Если комната уже существует
        raise HTTPException(status_code=400, detail="Room already exists")  # Возвращаем ошибку

    new_room = models.ChatRoom(name=room_name, owner_id=user.id)  # Создаем новую комнату
    db.add(new_room)  # Добавляем комнату в сессию
    db.commit()  # Коммитим изменения
    return RedirectResponse(url="/chat", status_code=303)  # Перенаправляем на страницу чата

# Обработка POST-запроса для удаления комнаты
@router.post("/delete-room", response_class=HTMLResponse)
async def delete_room(request: Request, room_id: int = Form(...), db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")  # Получаем токен из cookie
    user_email = decode_jwt(token)  # Декодируем токен
    user = db.query(models.User).filter(models.User.email == user_email).first()  # Находим пользователя

    room = db.query(models.ChatRoom).filter(models.ChatRoom.id == room_id, models.ChatRoom.owner_id == user.id).first()  # Проверяем, есть ли комната у пользователя
    if not room:  # Если комната не найдена
        raise HTTPException(status_code=403, detail="Not authorized to delete this room")  # Возвращаем ошибку

    db.delete(room)  # Удаляем комнату из базы данных
    db.commit()  # Коммитим изменения
    return RedirectResponse(url="/chat", status_code=303)  # Перенаправляем на страницу чата

# функция поиска
@router.get("/search-rooms", response_class=HTMLResponse)
async def search_rooms(request: Request, search_query: str, db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")  # Получаем токен из cookie
    user_email = decode_jwt(token)  # Декодируем токен
    user = db.query(models.User).filter(models.User.email == user_email).first()  # Находим пользователя

    if not user:  # Если пользователь не найден
        return RedirectResponse(url="/login")  # Перенаправляем на страницу входа

    # Получить список комнат, названия которых содержат строку поиска
    rooms = db.query(models.ChatRoom).filter(models.ChatRoom.name.contains(search_query)).all()  # Получаем комнаты, соответствующие запросу
    return templates.TemplateResponse("chat.html", {"request": request, "rooms": rooms, "user": user, "search_query": search_query})  # Возвращаем результаты поиска

# Обработка GET-запроса для страницы чата в конкретной комнате
@router.get("/chat/{room_name}", response_class=HTMLResponse)
async def room_chat_page(request: Request, room_name: str, db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")  # Получаем токен из cookie
    user_email = decode_jwt(token)  # Декодируем токен
    user = db.query(models.User).filter(models.User.email == user_email).first()  # Находим пользователя

    room = db.query(models.ChatRoom).filter(models.ChatRoom.name == room_name).first()  # Ищем комнату по имени
    if not room:  # Если комната не найдена
        raise HTTPException(status_code=404, detail="Room not found")  # Возвращаем ошибку

    messages = db.query(models.Message).filter(models.Message.room_id == room.id).order_by(models.Message.timestamp).all()  # Получаем сообщения из комнаты
    return templates.TemplateResponse("room_chat.html", {"request": request, "room": room, "user": user, "messages": messages})  # Возвращаем страницу чата в комнате

# Обработка WebSocket-соединения
@router.websocket("/ws/{room_name}")
async def websocket_endpoint(websocket: WebSocket, room_name: str, db: Session = Depends(get_db)):
    await manager.connect(websocket, room_name)  # Подключаем пользователя к комнате WebSocket

    room = db.query(models.ChatRoom).filter(models.ChatRoom.name == room_name).first()  # Ищем комнату по имени
    if not room:  # Если комната не найдена
        await websocket.close()  # Закрываем WebSocket
        return

    token = websocket.cookies.get("access_token")  # Получаем токен из cookie
    user_email = decode_jwt(token)  # Декодируем токен
    user = db.query(models.User).filter(models.User.email == user_email).first()  # Находим пользователя
    
    if not user:  # Если пользователь не найден
        await websocket.close()  # Закрываем WebSocket
        return

    username = user.username  # Получаем имя пользователя

    messages = db.query(models.Message).filter(models.Message.room_id == room.id).order_by(models.Message.timestamp).all()  # Получаем сообщения из комнаты
    for message in messages:  # Отправляем все сообщения в комнату
        await websocket.send_text(f"{message.username}: {message.content}")

    try:
        while True:
            content = await websocket.receive_text()  # Ожидаем новое сообщение
            new_message = models.Message(content=content, room_id=room.id, username=username)  # Создаем новое сообщение
            db.add(new_message)  # Добавляем сообщение в сессию
            db.commit()  # Коммитим изменения
            await manager.broadcast(f"{username}: {content}", room_name)  # Рассылаем сообщение всем пользователям в комнате
    except WebSocketDisconnect:  # Обработка отключения WebSocket
        manager.disconnect(websocket, room_name)  # Отключаем пользователя из комнаты

