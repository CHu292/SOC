# 5. Tầng Liên Kết Dữ Liệu Trong Mô Hình OSI

**Tầng liên kết dữ liệu** (*Data Link Layer*) là tầng thứ hai trong mô hình OSI, nằm giữa tầng vật lý và tầng mạng. Nó đảm bảo việc truyền dữ liệu nhận được từ tầng mạng thông qua tầng vật lý đến các thiết bị được kết nối trực tiếp.

**Các chức năng chính của tầng liên kết dữ liệu:**
- Quản lý quyền truy cập vào môi trường truyền dẫn;
- Quản lý luồng dữ liệu;
- Địa chỉ hóa ở mức vật lý (phần cứng);
- Định dạng và tạo khung dữ liệu;
- Đảm bảo tính xác thực của dữ liệu nhận được;
- Cung cấp địa chỉ hóa cho giao thức của tầng trên.

**Các giao thức của tầng liên kết dữ liệu:**
Hoạt động của tầng liên kết dữ liệu được quyết định bởi các giao thức của nó. Ví dụ về các giao thức này bao gồm:
- Họ giao thức Ethernet (IEEE 802.3);
- Giao thức mạng không dây (IEEE 802.11).

**Các thiết bị hoạt động ở tầng liên kết dữ liệu:**
- Bộ điều hợp mạng (network adapters);
- Bộ chuyển đổi (switches);
- Bộ điều hợp mạng thông minh với các chức năng nâng cao;
- Điểm truy cập (access points).

---

## 5.1 Phương Pháp Chuyển Mạch

Trong thực tế, việc truyền tải luồng dữ liệu từ nhiều người dùng bằng cách sử dụng chung một môi trường truyền dẫn là điều phổ biến. Trong cấu trúc mạng cục bộ thường gặp như "ngôi sao mở rộng", các đường kết nối giữa thiết bị người dùng (máy tính, máy chủ, máy in) và thiết bị truyền dẫn (switch, router) là riêng biệt, trong khi đó kết nối giữa các thiết bị truyền dẫn là dùng chung vì nó phải xử lý lưu lượng từ nhiều thiết bị người dùng khác nhau. 

Để có thể truyền đồng thời nhiều tín hiệu từ các người dùng qua một cáp duy nhất, các phương pháp ghép kênh (multiplexing) được sử dụng. Các thiết bị truyền dẫn trong trường hợp này cần có khả năng xác định hướng truyền dữ liệu, tức là thực hiện chuyển mạch (*switching*).

Phương pháp ghép kênh đồng bộ và không đồng bộ dựa trên chia sẻ thời gian (TDM) đã trở thành nền tảng cho hai nguyên lý cơ bản của chuyển mạch trong mạng máy tính:
- **Chuyển mạch kênh (circuit switching)**;
- **Chuyển mạch gói (packet switching)**.
---

### 5.1.1 Chuyển Mạch Kênh

**Chuyển mạch kênh** dựa trên TDM đồng bộ. Phương pháp này cung cấp cho mỗi cặp thiết bị đang giao tiếp một chuỗi các kênh (logic) riêng để sử dụng độc quyền.

Trong các mạng sử dụng chuyển mạch kênh, các thiết bị đầu cuối có thể được cung cấp:
- **Kênh chuyển mạch**: Kênh chỉ tồn tại trong thời gian phiên kết nối diễn ra và được giải phóng sau khi phiên kết thúc.
- **Kênh không chuyển mạch**: Kênh cố định, không bị thay đổi theo thời gian.

Kênh liên lạc, nơi dữ liệu được truyền tải, chỉ được thiết lập sau khi kết nối giữa hai hệ thống giao tiếp được hình thành. Những kênh này được gọi là **kênh chuyển mạch** hoặc **kênh tạm thời**. Kênh chỉ tồn tại trong thời gian phiên truyền dữ liệu và sẽ được giải phóng ngay khi phiên kết thúc. Quá trình chuyển mạch chỉ diễn ra vào thời điểm bắt đầu phiên kết nối. Thiết bị khởi tạo sẽ gửi yêu cầu qua mạng đến thiết bị đích, tạo ra một chuỗi kênh liên tiếp để kết nối chúng. 

 Ưu điểm và nhược điểm
- **Ưu điểm**: Chi phí thấp.
- **Nhược điểm**: Thời gian chờ kết nối lâu và khả năng bị chặn khi kênh bị "bận".

 Ví dụ thực tế
Một ví dụ điển hình của chuyển mạch kênh là **hệ thống điện thoại cố định**. Người dùng phải quay số trước khi bắt đầu cuộc gọi, và một kênh liên lạc liên tục được thiết lập thông qua các bộ chuyển mạch trung gian. Trong thời gian kênh được thiết lập, không thiết bị nào khác có thể sử dụng cùng kênh này. Sau khi kết thúc cuộc gọi, kết nối bị phá vỡ và kênh được giải phóng.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/5_1.png" alt="Hình minh họa 5.1: Quá trình chuyển mạch kênh." width="1000">
</p>
<p align="center"><b>Hình minh họa 5.1: Quá trình chuyển mạch kênh.</b></p>


