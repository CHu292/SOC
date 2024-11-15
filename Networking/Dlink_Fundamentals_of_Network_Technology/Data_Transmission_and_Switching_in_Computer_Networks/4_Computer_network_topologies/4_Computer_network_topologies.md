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


# 4.2 Thiết bị mạng trong cấu trúc liên kết (network topology)

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
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_1.png" alt="Hình 4.1 Ứng dụng của bộ lặp trong mạng Ethernet sử dụng cáp đồng trục" width="1000">
</p>
<p align="center"><b>Hình 4.1 Ứng dụng của bộ lặp trong mạng Ethernet sử dụng cáp đồng trục</b></p>


Các thông số kỹ thuật của Ethernet 10BASE2 và 10BASE5 đã lỗi thời và bộ lặp cho các mạng này không còn được sản xuất và sử dụng.

Hiện nay, có các bộ lặp được sản xuất cho **mạng không dây (wireless networks)**.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_2.png" alt="Hình 4.2 Bộ lặp không dây" width="1000">
</p>
<p align="center"><b>Hình 4.2 Bộ lặp không dây</b></p>


**Bộ lặp không dây** khôi phục các tín hiệu vô tuyến để tăng bán kính hoạt động của mạng không dây. Bộ lặp không kết nối vật lý với bất kỳ phần nào của mạng không dây. Thay vào đó, nó nhận tín hiệu từ **điểm truy cập (access point)**, thiết bị khách, **bộ định tuyến không dây (wireless router)** hoặc một bộ lặp khác trên một kênh tần số vô tuyến xác định, khuếch đại và truyền lại trên cùng một kênh, không thay đổi khung tín hiệu. Nói cách khác, bộ lặp nằm giữa điểm truy cập và thiết bị ở xa, hoạt động như một điểm trung chuyển khung tín hiệu giữa chúng. Điều này giúp giảm suy hao của tín hiệu tần số vô tuyến. Hãng D-Link sản xuất các bộ lặp độc lập. Ngoài ra, điểm truy cập có thể được cấu hình để hoạt động ở chế độ bộ lặp.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_3.jpg" alt="Hình 4.3 Nguyên lý hoạt động của bộ lặp không dây" width="1000">
</p>
<p align="center"><b>Hình 4.3 Nguyên lý hoạt động của bộ lặp không dây</b></p>


Sau khi thông số kỹ thuật **Ethernet 10Base-T** ra đời, mỗi nút được kết nối bằng một cáp riêng biệt dạng **cáp xoắn đôi (twisted pair cable)** tới một thiết bị trung tâm — **hub** (còn gọi là concentrator).

**Hub (concentrator)** là một bộ lặp có nhiều cổng và kết nối nhiều phân đoạn vật lý của mạng (đoạn cáp). Hub hoạt động ở tầng vật lý (tầng 1) của mô hình OSI. Nhiệm vụ chính của nó là lặp lại tín hiệu nhận được từ một cổng sang tất cả các cổng khác, đồng thời khôi phục tín hiệu. Hub cũng không có chức năng xử lý lưu lượng, do đó mạng được xây dựng bằng hub có thể có cấu trúc liên kết vật lý khác nhau, nhưng cấu trúc liên kết logic luôn là dạng **"bus"**.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_4.png" alt="Hình 4.4 Truyền dữ liệu trong mạng qua hub" width="1000">
</p>
<p align="center"><b>Hình 4.4 Truyền dữ liệu trong mạng qua hub</b></p>


Hub tạo ra một môi trường truyền tín hiệu chung cho tất cả các nút trong **mạng cục bộ (LAN)**. Tại một thời điểm, chỉ có một máy tính trong mạng có thể truyền dữ liệu. Nếu tín hiệu đồng thời xuất hiện trên hai hoặc nhiều cổng của hub, sẽ xảy ra **va chạm (collision)**, dẫn đến hư hỏng các khung truyền. Vì vậy, tất cả các thiết bị kết nối với hub nằm trong cùng một **miền va chạm (collision domain)**.

- **Va chạm (collision)**: Là hiện tượng chồng lấn hoặc xung đột tín hiệu xảy ra khi hai hoặc nhiều nút truyền dữ liệu đồng thời, gây hỏng dữ liệu.
- **Miền va chạm (collision domain)**: Là một mạng Ethernet hoạt động ở chế độ bán song công (half-duplex) và sử dụng phương thức truy cập CSMA/CD.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_5.png" alt="Hình 4.5 Miền va chạm" width="1000">
</p>
<p align="center"><b>Hình 4.5 Miền va chạm</b></p>


