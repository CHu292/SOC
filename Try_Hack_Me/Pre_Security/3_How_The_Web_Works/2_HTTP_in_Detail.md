# HTTP in Detail

> Tìm hiểu cách bạn yêu cầu nội dung từ máy chủ web bằng giao thức HTTP.


## Mục Lục

1. [Task 1: What is HTTP(S)?](#task-1-what-is-https)  
2. [Task 2: Requests And Responses](#task-2-requests-and-responses)  
3. [Task 3: HTTP Methods](#task-3-http-methods)  
4. [Task 4: HTTP Status Codes](#task-4-http-status-codes)  
5. [Task 5: Headers](#task-5-headers)  
6. [Task 6: Cookies](#task-6-cookies)  
7. [Task 7: Making Requests](#task-7-making-requests)

## Nội dung

# Task 1: What is HTTP(S)?

**HTTP là gì? (HyperText Transfer Protocol)**

HTTP được sử dụng bất cứ khi nào bạn truy cập một trang web, được phát triển bởi Tim Berners-Lee và nhóm của ông trong khoảng thời gian 1989-1991. HTTP là tập hợp các quy tắc dùng để giao tiếp với máy chủ web nhằm truyền dữ liệu trang web, bao gồm HTML, hình ảnh, video, v.v.

**HTTPS là gì? (HyperText Transfer Protocol Secure)**

HTTPS là phiên bản bảo mật của HTTP. Dữ liệu HTTPS được mã hóa, giúp ngăn chặn người khác xem dữ liệu bạn nhận và gửi. Đồng thời, HTTPS đảm bảo rằng bạn đang giao tiếp với máy chủ web chính xác, không phải một máy chủ giả mạo.

**Câu hỏi:**

**Câu hỏi 1:** HTTP là viết tắt của cụm từ gì?  
<details>  
<summary>Hiển thị đáp án</summary>  
Đáp án: HyperText Transfer Protocol  
</details>  

**Câu hỏi 2:** Chữ "S" trong HTTPS là viết tắt của từ gì?  
<details>  
<summary>Hiển thị đáp án</summary>  
Đáp án: secure  
</details>  

**Câu hỏi 3:** Trên trang web giả lập bên phải có một vấn đề. Sau khi tìm ra vấn đề, hãy nhấp vào nó. Flag của thử thách là gì?  

![HTTPS](./img/2_HTTP_in_Detail/1.1.png)

<details>  
<summary>Hiển thị đáp án</summary>  
Đáp án: THM{INVALID_HTTP_CERT}  
</details>  