Các kênh liên lạc giữa các hệ thống đầu cuối, sẵn sàng để truyền dữ liệu trong thời gian dài nhờ vào kết nối cố định với các đặc tính được chỉ định, được gọi là **kênh chuyên dụng (dedicated channels)** hoặc **kênh không chuyển mạch (non-switched channels)**. Kênh chuyên dụng còn được gọi là **kênh thuê bao (leased channels)**, luôn sẵn sàng cho việc truyền dữ liệu. Tuy nhiên, chi phí của các kênh này cao hơn so với **kênh chuyển mạch (switched channels)**.

Trong TDM đồng bộ (*synchronous TDM*), thời gian hoạt động của kênh vật lý được chia thành các chu kỳ lặp lại, bao gồm các khung TDM (*TDM frames*). Mỗi khung TDM bắt đầu bằng một chuỗi đồng bộ hóa (*synchronization sequence*) và bao gồm các khe thời gian (*time slots*) có độ dài bằng nhau, mỗi khe thời gian được gán cho một kênh logic riêng. Các khe thời gian được phân bổ cho tất cả các kênh đầu vào (*input channels*), được đánh số và sắp xếp theo thứ tự trong khung TDM. Các kênh đầu vào lần lượt truyền các khối dữ liệu có kích thước bằng nhau trong mỗi chu kỳ để thiết bị truyền tải ở đầu bên kia có thể hiểu đúng và định tuyến dữ liệu đến địa chỉ tương ứng.

Để thực hiện điều này, thiết bị truyền tải cần duy trì một bảng chuyển mạch (*switching table*), bảng này xác định mối quan hệ giữa:
- Cổng thuê bao đầu vào (*incoming subscriber port*) và cổng/khung thời gian đầu ra trên đường trục (*outgoing trunk port/time slot*);
- Cổng đường trục đầu vào (*incoming trunk port*) và cổng/khung thời gian đầu ra trên đường trục trung gian (*outgoing trunk port/time slot*), nếu dữ liệu được truyền qua các nút trung gian;
- Cổng đường trục đầu vào và cổng thuê bao đầu ra (*outgoing subscriber port*).

Do các hệ thống giao tiếp nhận dữ liệu trong cùng một chu kỳ và với cùng một số khe thời gian, các khối dữ liệu truyền đến phía nhận trong cùng một khoảng thời gian với độ trễ tối thiểu. Vì vậy, mạng sử dụng chuyển mạch kênh (*circuit-switched networks*) rất phù hợp cho việc truyền tải lưu lượng thoại (*voice traffic*) hoặc lưu lượng dữ liệu (*data traffic*) đồng bộ.

 Nhược điểm của chuyển mạch kênh
Một trong những nhược điểm chính của mạng chuyển mạch kênh là việc sử dụng không hiệu quả băng thông (*bandwidth inefficiency*). Trong thời gian phiên kết nối, các khe thời gian trong kênh được phân bổ nhưng không phải lúc nào cũng được sử dụng đầy đủ, dẫn đến việc các kênh còn lại không được khai thác hiệu quả.

---

### 5.1.2 Chuyển Mạch Gói

**Công nghệ chuyển mạch gói (Packet Switching)** dựa trên việc sử dụng **TDM không đồng bộ (asynchronous TDM)** hoặc **TDM thống kê (statistical TDM)**. Phương pháp này cho phép các hệ thống đầu cuối truyền dữ liệu qua mạng mà không cần chiếm dụng độc quyền kênh truyền dẫn, ngay cả trong suốt phiên kết nối. Dữ liệu được chia thành các khối nhỏ hơn, gọi là **gói (packet)**, và được truyền qua cùng một kênh dựa trên nhu cầu, không phụ thuộc vào nguồn gốc và đích đến của chúng. Các hệ thống giao tiếp chỉ chiếm dụng kênh trong thời gian cần thiết để truyền gói.

 Cơ chế hoạt động
Khác với **TDM đồng bộ (synchronous TDM)**, trong TDM không đồng bộ không có sự gắn kết cố định giữa khe thời gian (*time slots*) và thiết bị đích. Do đó, trong mạng sử dụng chuyển mạch gói, các khối dữ liệu cần được cung cấp thông tin định tuyến (**addressing information**). Mỗi gói dữ liệu bao gồm hai phần:
- **Tiêu đề (header)**: Chứa thông tin quản lý cần thiết để truyền gói, như địa chỉ, thứ tự gói, v.v.;
- **Dữ liệu (payload)**: Chứa thông tin cần truyền.

Thứ tự truyền gói, kích thước gói, và nội dung cụ thể của tiêu đề được xác định bởi giao thức mạng. Vì vậy, không giống như TDM đồng bộ, TDM không đồng bộ không minh bạch với các giao thức. Trong mạng chuyển mạch gói, cả thiết bị đầu cuối và thiết bị truyền dẫn (như **switches** và **routers**) đều phải hỗ trợ cùng một giao thức.

 Đặc điểm của gói dữ liệu
Thuật ngữ "gói" trong trường hợp này được dùng để chỉ khối dữ liệu được truyền. Ở mỗi tầng mạng, khối dữ liệu này được gọi bằng tên khác nhau:
- Ở **tầng liên kết dữ liệu (Data Link Layer)**: gọi là **khung (frame)**;
- Ở **tầng mạng (Network Layer)**: gọi là **gói (packet)** hoặc **datagram**;
- Ở **tầng vận chuyển (Transport Layer)**: gọi là **đoạn (segment)**.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/5_2.png" alt="Hình 5.2 quá trình chuyển mạch gói" width="1000">
</p>
<p align="center"><b>Hình 5.2 quá trình chuyển mạch gói</b></p>


