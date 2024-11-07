## Cây thư mục

```css
project-root/
├── .gitignore                  # Loại trừ các file/thư mục không cần thiết khi push lên Git
├── .dockerignore              # Loại trừ các file/thư mục không cần thiết khi build Docker image
├── docker-compose.yml         # Cấu hình Docker Compose cho toàn bộ dự án
│
├── website/                   # Microservice quản lý người dùng và phòng chat
│   ├── app/
│   │   ├── main.py            # Điểm khởi đầu của ứng dụng website
│   │   ├── database.py        # Cấu hình kết nối với PostgreSQL và ORM
│   │   ├── models.py          # Các model cho người dùng và phòng chat
│   │   ├── schemas.py         # Các schema cho dữ liệu đầu vào/đầu ra
│   │   ├── routers/           # Các route cho website
│   │   │   ├── auth.py        # Đăng ký và đăng nhập người dùng
│   │   │   ├── chat.py        # Quản lý phòng chat (tạo, tìm kiếm)
|   |   |   └── websocket_handler.py
│   │   ├── templates/         # Các template HTML sử dụng Jinja2
│   │   │   ├── index.html     # Template cho trang chủ
|   |   |   ├── chat.html 
|   |   |   ├── login.html
|   |   |   ├── register.html
|   |   |   └── room_chat.html
│   │   └── static/            
|   |       └── favicon.ico
│   ├── Dockerfile             # Dockerfile cho website service
│   ├── requirements.txt       # Các thư viện cần thiết cho website
|   └── .gitignore 
│
├── chat/                      # Microservice WebSocket cho phòng chat
│   ├── app/
│   │   ├── main.py            # Điểm khởi đầu cho WebSocket server
│   │   └── websocket_handler.py # Xử lý các sự kiện WebSocket
│   ├── Dockerfile             # Dockerfile cho chat service
│   └── requirements.txt       # Các thư viện cần thiết cho chat
│
├── db/                        # Cấu hình cho cơ sở dữ liệu PostgreSQL
|   ├── dump/
│   ├── Dockerfile             # Dockerfile cho PostgreSQL
│   └── init.sql               # Cấu trúc bảng và dữ liệu khởi tạo
│
└── nginx/                     # Cấu hình cho Nginx
    ├── nginx.conf             # Cấu hình reverse proxy cho website và chat
    └── Dockerfile             # Dockerfile cho Nginx
```
