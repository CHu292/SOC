# Mô hình tương tác mạng

## 2.1 Mô hình OSI

Vào cuối thập niên 1970, hai dự án độc lập đã được khởi động nhằm xác định tiêu chuẩn thống nhất cho kiến trúc của các hệ thống mạng. Một dự án được thực hiện bởi Tổ chức Tiêu chuẩn hóa Quốc tế (International Organization for Standardization, ISO), và dự án kia do Ủy ban Cố vấn Quốc tế về Điện báo và Điện thoại (International Telegraph and Telephone Consultative Committee, CCITT) thực hiện. Cả hai tổ chức đều phát triển các tài liệu mô tả các mô hình mạng tương tự nhau. Vào năm 1983, những tài liệu này đã được hợp nhất thành một tiêu chuẩn gọi là "Mô hình tham chiếu cơ bản cho kết nối hệ thống mở" (The Basic Reference Model for Open Systems Interconnection). Tiêu chuẩn này, thường được gọi là mô hình tham chiếu OSI (Open Systems Interconnection Reference Model) hoặc mô hình OSI, đã được ISO công bố (dưới tên ISO 7498) và CCITT (dưới tên X.200) vào năm 1984. Hiện tại, CCITT được gọi là ITU-T (Sektor Tiêu chuẩn hóa Viễn thông của Liên minh Viễn thông Quốc tế).

Mô hình tham chiếu kết nối hệ thống mở hoặc mô hình OSI xác định các lớp của hệ thống tương tác, tên gọi chuẩn và các chức năng mà mỗi lớp phải thực hiện.

Ban đầu, mô hình OSI được tạo ra như là cơ sở để phát triển một bộ giao thức phổ quát, gọi là Bộ giao thức OSI (OSI Protocol Suite). Tuy nhiên, nó không được phổ biến rộng rãi, nhưng mô hình này đã trở thành một công cụ hữu ích cho việc học tập các công nghệ mạng và phát triển các giao thức và thiết bị.

## 2.2 Các lớp của mô hình OSI

Mô hình OSI chia nhiệm vụ truyền thông tin giữa các nút thành bảy cấp độ, mỗi cấp độ thực hiện một nhiệm vụ cụ thể và tương tác với các cấp độ phía trên và phía dưới. Các cấp độ tương đối độc lập với nhau, vì vậy các nhiệm vụ liên quan đến từng cấp độ có thể được thực hiện một cách độc lập. Điều này cho phép thay đổi cách giải quyết các vấn đề ở một cấp độ mà không gây xung đột với các cấp độ khác. Việc phân chia theo cấp độ này được gọi là biểu diễn phân cấp, vì vậy mô hình OSI thường được gọi là mô hình phân cấp.


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/2_Network_interaction_models/image/2_1_OSI_model.png" alt="Hình 2.1 - OSI model" width="1000">
</p>
<p align="center"><b>Mô hình OSI</b></p>

- Các lớp dưới của mô hình OSI (từ tầng 1 đến tầng 3) quản lý việc truyền tải vật lý dữ liệu qua mạng và được triển khai dưới dạng phần cứng và phần mềm.

- Các lớp trên của mô hình OSI (4 đến 7) cho phép phân phối dữ liệu chính xác giữa các ứng dụng chạy trên các nút mạng và thường chỉ được triển khai trong phần mềm.

- Mỗi lớp, ngoại trừ lớp ứng dụng, cung cấp các dịch vụ cho lớp trên. Bất kỳ lớp nào ngoài lớp vật lý đều sử dụng các dịch vụ được cung cấp bởi lớp bên dưới. Nói cách khác, lớp N cung cấp dịch vụ cho lớp N+1 và sử dụng các dịch vụ từ lớp N-1

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/2_Network_interaction_models/image/2_2_services_provided_by_the_layers_of_the_OSI_model.png" alt="Các dịch vụ được cung cấp bởi các lớp của mô hình OSI" width="1000">
</p>
<p align="center"><b>Hình 2.2 - Các dịch vụ được cung cấp bởi các lớp của mô hình OSI</b></p>

- Mô hình OSI không mô tả các dịch vụ và giao thức được sử dụng ở mỗi lớp, nó xác định một tập hợp các hành động mà lớp đó phải thực hiện để truyền thông tin giữa các nút. Tuy nhiên, ISO cũng đã phát triển các tiêu chuẩn cho từng cấp độ không có trong mô hình tham chiếu mà mỗi cấp độ được công bố dưới dạng Tiêu chuẩn quốc tế riêng biệt.


