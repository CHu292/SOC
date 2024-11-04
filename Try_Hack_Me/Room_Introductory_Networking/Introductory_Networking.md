# Room Introductory Networking
- [x] The OSI Model
- [x] The TCP/IP Model
- [x] How these models look in practice
- [x] An introduction to basic networking tools

## 1. The OSI Model: An Overview

### 1.1 Khái niệm

**Mô hình OSI** (Open Systems Interconnection) - mô hình kết nối các hệ thống mở.

Mô hình Kết nối các hệ thống mở (OSI) là một khung khái niệm chia các chức năng truyền thông mạng thành 7 lớp. Việc gửi dữ liệu qua mạng rất phức tạp vì các công nghệ phần cứng và phần mềm khác nhau phải hoạt động một cách hài hòa qua các ranh giới địa lý và chính trị. Mô hình dữ liệu OSI cung cấp một ngôn ngữ phổ quát cho mạng máy tính, vì vậy các công nghệ đa dạng có thể giao tiếp bằng cách sử dụng các giao thức tiêu chuẩn hoặc quy tắc truyền thông. Mỗi công nghệ trong một lớp cụ thể phải cung cấp các khả năng nhất định và thực hiện các chức năng cụ thể để trở nên hữu ích trong mạng. Các công nghệ ở những lớp cao hơn hưởng lợi từ việc rút gọn này vì chúng có thể sử dụng các công nghệ cấp thấp hơn mà không phải lo lắng về các chi tiết triển khai cơ bản.

Mô hình OSI gồm có 7 lớp:

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Try_Hack_Me/Room_Introductory_Networking/image/1_1.png" width="500">
</p>
<p align="center"><b>Hình 1.1</b></p>


### 1.2  Tổng quan

- **Lớp 7**: Chấp nhận yêu cầu liên lạc từ các ứng dụng.
- **Lớp 6**: Mã hóa, nén, biến dữ liệu ban đầu để cung cấp cho nó định dạng chuẩn.
- **Lớp 5**: Theo dõi thông tin liên lạc giữa máy chủ và máy tính nhận.
- **Lớp 4**: Lựa chọn gửi dữ liệu qua TCP hoặc UDP.
- **Lớp 3**: Xử lý địa chỉ logic (IP).
- **Lớp 2**: Kiểm tra thông tin nhận để đảm bảo nó không bị hỏng, cũng như định dạng dữ liệu để chuẩn bị truyền tải.
- **Lớp 1**: Truyền và nhận dữ liệu.


### Layer 7 -- Application
Lớp ứng dụng của mô hình OSI cung cấp các tùy chọn kết nối mạng cho các chương trình chạy trên máy tính. Lớp này hầu như chỉ hoạt động với các ứng dụng, cung cấp giao diện cho chúng sử dụng để truyền dữ liệu. Khi dữ liệu được đưa đến lớp Application, nó sẽ được chuyển xuống lớp Presentation.

Ví dụ: các trình duyệt có thể giao tiếp bằng cách sử dụng giao thức truyền siêu văn bản an toàn (HyperText Transfer Protocol Secure - HTTPS), HTTP; và ứng dụng email có thể giao tiếp bằng POP3 (Post Office Protocol 3) và SMTP (Simple Mail Transfer Protocol - Giao thức truyền thư đơn giản).

### Layer 6 -- Presentation
Lớp Presentation (Trình bày) nhận dữ liệu từ lớp Application. Dữ liệu thường ở định dạng mà ứng dụng có thể hiểu được nhưng không nhất thiết phải ở định dạng chuẩn mà lớp Application trong máy tính nhận có thể hiểu được.

Lớp Presentation chuyển dữ liệu sang định dạng chuẩn hóa, xử lý mọi mã hóa, nén hoặc biến đổi đối với dữ liệu. Khi hoàn thành, dữ liệu sẽ được chuyển xuống lớp Session (lớp phiên). Lớp Presentation chủ yếu liên quan đến cú pháp của chính dữ liệu để các ứng dụng gửi và sử dụng.

Ví dụ: các ngôn ngữ như Hypertext Markup Language (HTML), JavaScript Object Notation (JSON), và Comma Separated Values (CSV) là các ngôn ngữ mô hình hóa để mô tả cấu trúc dữ liệu tại lớp trình bày.

