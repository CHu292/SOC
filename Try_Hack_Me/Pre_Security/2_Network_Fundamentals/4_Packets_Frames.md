# Packets & Frames

> Hiểu cách dữ liệu được chia thành các phần nhỏ hơn và truyền qua mạng đến một thiết bị khác.

## Mục Lục

1. [Task 1: What are Packets and Frames](#task-1-what-are-packets-and-frames)
2. [Task 2: TCP/IP (The Three-Way Handshake)](#task-2-tcp-ip-the-three-way-handshake)
3. [Task 3: Practical - Handshake](#task-3-practical-handshake)
4. [Task 4: UDP/IP](#task-4-udp-ip)
5. [Task 5: Ports 101 (Practical)](#task-5-ports-101-practical)

## Nội dung

# Task 1: What are Packets and Frames

Gói tin (**packets**) và khung (**frames**) là những phần nhỏ của dữ liệu, khi kết hợp lại sẽ tạo thành một mảnh thông tin hoặc thông điệp lớn hơn. Tuy nhiên, chúng là hai khái niệm khác nhau trong mô hình OSI. Một **khung** nằm ở lớp 2 — lớp liên kết dữ liệu (**data link layer**), nghĩa là không có thông tin như địa chỉ IP. Hãy nghĩ về điều này như việc đặt một phong bì bên trong một phong bì khác và gửi đi. Phong bì đầu tiên sẽ là gói tin mà bạn gửi đi, nhưng khi nó được mở ra, phong bì bên trong vẫn tồn tại và chứa dữ liệu (đây chính là khung).

Quá trình này được gọi là **encapsulation** (đóng gói), mà chúng ta đã thảo luận trong **Phòng 3: Mô hình OSI**. Tại giai đoạn này, chúng ta có thể giả định rằng bất kỳ khi nào đề cập đến địa chỉ IP, chúng ta đang nói về **gói tin**. Khi thông tin đóng gói được loại bỏ, chúng ta đang nói đến chính **khung**.

**Gói tin** là một cách hiệu quả để truyền dữ liệu giữa các thiết bị mạng, như đã giải thích trong Nhiệm vụ 1. Vì dữ liệu được trao đổi dưới dạng các phần nhỏ, khả năng xảy ra **tắc nghẽn mạng** sẽ ít hơn so với việc gửi các thông điệp lớn cùng một lúc.

Ví dụ, khi tải một hình ảnh từ một trang web, hình ảnh này không được gửi đến máy tính của bạn dưới dạng một khối lớn mà được chia thành các phần nhỏ hơn, sau đó được tái cấu trúc trên máy tính của bạn. Hãy xem hình ảnh dưới đây như một minh họa cho quá trình này. Hình ảnh con chó được chia thành ba gói tin, sau đó được tái tạo lại trên máy tính để tạo thành hình ảnh cuối cùng.

![4 giai đoạn ứng phó sự cố](./img/4_Packets_Frames/1.1.png)

**Gói tin có các cấu trúc khác nhau tùy thuộc vào loại gói tin được gửi.** Như chúng ta sẽ thảo luận tiếp, mạng máy tính đầy rẫy các tiêu chuẩn và giao thức hoạt động như một tập hợp các quy tắc để xử lý gói tin trên một thiết bị. Với việc Internet được dự đoán sẽ có khoảng **50 tỷ thiết bị kết nối vào cuối năm 2020**, mọi thứ sẽ nhanh chóng trở nên hỗn loạn nếu không có sự chuẩn hóa.

Hãy tiếp tục với ví dụ về **Giao thức Internet (Internet Protocol - IP)**. Một gói tin sử dụng giao thức này sẽ có một tập hợp các **header** chứa thông tin bổ sung cho dữ liệu được gửi qua mạng.

Một số header đáng chú ý bao gồm: 

| **Header**             | **Mô tả**                                                                                             |
|-------------------------|-------------------------------------------------------------------------------------------------------|
| **Time to Live**        | Trường này đặt bộ đếm thời gian hết hạn cho gói tin để tránh làm tắc nghẽn mạng nếu gói tin không thể đến đích hoặc thoát khỏi mạng. |
| **Checksum**            | Trường này cung cấp cơ chế kiểm tra tính toàn vẹn cho các giao thức như TCP/IP. Nếu dữ liệu bị thay đổi, giá trị này sẽ khác với giá trị mong đợi và do đó gói tin bị hỏng. |
| **Source Address**      | Địa chỉ IP của thiết bị mà gói tin được gửi đi, để dữ liệu biết nơi cần quay lại.                     |
| **Destination Address** | Địa chỉ IP của thiết bị mà gói tin được gửi đến, để dữ liệu biết điểm đến tiếp theo.                  |

**Câu hỏi:**  

**1. Tên của một phần dữ liệu khi nó có thông tin địa chỉ IP là gì?**  

<details>  
  <summary>Hiển thị đáp án</summary>  
  Đáp án: Packet  
</details>  

**2. Tên của một phần dữ liệu khi nó không có thông tin địa chỉ IP là gì?**  

<details>  
  <summary>Hiển thị đáp án</summary>  
  Đáp án: Frame  
</details>  