Khi số lượng phân đoạn mạng và máy tính tăng lên, số lượng va chạm cũng tăng lên. Ngoài ra, số lượng hub và các phân đoạn mạng mà chúng kết nối bị giới hạn do độ trễ thời gian và giảm **băng thông mạng (network bandwidth)**. Hơn nữa, mạng được xây dựng bằng hub có mức độ bảo mật thấp, vì dữ liệu được truyền qua tất cả các cổng, cho phép thông tin truyền trong mạng bị “nghe lén”. Băng thông thấp và mức bảo mật kém dẫn đến việc hub không còn được sử dụng trong các mạng máy tính hiện đại; đầu tiên chúng được thay thế bằng **bridge (cầu nối)**, sau đó là **switch (bộ chuyển mạch)**.

---

## 4.2.2 Cầu nối (Bridge)

Cầu nối (bridge) được phát triển bởi công ty Digital Equipment Corporation (DEC) vào đầu những năm 1980 và là thiết bị hoạt động trên tầng vật lý (Physical Layer) và tầng liên kết dữ liệu (Data Link Layer) của mô hình OSI, dùng để kết nối hai mạng cục bộ (LAN) hoặc hai phân đoạn của cùng một mạng.

Không giống như bộ tập trung (hub) chỉ tăng cường và khôi phục dạng tín hiệu khi truyền từ cổng này sang cổng khác, cầu nối có các chức năng thông minh. Nó chỉ truyền qua các khung (frame - khối dữ liệu ở tầng liên kết dữ liệu) khi cần thiết, nghĩa là khi địa chỉ vật lý (MAC address - địa chỉ MAC) của thiết bị đích thuộc về phân đoạn mạng khác hoặc mạng khác. Cầu nối thực hiện điều này bằng cách sử dụng một bảng chuyển mạch được lưu trữ trong bộ nhớ - một bảng tương ứng giữa các cổng của nó và các địa chỉ MAC được sử dụng trong mỗi mạng hoặc phân đoạn mạng, bảng này được thiết lập ngay sau khi bật nguồn. Nhờ vậy, cầu nối cách ly lưu lượng của một phân đoạn mạng khỏi phân đoạn khác, giảm thiểu các va chạm (collision) bằng cách chia một miền va chạm lớn thành hai miền nhỏ hơn, từ đó cải thiện hiệu suất tổng thể của mạng. Cầu nối cũng làm giảm khả năng truy cập trái phép vào dữ liệu vì các khung không rời khỏi phân đoạn của nó, giúp khó bị tin tặc chặn lại hơn.



**Minh họa về kết nối hai phân đoạn mạng thông qua cầu nối**

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_6.png" alt="Hình 4.6 Kết nối hai phân đoạn mạng bằng cầu nối" width="1000">
</p>
<p align="center"><b>Hình 4.6 Kết nối hai phân đoạn mạng bằng cầu nối</b></p>


Hiện nay, các cầu nối được sản xuất cho mạng không dây. Với các cầu nối không dây (wireless bridges), có thể kết nối các mạng có dây ở khoảng cách gần như các tòa nhà liền kề hoặc các phòng trong cùng một tòa nhà, hoặc ở khoảng cách lên tới vài km.

Các cầu nối được thiết kế để sử dụng trong nhà cho phép kết nối từ một đến nhiều thiết bị không có giao diện không dây vào mạng không dây. Ví dụ, chúng rất hữu ích khi kết nối các thiết bị như máy in hoặc máy chơi game, vốn chỉ có cổng Ethernet.


**Ví dụ về việc sử dụng cầu nối không dây**

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_7.png" alt="Hình 4.7 Ví dụ về việc sử dụng cầu nối không dây" width="1000">
</p>
<p align="center"><b>Hình 4.7 Ví dụ về việc sử dụng cầu nối không dây</b></p>


---


## 4.2.3 Bộ chuyển mạch (Switches)

Các bộ cầu nối (bridge) cho mạng có dây hiện đã lỗi thời và được thay thế bằng các bộ chuyển mạch (switch). Bộ chuyển mạch là một cầu nối đa cổng (multi-port bridge) và hoạt động tương tự trong việc xử lý dữ liệu, nhưng hỗ trợ nhiều tính năng bổ sung hơn so với cầu nối. Bộ chuyển mạch hoạt động ở tầng liên kết dữ liệu (data link layer, tầng thứ hai) của mô hình OSI và được sử dụng để kết nối các thiết bị mạng trong cùng một hoặc nhiều phân đoạn (segment) của mạng.