### Layer 5 -- Session
Khi lớp Phiên (Session) nhận được dữ liệu được định dạng chính xác từ lớp Presentation, nó sẽ xem liệu nó có thể thiết lập kết nối với máy tính khác trên mạng hay không. Nếu không thể thì nó sẽ gửi lại lỗi và quá trình này sẽ không diễn ra nữa.

Nếu một phiên có thể được thiết lập thì công việc của lớp phiên là duy trì phiên đó, cũng như hợp tác với phiên của máy tính từ xa để đồng bộ hóa thông tin liên lạc. Lớp phiên đặc biệt quan trọng vì phiên mà nó tạo ra là duy nhất cho giao tiếp được đề cập.

Đây là tính năng cho phép bạn thực hiện đồng thời nhiều yêu cầu đến các điểm cuối khác nhau mà không xáo trộn tất cả dữ liệu, ví dụ như việc mở 2 tab trong trình duyệt web cùng một lúc.

Khi lớp phiên đã ghi thành công kết nối giữa máy chủ và máy tính từ xa, dữ liệu sẽ được chuyển xuống lớp dưới - Transport (lớp vận chuyển). Lớp phiên chịu trách nhiệm điều phối mạng giữa hai ứng dụng riêng biệt trong một phiên. Một phiên quản lý một kết nối ứng dụng một-một từ khi bắt đầu đến khi kết thúc và xung đột đồng bộ hóa.

Các giao thức được sử dụng ở lớp phiên: Hệ thống tệp mạng (Network File System - NSF) và khối tin nhắn máy chủ (Server Message Block - SMB).

### Layer 4 -- Transport
Mục đích đầu tiên của lớp truyền tải (Transport) là lựa chọn giao thức mà dữ liệu sẽ được truyền đi. Hai giao thức phổ biến nhất trong lớp truyền tải là TCP (Transmission Control Protocol - Giao thức điều khiển truyền) và UDP (User Datagram Protocol - giao thức gói dữ liệu người dùng).

Với TCP, việc truyền là dựa trên kết nối, có nghĩa là kết nối giữa các máy tính được thiết lập và duy trì trong thời gian yêu cầu. Điều này cho phép truyền tải đáng tin cậy vì kết nối có thể được sử dụng để đảm bảo rằng các gói đều đến đúng nơi. Kết nối TCP cho phép hai máy tính duy trì liên lạc liên tục để đảm bảo dữ liệu được gửi với tốc độ chấp nhận được và mọi dữ liệu bị mất sẽ được gửi lại.

Ngược lại với UDP, dữ liệu sẽ được ném vào máy tính nhận mà không yêu cầu kết nối liên tục - nếu máy nhận không theo kịp thì đó là vấn đề. Điều này có nghĩa là TCP thường được chọn cho các tình huống mà độ chính xác ưu tiên hơn tốc độ, còn UDP sẽ được sử dụng trong các tình huống cần tốc độ nhanh, ví dụ như phát trực tiếp video.

Với giao thức được chọn, lớp truyền tải sẽ chia quá trình truyền thành các phần nhỏ (trên TCP gọi là phân đoạn; trên UDP gọi là datagram), giúp việc truyền tải dễ dàng hơn.

### Layer 3 -- Network
Lớp Mạng (Network) chịu trách nhiệm xác định đích đến của yêu cầu của bạn. Ví dụ, khi bạn muốn yêu cầu thông tin từ một trang web, lớp mạng sẽ lấy địa chỉ IP cho trang đó và tìm ra con đường tốt nhất để đi.

Ở giai đoạn này, làm việc với địa chỉ logic (Logical Addressing - tức là địa chỉ IP) được kiểm soát bằng phần mềm. Địa chỉ logic được sử dụng để cung cấp thứ tự cho các mạng, phân loại chúng và cho phép chúng ta sắp xếp chúng một cách chính xác. Hiện tại, địa chỉ logic phổ biến nhất là IPv4 (ví dụ, 192.168.1.1 là địa chỉ chung cho bộ định tuyến gia đình).

### Layer 2 -- Data Link
Lớp liên kết dữ liệu (Data Link) tập trung vào việc đánh địa chỉ vật lý của đường truyền. Nó nhận một gói từ lớp mạng (bao gồm địa chỉ IP cho máy tính từ xa) và thêm địa chỉ vật lý (MAC) của điểm cuối nhận.

