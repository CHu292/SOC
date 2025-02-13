### Kiến thức cơ bản về **tcpdump**:
**tcpdump** là một công cụ dòng lệnh dùng để bắt gói tin trên mạng, giúp phân tích và chẩn đoán lưu lượng mạng.

## 1. **Cài đặt tcpdump**
- **Ubuntu/Debian:**  
  ```bash
  sudo apt install tcpdump
  ```
- **CentOS/RHEL:**  
  ```bash
  sudo yum install tcpdump
  ```
- **macOS (Homebrew):**  
  ```bash
  brew install tcpdump
  ```

---

## 2. **Các lệnh cơ bản**
- **Kiểm tra danh sách giao diện mạng**  
  ```bash
  tcpdump -D
  ```

  ![kiểm tra danh sách giao diện mạng](./img/1.png)

- **Bắt gói tin trên một giao diện**  
  ```bash
  sudo tcpdump -i eth0
  ```
  (Thay `eth0` bằng giao diện mạng của bạn)

- **Lưu gói tin vào file để phân tích sau**  
  ```bash
  sudo tcpdump -i eth0 -w file.pcap
  ```
![Lưu gói tin](./img/2.png)

  Đọc lại file đã lưu:
  ```bash
  tcpdump -r file.pcap
  ```

---

## 3. **Lọc gói tin**
### a) **Lọc theo địa chỉ IP**
- Bắt gói tin từ hoặc đến một IP:
  ```bash
  tcpdump -i eth0 host 192.168.1.1
  ```
- Chỉ bắt gói tin đi từ một IP:
  ```bash
  tcpdump -i eth0 src host 192.168.1.1
  ```
- Chỉ bắt gói tin đến một IP:
  ```bash
  tcpdump -i eth0 dst host 192.168.1.1
  ```

### b) **Lọc theo giao thức**
- Bắt gói tin TCP:
  ```bash
  tcpdump -i eth0 tcp
  ```
- Bắt gói tin UDP:
  ```bash
  tcpdump -i eth0 udp
  ```
- Bắt gói tin ICMP (ping):
  ```bash
  tcpdump -i eth0 icmp
  ```

### c) **Lọc theo cổng**
- Bắt gói tin HTTP (cổng 80):
  ```bash
  tcpdump -i eth0 port 80
  ```
- Bắt gói tin SSH (cổng 22):
  ```bash
  tcpdump -i eth0 port 22
  ```
- Bắt gói tin từ hoặc đến nhiều cổng:
  ```bash
  tcpdump -i eth0 port 22 or port 443
  ```

### d) **Lọc theo mạng**
- Bắt gói tin từ mạng 192.168.1.0/24:
  ```bash
  tcpdump -i eth0 net 192.168.1.0/24
  ```

---

## 4. **Hiển thị thông tin gói tin chi tiết**
- Hiển thị chi tiết tiêu đề gói tin:
  ```bash
  tcpdump -i eth0 -v
  ```
- Hiển thị rất chi tiết:
  ```bash
  tcpdump -i eth0 -vv
  ```
- Hiển thị cả dữ liệu thô của gói tin:
  ```bash
  tcpdump -i eth0 -X
  ```
- Hiển thị dữ liệu dạng hex và ASCII:
  ```bash
  tcpdump -i eth0 -XX
  ```

---

## 5. **Kết hợp nhiều bộ lọc**
- Bắt gói tin TCP từ 192.168.1.1 đến cổng 80:
  ```bash
  tcpdump -i eth0 tcp and src host 192.168.1.1 and port 80
  ```
- Bắt tất cả gói tin ngoại trừ SSH:
  ```bash
  tcpdump -i eth0 not port 22
  ```

---

## 6. **Một số tùy chọn hữu ích**
- **Giới hạn số lượng gói tin bắt được** (ví dụ: 10 gói):
  ```bash
  tcpdump -i eth0 -c 10
  ```
- **Giới hạn kích thước gói tin được bắt** (chỉ lấy 100 byte đầu mỗi gói):
  ```bash
  tcpdump -i eth0 -s 100
  ```
- **Bắt gói tin nhưng không phân giải tên miền** (giảm tải hệ thống):
  ```bash
  tcpdump -i eth0 -n
  ```
- **Bắt gói tin và hiển thị thời gian đầy đủ**:
  ```bash
  tcpdump -i eth0 -tttt
  ```

---

## 7. **Phân tích file .pcap bằng Wireshark**
File `.pcap` có thể mở bằng **Wireshark** để phân tích trực quan hơn.

Cài Wireshark:
```bash
sudo apt install wireshark
```
Mở file `.pcap`:
```bash
wireshark file.pcap
```

---

## 8. **Ví dụ thực tế**
### a) **Giám sát lưu lượng HTTP**
```bash
sudo tcpdump -i eth0 port 80 -A
```
(Xem nội dung HTTP dưới dạng ASCII)

### b) **Phát hiện cuộc tấn công ping flood**
```bash
sudo tcpdump -i eth0 icmp
```

### c) **Kiểm tra lưu lượng SSH**
```bash
sudo tcpdump -i eth0 port 22
```

---

## **Tóm tắt nhanh**
| Lệnh | Chức năng |
|------|----------|
| `tcpdump -i eth0` | Bắt tất cả gói tin trên `eth0` |
| `tcpdump -D` | Liệt kê các giao diện mạng |
| `tcpdump -i eth0 port 80` | Bắt gói tin HTTP |
| `tcpdump -i eth0 host 192.168.1.1` | Bắt gói tin từ/đến IP 192.168.1.1 |
| `tcpdump -i eth0 -w file.pcap` | Lưu gói tin vào file |
| `tcpdump -r file.pcap` | Đọc file gói tin |
| `tcpdump -i eth0 -n` | Không phân giải tên miền |
| `tcpdump -i eth0 -X` | Hiển thị dữ liệu thô của gói tin |

---

Với các kiến thức trên, bạn có thể sử dụng **tcpdump** để chẩn đoán mạng, phát hiện tấn công, kiểm tra kết nối và phân tích lưu lượng hiệu quả! 🚀