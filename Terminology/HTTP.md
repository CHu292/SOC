# HTTP


<h1 id="muc-luc">Mục lục</h1>

## [Phần I: HTTP là gì? Các khía cạnh cơ bản của HTTP](#http-la-gi)
- [Chương 1: HTTP là gì?](#chuong-1)
- [Chương 2: Các nguyên tắc chung trong xây dựng mạng](#chuong-2-cac-nguyen-tac-chung-trong-xay-dung-mang)
- [Chương 3: Chuyển mạch kênh và chuyển mạch gói](#chuong-3-chuyen-mach-kenh-va-chuyen-mach-goi)
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

Hiểu rõ về HTTP giúp bạn nắm bắt cách thức hoạt động của web và tầm quan trọng của việc bảo mật thông tin trực tuyến. 
