from fastapi import APIRouter, Request, Depends, Form, Query
from fastapi.responses import HTMLResponse, StreamingResponse, RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import text
from app.database import get_db
from fastapi.templating import Jinja2Templates
import logging
import time
import csv
from io import StringIO

# Cấu hình logging
logging.basicConfig(filename="query.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Khai báo router
router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# Lưu lịch sử truy vấn
query_history = []

# Danh sách quyền cho các vai trò
ALLOWED_TABLES_MANAGER = ["orders", "product", "customer"]
ALLOWED_VIEWS_STAFF = ["sales_employee_view", "customer_view"]
SENSITIVE_TABLES = ["main_log"]
FORBIDDEN_KEYWORDS = ["drop", "truncate", "alter"]

# Endpoint GET để hiển thị dashboard
@router.get("/", response_class=HTMLResponse)
async def get_dashboard(request: Request):
    username = request.session.get("username")
    role = request.session.get("role")

    if not username or not role:
        return templates.TemplateResponse("login.html", {
            "request": request,
            "error": "Unauthorized. Please log in."
        })

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "username": username,
        "role": role,
        "history": query_history,
        "result": None,
        "last_query": None,
        "error": None
    })

# Endpoint POST để thực hiện truy vấn
@router.post("/", response_class=HTMLResponse)
async def execute_query(
    request: Request,
    query: str = Form(...),
    page: int = Query(1, ge=1),  # Phân trang
    db: AsyncSession = Depends(get_db)
):
    try:
        # Lấy vai trò và tên người dùng từ session
        role = request.session.get("role")
        username = request.session.get("username")

        if not role or not username:
            return templates.TemplateResponse("dashboard.html", {
                "request": request,
                "error": "Unauthorized. Please log in.",
                "last_query": None,
                "history": query_history,
            })

        # Kiểm tra từ khóa nguy hiểm
        if any(keyword in query.lower() for keyword in FORBIDDEN_KEYWORDS):
            return templates.TemplateResponse("dashboard.html", {
                "request": request,
                "error": "Dangerous queries are not allowed.",
                "last_query": query,
                "history": query_history,
                "username": username,
                "role": role,
            })

        # Phân tích câu truy vấn
        query_lower = query.strip().lower()
        query_parts = query_lower.split()
        command = query_parts[0]  # Lệnh SQL (SELECT, INSERT, ...)
        target_table_or_view = (
            query_parts[query_parts.index("from") + 1] if "from" in query_parts else None
        )
        target_table_or_view = target_table_or_view.rstrip(";").strip()  # Bỏ dấu chấm phẩy và khoảng trắng

        # Kiểm tra quyền của `role_manager`
        if role == "role_manager":
            if command not in ["select", "insert", "update", "delete"]:
                return templates.TemplateResponse("dashboard.html", {
                    "request": request,
                    "error": f"Command '{command.upper()}' is not allowed for manager.",
                    "last_query": query,
                    "history": query_history,
                    "username": username,
                    "role": role,
                })
            if target_table_or_view not in [table.lower() for table in ALLOWED_TABLES_MANAGER]:
                return templates.TemplateResponse("dashboard.html", {
                    "request": request,
                    "error": f"Access to '{target_table_or_view}' is not allowed for manager.",
                    "last_query": query,
                    "history": query_history,
                    "username": username,
                    "role": role,
                })

        # Kiểm tra quyền của `role_staff`
        elif role == "role_staff":
            if command != "select":
                return templates.TemplateResponse("dashboard.html", {
                    "request": request,
                    "error": "Only SELECT queries are allowed for staff.",
                    "last_query": query,
                    "history": query_history,
                    "username": username,
                    "role": role,
                })
            if target_table_or_view not in [view.lower() for view in ALLOWED_VIEWS_STAFF]:
                return templates.TemplateResponse("dashboard.html", {
                    "request": request,
                    "error": f"Access to '{target_table_or_view}' is not allowed for staff.",
                    "last_query": query,
                    "history": query_history,
                    "username": username,
                    "role": role,
                })

        # Nếu vai trò không xác định
        else:
            return templates.TemplateResponse("dashboard.html", {
                "request": request,
                "error": "Invalid role.",
                "last_query": query,
                "history": query_history,
                "username": username,
                "role": role,
            })

        # Ghi log truy vấn
        logging.info(f"[{role.upper()}] {username} executed query: {query}")

        # Bắt đầu tính thời gian thực thi
        start_time = time.time()

        # Thực thi truy vấn SQL
        result = await db.execute(text(query))
        rows = result.fetchall()
        column_names = result.keys()

        # Kết thúc tính thời gian thực thi
        execution_time = time.time() - start_time
        logging.info(f"Query executed in {execution_time:.4f} seconds")

        # Phân trang kết quả
        rows_per_page = 10
        total_rows = len(rows)
        start_index = (page - 1) * rows_per_page
        end_index = start_index + rows_per_page
        paginated_rows = rows[start_index:end_index]

        # Chuyển đổi kết quả thành danh sách dictionary
        data = [dict(zip(column_names, row)) for row in paginated_rows]

        # Thêm truy vấn vào lịch sử
        query_history.append(query)
        if len(query_history) > 10:  # Giới hạn tối đa 10 truy vấn trong lịch sử
            query_history.pop(0)

        # Hiển thị kết quả trên dashboard
        return templates.TemplateResponse("dashboard.html", {
            "request": request,
            "result": data,
            "last_query": query,
            "history": query_history,
            "execution_time": f"{execution_time:.4f} seconds",
            "total_rows": total_rows,
            "current_page": page,
            "total_pages": (total_rows // rows_per_page) + (1 if total_rows % rows_per_page else 0),
            "username": username,
            "role": role,
        })
    except SQLAlchemyError as e:
        # Ghi log lỗi
        logging.error(f"Error executing query: {query} - {str(e)}")

        # Xử lý lỗi và hiển thị trên giao diện
        return templates.TemplateResponse("dashboard.html", {
            "request": request,
            "error": f"Error executing query: {str(e)}",
            "last_query": query,
            "history": query_history,
            "username": username,
            "role": role,
        })

# Thêm route đăng xuất
@router.get("/logout", response_class=RedirectResponse)
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/auth/login")
