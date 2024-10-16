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
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/code_run_result_redoc.png" alt="" width="1000">
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


### Path parameters with types
- Bạn cũng có thể khai báo định dạng của param để trả về khi truyền biến đúng định dạng sẽ trả về giá trị.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
	return {"item_id": item_id}
```

  <p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/Path_parameters_with_types.png" alt="" width="1000">
</p>
<p align="center"><b>Path parameters with types</b></p>

### Data validation

- Còn nếu không đúng định dạng thì trả về thông báo. Mọi dữ liệu được validate đều dựa trên Pydantic.

  <p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/Data_validation.png" alt="" width="1000">
</p>
<p align="center"><b>Data validation</b></p>

### Order

Nếu bạn có khai báo đường dẫn trùng lặp như thế này:

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/me")
async def read_users_me():
	return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
	return {"user_id": user_id}
```
Thì nhớ để theo thứ tự /users/me trước rồi đến /users/{user_id} sau, ngược lại nếu /users/{user_id} ở trước thì sẽ nghĩ rằng "user_id" được nhận giá trị me.

### Path in path

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
	return {"file_fath": file_path}
```

  <p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/path_in_path.png" alt="" width="1000">
</p>
<p align="center"><b>Path in path</b></p>


### Query Parameters

- Nếu bạn truyền param dưới dạng key-value thì ở trong FastAPI có hỗ trợ với tên gọi "query" parameters.

```python
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Ch"}, {"item_name": "Mi"}, {"item_name": "ran"}] # pair format: key-value

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
	return fake_items_db[skip: skip+limit] # trả về dữ liệu từ skip đến skip  + limit
```

- Cùng kiểm tra kết quả
  
<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/query_parameters.png" alt="" width="700">
</p>
<p align="center"><b>Query Parameters</b></p>

- Nếu bạn để ý skip và limit có format string khi làm đường dẫn nhưng một khi truyền về hàm thì sẽ ngay lập tức được convert từ string về int.

### Optional parameters

- Ngoài ra FastAPI cung cấp một cách khai báo optional query parameters, mặc định là None.

```python
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    '''
    param item_id: format string
    param q: format string, default value: None, Optional: help you find error that happen
    '''
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
```
- Như bạn thấy ở trên param truyền ở đường dẫn là item_id, nhưng trong hàm có thêm param q. FastAPI chỉ sử dụng str để nhận định format của param còn Optional thì FastAPI không sử dụng, chỉ có tác dụng check lỗi nếu xảy ra.

- Bạn có thể test bằng đường dẫn sau.

``` http://127.0.0.1:8000/items/1?q=1 # 1 là item_id và ?q=1 là giá trị của q```


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/optional_parameters.png" alt="" width="700">
</p>
<p align="center"><b>Optional parameters</b></p>

### Query parameter type conversion

Thay đổi giá trị mặc định bằng cách truyền giá trị trên đường dẫn.

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, short: bool = False): # param short với định dạng boolean có giá trị mặc định là False
    item = {"item_id": item_id}
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
```
- Trong trường hợp này

```http://127.0.0.1:8000/items/1?short=1```

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/Query_parameter_type_conversion_1.png" alt="" width="700">
</p>
<p align="center"><b>Query parameter type conversions 1 </b></p>

```http://127.0.0.1:8000/items/1?short=true```

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/Query_parameter_type_conversion_true.png" alt="" width="700">
</p>
<p align="center"><b>Query parameter type conversions true</b></p>

```http://127.0.0.1:8000/items/1?short=false```

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/FastAPI/Query_parameter_type_conversion_false.png" alt="" width="700">
</p>
<p align="center"><b>Query parameter type conversions - false</b></p>