Trong mỗi máy tính hỗ trợ mạng đều có một thẻ giao diện mạng (Network Interface Card - NIC) đi kèm với một địa chỉ MAC (Media Access Control - Kiểm soát truy cập phương tiện) duy nhất để nhận dạng nó. Địa chỉ MAC được nhà sản xuất đặt và ghi vào thẻ, chúng không thể thay đổi được nhưng vẫn có thể bị giả mạo. Khi gửi thông tin qua mạng, địa chỉ vật lý được sử dụng để xác định chính xác nơi gửi thông tin.

Ngoài ra, lớp Data Link còn trình bày dữ liệu ở định dạng phù hợp để truyền tải. Khi nhận dữ liệu, nó kiểm tra thông tin nhận được để đảm bảo không bị hỏng trong quá trình truyền, điều này cũng có thể xảy ra khi dữ liệu được truyền qua lớp 1 - Physical layer.

### Layer 1 -- Physical
Lớp vật lý (Physical) nằm ngay dưới phần cứng của máy tính. Đây là nơi các xung điện tạo nên việc truyền dữ liệu qua mạng được gửi và nhận.

Công việc của lớp vật lý là chuyển đổi dữ liệu nhị phân của quá trình truyền thành tín hiệu và truyền chúng qua mạng, cũng như nhận tín hiệu và chuyển đổi chúng trở lại thành dữ liệu nhị phân.

Lớp vật lý là phương tiện truyền dẫn vật lý và các công nghệ để truyền dữ liệu qua phương tiện đó. Về cốt lõi, hoạt động truyền dữ liệu là việc truyền tín hiệu kỹ thuật số và điện tử qua các kênh vật lý khác nhau như cáp quang, cáp đồng và không khí. Lớp vật lý bao gồm tiêu chuẩn cho các công nghệ và chỉ số liên quan chặt chẽ với các kênh, chẳng hạn như Bluetooth, NFC và tốc độ truyền dữ liệu.

## 2. Encapsulation

Khi dữ liệu được truyền xuống từng lớp của mô hình OSI, thông tin cụ thể cho từng lớp sẽ được thêm vào, bắt đầu từ khi dữ liệu được truyền đi. Ví dụ, tiêu đề do Lớp Mạng thêm vào sẽ bao gồm địa chỉ IP nguồn và đích, trong khi tiêu đề của Lớp Vận chuyển sẽ chứa thông tin liên quan đến giao thức truyền đang được sử dụng. Lớp Liên kết Dữ liệu cũng thêm một phần vào cuối quá trình truyền, nhằm xác minh rằng dữ liệu không bị hỏng trong quá trình truyền. Điều này cũng tăng cường bảo mật, vì dữ liệu không thể bị chặn và giả mạo mà không làm hỏng phần cuối. Toàn bộ quá trình này được gọi là đóng gói, là cách thức dữ liệu được gửi từ máy tính này sang máy tính khác.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Try_Hack_Me/Room_Introductory_Networking/image/2_1.png" width="900">
</p>
<p align="center"><b>Hình 2.1 </b></p>

Lưu ý rằng dữ liệu được đóng gói có tên gọi khác nhau ở từng lớp trong quy trình. Tại các Lớp 7, 6 và 5, dữ liệu được gọi đơn giản là **dữ liệu**. Ở Lớp Vận chuyển, dữ liệu đóng gói được gọi là **phân đoạn** (segment) hoặc **gói dữ liệu** (datagram), tùy thuộc vào việc TCP hay UDP là giao thức truyền. Tại Lớp Mạng, dữ liệu được gọi là **gói**. Khi gói được truyền xuống Lớp Liên kết Dữ liệu, nó trở thành **khung**, và khi truyền qua mạng, khung được chia thành các **bit**.

Khi máy tính đích nhận được dữ liệu, nó đảo ngược quy trình này – bắt đầu từ Lớp Vật lý và xử lý lên tới Lớp Ứng dụng, lần lượt loại bỏ các thông tin đã được thêm vào. Quá trình này gọi là giải đóng gói (de-encapsulation). Có thể coi các lớp của mô hình OSI tồn tại bên trong mọi máy tính có khả năng mạng, dù không thực sự rõ ràng. Tất cả các máy tính đều tuân theo quy trình đóng gói để gửi dữ liệu và giải đóng gói khi nhận dữ liệu.

