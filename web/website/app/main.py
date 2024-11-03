from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from .routers import auth, chat
from .database import engine, Base

app = FastAPI()

# Khởi tạo bảng trong cơ sở dữ liệu
Base.metadata.create_all(bind=engine)

# Đăng ký các router
app.include_router(auth.router)
app.include_router(chat.router)

# Route cho trang chủ
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>Chat App</title>
        </head>
        <body>
            <h1>Welcome to the Chat App!</h1>
            <p>Go to <a href="/register">Register</a> or <a href="/login">Login</a>.</p>
        </body>
    </html>
    """

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Route cho favicon
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return RedirectResponse(url="/static/favicon.ico")

