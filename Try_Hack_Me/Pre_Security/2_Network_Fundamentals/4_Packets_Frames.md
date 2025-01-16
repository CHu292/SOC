# Packets & Frames

> Hiểu cách dữ liệu được chia thành các phần nhỏ hơn và truyền qua mạng đến một thiết bị khác.

## Mục Lục

1. [Task 1: What are Packets and Frames](#task-1-what-are-packets-and-frames)
2. [Task 2: TCP/IP (The Three-Way Handshake)](#task-2-tcpip-the-three-way-handshake)
3. [Task 3: Practical - Handshake](#task-3-practical---handshake)
4. [Task 4: UDP/IP](#task-4-udpip)
5. [Task 5: Ports 101 (Practical)](#task-5-ports-101-practical)


## Nội dung

# Task 1: What are Packets and Frames

Gói tin (**packets**) và khung (**frames**) là những phần nhỏ của dữ liệu, khi kết hợp lại sẽ tạo thành một mảnh thông tin hoặc thông điệp lớn hơn. Tuy nhiên, chúng là hai khái niệm khác nhau trong mô hình OSI. Một **khung** nằm ở lớp 2 — lớp liên kết dữ liệu (**data link layer**), nghĩa là không có thông tin như địa chỉ IP. Hãy nghĩ về điều này như việc đặt một phong bì bên trong một phong bì khác và gửi đi. Phong bì đầu tiên sẽ là gói tin mà bạn gửi đi, nhưng khi nó được mở ra, phong bì bên trong vẫn tồn tại và chứa dữ liệu (đây chính là khung).

Quá trình này được gọi là **encapsulation** (đóng gói), mà chúng ta đã thảo luận trong **Phòng 3: Mô hình OSI**. Tại giai đoạn này, chúng ta có thể giả định rằng bất kỳ khi nào đề cập đến địa chỉ IP, chúng ta đang nói về **gói tin**. Khi thông tin đóng gói được loại bỏ, chúng ta đang nói đến chính **khung**.

**Gói tin** là một cách hiệu quả để truyền dữ liệu giữa các thiết bị mạng, như đã giải thích trong Nhiệm vụ 1. Vì dữ liệu được trao đổi dưới dạng các phần nhỏ, khả năng xảy ra **tắc nghẽn mạng** sẽ ít hơn so với việc gửi các thông điệp lớn cùng một lúc.

Ví dụ, khi tải một hình ảnh từ một trang web, hình ảnh này không được gửi đến máy tính của bạn dưới dạng một khối lớn mà được chia thành các phần nhỏ hơn, sau đó được tái cấu trúc trên máy tính của bạn. Hãy xem hình ảnh dưới đây như một minh họa cho quá trình này. Hình ảnh con chó được chia thành ba gói tin, sau đó được tái tạo lại trên máy tính để tạo thành hình ảnh cuối cùng.

![](./img/4_Packets_Frames/1.1.png)

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

# Task 2: TCP/IP (The Three-Way Handshak)

**TCP** (hay viết tắt của **Transmission Control Protocol**) là một trong những quy tắc khác được sử dụng trong mạng máy tính.

Giao thức này rất giống với mô hình OSI mà chúng ta đã thảo luận trước đây trong **Phòng 3 của mô-đun này**. Giao thức **TCP/IP** bao gồm bốn lớp và có thể được coi như một phiên bản tóm tắt của mô hình OSI. Các lớp này bao gồm:  

1. **Application**  
2. **Transport**  
3. **Internet**  
4. **Network Interface**  

Rất giống với cách hoạt động của mô hình OSI, thông tin được thêm vào mỗi lớp trong mô hình TCP khi dữ liệu (hay **gói tin**) đi qua nó. Như bạn có thể nhớ, quá trình này được gọi là **encapsulation** (đóng gói), trong khi quá trình ngược lại được gọi là **decapsulation** (giải đóng gói).  

Một tính năng nổi bật của TCP là nó dựa trên kết nối (**connection-based**), nghĩa là TCP phải thiết lập một kết nối giữa **client** (máy khách) và thiết bị đóng vai trò **server** (máy chủ) trước khi dữ liệu được gửi đi.

Nhờ đặc điểm này, TCP đảm bảo rằng bất kỳ dữ liệu nào được gửi đi sẽ được nhận ở đầu bên kia. Quá trình này được gọi là **Three-way handshake** (bắt tay ba bước), mà chúng ta sẽ thảo luận chi tiết hơn ngay sau đây. Bảng so sánh các ưu điểm và nhược điểm của TCP được trình bày bên dưới:

| **Ưu điểm của TCP**                                                                 | **Nhược điểm của TCP**                                                                                               |
|-------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| **Đảm bảo tính toàn vẹn của dữ liệu.**                                              | **Yêu cầu một kết nối đáng tin cậy giữa hai thiết bị. Nếu một phần nhỏ của dữ liệu không được nhận, toàn bộ dữ liệu phải được gửi lại.** |
| **Có khả năng đồng bộ hóa hai thiết bị để ngăn chặn việc dữ liệu bị tràn hoặc gửi sai thứ tự.** | **Kết nối chậm có thể làm nghẽn thiết bị khác vì kết nối sẽ được duy trì trên thiết bị nhận trong suốt thời gian này.** |
| **Thực hiện nhiều quy trình hơn để đảm bảo độ tin cậy.**                             | **TCP chậm hơn đáng kể so với UDP vì các thiết bị sử dụng giao thức này phải thực hiện nhiều xử lý hơn.**               |

**Các gói tin TCP** chứa nhiều phần thông tin khác nhau được gọi là **headers** (phần tiêu đề), được thêm vào trong quá trình đóng gói (**encapsulation**). Hãy cùng giải thích một số header quan trọng trong bảng dưới đây:

| **Header**               | **Mô tả**                                                                                                                                                                   |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Source Port**           | Đây là cổng được mở bởi thiết bị gửi để gửi gói tin TCP. Giá trị này được chọn ngẫu nhiên (trong các cổng từ 0-65535 chưa được sử dụng tại thời điểm đó).                      |
| **Destination Port**      | Đây là số cổng mà một ứng dụng hoặc dịch vụ đang chạy trên máy chủ từ xa (máy nhận dữ liệu). Ví dụ, một máy chủ web đang chạy trên cổng 80. Không giống cổng nguồn, giá trị này không được chọn ngẫu nhiên. |
| **Source IP**             | Đây là địa chỉ IP của thiết bị gửi gói tin.                                                                                                                                |
| **Destination IP**        | Đây là địa chỉ IP của thiết bị mà gói tin được gửi đến.                                                                                                                    |
| **Sequence Number**       | Khi kết nối được thiết lập, phần dữ liệu đầu tiên được truyền đi sẽ được gán một số ngẫu nhiên. Chúng ta sẽ giải thích chi tiết hơn về điều này ở phần sau.                       |
| **Acknowledgement Number**| Sau khi một phần dữ liệu được gán số thứ tự, số cho phần dữ liệu tiếp theo sẽ là số thứ tự hiện tại +1. Điều này cũng sẽ được giải thích chi tiết hơn ở phần sau.               |
| **Checksum**              | Đây là giá trị đảm bảo tính toàn vẹn của TCP. Một phép tính toán học được thực hiện để ghi nhớ đầu ra. Khi thiết bị nhận thực hiện phép tính này, dữ liệu sẽ bị coi là hỏng nếu đầu ra khác với đầu ra đã gửi. |
| **Data**                  | Tiêu đề này là nơi chứa dữ liệu, ví dụ: các byte của một tệp đang được truyền.                                                                                               |
| **Flag**                  | Tiêu đề này xác định cách gói tin sẽ được xử lý bởi thiết bị trong quá trình bắt tay (handshake). Các cờ cụ thể sẽ xác định các hành vi cụ thể, điều này sẽ được giải thích chi tiết hơn bên dưới. |

Tiếp theo, chúng ta sẽ thảo luận về **Three-way handshake** — thuật ngữ được sử dụng để mô tả quá trình thiết lập kết nối giữa hai thiết bị. **Three-way handshake** giao tiếp bằng một số thông điệp đặc biệt — bảng dưới đây nêu bật các thông điệp chính:

| **Bước** | **Thông điệp** | **Mô tả**                                                                                                                                                                           |
|----------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **1**    | **SYN**        | Một thông điệp SYN là gói tin ban đầu được gửi bởi client trong quá trình bắt tay. Gói tin này được sử dụng để bắt đầu một kết nối và đồng bộ hóa hai thiết bị với nhau.               |
| **2**    | **SYN/ACK**    | Gói tin này được gửi bởi thiết bị nhận (server) để xác nhận nỗ lực đồng bộ hóa từ client.                                                                                        |
| **3**    | **ACK**        | Gói tin xác nhận có thể được sử dụng bởi client hoặc server để xác nhận rằng một chuỗi các thông điệp/gói tin đã được nhận thành công.                                             |
| **4**    | **DATA**       | Sau khi kết nối được thiết lập, dữ liệu (chẳng hạn như các byte của một tệp) được gửi qua thông điệp "DATA".                                                                       |
| **5**    | **FIN**        | Gói tin này được sử dụng để **đóng kết nối một cách gọn gàng** sau khi quá trình truyền tải đã hoàn tất.                                                                          |
| **#**    | **RST**        | Gói tin này đột ngột chấm dứt toàn bộ giao tiếp. Đây là biện pháp cuối cùng và cho thấy đã xảy ra một vấn đề trong quá trình thực hiện. Ví dụ: dịch vụ hoặc ứng dụng không hoạt động đúng, hoặc hệ thống gặp lỗi như thiếu tài nguyên. |  

Khi dữ liệu được gửi, nó được gán một chuỗi số ngẫu nhiên (**Sequence Number**) và được tái cấu trúc bằng cách sử dụng chuỗi số này, tăng dần lên 1. Cả hai máy tính phải đồng ý về cùng một chuỗi số để dữ liệu được gửi theo đúng thứ tự. Trình tự này được thống nhất qua ba bước:

1. **SYN — Client:** Đây là **Initial Sequence Number (ISN)** của tôi để đồng bộ hóa (**SYNchronise**) (0).  
2. **SYN/ACK — Server:** Đây là **Initial Sequence Number (ISN)** của tôi để đồng bộ hóa (**SYNchronise**) (5.000), và tôi **ACKnowledge** chuỗi số ban đầu của bạn (0).  
3. **ACK — Client:** Tôi **ACKnowledge** **Initial Sequence Number (ISN)** của bạn là (5.000), đây là một số dữ liệu với ISN của tôi +1 (5.000 + 1).

![](./img/4_Packets_Frames/2.1.png)

Bất kỳ dữ liệu nào được gửi đều được gán một **chuỗi số ngẫu nhiên** (**Sequence Number**) và được tái cấu trúc bằng cách sử dụng chuỗi số này, tăng dần lên 1. Cả hai máy tính phải đồng ý về cùng một chuỗi số để dữ liệu được gửi theo đúng thứ tự. Thứ tự này được thống nhất qua ba bước:

1. **SYN — Client:** Đây là **Initial Sequence Number (ISN)** của tôi để **đồng bộ hóa** (**SYNchronise**) (0).  
2. **SYN/ACK — Server:** Đây là **Initial Sequence Number (ISN)** của tôi để **đồng bộ hóa** (**SYNchronise**) (5.000), và tôi **xác nhận** (**ACKnowledge**) chuỗi số ban đầu của bạn (0).  
3. **ACK — Client:** Tôi **xác nhận** (**ACKnowledge**) **Initial Sequence Number (ISN)** của bạn là (5.000), đây là một số dữ liệu với ISN của tôi +1 (5.000 + 1).

| **Thiết bị**          | **Chuỗi số ban đầu (ISN)** | **Chuỗi số cuối cùng** |
|------------------------|----------------------------|-------------------------|
| **Client (Sender)**    | 0                          | 0 + 1 = 1               |
| **Client (Sender)**    | 1                          | 1 + 1 = 2               |
| **Client (Sender)**    | 2                          | 2 + 1 = 3               |


 **Đóng kết nối TCP:**

Hãy nhanh chóng giải thích quá trình đóng kết nối TCP. Đầu tiên, TCP sẽ đóng một kết nối sau khi một thiết bị xác định rằng thiết bị khác đã nhận thành công toàn bộ dữ liệu.

Vì TCP giữ lại tài nguyên hệ thống trên một thiết bị, nên việc đóng kết nối TCP càng sớm càng tốt là một **thực hành tốt**.

Để bắt đầu quá trình đóng kết nối TCP, thiết bị sẽ gửi một gói tin **“FIN”** đến thiết bị khác. Tất nhiên, với TCP, thiết bị nhận cũng phải **xác nhận** (**acknowledge**) gói tin này.

Hãy minh họa quá trình này bằng cách sử dụng ví dụ **Alice và Bob**, như chúng ta đã làm trước đây.

![Đóng kết nối TCP](./img/4_Packets_Frames/2.2.png)

Trong hình minh họa, chúng ta có thể thấy rằng **Alice** đã gửi một gói tin **“FIN”** cho **Bob**. Vì **Bob** đã nhận được gói tin này, anh ấy sẽ thông báo cho **Alice** rằng anh ấy đã nhận được và cũng muốn đóng kết nối (bằng cách sử dụng **FIN**). **Alice** đã nhận rõ thông báo của **Bob** và sẽ cho **Bob** biết rằng cô ấy **xác nhận** (**acknowledge**) điều này.

**Câu hỏi:**  

**1. Tiêu đề nào trong một gói tin TCP đảm bảo tính toàn vẹn của dữ liệu?**  

<details>  
  <summary>Hiển thị đáp án</summary>  
  Đáp án: Checksum  
</details>  

**2. Cung cấp thứ tự của một quá trình bắt tay ba bước thông thường (mỗi bước được phân tách bằng dấu phẩy)?**  

<details>  
  <summary>Hiển thị đáp án</summary>  
  Đáp án: SYN, SYN/ACK, ACK  
</details>  


