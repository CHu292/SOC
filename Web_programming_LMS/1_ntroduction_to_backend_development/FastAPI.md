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
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/1_Basic_concepts_of_network_technologies/image/4_Typical_switched_data_center_network_architecture.png" alt="Kiến trúc mạng chuyển mạch trung tâm dữ liệu điển hình" width="1000">
</p>
<p align="center"><b>Hình minh họa</b></p>

- Nếu như WSGI là tiêu chuẩn cho các synchronous Python appsthì ASGI là tiêu chuẩn cho cả synchronous và asynchronous Python apps. ASGI phù hợp với tất cả ứng dụng sử dụng WSGI do có cơ chế tương thích ngược.

