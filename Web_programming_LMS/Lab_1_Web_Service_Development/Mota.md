Dự án này là một ứng dụng chat trực tuyến, bao gồm các thành phần microservice sử dụng kiến trúc web socket để cung cấp chức năng trò chuyện thời gian thực. Dưới đây là mô tả chi tiết về cách hoạt động của từng thành phần trong dự án.

### 1. Thành phần và kiến trúc tổng quát
Dự án này được chia thành các microservice chính sau:

- **Website microservice**: Chịu trách nhiệm quản lý người dùng và các phòng chat. Đây là nơi người dùng có thể đăng ký, đăng nhập, tạo phòng chat, tìm kiếm phòng chat và gửi tin nhắn.
- **Chat WebSocket microservice**: Xử lý các kết nối WebSocket cho các phòng chat, giúp truyền tải tin nhắn giữa các người dùng trong cùng phòng chat.
- **Database (PostgreSQL)**: Lưu trữ dữ liệu về người dùng, các phòng chat và tin nhắn.
- **Nginx**: Hoạt động như một reverse proxy, chuyển tiếp các yêu cầu HTTP cho website microservice và các kết nối WebSocket cho chat microservice.

### 2. Cách thức hoạt động của từng thành phần

#### 2.1 Website Microservice
- **Quản lý người dùng**: Người dùng có thể đăng ký tài khoản mới bằng email, username và mật khẩu. Khi đăng ký, hệ thống sẽ lưu trữ thông tin này trong bảng `users` của cơ sở dữ liệu với mật khẩu được mã hóa.
- **Đăng nhập và xác thực**: Khi người dùng đăng nhập, hệ thống sẽ kiểm tra thông tin xác thực (email và mật khẩu) và, nếu hợp lệ, tạo một token JWT để xác thực phiên làm việc của người dùng. Token này sẽ được lưu dưới dạng cookie trong trình duyệt để xác thực các yêu cầu tiếp theo.
- **Tạo phòng chat**: Người dùng đã đăng nhập có thể tạo các phòng chat mới. Thông tin về phòng chat sẽ được lưu trữ trong bảng `chat_rooms` với ID của người tạo (owner_id) để xác định quyền xóa phòng.
- **Tìm kiếm phòng chat**: Người dùng có thể tìm kiếm các phòng chat dựa trên tên phòng, cho phép họ tham gia vào các cuộc trò chuyện có sẵn.
- **Xóa phòng chat**: Chỉ chủ sở hữu phòng chat mới có thể xóa phòng đó. Khi phòng bị xóa, tất cả các tin nhắn trong phòng cũng sẽ bị xóa.

#### 2.2 Chat WebSocket Microservice
- **Quản lý kết nối WebSocket**: Khi người dùng tham gia vào phòng chat, hệ thống sẽ thiết lập một kết nối WebSocket tới chat microservice qua một endpoint `/ws/{room_name}`. Tại đây, `room_name` là tên của phòng chat mà người dùng muốn tham gia.
- **Gửi và nhận tin nhắn**: Sau khi kết nối thành công, người dùng có thể gửi tin nhắn đến các thành viên khác trong phòng chat. Tin nhắn sẽ được truyền tới chat WebSocket microservice, nơi sẽ phát sóng tin nhắn đến tất cả người dùng hiện đang kết nối trong cùng phòng chat đó.
- **Lưu trữ tin nhắn**: Khi một tin nhắn mới được gửi đến, nó sẽ được lưu vào bảng `messages` trong cơ sở dữ liệu với thông tin về nội dung, tên người gửi, và thời gian gửi.

#### 2.3 Database (PostgreSQL)
Cơ sở dữ liệu được dùng để lưu trữ toàn bộ dữ liệu của dự án:
- **Bảng `users`**: Lưu trữ thông tin người dùng, bao gồm `id`, `email`, `username`, và `hashed_password`.
- **Bảng `chat_rooms`**: Lưu trữ thông tin phòng chat, bao gồm `id`, `name` (tên phòng), và `owner_id` (ID của người tạo).
- **Bảng `messages`**: Lưu trữ các tin nhắn, bao gồm `id`, `content` (nội dung tin nhắn), `room_id` (ID của phòng chứa tin nhắn), `username` (người gửi), và `timestamp` (thời gian gửi tin nhắn).

#### 2.4 Nginx
Nginx được cấu hình như một reverse proxy để chuyển tiếp các yêu cầu đến các microservice khác nhau:
- **Chuyển tiếp HTTP**: Các yêu cầu HTTP từ người dùng sẽ được chuyển đến website microservice, bao gồm các yêu cầu như đăng nhập, đăng ký, tạo phòng chat, và tìm kiếm phòng chat.
- **Chuyển tiếp WebSocket**: Các kết nối WebSocket từ người dùng sẽ được chuyển tiếp đến chat WebSocket microservice, giúp thực hiện chức năng trò chuyện thời gian thực giữa các người dùng trong phòng chat.

### 3. Quy trình hoạt động của hệ thống

1. **Người dùng truy cập trang chính**: Người dùng có thể đăng ký hoặc đăng nhập bằng email và mật khẩu.
2. **Tạo phòng chat**: Sau khi đăng nhập, người dùng có thể tạo một phòng chat mới hoặc tìm kiếm các phòng chat hiện có để tham gia.
3. **Tham gia vào phòng chat**: Khi tham gia vào một phòng chat, kết nối WebSocket được thiết lập để người dùng có thể gửi và nhận tin nhắn trong thời gian thực.
4. **Gửi và nhận tin nhắn**: Tin nhắn được phát sóng tới tất cả người dùng trong phòng qua kết nối WebSocket, và được lưu lại trong cơ sở dữ liệu để người dùng có thể xem lại khi truy cập lại phòng chat sau này.
5. **Kết thúc phiên làm việc**: Khi người dùng ngắt kết nối WebSocket hoặc thoát khỏi phòng chat, hệ thống sẽ tự động ngắt kết nối.

### 4. Kết luận
Dự án này xây dựng thành công hệ thống chat trực tuyến với các chức năng cơ bản như đăng ký, đăng nhập, tạo phòng, tham gia phòng, và gửi tin nhắn thời gian thực. Việc sử dụng các công nghệ như FastAPI, WebSocket và Nginx cho phép dự án đạt được hiệu suất và khả năng mở rộng tốt, phù hợp với các hệ thống chat lớn.
