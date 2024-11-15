# Các cấu trúc liên kết (topologies) của mạng máy tính

# 4.1 Khái niệm cấu trúc liên kết mạng (network topology)

Khi tổ chức một **mạng máy tính (computer network)**, một trong những vấn đề quan trọng là lựa chọn **cấu trúc liên kết (topology)** phù hợp, vì cấu hình mạng đúng đắn là cần thiết để đảm bảo hoạt động đáng tin cậy và hiệu quả cho toàn bộ mạng, cũng như khả năng mở rộng trong tương lai với chi phí thấp nhất.

**Cấu trúc liên kết mạng** là phương pháp mô tả cấu hình mạng, sơ đồ bố trí và kết nối các **thiết bị mạng (network devices)**.
Cần phân biệt giữa hai khái niệm **cấu trúc liên kết vật lý (physical topology)**, mô tả vị trí thực tế và kết nối của các nút mạng, và **cấu trúc liên kết logic (logical topology)** - các cách thức tương tác giữa các nút và cách tín hiệu truyền trong mạng theo cấu trúc liên kết vật lý.

Nói cách khác, cấu trúc liên kết vật lý xác định cách các thiết bị được bố trí và kết nối, trong khi cấu trúc liên kết logic xác định cách dữ liệu truyền giữa các thiết bị, bất kể vị trí vật lý của chúng.

**Cấu trúc liên kết logic và vật lý của mạng** không nhất thiết phải trùng khớp. Ví dụ, mạng **Ethernet cục bộ (Ethernet LAN)**, được xây dựng bằng **các hub (concentrators)** và **cáp xoắn đôi (twisted pair cable)** làm phương tiện truyền, có cấu trúc liên kết vật lý dạng **"sao" (star)**, nhưng cấu trúc liên kết logic lại là dạng **"bus" (bus)**. Cấu trúc liên kết logic thường được xác định bởi **các giao thức mạng (network protocols)** và liên quan đến các phương pháp quản lý quyền truy cập vào phương tiện truyền dẫn. Nó có thể được thay đổi linh hoạt nhờ việc sử dụng **thiết bị mạng (network equipment)** như **bộ định tuyến (routers)**, **bộ chuyển mạch (switches)** hoặc **điểm truy cập (access points)**.

Cấu trúc liên kết vật lý phụ thuộc vào vị trí và khả năng của các thiết bị mạng, phương tiện truyền dẫn và chi phí triển khai cơ sở hạ tầng mạng và cáp.

Có các cấu trúc liên kết cơ bản sau, dựa trên đó các mạng máy tính được xây dựng:

- **"bus" (bus)** - cấu trúc liên kết dạng **"dải"**,
- **"ring" (ring)** - cấu trúc liên kết dạng **"vòng"**,
- **"star" (star)** - cấu trúc liên kết dạng **"sao"**,
- **"tree" (tree)** - cấu trúc liên kết dạng **"cây"**,
- **cấu trúc liên kết lưới hoàn toàn kết nối (fully connected mesh)**,
- **cấu trúc liên kết lưới kết nối một phần (partially connected mesh)**.

Trước khi đi vào tìm hiểu các cấu trúc liên kết mạng, hãy cùng làm quen với các thiết bị mạng hỗ trợ việc hình thành cấu trúc của mạng.


# 4.2 Thiết bị mạng trong cấu trúc liên kết (network topology)**

Để xây dựng một **mạng máy tính (computer network)**, cần có **thiết bị mạng hoặc thiết bị viễn thông (network or telecommunication equipment)**, với nhiệm vụ chính là kết nối các máy tính và các thiết bị khác vào mạng, truyền dữ liệu giữa chúng, kết nối các mạng máy tính có cấu trúc liên kết và công nghệ khác nhau với nhau, và tăng khoảng cách truyền tín hiệu. Ngoài ra, thiết bị mạng còn cho phép giải quyết các nhiệm vụ như đảm bảo **an ninh mạng (network security)**, quản lý **dòng dữ liệu (data flow)**, cung cấp **chất lượng dịch vụ (Quality of Service - QoS)**, và nhiều chức năng khác.

Tiếp theo trong phần này sẽ là mô tả ngắn gọn về các **thiết bị mạng (network devices)** được sử dụng trong **mạng cục bộ Ethernet (Ethernet LAN)** và **Wi-Fi**. Việc mô tả các thiết bị sẽ dựa trên chức năng của chúng tương ứng với các tầng của **mô hình OSI (OSI model)**, bắt đầu từ tầng vật lý.

--- 

## 4.2.1 Bộ lặp và Hub (Repeater và Hub)

**Bộ lặp (repeater)** là một trong những thiết bị mạng đơn giản nhất. Nó hoạt động ở **tầng vật lý (physical layer)** (tầng 1) của **mô hình OSI (OSI model)** và được sử dụng để kết nối các phân đoạn của phương tiện truyền dẫn nhằm tăng chiều dài tổng thể của mạng.

Khoảng cách mà tín hiệu từ một thiết bị có thể truyền đến thiết bị khác mà không bị biến dạng là có giới hạn. Điều này xảy ra vì nhiều lý do, một trong số đó là **suy hao tín hiệu (attenuation)**. Suy hao tín hiệu là sự mất mát công suất của tín hiệu. Để xây dựng mạng có độ dài lớn, cần phải khuếch đại tín hiệu ở một số điểm.

