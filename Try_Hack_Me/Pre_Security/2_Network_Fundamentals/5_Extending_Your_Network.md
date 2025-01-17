# Extending Your Network

> Tìm hiểu về một số công nghệ được sử dụng để mở rộng mạng ra Internet và các động cơ đằng sau việc này.

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

Ví dụ, một máy chủ có địa chỉ IP **“192.168.1.10”** chạy dịch vụ trên cổng **80**, cùng với hai máy tính được kết nối với nó (mạng nội bộ - intranet). Quản trị viên muốn làm cho nội dung trên máy chủ này hiển thị công khai cho mọi người. Vì vậy, anh ấy sử dụng khái niệm **chuyển tiếp cổng (port forwarding)** để nội dung này có thể được truy cập từ internet.

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

# Task 2: Firewalls 101

**Tường lửa (Firewall)** là một thiết bị trong mạng chịu trách nhiệm xác định loại lưu lượng nào được phép ra vào mạng. Hãy nghĩ về tường lửa như một lớp bảo vệ biên giới cho mạng. Quản trị viên có thể cấu hình tường lửa để **cho phép (permit)** hoặc **từ chối (deny)** lưu lượng truy cập vào hoặc ra khỏi mạng dựa trên nhiều yếu tố như:

- **Lưu lượng đến từ đâu?** (Tường lửa đã được cấu hình để chấp nhận/từ chối lưu lượng từ một mạng cụ thể chưa?)  
- **Lưu lượng đi đến đâu?** (Tường lửa đã được cấu hình để chấp nhận/từ chối lưu lượng đến một mạng cụ thể chưa?)  
- **Lưu lượng truy cập đến cổng nào?** (Tường lửa đã được cấu hình để chấp nhận/từ chối lưu lượng đến cổng 80 chưa?)  
- **Lưu lượng sử dụng giao thức nào?** (Tường lửa đã được cấu hình để chấp nhận/từ chối lưu lượng sử dụng giao thức **UDP**, **TCP** hay cả hai chưa?)  

Tường lửa thực hiện kiểm tra gói tin (**packet inspection**) để trả lời các câu hỏi trên.

**Tường lửa** có nhiều kích thước và hình dạng khác nhau. Từ các thiết bị phần cứng chuyên dụng (thường được tìm thấy trong các mạng lớn như doanh nghiệp) có thể xử lý lượng dữ liệu khổng lồ, đến các bộ định tuyến dân dụng (như tại nhà bạn!) hoặc phần mềm như **Snort**, tường lửa có thể được phân loại thành **2 đến 5 loại**.

Chúng ta sẽ khám phá **hai loại chính** của tường lửa trong bảng dưới đây:

| **Loại tường lửa** | **Mô tả**                                                                                                                                       |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| **Stateful**        | Loại tường lửa này sử dụng toàn bộ thông tin từ một kết nối; thay vì kiểm tra từng gói tin riêng lẻ, tường lửa này xác định hành vi của một thiết bị dựa trên toàn bộ kết nối. <br><br> Loại tường lửa này tiêu thụ nhiều tài nguyên hơn so với tường lửa không trạng thái vì quá trình ra quyết định là động. Ví dụ: một tường lửa có thể cho phép các phần đầu tiên của quá trình bắt tay TCP, nhưng sau đó phát hiện và chặn nếu kết nối thất bại. <br><br>  Nếu một kết nối từ một host là xấu, nó sẽ chặn toàn bộ thiết bị. |
| **Stateless**       | Loại tường lửa này sử dụng một tập hợp quy tắc tĩnh để xác định liệu các gói tin riêng lẻ (individual packets) có được chấp nhận hay không. Ví dụ: một thiết bị gửi một gói tin xấu sẽ không đồng nghĩa với việc toàn bộ thiết bị đó bị chặn. <br><br> Mặc dù các tường lửa này sử dụng ít tài nguyên hơn so với các lựa chọn khác, nhưng chúng kém thông minh hơn. Ví dụ: các tường lửa này chỉ hiệu quả nếu các quy tắc được định nghĩa chính xác. Nếu quy tắc không khớp chính xác, tường lửa sẽ không hoạt động hiệu quả. <br><br> Tuy nhiên, các tường lửa này rất hiệu quả khi xử lý lượng lớn lưu lượng từ một tập hợp các host (chẳng hạn như trong một cuộc tấn công từ chối dịch vụ phân tán - DDoS).|

