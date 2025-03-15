**2. Chuẩn bị triển khai và tải xuống image VM**  

### **1. Cần tải xuống và cài đặt hypervisor từ VMware**  
(Phần mềm để chạy máy ảo)  

Phần mềm **VirtualBox** có hỗ trợ hạn chế đối với ảo hóa lồng nhau (**Host nested virtualization**). Một số ảnh máy ảo có thể không khởi động hoặc chạy rất chậm.  

---

### **2. Có thể tải xuống từ các liên kết sau:**  

**VMware Workstation** (yêu cầu bản quyền):  
- **Dành cho Windows:** [Tải xuống](https://www.vmware.com/go/getworkstation-win)  
- **Dành cho MacOS:** [Tải xuống](https://www.vmware.com/go/getfusion)  
- **Dành cho Linux:** [Tải xuống](https://www.vmware.com/go/getworkstation-linux)  

**VMware Player** *(miễn phí)*:  
- [Tải xuống](https://www.vmware.com/products/workstation-player/workstation-player-evaluation.html)  

---

### ⚠ **CÀI ĐẶT VMware Workstation vào thư mục mặc định!!!**  

Có nhiều trường hợp cài đặt VMware vào thư mục khác với mặc định dẫn đến lỗi với **các bộ điều hợp mạng ảo** *(driver của giao diện mạng ảo không thể cài đặt được)*.  
Việc **cài lại VMware vào thư mục mặc định thường không giải quyết được lỗi** này.  

---

### **Nhập image máy ảo PNET-Lab**  

Nếu bạn đã tải xuống phiên bản có thể nhập trực tiếp, bạn có thể **import vào bất kỳ thư mục nào** *(đảm bảo rằng không có ký tự tiếng Nga trong đường dẫn)*.  

Phiên bản yêu cầu cài đặt có thể **không hoạt động ngay lập tức**, **chỉ hoạt động trên VMware Workstation 16 Pro**.

**3. Tải xuống image PNET-Lab**  

Cần tải xuống tất cả các tệp và đặt chúng vào đường dẫn khuyến nghị:  

```
X:/VM/pnet/
```
*(Trong đó **X** là ổ cứng HDD có dung lượng lớn nhất hoặc ổ SSD có dung lượng lớn.)*  

---

### **a) Phiên bản (PNET-LAB 5.5.18)**  

- **Dành cho khóa học mạng (học kỳ 1)**  
- **Dành cho MIRЭA** *(4.83 GB)*  
- **Ngày phát hành:** **Tháng 10/2023**  
- **Tải xuống:** [MAIL-CLOUD](https://cloud.mail.ru/public/Adh2/VdGF6h746)  

---

### ⚠ **QUAN TRỌNG!!! Khi đăng nhập lần đầu, phải chọn "Offline login"**  

- **Đăng nhập SSH:**  
  - **user:** `root`  
  - **password:** `eve`  

- **Đăng nhập web:**  
  - **user:** `admin`  
  - **password:** `pnet`  

---

### **Các ảnh máy ảo đi kèm trong bộ cài đặt:**  
- **Cisco IOL** L2, L3  
- **Mikrotik** v6.39, v6.49.1, v7.11.3  
- **Linux Debian 11 Server**  

### **b) Phiên bản phổ quát (PNET-LAB 4.2.10)**  

- **Dành cho khóa học mạng (học kỳ 1,2):**  
  - **Pentest, Bảo mật hệ thống thông tin (СЗИ), PT-START, PT-PROFF**  
  - **Dung lượng:** 31.3 GB  
  - **Ngày phát hành:** **Tháng 11/2022**  

- **Tải xuống:**  
  - [GOOGLE-CLOUD]  
  - [MAIL-CLOUD](https://cloud.mail.ru/public/Adi9/rYjFGSTHY)  
  - [MIREA-CLOUD]  

📌 Cần tải xuống, sau đó **import vào VMware**, chỉ định đường dẫn để nhập và khởi động.  

💾 **Yêu cầu dung lượng trống trên ổ cứng từ 80GB**  

---

### **c) Phiên bản "PT-START" (PNET-LAB 6.0.100)**  

- **Dành cho module "PT-START" của Positive Technologies**  
  - **Dung lượng:** 31.6 GB  
  - **Ngày phát hành:** **Tháng 9/2023**  
  - **Tải xuống:** [MAIL-CLOUD](https://cloud.mail.ru/public/rTHq/hvch6G6aa)  

📌 **Thông tin đăng nhập:**  
- **SSH:** `root/eve`  
- **Web:** `admin/pnet`  

⚠ **QUAN TRỌNG!!! Khi đăng nhập lần đầu, phải chọn "Offline login"**  

📌 **Hướng dẫn cài đặt:**  
- Tải xuống, sau đó **import vào VMware**, chỉ định đường dẫn để nhập và khởi động.

### **d) Phiên bản "PT-PROFF" (PNET-LAB 6.0.100)**  

- **Dành cho module "PT-PROFF" của Positive Technologies**  
  - **Ngày phát hành:** **Dự kiến tháng 11/2023**  

📌 **Hướng dẫn cài đặt:**  
- Tải xuống, sau đó **import vào VMware**, chỉ định đường dẫn để nhập và khởi động.  

---

### **PS: Nếu muốn tùy chỉnh, bạn có thể tự tạo hệ thống PNET-Lab**  

#### **1*. Tải xuống ảnh máy ảo sạch của PNET-LAB (phiên bản thay thế EVE-NG có phí)**  
- **Ảnh VM cho VMware (2GB):** [Tải xuống](https://cloud.mirea.tech/index.php/s/qk5mtPr2CLixTc5)  
- Hoặc tự cài đặt phiên bản beta bằng cách:  
  - **Cài đặt Ubuntu Server 20.04**  

#### **2*. Ảnh hệ thống cho EVE-NG và PNET-LAB**  
- **Ảnh VM cho EVE-NG và PNET-LAB:** [Tải xuống](https://cloud.mirea.tech/index.php/s/m647QEq7Y92cjYD)  
- Hoặc tải từ nguồn gốc:  
  - **[UNETLAB CLOUD](https://ww7.unetlab.cloud/?usid=20&utid=15261101820)**  

---

### **PS: Dự phòng – Phiên bản cũ của EVE-NG**  

📌 **Tải xuống ảnh máy ảo EVE-NG**  
- **Ảnh VM cho VMware (30GB):** [YandexDisk](https://disk.yandex.ru/d/b2cbPc_LXcU_EQ)  

📌 **Yêu cầu hệ thống:**  
- Cần ít nhất **70GB dung lượng trống** trên ổ cứng.  
- Sau khi import có thể xóa ảnh gốc để tiết kiệm dung lượng.