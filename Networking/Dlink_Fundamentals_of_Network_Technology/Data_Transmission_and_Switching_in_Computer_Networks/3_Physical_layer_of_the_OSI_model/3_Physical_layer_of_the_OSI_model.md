# 3 Lớp vật lý của mô hình OSI
Lớp vật lý (Physical) là lớp thấp nhất trong mô hình OSI. Nó thực hiện việc truyền một luồng bit nhận được từ lớp liên kết (Data Link) thông qua môi trường vật lý dưới dạng tín hiệu điện, quang học hoặc vô tuyến. Lớp vật lý chịu trách nhiệm thiết lập, duy trì và hủy kích hoạt kênh giữa các hệ thống đầu cuối, xác định các kênh, thông báo về việc xảy ra lỗi và lỗi, đồng thời, nếu cần, lắng nghe các kênh để xác định hoạt động trong đó. Liên minh Viễn thông Quốc tế (International Telecommunication Union - ITU) đã áp dụng một số tiêu chuẩn lớp vật lý. Các tiêu chuẩn lớp vật lý do Liên minh Công nghiệp Điện tử (Electronics Industries Alliance- EIA) và Hiệp hội Công nghiệp Viễn thông (Telecommunications Industry Association, - TIA) phát triển được biết đến và sử dụng rộng rãi. Thông số kỹ thuật của lớp vật lý mô tả chi tiết các giao diện cơ, quang, điện, chức năng với môi trường truyền dẫn: điện áp, tần số, bước sóng, đầu nối, số lượng và chức năng của các tiếp điểm, sơ đồ mã hóa tín hiệu, v.v. Lớp vật lý cũng xem xét các vấn đề liên quan đến cấu trúc liên kết vật lý của mạng.


## 3.1 Khái niệm về đường truyền và kênh liên lạc

Đường truyền thông được sử dụng để truyền tín hiệu giữa các hệ thống tương tác trong mạng máy tính.

Theo nghĩa hẹp, thuật ngữ liên kết truyền tải hoặc **đường truyền** (transmission link, link) dùng để chỉ môi trường vật lý mà qua đó tín hiệu được truyền giữa hai hệ thống đầu cuối. Tín hiệu được tạo ra bằng các phương tiện kỹ thuật đặc biệt (máy phát, bộ khuếch đại, bộ ghép kênh, v.v.) liên quan đến thiết bị mạng.

**Môi trường truyền dẫn (transmission medium)** hoặc môi trường vật lý là một chất liệu mà qua đó tín hiệu được truyền đi.

Mạng máy tính sử dụng hai loại phương tiện truyền dẫn: cáp và không dây.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_1_Types_of_transmission_media.png" alt="Hình 3.1 - Các loại phương tiện truyền dẫn" width="1000">
</p>
<p align="center"><b>Hình 3.1 - Các loại phương tiện truyền dẫn"</b></p>

Cơ sở của phương tiện truyền dẫn không dây là bầu khí quyển của trái đất hoặc không gian bên ngoài mà sóng điện từ lan truyền qua đó. Phương tiện truyền dẫn cáp sử dụng nhiều loại cáp: cáp đồng trục, cáp quang, cáp xoắn đôi. Việc truyền dữ liệu tới chúng được thực hiện bằng tín hiệu điện (dòng điện) hoặc tín hiệu quang (ánh sáng).

Theo nghĩa rộng, thuật ngữ “đường truyền - communication line” trong lĩnh vực mạng máy tính dùng để chỉ một kênh liên lạc.

**Kênh liên lạc (channel, data link)** là một tập hợp gồm một hoặc nhiều phương tiện truyền dẫn vật lý và thiết bị tạo kênh (mạng) cung cấp khả năng truyền dữ liệu giữa các hệ thống tương tác dưới dạng tín hiệu tương ứng với loại phương tiện vật lý.

Trong bối cảnh này, thuật ngữ "đường truyền" và "kênh liên lạc" là đồng nghĩa.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_2_Communication_channel.png" alt="Hình 3.2 - Kênh liên lạc" width="1000">
</p>
<p align="center"><b>Hình 3.2 - Kênh liên lạc</b></p>

Có các kênh **vật lý (physical link)** và **kênh logic (logical link)**. Kênh liên lạc vật lý là phương tiện truyền tín hiệu giữa các hệ thống tương tác. Tùy thuộc vào loại tín hiệu truyền và môi trường vật lý được sử dụng để phân phối, các kênh vật lý được chia thành điện (cặp xoắn, cáp đồng trục), quang (cáp quang) và không dây (kênh vô tuyến, kênh hồng ngoại, v.v.).

Các kênh logic được thiết lập giữa các giao thức của bất kỳ lớp nào trong mô hình OSI của các hệ thống tương tác và xác định đường dẫn dữ liệu được truyền từ nguồn đến máy thu thông qua một hoặc một chuỗi các kênh vật lý.