### 2.2.1 Tương tác giữa các lớp

- Mô hình OSI xác định sơ đồ trao đổi dữ liệu giữa các nút mạng, nhưng bản thân nó không phải là một phương thức trao đổi như vậy. Trao đổi dữ liệu được thực hiện nhờ các giao thức.
- **Giao thức-protocol** là một bộ quy tắc và thỏa thuận chính thức chi phối việc trao đổi thông tin giữa các nút trên mạng. Nó thực hiện các chức năng của một hoặc nhiều lớp OSI.
- Có một số lượng lớn các giao thức trao đổi dữ liệu - *giao thức mạng cục bộ và toàn cầu, giao thức định tuyến, giao thức mạng.*
- **Các giao thức mạng cục bộ-local network protocol** hoạt động ở cấp độ liên kết vật lý và dữ liệu của mô hình OSI và xác định các quy tắc trao đổi dữ liệu qua các kênh liên lạc khác nhau được sử dụng trong mạng cục bộ.
- **Các giao thức mạng toàn cầu-global network protocol** xác định các quy tắc trao đổi dữ liệu qua các kênh truyền thông mạng toàn cầu khác nhau.
- **Giao thức định tuyến-routing protocol** là các giao thức hoạt động ở lớp mạng của mô hình OSI và cho phép bạn xác định tuyến đường tốt nhất để truyền dữ liệu giữa các nút.
- **Các giao thức mạng-network protocol** bao gồm các giao thức khác nhau hoạt động ở cấp độ mạng trở lên.

- Theo mô hình OSI, mỗi cấp độ của nút gửi thông tin một cách hợp lý (theo chiều ngang) tương tác với cấp độ tương tự của nút nhận thông tin theo quy tắc của một giao thức cụ thể. Mỗi cấp độ “dường như” tương tác trực tiếp với cùng cấp độ của một nút khác. Điều này cho phép tương tác giữa trình duyệt Web và máy chủ Web, ứng dụng email và máy chủ email, v.v.

- Tuy nhiên, kết nối vật lý của các thiết bị chỉ xảy ra ở lớp vật lý của mô hình OSI; vì vậy, để dữ liệu được truyền qua mạng đến một thiết bị khác, nó phải "xuống" từ lớp ứng dụng xuống lớp vật lý trong nút truyền. Khi dữ liệu được truyền qua kênh liên lạc, lớp vật lý của thiết bị nhận sẽ trích xuất nó từ môi trường truyền và chuyển lên lớp trên. Do đó, sự tương tác thực sự của các lớp cùng tên diễn ra theo chiều dọc thông qua việc tương tác với các lớp liền kề (lớp dưới và lớp trên) của ngăn xếp giao thức-protocol stack của chúng.
- **Ngăn xếp giao thức-protocol stack** là tập hợp các giao thức ở các cấp độ khác nhau. Nổi tiếng nhất là ngăn xếp giao thức TCP/IP.
- Các quy tắc và thủ tục chịu trách nhiệm tương tác giữa các lớp liền kề được gọi là giao diện - interfaces.
- Thông tin dữ liệu và dịch vụ được truyền giữa các cấp theo cả hai hướng. Có các giao diện nổi tiếng giữa các lớp, cho phép chúng giao tiếp với nhau mà không cần suy nghĩ về việc triển khai.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/2_Network_interaction_models/image/2_3_Interaction_between_levels.png" alt="Tương tác giữa các lớp" width="1000">
</p>
<p align="center"><b>Hình 2.3 - Tương tác giữa các lớp</b></p>

### 2.2.2 Đóng gói dữ liệu - Data Encapsulation

