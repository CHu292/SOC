# HTTP


<h1 id="muc-luc">Mục lục</h1>

## [Phần I: HTTP là gì? Các khía cạnh cơ bản của HTTP](#http-la-gi)
- [Chương 1: HTTP là gì?](#chuong-1)
- [Chương 2: Cấu trúc cơ bản của HTTP](#chuong-2)
- [Chương 3: Kết nối của HTTP](#chuong-3)
- [Chương 4: Chuẩn hóa và phân loại mạng](#chuong-4-chuan-hoa-va-phan-loai-mang)
- [Chương 5: Các đặc tính mạng và chất lượng dịch vụ](#chuong-5-cac-dac-tinh-mang-va-chat-luong-dich-vu)
- [Câu hỏi cho Phần I](#cau-hoi-cho-phan-i)


# Nội dung


<h2 id="http-la-gi">Phần I: HTTP là gì? Các khía cạnh cơ bản của HTTP</h3>


<h3 id="chuong-1">Chương 1: HTTP là gì?</h3>


HTTP (HyperText Transfer Protocol) là giao thức truyền tải siêu văn bản, được sử dụng để trao đổi thông tin giữa máy khách (client) và máy chủ (server) trên World Wide Web. HTTP hoạt động theo mô hình yêu cầu-phản hồi: máy khách gửi yêu cầu (request) đến máy chủ, và máy chủ phản hồi (response) với dữ liệu tương ứng. 

**Đặc điểm của HTTP:**

- **Đơn giản:** HTTP được thiết kế để dễ hiểu và triển khai, với cú pháp rõ ràng, giúp các nhà phát triển dễ dàng kiểm thử và phát triển ứng dụng web. 

- **Không trạng thái (stateless):** Mỗi yêu cầu HTTP được xử lý độc lập, không lưu trữ thông tin về các yêu cầu trước đó. Điều này giúp giảm tải cho máy chủ, nhưng cũng đòi hỏi các cơ chế bổ sung như cookies để quản lý trạng thái người dùng. 

- **Mở rộng:** HTTP cho phép bổ sung các header mới, giúp mở rộng chức năng và cải thiện hiệu suất mà không cần thay đổi cấu trúc cơ bản. 

**Các phiên bản HTTP:**

- **HTTP/1.0:** Phiên bản đầu tiên, mỗi kết nối chỉ xử lý một yêu cầu-phản hồi, dẫn đến hiệu suất thấp. 

- **HTTP/1.1:** Cải tiến với kết nối liên tục (persistent connection), cho phép nhiều yêu cầu trên một kết nối, tăng hiệu suất truyền tải. 

- **HTTP/2:** Tối ưu hóa bằng cách đóng gói các yêu cầu và phản hồi vào các khung (frame), cải thiện tốc độ và hiệu suất của website. 

- **HTTP/3:** Sử dụng giao thức QUIC thay vì TCP, giảm độ trễ và tăng tốc độ truyền tải dữ liệu trên web. 

**Sự khác biệt giữa HTTP và HTTPS:**

HTTPS (HTTP Secure) là phiên bản bảo mật của HTTP, sử dụng mã hóa TLS (Transport Layer Security) để bảo vệ dữ liệu trong quá trình truyền tải, đảm bảo tính toàn vẹn và bảo mật thông tin giữa máy khách và máy chủ. 

<h3 id="chuong-2">Chương 2: Cấu trúc cơ bản của HTTP</h3>


**Cấu trúc của một yêu cầu HTTP (HTTP Request):**

1. **Dòng yêu cầu (Request Line):**
   - **Phương thức HTTP (HTTP Method):** Xác định hành động cần thực hiện, như GET, POST, PUT, DELETE.
   - **Đường dẫn tài nguyên (Request-URI):** Địa chỉ của tài nguyên trên máy chủ.
   - **Phiên bản HTTP (HTTP Version):** Ví dụ: HTTP/1.1.

2. **Tiêu đề yêu cầu (Request Headers):**
   - Chứa các cặp khóa-giá trị cung cấp thông tin bổ sung về yêu cầu, như loại trình duyệt, định dạng dữ liệu chấp nhận.

3. **Dòng trống:**
   - Phân tách phần tiêu đề và thân yêu cầu.

4. **Thân yêu cầu (Request Body) (tùy chọn):**
   - Chứa dữ liệu gửi kèm, thường dùng trong các yêu cầu POST hoặc PUT.

**Cấu trúc của một phản hồi HTTP (HTTP Response):**

1. **Dòng trạng thái (Status Line):**
   - **Phiên bản HTTP (HTTP Version):** Ví dụ: HTTP/1.1.
   - **Mã trạng thái (Status Code):** Cho biết kết quả xử lý, như 200 (OK), 404 (Not Found).
   - **Thông điệp trạng thái (Reason Phrase):** Mô tả ngắn gọn về mã trạng thái.

2. **Tiêu đề phản hồi (Response Headers):**
   - Cung cấp thông tin về máy chủ, loại nội dung, độ dài nội dung.

3. **Dòng trống:**
   - Phân tách phần tiêu đề và thân phản hồi.

4. **Thân phản hồi (Response Body):**
   - Chứa dữ liệu được yêu cầu, như nội dung HTML, hình ảnh, hoặc dữ liệu khác.


![Cấu trúc cơ bản của HTTP](./img/HTTP/cau_truc_co_ban_HTTP.png)

<h3 id="chuong-3">Chương 3: Kết nối của HTTP</h3>

Kết nối trong HTTP được thiết lập qua các phương thức sau:

**Kết nối không liên tục (Non-Persistent Connection):**

- Trong HTTP/1.0, mỗi yêu cầu từ máy khách đến máy chủ thiết lập một kết nối TCP riêng biệt. Sau khi máy chủ phản hồi, kết nối này sẽ được đóng lại. Phương thức này không hiệu quả khi cần tải nhiều tài nguyên, do phải thiết lập nhiều kết nối liên tiếp, tăng độ trễ và tải cho máy chủ. 

**Kết nối liên tục (Persistent Connection):**

- Để cải thiện hiệu suất, HTTP/1.1 giới thiệu kết nối liên tục, cho phép sử dụng một kết nối TCP duy nhất cho nhiều yêu cầu và phản hồi giữa máy khách và máy chủ. Điều này giảm thiểu thời gian thiết lập kết nối mới cho mỗi yêu cầu, tăng tốc độ tải trang và giảm tải cho máy chủ. 

**Kết nối trong HTTP/2 và HTTP/3:**

- HTTP/2 nâng cao hiệu quả bằng cách cho phép gửi nhiều yêu cầu và nhận nhiều phản hồi đồng thời qua một kết nối duy nhất, sử dụng kỹ thuật ghép kênh (multiplexing). Điều này giúp giảm độ trễ và tăng tốc độ truyền tải dữ liệu. 

- HTTP/3, dựa trên giao thức QUIC, tiếp tục cải thiện hiệu suất và bảo mật bằng cách sử dụng UDP thay vì TCP, giúp thiết lập kết nối nhanh hơn và giảm độ trễ trong truyền tải dữ liệu. 
