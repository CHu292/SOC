# Mục lục

1. [Tường lửa là gì?](#tường-lửa-là-gì)
2. [Tường lửa gồm có bao nhiêu loại?](#tường-lửa-gồm-có-bao-nhiêu-loại)
   - [Tường lửa Personal](#tường-lửa-personal)
   - [Network Firewalls](#network-firewalls)
3. [Cách thức hoạt động của tường lửa như thế nào?](#cách-thức-hoạt-động-của-tường-lửa-như-thế-nào)
4. [Nhiệm vụ của tường lửa (Firewall) là gì?](#nhiệm-vụ-của-tường-lửa-firewall-là-gì)
5. [Ưu và nhược điểm của tường lửa](#ưu-và-nhược-điểm-của-tường-lửa)
   - [Ưu điểm của tường lửa](#ưu-điểm-của-tường-lửa)
   - [Nhược điểm của tường lửa](#nhược-điểm-của-tường-lửa)
6. [Những tùy chọn khi triển khai Firewall mà bạn nên biết](#những-tùy-chọn-khi-triển-khai-firewall-mà-bạn-nên-biết)
   - [Stateful firewall (Tường lửa có trạng thái)](#stateful-firewall-tường-lửa-có-trạng-thái)
   - [Next-generation firewalls – NGFW (Tường lửa thế hệ tiếp theo)](#next-generation-firewalls-ngfw-tường-lửa-thế-hệ-tiếp-theo)
   - [Proxy-based firewall (Tường lửa dựa trên proxy)](#proxy-based-firewall-tường-lửa-dựa-trên-proxy)
   - [Web application firewall – WAF (Tường lửa ứng dụng web)](#web-application-firewall-waf-tường-lửa-ứng-dụng-web)
   - [Tường lửa phần cứng](#tường-lửa-phần-cứng)
   - [Tường lửa phần mềm](#tường-lửa-phần-mềm)
   - [Kiểm tra trạng thái tường lửa](#kiểm-tra-trạng-thái-tường-lửa)
   - [Tường lửa phát hiện và diệt virus](#tường-lửa-phát-hiện-và-diệt-virus)
   - [Kiểm tra tầng ổ bảo mật SSL](#kiểm-tra-tầng-ổ-bảo-mật-ssl)
   - [Intrusion Prevention Systems – IPS (Hệ thống phòng chống xâm nhập)](#intrusion-prevention-systems-ips-hệ-thống-phòng-chống-xâm-nhập)
   - [Theo dõi lưu lượng gửi đi (DPI)](#theo-dõi-lưu-lượng-gửi-đi-dpi)
7. [Những lỗ hổng của tường lửa](#những-lỗ-hổng-của-tường-lửa)
   - [Tấn công nội bộ](#tấn-công-nội-bộ)
   - [Tấn công từ chối dịch vụ phân tán (DDos)](#tấn-công-từ-chối-dịch-vụ-phân-tán-ddos)
   - [Các phần mềm độc hại](#các-phần-mềm-độc-hại)
   - [Cấu hình tường lửa kém, thiếu cập nhật](#cấu-hình-tường-lửa-kém-thiếu-cập-nhật)

---

# Nội dung

## 1. Tường lửa là gì?
Tường lửa là một công cụ bảo mật mạng, hoạt động như rào chắn giữa mạng nội bộ an toàn và các mạng bên ngoài, chẳng hạn như Internet.

## 2. Tường lửa gồm có bao nhiêu loại?
### 2.1. Tường lửa Personal
Tường lửa Personal được cài đặt trên máy tính cá nhân để bảo vệ thiết bị trước các mối đe dọa từ bên ngoài.

### 2.2. Network Firewalls
Tường lửa mạng bảo vệ toàn bộ hệ thống mạng khỏi các cuộc tấn công từ bên ngoài, thường được sử dụng trong doanh nghiệp.

## 3. Cách thức hoạt động của tường lửa như thế nào?
Tường lửa kiểm tra và lọc các luồng dữ liệu vào và ra dựa trên các quy tắc bảo mật đã được định sẵn.

## 4. Nhiệm vụ của tường lửa (Firewall) là gì?
- Bảo vệ mạng nội bộ.
- Ngăn chặn truy cập trái phép.
- Giám sát lưu lượng mạng.

## 5. Ưu và nhược điểm của tường lửa
### 5.1. Ưu điểm của tường lửa
- Bảo vệ dữ liệu và hệ thống mạng.
- Ngăn chặn truy cập trái phép.
- Dễ dàng quản lý.

### 5.2. Nhược điểm của tường lửa
- Có thể gây chậm mạng.
- Không ngăn chặn được tấn công từ bên trong.
- Chi phí triển khai cao.

## 6. Những tùy chọn khi triển khai Firewall mà bạn nên biết
### 6.1. Stateful firewall (Tường lửa có trạng thái)
Lưu trạng thái của các kết nối mạng để quyết định chặn hoặc cho phép.

### 6.2. Next-generation firewalls – NGFW (Tường lửa thế hệ tiếp theo)
Kết hợp chức năng tường lửa truyền thống với các tính năng nâng cao như kiểm tra sâu gói tin (DPI).

### 6.3. Proxy-based firewall (Tường lửa dựa trên proxy)
Đóng vai trò trung gian giữa người dùng và mạng.

### 6.4. Web application firewall – WAF (Tường lửa ứng dụng web)
Bảo vệ các ứng dụng web khỏi các cuộc tấn công phổ biến.

### 6.5. Tường lửa phần cứng
Hoạt động độc lập dưới dạng thiết bị vật lý.

### 6.6. Tường lửa phần mềm
Cài đặt trên máy chủ hoặc máy tính.

### 6.7. Kiểm tra trạng thái tường lửa
Giám sát các quy tắc và kết nối hiện hành của tường lửa.

### 6.8. Tường lửa phát hiện và diệt virus
Kết hợp tường lửa và phần mềm chống virus.

### 6.9. Kiểm tra tầng ổ bảo mật SSL
Phân tích và giám sát lưu lượng được mã hóa SSL.

### 6.10. Intrusion Prevention Systems – IPS (Hệ thống phòng chống xâm nhập)
Ngăn chặn các mối đe dọa bằng cách phân tích lưu lượng.

### 6.11. Theo dõi lưu lượng gửi đi (DPI)
Giám sát và kiểm soát các gói dữ liệu gửi ra bên ngoài.

## 7. Những lỗ hổng của tường lửa
### 7.1. Tấn công nội bộ
Kẻ tấn công có quyền truy cập mạng nội bộ.

### 7.2. Tấn công từ chối dịch vụ phân tán (DDos)
Làm hệ thống quá tải bằng cách gửi lượng lớn yêu cầu.

### 7.3. Các phần mềm độc hại
Không thể phát hiện và ngăn chặn phần mềm độc hại phức tạp.

### 7.4. Cấu hình tường lửa kém, thiếu cập nhật
Dễ bị khai thác do các cấu hình yếu hoặc không được cập nhật.
