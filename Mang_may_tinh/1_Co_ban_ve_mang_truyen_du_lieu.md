## Mục lục

# Phần I: Cơ bản về mạng truyền dữ liệu
- [Chương 1: Sự phát triển của mạng máy tính](#chuong-1-su-phat-trien-cua-mang-may-tinh)
- [Chương 2: Các nguyên tắc chung trong xây dựng mạng](#chuong-2-cac-nguyen-tac-chung-trong-xay-dung-mang)
- [Chương 3: Chuyển mạch kênh và chuyển mạch gói](#chuong-3-chuyen-mach-kenh-va-chuyen-mach-goi)
- [Chương 4: Chuẩn hóa và phân loại mạng](#chuong-4-chuan-hoa-va-phan-loai-mang)
- [Chương 5: Các đặc tính mạng và chất lượng dịch vụ](#chuong-5-cac-dac-tinh-mang-va-chat-luong-dich-vu)
- [Câu hỏi cho Phần I](#cau-hoi-cho-phan-i)

## Nội dung

# Phần I: Cơ bản về mạng truyền dữ liệu

<h2 id="chuong-1-su-phat-trien-cua-mang-may-tinh">CHƯƠNG 1: Sự phát triển của mạng máy tính</h2>

### 1.1 Hai nguồn gốc của mạng máy tính
 
- **Mạng máy tính** là kết quả phát triển từ hai ngành quan trọng: **kỹ thuật tính toán (computing technology)** và **viễn thông (telecommunications technology)**.  
- Chúng có hai vai trò chính:  
  1. **Hệ thống máy tính liên kết (interconnected computer system)** giúp trao đổi dữ liệu và thực hiện các nhiệm vụ tự động.  
  2. **Phương tiện truyền thông tin (information transmission medium)** giúp mã hóa, truyền và xử lý dữ liệu trong các hệ thống viễn thông như mạng điện thoại.

![Nguồn gốc của mạng máy tính](./img/1.1.png)

Hình 1.1. Sự tiến hóa của mạng máy tính tại giao điểm của công nghệ tính toán và công nghệ viễn thông.

### 1.2 Những mạng máy tính đầu tiên

#### 1.2.1 Hệ thống xử lý theo lô

- **Hệ thống xử lý theo lô (batch processing systems)** dựa trên **máy tính lớn (mainframe)**, nơi người dùng chuẩn bị **thẻ đục lỗ (punched cards)** chứa dữ liệu và chương trình, sau đó gửi vào trung tâm tính toán (computing center).  
- Tác vụ của nhiều người dùng được nhóm thành **gói (batch)** và xử lý tuần tự, tối ưu hóa việc sử dụng bộ xử lý .  
- Người dùng nhận kết quả sau một chu kỳ xử lý, gây độ trễ cao.  
- Chế độ tương tác chưa phổ biến do ưu tiên hiệu suất bộ xử lý hơn trải nghiệm người dùng.

![Hệ thống xử lý theo lô](./img/1.2.png)

Hình 1.2. Hệ thống tập trung dựa trên máy tính trung tâm (mainframe).

#### 1.2.2 Hệ thống đa thiết bị đầu cuối — hình mẫu của mạng

- **Hệ thống đa thiết bị đầu cuối (multi-terminal systems)** với **chế độ chia sẻ thời gian (time-sharing mode)** cho phép mỗi người dùng có phiên làm việc riêng, giúp tương tác trực tiếp với mainframe.  
- Bộ xử lý phân chia tài nguyên theo thời gian, đảm bảo người dùng không nhận thấy độ trễ do chia sẻ hệ thống.  
- **Thiết bị đầu cuối (terminals)** mở rộng ra ngoài trung tâm tính toán, phân tán trong doanh nghiệp, trong khi khả năng tính toán vẫn tập trung.  
- Một số chức năng như **nhập/xuất dữ liệu (data input/output)** trở thành **hệ thống phân tán (distributed system)**.  
- Người dùng có thể  truy cập file và chạy chương trình từ bất kỳ thiết bị nào mà không cần thiết bị lưu trữ cá nhân.  
- Hệ thống này trở thành tiền đề cho **mạng máy tính cục bộ (local computer networks - LANs)**.

![Hệ thống đa thiết bị đầu cuối — hình mẫu của mạng](./img/1.3.png)

Hình 1.3. Hệ thống đa thiết bị đầu cuối — hình mẫu của mạng tính toán

#### 1.2.3 Những mạng toàn cầu đầu tiên

- **Mạng diện rộng hay còn gọi là mạng toàn cầu (Wide Area Network - WAN)** kết nối các máy tính phân tán về mặt địa lý, ban đầu thông qua mạng điện thoại và **modem**.  
- Hệ thống phát triển từ **kết nối thiết bị đầu cuối - máy tính (terminal-computer)** sang **kết nối máy tính - máy tính (computer-computer)**, cho phép trao đổi dữ liệu tự động.  
- Các dịch vụ ban đầu bao gồm chia sẻ tệp tin, **đồng bộ hóa cơ sở dữ liệu (database synchronization)** và **thư điện tử (email)**.  
- Giao thức mạng phát triển với mô hình truyền gói tin thay thế **chuyển mạch kênh (circuit switching)**, giúp tối ưu băng thông và giảm chi phí.  
- Ban đầu, **kênh truyền (communication channels)** có tốc độ thấp (~kbit/s), chủ yếu hỗ trợ truyền file và email, nhưng dần nâng cấp với các tiêu chuẩn như **X.25** vào thập niên 1970.  
- **ARPANET**, phát triển bởi Bộ Quốc phòng Mỹ năm 1969, là tiền thân của **Internet**, áp dụng **hệ điều hành mạng (network operating systems)** để quản lý tài nguyên phân tán và **giao thức truyền thông (communication protocols)**.  
- **Số hóa thoại (digital voice transmission)** trong mạng điện thoại thúc đẩy sự phát triển của **mạng số tốc độ cao (high-speed digital networks)**, giúp **mạng WAN** đạt chất lượng dịch vụ ngang tầm **mạng LAN**.