**Câu hỏi :**  

1. Tường lửa hoạt động ở những lớp nào trong mô hình OSI?
   
<details>  
  <summary>Hiển thị đáp án</summary>  
  Đáp án: Layer 3, Layer 4  
</details>  

2. Loại tường lửa nào kiểm tra toàn bộ kết nối?  

<details>  
  <summary>Hiển thị đáp án</summary>  
  Đáp án: stateful  
</details>  

3. Loại tường lửa nào kiểm tra từng gói tin riêng lẻ?  

<details>  
  <summary>Hiển thị đáp án</summary>  
  Đáp án: stateless  
</details>  

# Task 3: Practical — Firewall

Trang web tại 203.0.110.1 đang bị tấn công! Hãy nhanh chóng thêm một số quy tắc tường lửa để ngăn máy chủ bị sập!

Các gói tin màu đỏ đến từ máy của kẻ tấn công!

![thực hành](./img/5_Extending_Your_Network/3.1.png)

![thực hành](./img/5_Extending_Your_Network/3.2.png)

Lựa chọn cổng 80 vì cổng này dành cho HyperText Transfer Protocol (HTTP).

![thực hành](./img/5_Extending_Your_Network/3.3.png)

![thực hành](./img/5_Extending_Your_Network/3.4.png)

# Task 4: VPN Basics

**Mạng riêng ảo (VPN)**  

**VPN** (viết tắt của Virtual Private Network) là một công nghệ cho phép các thiết bị trên các mạng riêng biệt giao tiếp an toàn bằng cách tạo ra một đường dẫn chuyên dụng giữa các thiết bị này qua Internet (được gọi là một "đường hầm"). Các thiết bị được kết nối trong đường hầm này sẽ tạo thành mạng riêng của chính chúng.  

Ví dụ, chỉ các thiết bị trong cùng một mạng (chẳng hạn như trong một doanh nghiệp) mới có thể giao tiếp trực tiếp với nhau. Tuy nhiên, **VPN** cho phép hai văn phòng được kết nối với nhau. Hãy xem sơ đồ bên dưới, nơi có ba mạng riêng biệt:  

![VPN](./img/5_Extending_Your_Network/4.1.png)

Các thiết bị kết nối trên **Mạng #3** vẫn là một phần của **Mạng #1** và **Mạng #2**, nhưng đồng thời cũng tạo thành một mạng riêng (**Mạng #3**) mà chỉ các thiết bị được kết nối qua **VPN** này mới có thể giao tiếp với nhau.

Hãy cùng khám phá một số lợi ích khác mà **VPN** mang lại trong bảng dưới đây:

| **Lợi ích**                                             | **Mô tả**                                                                                                                                                                                                                   |
|---------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Kết nối các mạng ở các địa điểm địa lý khác nhau.**   | Ví dụ, một doanh nghiệp có nhiều văn phòng sẽ thấy VPN hữu ích vì nó cho phép truy cập tài nguyên như máy chủ/hạ tầng từ một văn phòng khác.                                                                                |
| **Cung cấp quyền riêng tư.**                            | Công nghệ VPN sử dụng mã hóa để bảo vệ dữ liệu. Điều này đảm bảo rằng dữ liệu chỉ có thể được hiểu bởi các thiết bị gửi và nhận, tránh bị đánh cắp dữ liệu (**sniffing**). <br> Mã hóa này hữu ích trong các mạng WiFi công cộng không cung cấp bảo mật. |
| **Cung cấp tính ẩn danh.**                              | Các nhà báo và nhà hoạt động dựa vào VPN để báo cáo các vấn đề toàn cầu tại những quốc gia kiểm soát quyền tự do ngôn luận. <br> Lưu lượng của bạn thường bị nhà cung cấp dịch vụ Internet (ISP) hoặc bên trung gian khác xem và theo dõi. <br> Mức độ ẩn danh VPN cung cấp phụ thuộc vào cách các thiết bị khác trên mạng tôn trọng quyền riêng tư. Ví dụ, một VPN ghi lại toàn bộ dữ liệu/lịch sử của bạn cũng tương đương với việc không sử dụng VPN trong khía cạnh này. |

