# What is networking?


Mạng chỉ đơn giản là những thứ được kết nối với nhau. Ví dụ như 2 điện thoại được kết nối với nhau qua Bluetooth hoặc kết nối điện thoại với máy tính bằng dây cáp, thì cũng được coi là mạng.

Trong điện toán, một mạng có thể được hình thành từ bất kỳ đâu từ 2 thiết bị đến hàng tỷ thiết bị. Những thiết bị này bao gồm mọi thứ từ máy tính xách tay và điện thoại của bạn đến camera an ninh, đèn giao thông và thậm chí cả nông nghiệp!

Mạng lưới được tích hợp vào cuộc sống hàng ngày của chúng ta. Có thể là thu thập dữ liệu về thời tiết, cung cấp điện cho các hộ gia đình hoặc thậm chí xác định ai có quyền ưu tiên trên đường. Vì mạng lưới được nhúng sâu vào thời hiện đại, nên mạng lưới là một khái niệm thiết yếu cần nắm bắt trong an ninh mạng.

## 1.  What is the Internet?

Internet là một mạng khổng lồ bao gồm rất nhiều mạng nhỏ trong đó.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Try_Hack_Me/Room_What_is_networking/image/1_1.png" alt="" width="1000">
</p>
<p align="center"><b>Hình 1.1 </b></p>

Xét ví dụ ở trên: Alice kết bạn với Zayn và Toby. Cô ấy muốn giới thiệu 2 người này cho Bob và Jim. Vấn đề là Alice là người duy nhất nói cùng ngôn ngữ với Zayn và Toby. Vậy để 2 người này giao tiếp được với Bob và Jim thì cần thông qua Alice. Do đó, họ giao tiếp với nhau thông qua Alice và tạo thành một mạng mới.

Internet được phát minh bởi Tim Berners-Lee nhờ sự sáng tạo của World Wide Web (WWW).

Internet giống như sau: 

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Try_Hack_Me/Room_What_is_networking/image/1_2.png" alt="" width="1000">
</p>
<p align="center"><b>Hình 1.2</b></p>

Như đã nói ở trên, Internet được tạo thành từ nhiều mạng nhỏ được kết nối với nhau. 

Những mạng nhỏ được gọi là **private networks**, trong khi Internet được gọi là **public networks**.

## 2. Identifying Devices on a Network (Nhận dạng thiết bị trên mạng)


Để liên lạc và duy trì trật tự, các thiết bị phải được nhận dạng và nhận diện trên mạng. Sẽ có ích gì nếu cuối ngày bạn không biết mình đang nói chuyện với ai?

Các thiết bị trên mạng rất giống với con người ở chỗ chúng ta có hai cách nhận dạng:

- **Tên**
- **Dấu vân tay-Fingerprints**

Chúng ta có thể thay đổi tên của mình thông qua thăm dò chứng thư, tuy nhiên, chúng ta không thể thay đổi dấu vân tay của mình. Mỗi người đều có một bộ dấu vân tay riêng, điều đó có nghĩa là ngay cả khi họ thay đổi tên, vẫn có danh tính đằng sau nó.

Tương tự trong mạng máy tính:

- **Địa chỉ IP**
- **Địa chỉ Media Access Control (MAC)** - Địa chỉ này tương tự như số seri.

### 2.1 IP Addresses-Địa chỉ IP

Tóm lại, địa chỉ IP (Internet Protocol) có thể được sử dụng để xác định máy chủ trên mạng trong một khoảng thời gian. Sau đó, địa chỉ IP này có thể được liên kết với một thiết bị khác mà không cần thay đổi địa chỉ IP.

#### Cấu trúc địa chỉ IP

Hãy xem xét địa chỉ sau:

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Try_Hack_Me/Room_What_is_networking/image/2_1.png" alt="" width="1000">
</p>
<p align="center"><b>Hình 2.1 "</b></p>

Địa chỉ IP là một tập hợp các số được chia thành 4 octets. Giá trị của mỗi octet tạo thành địa chỉ IP của thiết bị mạng. Các con số này được tính toán thông qua một kỹ thuật gọi là địa chỉ IP và mạng con (*IP addressing & subnetting*). Điều quan trọng là địa chỉ IP có thể thay đổi từ thiết bị này sang thiết bị khác nhưng không thể sử dụng đồng thời nhiều lần trong cùng một mạng.


Địa chỉ IP tuân theo một bộ tiêu chuẩn được gọi là giao thức (*protocol*). Các giao thức này là xương sống của mạng, giúp các thiết bị có thể giao tiếp cùng một ngôn ngữ. Tùy thuộc vào vị trí của thiết bị sẽ xác định loại địa chỉ là:

