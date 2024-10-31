
**Mục lục**

- Giới thiệu
- Thực hiện công việc
  - 1.1 Xác định phân phối hệ điều hành và hệ thống thông tin
  - 1.2 Xác định các yêu cầu bảo mật dựa trên quy định của hệ thống tự động hóa lớp 2B
  - 1.3 Cấu hình Debian theo yêu cầu của các quy định
- Kết luận

---

**Giới thiệu**

**Mục tiêu** của bài thực hành là làm quen với các mô-đun bảo mật cơ bản của hệ thống Unix.

Để đạt được mục tiêu, cần thực hiện các nhiệm vụ sau:
- Xác định phân phối hệ điều hành.
- Xác định hệ thống bảo vệ điểm cuối.
- Đặt các yêu cầu bảo mật dựa trên quy định.
- Cấu hình hệ thống Unix theo yêu cầu của cơ quan quản lý.

---

**Thực hiện công việc**

- Phân phối: Debian
- Hệ thống thông tin (IS): Hệ thống tự động hóa lớp 2B

### 1.1 Xác định phân phối hệ điều hành và hệ thống thông tin

Debian là hệ điều hành mã nguồn mở phổ biến với nhân tương tự Unix (thường là Linux) và các thành phần phần mềm từ dự án GNU. Hệ thống tự động hóa lớp 2B cho phép người dùng có quyền truy cập giống nhau vào toàn bộ thông tin của hệ thống.

### 1.2 Xác định các yêu cầu bảo mật dựa trên quy định của hệ thống tự động hóa lớp 2B

Theo tài liệu hướng dẫn của FSTEK ngày 30 tháng 3 năm 1992, hệ thống tự động hóa được phân loại theo các mức độ bảo mật khác nhau, từ 1A đến 3B. Hệ thống lớp 2B yêu cầu các biện pháp bảo mật như quản lý truy cập, ghi nhận và giám sát hệ thống, sử dụng các phương tiện bảo mật cơ bản để ngăn chặn truy cập trái phép.

### 1.3 Cấu hình Debian theo yêu cầu của các quy định

1. **Cấu hình quản lý truy cập**:
   - Cài đặt nhận dạng và xác thực người dùng bằng cách thêm người dùng mới "user1" và đặt mật khẩu trong file `pwquality.conf` với các quy định như độ dài tối thiểu của mật khẩu.

2. **Cấu hình ghi nhận và giám sát**:
   - Ghi nhận lịch sử đăng nhập hệ thống và các lần đăng nhập thất bại bằng các lệnh `last` và `lastb`.
   - Thực hiện kiểm tra thông báo từ `kernel ring buffer` để lưu các bản ghi lỗi và tin nhắn từ hệ thống bằng lệnh `dmesg`.

3. **Cấu hình đảm bảo tính toàn vẹn**:
   - Cài đặt ClamAV làm công cụ chống virus để kiểm tra tính toàn vẹn của file cấu hình và thực hiện xác thực bằng hàm băm `sha256`.
   - Thiết lập công cụ `luckyBackup` để sao lưu dữ liệu, cho phép sao lưu từ xa thông qua SSH và cấu hình lịch trình sao lưu tự động.
   - Thực hiện kiểm tra định kỳ hệ thống bảo mật thông qua Vulners agent để phát hiện các điểm yếu của hệ điều hành.

### 4. Kết luận

Bài thực hành hoàn tất việc cấu hình hệ điều hành Debian theo yêu cầu của FSTEK đối với hệ thống tự động hóa lớp 2B, đáp ứng các nhiệm vụ và mục tiêu đã đề ra.

---

**PHỤ LỤC – Mã chương trình “app.py”**

Ứng dụng Flask Python giới hạn quyền truy cập sau ba lần đăng nhập thất bại, chặn địa chỉ IP đã thực hiện các lần đăng nhập thất bại liên tiếp.