Trong các mạng **Ethernet** đầu tiên (10BASE2 và 10BASE5), mỗi máy tính được kết nối với các thiết bị khác thông qua một **cáp đồng trục (coaxial cable)** duy nhất. Các bộ lặp được sử dụng để tăng chiều dài của mạng. Chúng được trang bị hai cổng và kết nối hai phân đoạn vật lý, tức là hai sợi cáp.

Bộ lặp hoạt động như sau: nó nhận tín hiệu từ một phân đoạn mạng, khuếch đại chúng, khôi phục đồng bộ và truyền sang phân đoạn khác. Bộ lặp không xử lý lưu lượng. Tổng số bộ lặp trong mạng và các phân đoạn mà chúng kết nối bị giới hạn do độ trễ thời gian và các nguyên nhân khác.


**Ứng dụng của bộ lặp trong mạng**

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_1_Types_of_transmission_media.png" alt="Hình 4.1 Ứng dụng của bộ lặp trong mạng Ethernet sử dụng cáp đồng trục" width="1000">
</p>
<p align="center"><b>Hình 4.1 Ứng dụng của bộ lặp trong mạng Ethernet sử dụng cáp đồng trục</b></p>


Các thông số kỹ thuật của Ethernet 10BASE2 và 10BASE5 đã lỗi thời và bộ lặp cho các mạng này không còn được sản xuất và sử dụng.

Hiện nay, có các bộ lặp được sản xuất cho **mạng không dây (wireless networks)**.

---

_Hình 4.2 Bộ lặp không dây_

---

**Bộ lặp không dây** khôi phục các tín hiệu vô tuyến để tăng bán kính hoạt động của mạng không dây. Bộ lặp không kết nối vật lý với bất kỳ phần nào của mạng không dây. Thay vào đó, nó nhận tín hiệu từ **điểm truy cập (access point)**, thiết bị khách, **bộ định tuyến không dây (wireless router)** hoặc một bộ lặp khác trên một kênh tần số vô tuyến xác định, khuếch đại và truyền lại trên cùng một kênh, không thay đổi khung tín hiệu. Nói cách khác, bộ lặp nằm giữa điểm truy cập và thiết bị ở xa, hoạt động như một điểm trung chuyển khung tín hiệu giữa chúng. Điều này giúp giảm suy hao của tín hiệu tần số vô tuyến. Hãng D-Link sản xuất các bộ lặp độc lập. Ngoài ra, điểm truy cập có thể được cấu hình để hoạt động ở chế độ bộ lặp.

---

_Hình 4.3 Nguyên lý hoạt động của bộ lặp không dây_

---

Sau khi thông số kỹ thuật **Ethernet 10Base-T** ra đời, mỗi nút được kết nối bằng một cáp riêng biệt dạng **cáp xoắn đôi (twisted pair cable)** tới một thiết bị trung tâm — **hub** (còn gọi là concentrator).

**Hub (concentrator)** là một bộ lặp có nhiều cổng và kết nối nhiều phân đoạn vật lý của mạng (đoạn cáp). Hub hoạt động ở tầng vật lý (tầng 1) của mô hình OSI. Nhiệm vụ chính của nó là lặp lại tín hiệu nhận được từ một cổng sang tất cả các cổng khác, đồng thời khôi phục tín hiệu. Hub cũng không có chức năng xử lý lưu lượng, do đó mạng được xây dựng bằng hub có thể có cấu trúc liên kết vật lý khác nhau, nhưng cấu trúc liên kết logic luôn là dạng **"bus"**.

---

_Hình 4.4 Truyền dữ liệu trong mạng qua hub_

---

Hub tạo ra một môi trường truyền tín hiệu chung cho tất cả các nút trong **mạng cục bộ (LAN)**. Tại một thời điểm, chỉ có một máy tính trong mạng có thể truyền dữ liệu. Nếu tín hiệu đồng thời xuất hiện trên hai hoặc nhiều cổng của hub, sẽ xảy ra **va chạm (collision)**, dẫn đến hư hỏng các khung truyền. Vì vậy, tất cả các thiết bị kết nối với hub nằm trong cùng một **miền va chạm (collision domain)**.

- **Va chạm (collision)**: Là hiện tượng chồng lấn hoặc xung đột tín hiệu xảy ra khi hai hoặc nhiều nút truyền dữ liệu đồng thời, gây hỏng dữ liệu.
- **Miền va chạm (collision domain)**: Là một mạng Ethernet hoạt động ở chế độ bán song công (half-duplex) và sử dụng phương thức truy cập CSMA/CD.

---

_Hình 4.5 Miền va chạm_

---

Khi số lượng phân đoạn mạng và máy tính tăng lên, số lượng va chạm cũng tăng lên. Ngoài ra, số lượng hub và các phân đoạn mạng mà chúng kết nối bị giới hạn do độ trễ thời gian và giảm **băng thông mạng (network bandwidth)**. Hơn nữa, mạng được xây dựng bằng hub có mức độ bảo mật thấp, vì dữ liệu được truyền qua tất cả các cổng, cho phép thông tin truyền trong mạng bị “nghe lén”. Băng thông thấp và mức bảo mật kém dẫn đến việc hub không còn được sử dụng trong các mạng máy tính hiện đại; đầu tiên chúng được thay thế bằng **bridge (cầu nối)**, sau đó là **switch (bộ chuyển mạch)**.