Các quy trình đóng gói và giải đóng gói rất quan trọng – không chỉ vì mục đích sử dụng thực tế mà còn vì chúng cung cấp một phương pháp chuẩn hóa để gửi dữ liệu. Điều này đảm bảo rằng mọi lần truyền sẽ tuân theo cùng một phương pháp, cho phép bất kỳ thiết bị mạng nào gửi yêu cầu đến bất kỳ thiết bị nào khác có thể truy cập được và đảm bảo yêu cầu đó được hiểu – bất kể chúng có cùng nhà sản xuất, hệ điều hành hay không.

## 3. The TCP/IP Model


Transmission Control Protocol (TCP) là một giao thức hướng kết nối yêu cầu **bắt tay ba bước TCP** (three-way handshake) để thiết lập kết nối. TCP cung cấp khả năng truyền dữ liệu đáng tin cậy, kiểm soát luồng và kiểm soát tắc nghẽn. Các giao thức cấp cao hơn như **HTTP**, **POP3**, **IMAP**, và **SMTP** sử dụng TCP.

 Mô hình TCP/IP và sự tương đồng với mô hình OSI
Mô hình **TCP/IP**, theo nhiều cách, rất giống với mô hình **OSI**. TCP/IP cũ hơn mô hình OSI vài năm và đóng vai trò là cơ sở cho mạng lưới trong thực tế. Mô hình TCP/IP bao gồm **bốn lớp**:

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Try_Hack_Me/Room_Introductory_Networking/image/3_1.png" width ="500">
</p>
<p align="center"><b>Hình 3.1 </b></p>

1. **Application Layer** - Tương đương với các lớp Application, Presentation, và Session trong mô hình OSI.
2. **Transport Layer** - Tương đương với Lớp Vận chuyển (Transport) trong mô hình OSI.
3. **Internet Layer** - Tương đương với Lớp Mạng (Network) trong mô hình OSI.
4. **Network Interface Layer** - Bao gồm chức năng của các Lớp Liên kết Dữ liệu (Data Link) và Vật lý (Physical) trong mô hình OSI.

Lưu ý về phân chia các lớp trong mô hình TCP/IP
Một số nguồn gần đây chia mô hình TCP/IP thành **năm lớp**, chia lớp **Network Interface** thành **Lớp Liên kết Dữ liệu** (Data Link) và **Lớp Vật lý** (Physical), giống như mô hình OSI. Điều này được chấp nhận và biết đến rộng rãi; tuy nhiên, nó không được định nghĩa chính thức, không giống như bốn lớp ban đầu trong RFC1122. Cả hai cách chia đều hợp lệ, tùy thuộc vào phiên bản mà bạn sử dụng.

 Cách khớp các lớp giữa hai mô hình:

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Try_Hack_Me/Room_Introductory_Networking/image/3_2.png" width ="500">
</p>
<p align="center"><b>Hình 3.2 </b></p>

#### Các quá trình đóng gói và giải đóng gói trong mô hình TCP/IP
Các quá trình **đóng gói** và **giải đóng gói** hoạt động tương tự với mô hình TCP/IP như với mô hình OSI. Ở mỗi lớp của mô hình TCP/IP, một **tiêu đề** được thêm vào trong quá trình đóng gói và được xóa trong quá trình giải đóng gói.

#### Bộ giao thức TCP/IP
Khi nói về TCP/IP, chúng ta nên hình dung một bảng có **bốn lớp**, nhưng thực chất đang đề cập đến một **bộ giao thức** -- tức là các quy tắc xác định cách thực hiện một hành động. TCP/IP lấy tên từ hai giao thức quan trọng nhất:

- **Transmission Control Protocol (TCP)**: Điều khiển luồng dữ liệu giữa hai điểm cuối.
- **Internet Protocol (IP)**: Kiểm soát cách các gói được xử lý và gửi đi.

#### Transmission Control Protocol (TCP) và quá trình bắt tay ba bước (three-way handshake)
**TCP** là một giao thức **dựa trên kết nối** (connection-based protocol). Nghĩa là, trước khi gửi bất kỳ dữ liệu nào qua TCP, phải tạo một kết nối ổn định giữa hai máy tính. Quá trình này gọi là **bắt tay ba bước**.