- Sự tương tác giữa các lớp giống nhau trong mô hình OSI được thực hiện theo logic bằng cách sử dụng các quy tắc của từng giao thức cụ thể. Sự tương tác này diễn ra dưới dạng truyền tin nhắn, gọi là các đơn vị dữ liệu giao thức (protocol data units, PDU). Mỗi PDU có một định dạng đặc biệt, được xác định theo các chức năng và yêu cầu của giao thức cụ thể.
- Để tổ chức việc truyền dữ liệu, giao thức của tầng N phải chuyển PDU xuống tầng dưới N-1. Giao thức của tầng N-1 sẽ cung cấp dịch vụ cho tầng trên N, tức là nó sẽ nhận PDU của giao thức tầng N, thứ sẽ trở thành dữ liệu cho tầng N-1, xử lý chúng và tiếp tục chuyển xuống tầng N-2. Ở tầng N-1, PDU của giao thức tầng N sẽ được gọi là đơn vị dữ liệu dịch vụ (service data unit, SDU). Để cung cấp dịch vụ, giao thức của tầng N-1 đặt SDU nhận được từ tầng N vào trường dữ liệu của PDU của mình và thêm thông tin điều khiển (header và/hoặc trailer) cần thiết cho giao thức để thực hiện chức năng của nó. Quá trình này được gọi là đóng gói dữ liệu (data encapsulation).
- Đóng gói (Encapsulation) là quá trình trong đó thông tin điều khiển của một giao thức (của tầng) được thêm vào dữ liệu trước khi gửi vào mạng.
- Các thuật ngữ đặc biệt được sử dụng để chỉ định PDU của một số giao thức. PDU của giao thức TCP, hoạt động ở tầng vận chuyển (transport) của mô hình OSI và ngăn xếp TCP/IP, được gọi là đoạn (segment). PDU của giao thức IP, hoạt động ở tầng mạng của mô hình OSI và tầng Internet của ngăn xếp TCP/IP, được gọi là gói tin (packet) hoặc datagram IP. Ở tầng liên kết dữ liệu (data link) của mô hình OSI và tầng truy cập mạng (network access) của ngăn xếp TCP/IP, PDU được gọi là khung (frame).
- Hãy xem xét quá trình đóng gói dữ liệu khi truyền dữ liệu giữa các nút, được minh họa trong Hình 2.4. Khi một ứng dụng trên máy tính A gửi tin nhắn đến ứng dụng trên máy tính B, nó sẽ chuyển tin nhắn này đến tầng ứng dụng của máy tính A. Sau đó, từ tầng ứng dụng, dữ liệu được truyền xuống tầng trình bày, rồi gửi xuống tầng phiên. Tầng phiên chuyển tiếp dữ liệu đến tầng vận chuyển, và tầng này tạo ra một đoạn (segment) bằng cách thêm thông tin điều khiển, rồi chuyển nó đến tầng mạng của mô hình OSI. Tầng mạng nhận đoạn đó và thêm tiêu đề của mình, hình thành một gói tin (packet), rồi chuyển gói tin xuống tầng dưới. Tầng liên kết dữ liệu tạo ra một khung (frame) bằng cách thêm tiêu đề và phần cuối của tầng liên kết dữ liệu, sau đó chuyển khung này đến tầng vật lý. Ở tầng vật lý, luồng bit được chuyển đổi thành các tín hiệu điện, điện từ, hoặc quang học và được gửi qua môi trường truyền dẫn đến máy tính B.

- Tầng vật lý của máy tính B nhận các tín hiệu từ môi trường truyền dẫn và trích xuất thông tin từ các tín hiệu đó dưới dạng luồng bit. Sau đó, từ luồng bit này, một khung (frame) được tạo ra và truyền lên tầng liên kết dữ liệu. Tầng liên kết dữ liệu nhận khung và phân tích thông tin điều khiển được gửi đến nó. Nếu không có lỗi nào, tầng liên kết dữ liệu sẽ trích xuất dữ liệu từ thông điệp, được gửi lên tầng mạng, và chuyển dữ liệu này lên tầng trên. Quá trình này lặp lại ở mỗi tầng phía trên cho đến tầng ứng dụng. Tầng ứng dụng của máy tính B truyền thông tin đến ứng dụng đích và quá trình trao đổi dữ liệu hoàn tất. Nói cách khác, khi thông điệp đến nút nhận, nó sẽ đi qua tất cả các tầng theo thứ tự ngược lại (từ tầng 1 đến tầng 7), lần lượt được chuyển đổi tại mỗi tầng bằng cách sử dụng thông tin điều khiển tương ứng, cho đến khi đến ứng dụng đích. Quá trình này được gọi là giải đóng gói dữ liệu (decapsulation).

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/2_Network_interaction_models/image/2_4_Data_exchange_between_network_nodes_according_to_the_OSI_model.png" alt="Trao đổi dữ liệu giữa các nút mạng theo mô hình OSI" width="1000">
</p>
<p align="center"><b>Hình 2.4 - Trao đổi dữ liệu giữa các nút mạng theo mô hình OSI</b></p>


  