---
Các thiết bị mạng có thể hoạt động trên một hoặc nhiều tầng của mô hình OSI. Thông thường khi mô tả thiết bị mạng, người ta sẽ nhắc đến tầng cao nhất của mô hình OSI mà thiết bị đó hỗ trợ. Điều này ngụ ý rằng thiết bị cũng có thể hoạt động trên các tầng thấp hơn. Ví dụ, khi nói rằng bộ chuyển mạch là thiết bị tầng liên kết dữ liệu (tầng thứ hai của OSI), tức là nó thực hiện các chức năng của cả tầng vật lý và tầng liên kết dữ liệu.
---

Bộ chuyển mạch có thể được trang bị nhiều cổng và thiết lập nhiều kết nối đồng thời giữa các cặp cổng khác nhau, cho phép các thiết bị kết nối với nó giao tiếp cùng lúc.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_8.png" alt=" Hình 4.8: Ứng dụng của bộ chuyển mạch trong mạng" width="1000">
</p>
<p align="center"><b> Hình 4.8: Ứng dụng của bộ chuyển mạch trong mạng</b></p>



Khi truyền khung (frame) qua bộ chuyển mạch, một kênh ảo hoặc thực (tùy theo kiến trúc) sẽ được tạo ra, qua đó dữ liệu được truyền trực tiếp từ cổng nguồn đến cổng đích với tốc độ cao nhất có thể theo công nghệ sử dụng. Nguyên tắc hoạt động này được gọi là "vi phân đoạn" (microsegmentation).

---
**Vi phân đoạn (microsegmentation)** là quá trình mà bộ chuyển mạch chia một miền va chạm (collision domain) của mạng LAN thành các miền nhỏ hơn cho mỗi cổng.
---

Nhờ vi phân đoạn, các bộ chuyển mạch có thể hoạt động ở chế độ song công toàn phần (full duplex), cho phép mỗi nút kết nối trực tiếp với cổng của bộ chuyển mạch có thể truyền và nhận dữ liệu đồng thời. Do đó, chế độ song công toàn phần đã loại bỏ khái niệm về miền va chạm (collision domain). Các nút không còn phải cạnh tranh băng thông với các thiết bị khác, nhờ đó không xảy ra va chạm và hiệu suất mạng được cải thiện.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_9.png" alt="Hình 4.9: Vi phân đoạn" width="1000">
</p>
<p align="center"><b>Hình 4.9: Vi phân đoạn</b></p>


Bộ chuyển mạch truyền dữ liệu dựa trên bảng chuyển mạch (switching table), giống như cầu nối, cho phép nó cô lập lưu lượng trong các phân đoạn mạng. Khi nhận được khung, bộ chuyển mạch sẽ trích xuất địa chỉ MAC (MAC address) của đích và tìm kiếm địa chỉ này trong bảng chuyển mạch. Khi tìm thấy một bản ghi trong bảng chuyển mạch kết hợp địa chỉ MAC của đích với một trong các cổng của bộ chuyển mạch, khung sẽ được truyền qua cổng tương ứng.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_10.png" alt=" Hình 4.10: Truyền khung qua bộ chuyển mạch" width="1000">
</p>
<p align="center"><b> Hình 4.10: Truyền khung qua bộ chuyển mạch</b></p>



Nếu trong bảng chuyển mạch không có bản ghi nào cho địa chỉ MAC của thiết bị và cổng hoặc địa chỉ MAC của đích là địa chỉ quảng bá (broadcast), bộ chuyển mạch sẽ truyền khung qua tất cả các cổng, giống như một bộ tập trung (hub). Trong trường hợp này, ta nói rằng bộ chuyển mạch tạo thành một miền quảng bá (broadcast domain).

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/4_Computer_network_topologies/img/4_11.png" alt="Hình 4.11: Quảng bá qua bộ chuyển mạch" width="1000">
</p>
<p align="center"><b>Hình 4.11: Quảng bá qua bộ chuyển mạch</b></p>



Hiện nay, các bộ chuyển mạch là thành phần chính trong việc xây dựng mạng LAN. Các bộ chuyển mạch Ethernet hiện đại ngoài nhiệm vụ chính còn có thể thực hiện nhiều chức năng bổ sung như tạo dự phòng và tăng cường khả năng chống lỗi của mạng, tạo các mạng LAN ảo (VLAN), kiểm soát và hạn chế quá tải trong mạng, bảo đảm an ninh, quản lý truyền phát đa điểm (multicast) và nhiều chức năng khác.

Thông tin chi tiết về các bộ chuyển mạch và các công nghệ được chúng hỗ trợ sẽ được trình bày trong Chương 6.

---