Khi đặt một số kênh logic trong một kênh vật lý, tài nguyên của kênh vật lý được phân phối giữa các kênh logic bằng phương pháp ghép kênh.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_3_Physical_and_logical_communication_channels.png" alt="Hình 3.3 - Các kênh truyền thông vật lý và logic" width="1000">
</p>
<p align="center"><b>Hình 3.3 - Các kênh truyền thông vật lý và logic</b></p>


Các kênh truyền liên lạc (đường truyền) có thể được phân loại dựa trên các đặc điểm sau:

- theo loại môi trường vật lý;
- theo kiểu trình bày thông tin được truyền đi;
- theo hướng truyền dữ liệu;
- theo thời gian tồn tại;
- bằng phương thức kết nối;
- về mặt băng thông.

Tùy thuộc vào loại trình bày thông tin được truyền, các kênh được chia thành kênh analog (liên tục), dành cho việc truyền tín hiệu liên tục và **rời rạc**, được sử dụng để truyền tín hiệu rời rạc (kỹ thuật số).

Tùy thuộc vào hướng truyền dữ liệu, các kênh được phân biệt:

- đơn giản (**simplex**), là chế độ truyền tín hiệu đơn giản và hiệu quả, được sử dụng trong các ứng dụng yêu cầu giao tiếp một chiều.
- bán song công (**half-duplex**),  là chế độ truyền tín hiệu hiệu quả, được sử dụng trong các ứng dụng yêu cầu giao tiếp hai chiều nhưng không đồng thời.
- song công (**full duplex**), là chế độ truyền tín hiệu hiệu suất cao, được sử dụng trong các ứng dụng yêu cầu giao tiếp hai chiều đồng thời.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_4_Simplex.png" alt="Hình 3.4 - Simplex" width="1000">
</p>
<p align="center"><b>"Hình 3.4 - Simplex</b></p>


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_5_half_duplex.png" alt="Hình 3.5 - Half Duplex" width="1000">
</p>
<p align="center"><b>"Hình 3.5 - Half Duplex</b></p>

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_6_Full_Duplex.png" alt="Hình 3.6 - Full Duplex" width="1000">
</p>
<p align="center"><b>"Hình 3.6 - Full Duplex</b></p>


Các kênh cũng có thể được phân loại theo thời gian sẵn có của người đăng ký. Các kênh giữa các hệ thống đầu cuối có sẵn để truyền dữ liệu dài hạn nhờ kết nối cố định với các đặc tính cụ thể được gọi là **kênh chuyên dụng (dedicated)** hoặc **kênh không chuyển mạch (non-switched)**. Các kênh liên lạc chỉ có thể truyền dữ liệu sau khi thiết lập kết nối giữa các hệ thống tương tác được gọi là **kênh chuyển mạch (switched)** hoặc **kênh tạm thời (temporary)**. Kênh này chỉ tồn tại trong suốt phiên kết nối, tức là chỉ trong thời gian cần thiết để truyền dữ liệu.

Theo phương thức kết nối, các kênh được chia thành: “điểm-điểm” **(point-to-point)**, “điểm-đa điểm” **(point-to-multipoint)**, “đa điểm” **(multipoint)**. Liên kết point-to-point chỉ kết nối hai nút hoặc hai hệ thống truyền thông. Liên kết point-to-multipoint kết nối một hệ thống trung tâm node (nút) với một nhóm các hệ thống node (nút) khác. Liên kết multipoint cho phép một nhóm nút hoặc hệ thống kết nối với nhau.

Một đặc tính quan trọng của kênh liên lạc là **băng thông (bandwidth)** của nó. Tùy thuộc vào băng thông (sự khác biệt giữa tần số cắt của băng thông) và phương thức truyền tín hiệu, các kênh được chia thành kênh **băng thông cơ sở (baseband channel)** và kênh **băng thông rộng (broadband channel)**.

Kênh băng thông cơ sở được đặc trưng bởi sự đơn giản và chi phí triển khai thấp và do đó được sử dụng rộng rãi trong các mạng cục bộ (từ “BASE” trong tên của các thông số kỹ thuật của lớp vật lý Ethernet (ví dụ: 10BASE-T, 100BASE-FX, 1000BASE-SX ) biểu thị việc truyền băng cơ sở). Tín hiệu qua kênh băng thông cơ sở được truyền trong tần số cở bản, tức là không điều chế sóng mang, với toàn bộ băng thông chỉ được sử dụng để truyền một tín hiệu.

Không giống như kênh băng thông cơ sở, toàn bộ băng thông của kênh băng rộng được phân chia giữa một số kênh logic bằng kỹ thuật ghép kênh, cho phép tín hiệu được truyền đồng thời và độc lập giữa nhiều cặp hệ thống liên lạc. Các công nghệ truy cập băng thông rộng (ví dụ: xDSL, PowerLine (PLC), 3G (UMTS), 4G (LTE)) được sử dụng để tổ chức kết nối với một loạt dịch vụ do các nhà khai thác viễn thông cung cấp.