- **Public Address**: Được sử dụng để nhận dạng các thiết bị trên Internet.
- **Private Address**: Được sử dụng để nhận dạng thiết bị trong mạng nội bộ.

Ví dụ:

| Device Name       | IP Address    | IP Address Type |
|-------------------|---------------|------------------|
| DESKTOP-KJE57FD   | 192.168.1.77  | Private         |
| DESKTOP-KJE57FD   | 86.157.52.21  | Public          |
| CMNatic-PC        | 192.168.1.74  | Private         |
| CMNatic-PC        | 86.157.52.21  | Public          |

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Try_Hack_Me/Room_What_is_networking/image/2_2.png" alt="" width="1000">
</p>
<p align="center"><b>Hình 2.2 "</b></p>

Ta thấy 2 thiết bị này dùng địa chỉ IP private để giao tiếp với nhau, Tuy nhiên dữ liệu tới internet của 2 thiết bị này được xác định bằng địa chỉ IP public. Địa chỉ IP public được cung cấp bởi ISP (Internet Service Provider - Nhà cung cấp dịch vụ internet).

Ví dụ: 

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Try_Hack_Me/Room_What_is_networking/image/2_3.png" alt="" width="1000">
</p>
<p align="center"><b>Hình 2.3 "</b></p>

Khi càng ngày càng có nhiều thiết bị kết nối, việc có được một địa chỉ IP public chưa được sử dụng trở nên khó khăn. Ví dụ, Cisco, một gã khổng lồ trong ngành về thế giới mạng, ước tính rằng sẽ có khoảng 50 tỷ thiết bị được kết nối trên Internet vào cuối năm 2021. Ở đây chúng ta đề cập đến internet protocol được gọi là IPv4 sử dụng hệ thống đánh số gồm 2^32 IP (tức 4.29 tỷ).

IPv6 là phiên bản mới của sơ đồ đánh địa chỉ giao thức internet giúp giải quyết vấn đề này.  IPv6 hỗ trợ tới 2^128 địa chỉ IP (hơn 340 nghìn tỷ)

So sánh 2 địa chỉ:

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Try_Hack_Me/Room_What_is_networking/image/2_4.png" alt="" width="1000">
</p>
<p align="center"><b>Hình 2.4 "</b></p>

### 2.2 Mac Address-Địa chỉ MAC

Các thiết bị trên mạng đều sẽ có giao diện mạng vật lý, đó là một bo mạch vi mạch được tìm thấy trên bo mạch chủ của thiết bị. Giao diện mạng này được gán một địa chỉ duy nhất tại nhà máy nơi nó được xây dựng, được gọi là địa chỉ MAC (Media Access Control - Kiểm soát truy cập phương tiện).

Địa chỉ MAC là một số thập lục phân gồm 12 ký tự (hệ thống đánh số 16 cơ sở được sử dụng trong điện toán để biểu thị các số) được chia thành hai số và phân cách bằng dấu hai chấm. Những dấu hai chấm này được coi là dấu phân cách.

Ví dụ: `a4:c3:f0:85:ac:2d`. Sáu ký tự đầu tiên đại diện cho công ty tạo ra giao diện mạng và sáu ký tự cuối cùng là một số duy nhất.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Try_Hack_Me/Room_What_is_networking/image/2_5.png" alt="" width="1000">
</p>
<p align="center"><b>Hình 2.5 "</b></p>

Tuy nhiên, một điều thú vị với địa chỉ MAC là chúng có thể bị làm giả hoặc "giả mạo" trong một quá trình được gọi là **spoofing**. Việc giả mạo này xảy ra khi một thiết bị nối mạng giả vờ nhận dạng là một thiết bị khác bằng địa chỉ MAC của nó. Khi điều này xảy ra, nó thường có thể phá vỡ các thiết kế bảo mật được triển khai kém vốn cho rằng các thiết bị giao tiếp trên mạng là đáng tin cậy.

Hãy xem tình huống sau: Tường lửa được cấu hình để cho phép mọi giao tiếp đến và đi từ địa chỉ MAC của quản trị viên. Nếu một thiết bị giả mạo hoặc "giả mạo" địa chỉ MAC này, tường lửa giờ đây sẽ cho rằng nó đang nhận thông tin liên lạc từ quản trị viên trong khi thực tế không phải vậy.

Các địa điểm như quán cà phê, quán cà phê và khách sạn thường sử dụng tính năng kiểm soát địa chỉ MAC khi sử dụng Wi-Fi "Guest" hoặc "Public" của họ. Cấu hình này có thể cung cấp các dịch vụ tốt hơn, tức là kết nối nhanh hơn với mức giá nếu bạn sẵn sàng trả phí cho mỗi thiết bị.