Khi cố gắng tạo kết nối:
1. Máy tính gửi một yêu cầu đặc biệt đến máy chủ từ xa để khởi tạo kết nối. Yêu cầu này chứa **bit SYN** (synchronise - đồng bộ hóa), tạo ra liên hệ đầu tiên trong quá trình kết nối.
2. Máy chủ phản hồi bằng một gói chứa **bit SYN** và **bit ACK** (acknowledgement - xác nhận).
3. Cuối cùng, máy tính của bạn sẽ gửi một gói chứa **bit ACK**, xác nhận rằng kết nối đã được thiết lập thành công.

Khi quá trình bắt tay ba bước hoàn tất, dữ liệu có thể được truyền giữa hai máy tính. Bất kỳ dữ liệu nào bị hỏng hoặc mất sẽ được gửi lại, đảm bảo kết nối ổn định. 

#### Quá trình bắt tay ba bước trong TCP/IP

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Try_Hack_Me/Room_Introductory_Networking/image/3_3.png" width ="500">
</p>
<p align="center"><b>Hình 3.3 </b></p>

## 4. Ping 


## Lệnh Ping

**Ping** (viết tắt của *Packet Internet Grouper*) là lệnh được sử dụng để kiểm tra khả năng kết nối với tài nguyên từ xa.

#### Cách thức hoạt động:

Lệnh **ping** hoạt động dựa trên giao thức **ICMP** (Internet Control Message Protocol), là một trong những giao thức thuộc bộ **TCP/IP**:
- ICMP hoạt động trên **lớp Network** của mô hình **OSI** và **lớp Internet** của mô hình **TCP/IP**.

#### Cú pháp cơ bản
```bash
ping <target>
```

Lệnh ping trả về **địa chỉ IP** của máy chủ, thay vì trả về URL đã yêu cầu. Để tìm hiểu chi tiết hơn, bạn có thể dùng lệnh `man ping`.

#### Công dụng
- **Ping** là một lệnh cơ bản để kiểm tra kết nối đến một địa chỉ cụ thể và xem mất bao lâu để nhận được phản hồi.
- Khi sử dụng lệnh **ping** với tên miền, bạn có thể kiểm tra được **địa chỉ IP** thực của trang web.
- Ping cũng thường được dùng để kiểm tra **thời gian phản hồi** từ thiết bị đến các nhà cung cấp dịch vụ Internet lớn.

Ví dụ:
- **FPT**: `ping 210.245.31.130`
- **Viettel**: `ping 203.113.131.1`
- **VNN**: `ping 203.162.4.190`

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Try_Hack_Me/Room_Introductory_Networking/image/4_1.png" width ="800">
</p>
<p align="center"><b>Hình 4.1 </b></p>


``` basg
64 bytes from lt-in-f102.1e100.net (108.177.14.102): icmp_seq=1 ttl=109 time=6.17 ms
```

- Phản hồi từ **IP 108.177.14.102**
- Dung lượng gói tin: **64 bytes**
- Thời gian phản hồi: **6.17 ms**

### Đánh giá thời gian phản hồi khi dùng lệnh ping

- **< 30 ms** - **Ping tuyệt vời**: Hầu như không có độ trễ, rất tốt cho các yêu cầu cần phản hồi nhanh như chơi game online (phản hồi thời gian thực).
- **30 đến 50 ms** - **Ping trung bình**: Phản hồi trang web vẫn nhanh.
- **50 đến 100 ms** - **Ping hơi chậm**: Web bắt đầu phản hồi chậm khi truy cập.
- **100 đến 500 ms** - **Ping chậm**: Ảnh hưởng rõ ràng đến trình duyệt web, load web rất lâu.
- **> 500 ms** - **Ping rất chậm**: Độ trễ đáng kể cho tất cả các yêu cầu; thường xảy ra khi nguồn và đích ở các khu vực khác nhau trên thế giới.

## 5. Traceroute - theo dõi lộ trình

#### Lệnh Traceroute

**Traceroute** là một lệnh dùng để ánh xạ đường dẫn mà yêu cầu của bạn đi qua để đến máy mục tiêu.

#### Cách thức hoạt động
Internet bao gồm rất nhiều máy chủ và các end-points khác nhau, tất cả đều được kết nối với nhau. Khi truy cập thông tin trên internet, yêu cầu của bạn phải đi qua nhiều máy chủ trung gian. **Traceroute** cho phép bạn xem từng kết nối này, hay chính là các bước trung gian từ máy tính của bạn đến tài nguyên mà bạn yêu cầu.

#### Cú pháp cơ bản
```bash
traceroute <destination>
```

Giao thức sử dụng:

