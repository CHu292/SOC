# Bảo vệ cơ sở dữ liệu
---
## Mục tiêu:
Luyện kỹ năng tạo hệ thống giám sát đơn giản, phân quyền truy cập và mã hóa bằng các công cụ của Hệ Quản Trị Cơ Sở Dữ Liệu (CSDL).
## Nhiệm vụ:
### 1 Nhiệm vụ giám sát CSDL
- Tạo bảng nhật ký, riêng biệt với các thực thể chính trong CSDL của bạn.
- Tạo trigger cho mỗi bảng chính trong CSDL của bạn, kích hoạt khi có bất kỳ thay đổi nào trong CSDL (thêm dữ liệu mới, chỉnh sửa bản ghi hiện có, xóa các hàng từ bảng). Khi kích hoạt, trigger phải ghi vào bảng nhật ký thông tin về thời điểm thay đổi, vai trò yêu cầu, các hàng thay đổi, giá trị cũ và mới.
