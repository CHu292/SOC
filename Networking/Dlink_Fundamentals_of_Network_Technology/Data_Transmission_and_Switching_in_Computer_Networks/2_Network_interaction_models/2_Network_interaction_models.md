# Mô hình tương tác mạng

## 2.1 Mô hình OSI

Vào cuối thập niên 1970, hai dự án độc lập đã được khởi động nhằm xác định tiêu chuẩn thống nhất cho kiến trúc của các hệ thống mạng. Một dự án được thực hiện bởi Tổ chức Tiêu chuẩn hóa Quốc tế (International Organization for Standardization, ISO), và dự án kia do Ủy ban Cố vấn Quốc tế về Điện báo và Điện thoại (International Telegraph and Telephone Consultative Committee, CCITT) thực hiện. Cả hai tổ chức đều phát triển các tài liệu mô tả các mô hình mạng tương tự nhau. Vào năm 1983, những tài liệu này đã được hợp nhất thành một tiêu chuẩn gọi là "Mô hình tham chiếu cơ bản cho kết nối hệ thống mở" (The Basic Reference Model for Open Systems Interconnection). Tiêu chuẩn này, thường được gọi là mô hình tham chiếu OSI (Open Systems Interconnection Reference Model) hoặc mô hình OSI, đã được ISO công bố (dưới tên ISO 7498) và CCITT (dưới tên X.200) vào năm 1984. Hiện tại, CCITT được gọi là ITU-T (Sektor Tiêu chuẩn hóa Viễn thông của Liên minh Viễn thông Quốc tế).

Mô hình tham chiếu kết nối hệ thống mở hoặc mô hình OSI xác định các lớp của hệ thống tương tác, tên gọi chuẩn và các chức năng mà mỗi lớp phải thực hiện.

Ban đầu, mô hình OSI được tạo ra như là cơ sở để phát triển một bộ giao thức phổ quát, gọi là Bộ giao thức OSI (OSI Protocol Suite). Tuy nhiên, nó không được phổ biến rộng rãi, nhưng mô hình này đã trở thành một công cụ hữu ích cho việc học tập các công nghệ mạng và phát triển các giao thức và thiết bị.

## 2.2 Các lớp của mô hình OSI

Mô hình OSI chia nhiệm vụ truyền thông tin giữa các nút thành bảy cấp độ, mỗi cấp độ thực hiện một nhiệm vụ cụ thể và tương tác với các cấp độ phía trên và phía dưới. Các cấp độ tương đối độc lập với nhau, vì vậy các nhiệm vụ liên quan đến từng cấp độ có thể được thực hiện một cách độc lập. Điều này cho phép thay đổi cách giải quyết các vấn đề ở một cấp độ mà không gây xung đột với các cấp độ khác. Việc phân chia theo cấp độ này được gọi là biểu diễn phân cấp, vì vậy mô hình OSI thường được gọi là mô hình phân cấp.


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/2_Network_interaction_models/image/2_1_OSI_model.png" alt="OSI model" width="1000">
</p>
<p align="center"><b>Mô hình OSI</b></p>

- Các lớp dưới của mô hình OSI (từ tầng 1 đến tầng 3) quản lý việc truyền tải vật lý dữ liệu qua mạng và được triển khai dưới dạng phần cứng và phần mềm.

- Các lớp trên của mô hình OSI (4 đến 7) cho phép phân phối dữ liệu chính xác giữa các ứng dụng chạy trên các nút mạng và thường chỉ được triển khai trong phần mềm.

- Mỗi lớp, ngoại trừ lớp ứng dụng, cung cấp các dịch vụ cho lớp trên. Bất kỳ lớp nào ngoài lớp vật lý đều sử dụng các dịch vụ được cung cấp bởi lớp bên dưới. Nói cách khác, lớp N cung cấp dịch vụ cho lớp N+1 và sử dụng các dịch vụ từ lớp N-1

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/2_Network_interaction_models/image/2_2_services_provided_by_the_layers_of_the_OSI_model.png" alt="Các dịch vụ được cung cấp bởi các lớp của mô hình OSI" width="1000">
</p>
<p align="center"><b>Các dịch vụ được cung cấp bởi các lớp của mô hình OSI</b></p>

- Mô hình OSI không mô tả các dịch vụ và giao thức được sử dụng ở mỗi lớp, nó xác định một tập hợp các hành động mà lớp đó phải thực hiện để truyền thông tin giữa các nút. Tuy nhiên, ISO cũng đã phát triển các tiêu chuẩn cho từng cấp độ không có trong mô hình tham chiếu mà mỗi cấp độ được công bố dưới dạng Tiêu chuẩn quốc tế riêng biệt.