- Trên Windows: Tiện ích tracert sử dụng giao thức ICMP, giống như lệnh ping.
- Trên Unix: Traceroute hoạt động bằng cách sử dụng UDP.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Try_Hack_Me/Room_Introductory_Networking/image/5_1.png" width ="1000">
</p>
<p align="center"><b>Hình 5.1 </b></p>

## 6. WHOIS


**WHOIS** cho phép bạn truy vấn thông tin về tên miền được đăng ký, bao gồm thông tin về chủ sở hữu tên miền đó.

#### Cài đặt WHOIS
Để cài đặt **WHOIS**, bạn có thể sử dụng lệnh sau:
```bash
$ sudo apt update && apt-get install whois
```

#### Cách sử dụng
Sau khi cài đặt, bạn có thể sử dụng lệnh **WHOIS** theo cú pháp sau:
```bash
whois <domain>
```
Thay `<domain>` bằng tên miền mà bạn muốn tra cứu.


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Try_Hack_Me/Room_Introductory_Networking/image/6_1.png" width ="1000">
</p>
<p align="center"><b>Hình 6.1 </b></p>


## 7. Dig


Bây giờ chúng ta sẽ nói về cách hoạt động của tên miền. Làm thế nào để một URL được chuyển thành địa chỉ IP mà máy tính có thể hiểu? Đó là giao thức TCP/IP có tên là **DNS** (Domain Name System - Hệ thống tên miền).

### Chức năng của DNS
Về cơ bản, DNS cho phép chúng ta yêu cầu một máy chủ đặc biệt cung cấp cho chúng ta địa chỉ IP của trang web mà chúng ta đang cố truy cập. 

**Ví dụ:** Khi chúng ta gửi yêu cầu đến địa chỉ trang web `www.google.com`, trước tiên máy tính sẽ gửi yêu cầu đến một máy chủ DNS đặc biệt. Sau đó, máy chủ sẽ tìm địa chỉ IP của Google và gửi lại cho chúng ta. Khi có địa chỉ IP, máy tính có thể gửi yêu cầu đến địa chỉ đó.

### Quy trình truy vấn DNS
1. **Kiểm tra Host file cục bộ:** 
   - Khi bạn thực hiện một yêu cầu đến một trang web, máy tính sẽ kiểm tra "Host file" cục bộ để xem liệu đã có ánh xạ tên miền đến địa chỉ IP hay chưa. Đây là hệ thống cũ hơn DNS và ít được sử dụng hơn, nhưng vẫn được ưu tiên trong thứ tự tìm kiếm của hầu hết các hệ điều hành.

2. **Kiểm tra bộ đệm DNS cục bộ:** 
   - Nếu không có ánh xạ nào được tạo thủ công, máy tính sẽ kiểm tra bộ đệm DNS cục bộ để xem liệu địa chỉ IP cho trang web đã được lưu trữ hay chưa.

3. **Gửi yêu cầu đến máy chủ DNS đệ quy:** 
   - Nếu địa chỉ chưa được tìm thấy, máy tính sẽ gửi yêu cầu đến **recursive DNS server** (máy chủ DNS đệ quy). 
   - Nhiều nhà cung cấp dịch vụ Internet (ISPs) duy trì máy chủ đệ quy riêng của họ, nhưng các công ty như Google hay OpenDNS cũng quản lý các máy chủ đệ quy.

4. **Gửi yêu cầu đến máy chủ gốc:** 
   - Nếu máy chủ đệ quy không có thông tin, nó sẽ chuyển yêu cầu đến **root name server**.
   - Trước năm 2004, thế giới có chính xác 13 máy chủ DNS root. Ngày nay, số lượng máy chủ này đã tăng lên, nhưng vẫn có thể truy cập bằng 13 địa chỉ IP được gán cho máy chủ gốc, giúp bạn đến gần máy chủ nhất khi thực hiện yêu cầu.

5. **Chuyển hướng đến máy chủ TLD:** 
   - Máy chủ tên miền cấp cao nhất (Top-Level Domain - TLD) được chia thành các phần mở rộng. 
   - Ví dụ, nếu bạn đang tìm kiếm `facebook.com`, yêu cầu của bạn sẽ được chuyển hướng đến máy chủ TLD xử lý các miền `.com`. 
   - Hoặc nếu bạn tìm kiếm `bbc.co.uk`, yêu cầu sẽ được chuyển đến máy chủ TLD xử lý các miền `.co.uk`.

