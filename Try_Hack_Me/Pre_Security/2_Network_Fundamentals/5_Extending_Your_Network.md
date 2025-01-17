# Extending Your Network

## Mục Lục

1. [Task 1: Introduction to Port Forwarding](#task-1-introduction-to-port-forwarding)  
2. [Task 2: Firewalls 101](#task-2-firewalls-101)  
3. [Task 3: Practical — Firewall](#task-3-practical--firewall)  
4. [Task 4: VPN Basics](#task-4-vpn-basics)  
5. [Task 5: LAN Networking Devices](#task-5-lan-networking-devices)  
6. [Task 6: Practical — Network Simulator](#task-6-practical--network-simulator)

## nội dung

# Task 1: Introduction to Port Forwarding

**Chuyển tiếp cổng (Port Forwarding)** là một thành phần hữu ích được sử dụng để kết nối các ứng dụng và dịch vụ với internet.  

Ví dụ, một máy chủ có địa chỉ IP **“192.168.1.10*.*”** chạy dịch vụ trên cổng **80**, cùng với hai máy tính được kết nối với nó (mạng nội bộ - intranet). Quản trị viên muốn làm cho nội dung trên máy chủ này hiển thị công khai cho mọi người. Vì vậy, anh ấy sử dụng khái niệm **chuyển tiếp cổng (port forwarding)** để nội dung này có thể được truy cập từ internet.

![Chuyển tiếp cổng](./img/5_Extending_Your_Network/1.1.png)

Nếu quản trị viên muốn trang web có thể được truy cập công khai (sử dụng Internet), họ sẽ phải triển khai **chuyển tiếp cổng (port forwarding)**, như trong sơ đồ bên dưới:

![Chuyển tiếp cổng](./img/5_Extending_Your_Network/1.2.png)

Với thiết kế này, **Mạng #2** bây giờ sẽ có thể truy cập vào máy chủ web đang chạy trên **Mạng #1** bằng cách sử dụng địa chỉ IP công khai của **Mạng #1** (**82.62.51.70**).

Rất dễ nhầm lẫn giữa **chuyển tiếp cổng (port forwarding)** với hành vi của **tường lửa (firewall)** (một công nghệ mà chúng ta sẽ thảo luận trong nhiệm vụ sau). Tuy nhiên, ở giai đoạn này, chỉ cần hiểu rằng chuyển tiếp cổng mở các cổng cụ thể (hãy nhớ cách các gói tin hoạt động). Ngược lại, **tường lửa** xác định xem lưu lượng truy cập có thể đi qua các cổng này hay không (ngay cả khi các cổng này đã được mở bằng cách chuyển tiếp cổng).

**Chuyển tiếp cổng** được cấu hình tại **router** của mạng.

**Câu hỏi:**  

Tên của thiết bị được sử dụng để cấu hình **chuyển tiếp cổng** là gì?  

<details>  
  <summary>Hiển thị đáp án</summary>  
  Đáp án: router  
</details>  