**TryHackMe** sử dụng **VPN** để kết nối bạn với các máy dễ bị tấn công mà không làm cho chúng có thể truy cập trực tiếp trên Internet! Điều này có nghĩa là:  

- Bạn có thể tương tác an toàn với các máy của chúng tôi.  
- Các nhà cung cấp dịch vụ như **ISP** sẽ không nghĩ rằng bạn đang tấn công một máy khác trên Internet (điều này có thể vi phạm điều khoản dịch vụ).  
- **VPN** cung cấp bảo mật cho **TryHackMe** vì các máy dễ bị tấn công sẽ không thể truy cập qua Internet.  

Công nghệ VPN đã được cải tiến qua các năm. Hãy cùng khám phá một số công nghệ **VPN** hiện tại dưới đây:  

| **Công nghệ VPN** | **Mô tả**                                                                                                                                                                                                                 |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **PPP**           | Công nghệ này được sử dụng bởi **PPTP** (được giải thích bên dưới) để cho phép xác thực và cung cấp mã hóa dữ liệu. VPN hoạt động bằng cách sử dụng khóa riêng (**private key**) và chứng chỉ công khai (**public certificate**) (tương tự như **SSH**). Một khóa riêng và chứng chỉ phải khớp để bạn có thể kết nối. <br> <br> Công nghệ này không thể tự rời khỏi mạng (không định tuyến được). |
| **PPTP**          | **Point-to-Point Tunneling Protocol (PPTP)** là công nghệ cho phép dữ liệu từ PPP di chuyển và thoát khỏi mạng. <br> <br> PPTP rất dễ thiết lập và được hầu hết các thiết bị hỗ trợ. Tuy nhiên, nó được mã hóa yếu hơn so với các lựa chọn thay thế. |
| **IPSec**         | **Internet Protocol Security (IPSec)** mã hóa dữ liệu bằng cách sử dụng cấu trúc giao thức Internet (**IP**) hiện có. <br> <br> IPSec khó thiết lập hơn so với các lựa chọn khác; tuy nhiên, nếu thành công, nó cung cấp mã hóa mạnh mẽ và được hỗ trợ trên nhiều thiết bị. |

**PPP** là viết tắt của **Point-to-Point Protocol**, một giao thức được sử dụng để truyền dữ liệu giữa hai thiết bị trực tiếp kết nối với nhau.  

Trong bối cảnh VPN, **PPP** được sử dụng bởi các giao thức như **PPTP (Point-to-Point Tunneling Protocol)** để cung cấp **mã hóa** và **xác thực dữ liệu** trước khi dữ liệu được truyền qua mạng.  

PPP không phải là một công nghệ VPN độc lập mà là một giao thức cơ sở hỗ trợ các công nghệ VPN khác như PPTP.

**Câu hỏi:**  

1. Công nghệ VPN nào chỉ mã hóa và cung cấp xác thực dữ liệu?  

<details>  
  <summary>Hiển thị đáp án</summary>  
  Đáp án: PPP  
</details>  

2. Công nghệ VPN nào sử dụng cấu trúc giao thức IP?  

<details>  
  <summary>Hiển thị đáp án</summary>  
  Đáp án: IPSec  
</details>  