6. **Chuyển đến máy chủ định danh có thẩm quyền:** 
   - Khi TLD server nhận được yêu cầu thông tin của bạn, máy chủ sẽ chuyển đến một máy chủ định danh có thẩm quyền thích hợp để lấy thông tin địa chỉ IP cuối cùng.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Try_Hack_Me/Room_Introductory_Networking/image/7_1.png" width ="700">
</p>
<p align="center"><b>Hình 7.1 </b></p>

### Authoritative Name Server

Một **máy chủ định danh có thẩm quyền** được sử dụng để lưu trữ trực tiếp bản ghi DNS cho tên miền. Nói cách khác, mọi tên miền trên thế giới sẽ có bản ghi DNS được lưu trữ trên **Authoritative name server** ở đâu đó; chúng là nguồn thông tin đáng tin cậy. 

Khi yêu cầu của bạn được gửi đến Authoritative name server cho tên miền mà bạn đang truy vấn, nó sẽ gửi lại thông tin liên quan cho bạn, cho phép máy tính của bạn kết nối với địa chỉ IP phía sau tên miền bạn đang yêu cầu.

#### Quá trình tự động
Khi bạn truy cập web bằng trình duyệt, tất cả quá trình này diễn ra tự động. Tuy nhiên, chúng ta có thể theo dõi quá trình này bằng công cụ có tên là **dig**.

#### Cú pháp sử dụng dig
`dig <domain> @<dns-server-ip>`

- **<domain>**: Tên miền mà bạn muốn truy vấn.
- **<dns-server-ip>**: Địa chỉ IP của máy chủ DNS mà bạn muốn sử dụng để thực hiện truy vấn.

Đây là một công cụ hữu ích để khắc phục các sự cố mạng.

```bash
chu@chu-Latitude-5510:~$ dig google.com @1.1.1.1
;; communications error to 1.1.1.1#53: timed out

; <<>> DiG 9.18.28-0ubuntu0.22.04.1-Ubuntu <<>> google.com @1.1.1.1
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 44075
;; flags: qr rd ra; QUERY: 1, ANSWER: 6, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;google.com.			IN	A

;; ANSWER SECTION:
google.com.		130	IN	A	64.233.164.138
google.com.		130	IN	A	64.233.164.102
google.com.		130	IN	A	64.233.164.139
google.com.		130	IN	A	64.233.164.101
google.com.		130	IN	A	64.233.164.100
google.com.		130	IN	A	64.233.164.113

;; Query time: 43 msec
;; SERVER: 1.1.1.1#53(1.1.1.1) (UDP)
;; WHEN: Thu Aug 15 13:10:00 MSK 2024
;; MSG SIZE  rcvd: 135
```



Trong bài học này, chúng ta sẽ tập trung vào phần **ANSWER** của kết quả trả về từ lệnh `dig`. Phần này cho chúng ta biết rằng chúng ta đã gửi một truy vấn thành công (tức là không có lỗi) và đã nhận được một câu trả lời đầy đủ như mong đợi. Câu trả lời này chứa các địa chỉ IP cho tên miền mà chúng ta đã truy vấn.

### TTL (Time To Live)

Một thông tin thú vị khác mà `dig` cung cấp là **TTL (Time To Live)** của bản ghi DNS được truy vấn. Khi máy tính của bạn truy vấn vào một tên miền, nó sẽ lưu kết quả vào bộ nhớ đệm cục bộ. TTL của bản ghi sẽ cho bạn biết khi nào nên dừng coi bản ghi là hợp lệ — tức là khi nào máy tính nên yêu cầu lại dữ liệu, thay vì dựa vào bản sao được lưu trong bộ nhớ đệm.

TTL có thể được tìm thấy trong cột thứ hai của phần **ANSWER SECTION**.

```bash
;; ANSWER SECTION:
google.com.		130	IN	A	64.233.164.138
google.com.		130	IN	A	64.233.164.102
google.com.		130	IN	A	64.233.164.139
google.com.		130	IN	A	64.233.164.101
google.com.		130	IN	A	64.233.164.100
google.com.		130	IN	A	64.233.164.113
```

Điều quan trọng cần lưu ý là TTL (trong ngữ cảnh bộ nhớ đệm DNS) được tính bằng giây. Với ví dụ trên sẽ là 2 phút 10 giây. 

