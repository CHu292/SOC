# Xây dựng máy quét cổng (Port Scanner)

> Viết chương trình python để quét các cổng mở trên một địa chỉ IP cụ thể

> Gợi ý: Sử dụng module `socket` để thử kết nối đến các cổng trong một phạm vi nhất định và xác định cổng nào đang mở

# Socket là gì?

Socket là các điểm đầu nút (endpoint) của một kênh giao tiếp song hướng. Các Socket có thể giao tiếp bên trong một tiến trình, giữa các tiến trình trên cùng một thiết bị hoặc giữa các tiến trình trên các lục địa khác nhau.

Các Socket có thể được triển khai thông qua các kênh khác nhau: domain, TCP, UDP, … Thư viện socket cung cấp các lớp riêng để xử lý các trình truyền tải cũng như một Interface chung để xử lý phần còn lại.

Socket có các khái niệm riêng như sau:

| Khái niệm  | Miêu tả |
|------------|---------|
| **domain** | Là family của các giao thức protocol được sử dụng như là kỹ thuật truyền tải. Các giá trị này là các hằng như AF_INET, PF_INET, PF_UNIX, PF_X25, ... |
| **type** | Kiểu giao tiếp giữa hai endpoint, đặc trưng là SOCK_STREAM cho các giao thức hướng kết nối (connection-oriented) và SOCK_DGRAM cho các giao thức không hướng kết nối |
| **protocol** | Đặc trưng là 0, mà có thể được sử dụng để nhận diện một biến thể của một giao thức bên trong một domain hoặc type |
| **hostname** | Định danh của một network interface: <br> - Một chuỗi, có thể là tên một host, địa chỉ IPV6, ... <br> - Một chuỗi `"<broadcast>"`, xác định một địa chỉ INADDR_BROADCAST <br> - Một chuỗi có độ dài là 0, xác định INADDR_ANY, hoặc <br> - Một số nguyên, được thông dịch dưới dạng một địa chỉ nhị phân trong thứ tự host byte |
| **port** | Mỗi Server nghe các lời gọi từ Client trên một hoặc nhiều cổng (port). Một port có thể là một chuỗi chứa số hiệu của port, một tên của một dịch vụ, ... |

## socket Module trong Python

Để tạo một Socket, bạn phải sử dụng hàm `socket.socket()` có sẵn trong socket Module, có cú pháp chung như sau:

```python
s = socket.socket (socket_family, socket_type, protocol=0)
```

Chi tiết về tham số:

socket_family: Đây hoặc là AF_UNIX hoặc AF_INET.

socket_type: Đây hoặc là SOCK_STREAM hoặc SOCK_DGRAM.

protocol: Thường được để trống, mặc định là 0.

