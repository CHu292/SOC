# Defensive Security Intro

**Giới thiệu về An ninh Phòng thủ**  

> Giới thiệu về an ninh phòng thủ và các chủ đề liên quan như: **Tình báo mối đe dọa (Threat Intelligence)**, **Trung tâm Điều hành An ninh (SOC)**, **Phân tích và Ứng phó Sự cố Kỹ thuật số (DFIR)**, **Phân tích phần mềm độc hại (Malware Analysis)**, và **Hệ thống Quản lý Sự kiện và Thông tin Bảo mật (SIEM)**.

### Mục Lục

1. [Task 1: Introduction to Defensive Security](#task-1-introduction-to-defensive-security)

2. [Task 2: Areas of Defensive Security](#task-2-areas-of-defensive-security)

3. [Task 3: Practical Example of Defensive Security](#task-3-practical-example-of-defensive-security)

### Nội dung

# Task 1: Introduction to Defensive Security

**Giới thiệu về An ninh Phòng thủ**  

Trong phòng học trước, chúng ta đã tìm hiểu về **an ninh tấn công** (offensive security), với mục tiêu xác định và khai thác các lỗ hổng hệ thống nhằm tăng cường các biện pháp bảo mật. Điều này bao gồm khai thác lỗi phần mềm, lợi dụng các cài đặt không an toàn, và tận dụng chính sách kiểm soát truy cập không được thực thi, cùng với các chiến lược khác. **Đội Red Team** và các chuyên gia kiểm tra xâm nhập (penetration testers) chuyên về những kỹ thuật tấn công này.  

Trong phòng học này, chúng ta sẽ khám phá đối trọng của nó, **an ninh phòng thủ** (defensive security). Nó tập trung vào hai nhiệm vụ chính:  

1. **Ngăn chặn các hành vi xâm nhập trước khi chúng xảy ra.**  
2. **Phát hiện các hành vi xâm nhập khi chúng xảy ra và phản hồi một cách thích hợp.**  

**Blue Team** (Đội Xanh) là một phần quan trọng của lĩnh vực an ninh phòng thủ.  

---

### **Một số nhiệm vụ liên quan đến an ninh phòng thủ bao gồm:**  

- **Nâng cao nhận thức về an ninh mạng cho người dùng:** Đào tạo người dùng về an ninh mạng giúp bảo vệ chống lại các cuộc tấn công nhắm vào hệ thống của họ.  
- **Lập tài liệu và quản lý tài sản:** Chúng ta cần biết các hệ thống và thiết bị nào cần quản lý và bảo vệ một cách phù hợp.  
- **Cập nhật và vá lỗi hệ thống:** Đảm bảo rằng máy tính, máy chủ, và các thiết bị mạng được cập nhật và vá lỗi đúng cách để chống lại bất kỳ lỗ hổng nào đã biết.  
- **Cài đặt các thiết bị bảo mật phòng ngừa:** Tường lửa (firewall) và hệ thống ngăn chặn xâm nhập (IPS) là các thành phần quan trọng của bảo mật phòng ngừa. Tường lửa kiểm soát lưu lượng mạng nào có thể đi vào và ra khỏi hệ thống hoặc mạng. **IPS** chặn bất kỳ lưu lượng mạng nào khớp với các quy tắc và chữ ký tấn công đã được định sẵn.  
- **Cài đặt các thiết bị ghi log và giám sát:** Việc ghi nhật ký và giám sát mạng đúng cách là điều cần thiết để phát hiện các hoạt động độc hại và hành vi xâm nhập. Nếu một thiết bị trái phép xuất hiện trên mạng của chúng ta, chúng ta cần có khả năng phát hiện ra nó.  

---

### **Ngoài ra, chúng ta sẽ tìm hiểu các chủ đề liên quan sau:**  

- **Trung tâm Điều hành An ninh (SOC)**  
- **Tình báo mối đe dọa (Threat Intelligence)**  
- **Phân tích pháp y số và ứng phó sự cố (DFIR)**  
- **Phân tích phần mềm độc hại (Malware Analysis)**

Trả lời các câu hỏi dưới đây:  
**Đội nào tập trung vào an ninh phòng thủ?**

<details>
  <summary>Hiển thị đáp án</summary>
  Đáp án: Blue Team
</details>

# Task 2: Areas of Defensive Security

