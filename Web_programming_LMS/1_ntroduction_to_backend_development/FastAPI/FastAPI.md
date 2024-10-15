#  FastAPI

## Khái niệm
- FastApi là 1 web framework dùng để build API có hiệu năng cao, code dễ ẹc, đơn giản nhưng cũng hỗ trợ tốt cho việc làm sản phẩm.
- Đặc điểm:

  - Fast: Hiệu suất cao ngang với NodeJS và Go.
  - Fast to code: Code nhanh hơn, tốc độ code các features tăng khoảng 200 đến 300 %.
  - Fewer bugs: do đơn giản nên giảm số bugs của developper đến 40%.
  - Intuitive: hỗ trợ code dễ hơn với tự động gợi ý, debug cần ít thời gian hơn so với trước.
  - Easy: được thiết kế sao cho dễ dùng dễ học.
  - Short: Tối thiểu việc lặp code. Các tham số truyền vào có nhiều tính năng. Ít bugs.
  - Robust: hiệu năng mạnh mẽ, có thể tương tác API qua docs.

## Cách cài đặt
- Yêu cầu: Python 3.6+.
- FastAPI được build dựa trên OpenAPI (trước có tên Swagger), phần web được support bởi Starlette, còn phần data được support bởi Pydantic.

### FastAPI CLI

- Để cài đặt framework này trên Ubuntu, bạn cần phiên bản python ≥ 3.6.
  
  ```pip install fastapi```
- Bạn cũng cần ASGI server khi deploy sản phẩm như Uvicorn hoặc Hypercorn.
``` pip install uvicorn```
- ASGI kế thừa từ WSGI. Mà WSGI là 1 chuẩn giao tiếp giữa web server và Python application server.
- WSGI có những tác dụng như sau:
  - WSGI mang tính linh hoạt: dev có thể chuyển đổi thành phần web như chuyển từ Gunicorn sang uWSGI.
  - WSGI xử lý nhiều request cùng lúc thay webserver và quyết định request nào được chuyển tới application web.

  <p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/Hinh_minh_.png" alt="" width="1000">
</p>
<p align="center"><b>Hình minh họa</b></p>

- Nếu như WSGI là tiêu chuẩn cho các ```synchronous Python apps``` thì ASGI là tiêu chuẩn cho cả ```synchronous``` và ```asynchronous Python apps```. ASGI phù hợp với tất cả ứng dụng sử dụng WSGI do có cơ chế tương thích ngược.

### FastAPI Docs

- Do based trên OpenAI mà trước đó có tên là Swagger nên FastAPI cung cấp doc có giao diện dễ nhìn, dễ sử dụng. Ví dụ minh họa:
- Khi bật doc bằng local url ```http://0.0.0.0:8000/docs```

  <p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/code_run_result.png" alt="" width="1000">
</p>
<p align="center"><b>Docs</b></p>

- 1 giao diện khác của FastAPI docs ```http://0.0.0.0:8000/redoc```

  <p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/1_Basic_concepts_of_network_technologies/image/4_Typical_switched_data_center_network_architecture.png" alt="Kiến trúc mạng chuyển mạch trung tâm dữ liệu điển hình" width="1000">
</p>
<p align="center"><b>Redoc</b></p>

### Performance
Các bạn có thể test hiệu năng của các web framework trên [trang này](https://www.techempower.com/benchmarks/)

### Optional Depencies

- Do FastAPI based trên Pydantic và Starlette nên có hỗ trợ thêm 1 số thư viện
- Pydantic:

  - ujson: JSON "parsing" nhanh hơn.
  - email_validator: validate email.

- Starlette:

  - requests: khi bạn muốn tạo request, dùng TestClient.
  - aiofiles: khi bạn muốn dùng FileResponse hoặc StaticFile.
  - jinja2: nếu bạn muốn dùng các mẫu config mặc định.
  - python-multipart: hỗ trợ "parsing" với request.form().
  - itsdangerous: hỗ trợ SessionMiddleware.
  -graphene: hỗ trợ GraphQL.

- FastAPI:

  - uvicorn: ASGI server phục vụ cho ứng dụng của bạn.
  - orjson: nếu muốn dùng ORJSONResponse.

- Nếu muốn dùng hết thư viện trên thì bạn chỉ cần dùng 1 câu lệnh đơn giản.

```pip install fastapi[all]```

## Hướng dẫn cơ bản
### Create a simple API
---
Các bước

Nói chung bạn chỉ cần 6 bước để tạo 1 API

- Bước 1: import fastapi
- Bước 2: tạo 1 instance của class FastAPI
- Bước 3: tạo đường dẫn, bắt đầu từ /
- Bước 4: khai báo phương thức HTTP: post, get, put, delete hay options, head, patch, trace
- Bước 5: khai báo hàm
- Bước 6: trả về content với format dict, list, str, int, ...
---

- Tạo một file main.py như sau:
  
```python
from fastapi import FastAPI #import class FastAPI() từ thư viện fastapi

app = FastAPI() # gọi constructor và gán vào biến app

@app.get("/") #giống flask, khai báo phương thức get và url
async def root(): #do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async
	return {"message": "Hello world"}
```

sau đó chạy app:
```uvicorn main:app --host 0.0.0.0 --port 8000```

  <p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/run_code_fastapi.png" alt="chạy app" width="1000">
</p>
<p align="center"><b>Chạy app </b></p>

**P/S: nếu bạn làm trong môi trường phát triển có thể thêm --reload để tự động restart sau khi thay đổi code.**

-  Chúng ta cùng xem trên giao diện Docs ```http://127.0.0.1:8000/docs```

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/code_run_result.png" alt="chạy app" width="1000">
</p>
<p align="center"><b>Xem kết quả trên giao diện Docs </b></p>

- Ấn vào Try it out -> Execute -> API trả về response.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/API_returns_response.png" alt="API trả về response" width="1000">
</p>
<p align="center"><b>API trả về response</b></p>

- Giao diện API này được thiết kế dựa trên OpenAPI. Có 1 khái niệm để define API gọi là "Schema". 
- Truy cập vào:  ```http://127.0.0.1:8000/openapi.json```

```
{
  "openapi": "3.1.0",
  "info": {
    "title": "FastAPI",
    "version": "0.1.0"
  },
  "paths": {
    "/": {
      "get": {
        "summary": "Root",
        "operationId": "root__get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {

                }
              }
            }
          }
        }
      }
    }
  }
}
```

### Path Parameters

- Bạn có thể truyền param thông qua đường dẫn.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id):
	return {"item_id": item_id}
```

- Biến item_id trên đường dẫn sẽ truyền vào hàm read_item với thông qua param trùng tên item_id. Test thử ```http://127.0.0.1:8000/items/abc```

  <p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/path_parameters_1.png" alt="" width="1000">
</p>
<p align="center"><b>Ví dụ thử trên web</b></p>

  <p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/path_parameters_2.png" alt="" width="1000">
</p>
<p align="center"><b>Kiểm tra trạng thái</b></p>


