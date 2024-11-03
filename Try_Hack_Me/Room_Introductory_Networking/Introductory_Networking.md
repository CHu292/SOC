# Room Introductory Networking
- [x] The OSI Model
- [x] The TCP/IP Model
- [x] How these models look in practice
- [x] An introduction to basic networking tools

## 1. The OSI Model: An Overview

### 1.1 Khái niệm

**Mô hình OSI** (Open Systems Interconnection) - mô hình kết nối các hệ thống mở.

Mô hình Kết nối các hệ thống mở (OSI) là một khung khái niệm chia các chức năng truyền thông mạng thành 7 lớp. Việc gửi dữ liệu qua mạng rất phức tạp vì các công nghệ phần cứng và phần mềm khác nhau phải hoạt động một cách hài hòa qua các ranh giới địa lý và chính trị. Mô hình dữ liệu OSI cung cấp một ngôn ngữ phổ quát cho mạng máy tính, vì vậy các công nghệ đa dạng có thể giao tiếp bằng cách sử dụng các giao thức tiêu chuẩn hoặc quy tắc truyền thông. Mỗi công nghệ trong một lớp cụ thể phải cung cấp các khả năng nhất định và thực hiện các chức năng cụ thể để trở nên hữu ích trong mạng. Các công nghệ ở những lớp cao hơn hưởng lợi từ việc rút gọn này vì chúng có thể sử dụng các công nghệ cấp thấp hơn mà không phải lo lắng về các chi tiết triển khai cơ bản.

Mô hình OSI gồm có 7 lớp:

### Tổng quan
- **Lớp 7**: Chấp nhận yêu cầu liên lạc từ các ứng dụng.
- **Lớp 6**: Mã hóa, nén, biến dữ liệu ban đầu để cung cấp cho nó định dạng chuẩn.
- **Lớp 5**: Theo dõi thông tin liên lạc giữa máy chủ và máy tính nhận.
- **Lớp 4**: Lựa chọn gửi dữ liệu qua TCP hoặc UDP.
- **Lớp 3**: Xử lý địa chỉ logic (IP).
- **Lớp 2**: Kiểm tra thông tin nhận để đảm bảo nó không bị hỏng, cũng như định dạng dữ liệu để chuẩn bị truyền tải.
- **Lớp 1**: Truyền và nhận dữ liệu.
