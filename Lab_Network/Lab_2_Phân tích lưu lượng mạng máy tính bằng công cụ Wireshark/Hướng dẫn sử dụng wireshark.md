# Hướng dẫn sử dụng WireShark

## WireShark là gì

> Wireshark là một ứng dụng dùng để bắt (capture), phân tích và xác định các vấn đề liên quan đến network như: rớt gói tin, kết nối chậm, hoặc các truy cập bất thường. Phần mềm này cho phép quản trị viên hiểu sâu hơn các Network Packets đang chạy trên hệ thống, qua đó dễ dàng xác định các nguyên nhân chính xác gây ra lỗi.

> Sử dụng WireShark có thể capture các packet trong thời gian thực (real time), lưu trữ chúng lại và phân tích chúng offline. Ngoài ra, nó cũng bao gồm các filter, color coding và nhiều tính năng khác, cho phép người dùng tìm hiểu sâu hơn về lưu lượng mạng cũng như inspect (kiểm tra) các packets.

Wireshark là một phần mềm dùng để phân tích và giám sát lưu lượng mạng. Dưới đây là một số chức năng chính của Wireshark:

Phân tích Gói Tin: Wireshark cho phép bạn theo dõi và phân tích từng gói tin dữ liệu trên mạng. Bạn có thể xem các thông tin chi tiết như nguồn, đích, loại gói tin, dữ liệu payload và nhiều thông tin khác.

Đánh giá Hiệu suất Mạng: Wireshark cung cấp thông tin về thời gian phản hồi (response time), độ trễ (latency), và các thống kê khác, giúp đánh giá hiệu suất của mạng.

Phân tích Giao thức: Wireshark hỗ trợ nhiều giao thức mạng khác nhau. Bạn có thể xem và phân tích giao thức [HTTP](../Các%20khái%20niệm/HTTP.md), [TCP](../Các%20khái%20niệm/TCP.md), [UDP](../Các%20khái%20niệm/UDP.md), [IP](../Các%20khái%20niệm/IP.md), [DNS](../Các%20khái%20niệm/DNS.md), và nhiều giao thức khác.
Điều tra Vấn đề Mạng: Khi xảy ra vấn đề mạng, Wireshark là một công cụ mạnh mẽ để phân tích và xác định nguyên nhân của sự cố.

Bảo mật Mạng: Wireshark có thể được sử dụng để phát hiện các hoạt động độc hại trên mạng. Nó cho phép bạn xem gói tin để phát hiện các tấn công mạng, như phishing hoặc kiểm soát truy cập không được ủy quyền.

> WireShark là một công cụ dùng để capture và phân tích các packet. Nó capture các lưu lượng mạng trên mạng cục bộ, sau đó sẽ lưu trữ nó để phân tích offline. Có thể capture các lưu lượng mạng từ các kết nối Ethernet, Bluetooth, Wireless (IEEE.802.11), Token Ring, Frame Relay…

> Wireshark cho phép thiết lập filter (bộ lọc) trước khi bắt đầu capture hoặc thậm chí là trong quá trình phân tích. Do đó, ta có thể thu hẹp phạm vi tìm kiếm trong quá trình theo dõi mạng. 

**Các tính năng nổi bật của phần mềm bắt gói tin Wireshark:**

- Hỗ trợ phân tích sâu hàng trăm giao thức và liên tục được cập nhật.
- Live capture và phân tích offline.
- Hoạt động đa nền tảng: Windows, Linux, MacOS, Solaris, FreeBSD, OpenBSD...
- Các gói tin đã capture có thể xem bằng giao diện hoặc sử dụng command line (tshark).
- Display filter mạnh mẽ.
- Hỗ trợ phân tích VoIP chuyên sâu.
- Hỗ trợ read/write nhiều định dạng: [tcpdump](../Các%20khái%20niệm/tcpdump.md) (libpcap), Pcap NG, Catapult DCT2000, 
  Cisco Secure IDS iplog, Microsoft Network Monitor, Network General Sniffer® 
  (compressed and uncompressed), Sniffer® Pro, and NetXray®, Network Instruments 
  Observer, NetScreen snoop, Novell LANalyzer, RADCOM WAN/LAN Analyzer, 
  Shomiti/Finisar Surveyor, Tektronix K12xx, Visual Networks Visual UpTime, 
  WildPackets EtherPeek/TokenPeek/AiroPeek ...
- File capture được nén bằng gzip có thể được giải nén "on the fly".
- Capture dữ liệu từ [Ethernet](../Các%20khái%20niệm/Ethernet.md), [IEEE 802.11](../Các%20khái%20niệm/IEEE.md), PPP/HDLC, ATM, Bluetooth, USB, Token Ring, 
  Frame Relay, FDDI ...
- Hỗ trợ decryption của nhiều giao thức như: IPsec, ISAKMP, Kerberos, SNMPv3, 
  SSL/TLS, WEP, và WPA/WPA2.
- Coloring rules cho phép thiết lập màu sắc cho các packet giúp phân tích nhanh và hiệu quả hơn.
- Output có thể export sang XML, PostScript®, CSV, hoặc plain text.

## Cách dùng WireShark

### Cách bắt và dừng gói tin

Giao diện của WireShark:

![Giao diện](../Lab_2_Phân%20tích%20lưu%20lượng%20mạng%20máy%20tính%20bằng%20công%20cụ%20Wireshark/img/interface_wireshark.png)


Bắt đầu bắt gói tin:```Capture -> Start``` Hoặc bấm tổ hợp phím ```Ctrl + E```

![Bắt gói tin](../Lab_2_Phân%20tích%20lưu%20lượng%20mạng%20máy%20tính%20bằng%20công%20cụ%20Wireshark/img/batgoitin.png)

Dừng gói tin bằng cách bấm vào nút màu đỏ hoặc ```Capture -> Stop``` Hoặc bấm tổ hợp phím ```Ctrl + E```

![Dừng bắt gói tin](../Lab_2_Phân%20tích%20lưu%20lượng%20mạng%20máy%20tính%20bằng%20công%20cụ%20Wireshark/img/Dunggoitin.png)

### Giao diện WireShark

Giao diện gồm: Packet List, Packet Detail, Packet Byte

![Giao diện gồm: Packet List, Packet Detail, Packet Byte](../Lab_2_Phân%20tích%20lưu%20lượng%20mạng%20máy%20tính%20bằng%20công%20cụ%20Wireshark/img/giao_dien.png)

Giao diện chính của Wireshark được chia thành 3 phần:

- Packet List: Chứa danh sách toàn bộ packet của file capture hiện tại. Nó thể hiện số thứ tự của gói tin, thời gian mà mà gói tin được bắt, source và destination IP, protocol của packet, chiều dài gói tin và các thông tin tổng quan khác.

- Packet Details: Khi bạn chọn một gói tin ở phần Packet List, thông tin chi tiết của gói tin sẽ được thể hiện ở phần Packet Detail. Các thông tin chi tiết có thể được collapsed hoặc expanded bằng cách click vào mũi tên hình tam giác ở đầu dòng. 

- Packet Bytes: Thể hiện packet ở định dạng raw dưới dạng hex hoặc binary và thể hiện cách mà packet được truyền trên đường truyền. 

### Mở và lưu gói tin

Để mở gói tin bằng Wireshark, bạn chọn File > Open và tìm đến đường dẫn của file cần mở.

![Mở file](../Lab_2_Phân%20tích%20lưu%20lượng%20mạng%20máy%20tính%20bằng%20công%20cụ%20Wireshark/img/mo_file.png)

Để lưu gói tin đã capture, bạn click vào File > Save, sau đó chọn đường dẫn để lưu trữ, đặt tên cho file capture và định dạng sẽ lưu.

![Luu file](../Lab_2_Phân%20tích%20lưu%20lượng%20mạng%20máy%20tính%20bằng%20công%20cụ%20Wireshark/img/luu_file.png)


### Cách lọc các gói tin trong phần mềm Wireshark

> Một cách cơ bản để sử dụng Wireshark để lọc là nhập điều kiện vào hộp bộ lọc ở đầu cửa sổ và sau đó nhấp vào Apply hoặc nhấn Enter. Ví dụ, nếu bạn nhập dns vào bộ lọc, chỉ các gói tin DNS sẽ được hiển thị. Wireshark cung cấp chức năng tự động hoàn thành bộ lọc khi bạn bắt đầu nhập.

![Cách lọc gói tin](../Lab_2_Phân%20tích%20lưu%20lượng%20mạng%20máy%20tính%20bằng%20công%20cụ%20Wireshark/img/cach_loc_goi_tin.png)

> Ngoài ra, bạn cũng có thể truy cập Analyze > Display Filters để chọn các bộ lọc mặc định của Wireshark hoặc thêm bộ lọc mới và lưu chúng để sử dụng sau này.

![Chọn bộ lọc mặc định](../Lab_2_Phân%20tích%20lưu%20lượng%20mạng%20máy%20tính%20bằng%20công%20cụ%20Wireshark/img/chon_bo_loc_mac_dinh.png)

> Khi muốn xem chi tiết một cuộc trò chuyện TCP giữa máy khách và máy chủ, bạn có thể chuột phải vào một tệp và chọn Follow > TCP Stream. Điều này sẽ hiển thị cuộc trò chuyện TCP đầy đủ. Bạn cũng có thể theo dõi các cuộc trò chuyện của các giao thức khác để hiểu rõ hơn về cách chúng hoạt động.

![Theo dõi cuộc trò chuyện TCP đầy đủ](../Lab_2_Phân%20tích%20lưu%20lượng%20mạng%20máy%20tính%20bằng%20công%20cụ%20Wireshark/img/Theo_doi_TCP.png)

>Sau khi áp dụng bộ lọc, Wireshark sẽ tự động hiển thị các gói tin liên quan đến cuộc trò chuyện, giúp bạn hiểu rõ cách lọc gói tin trong Wireshark.

![Hiển thị các gói tin](../Lab_2_Phân%20tích%20lưu%20lượng%20mạng%20máy%20tính%20bằng%20công%20cụ%20Wireshark/img/hien_thi_goi_tin_sau_khi_ap_dung_bo_loc.png)

### Cách Color Coding trong Wireshark

Trong Wireshark, quy tắc tô màu (Coloring Rules) giúp người dùng dễ dàng nhận diện và phân loại các loại gói tin dựa trên đặc điểm và lỗi mạng. Dưới đây là ý nghĩa của các màu sắc đánh dấu gói tin trong hình ảnh:

1. **Màu đỏ (Red)**
   - **Gói tin lỗi nghiêm trọng hoặc cảnh báo quan trọng**.
   - Ví dụ: `Bad TCP`, `TCP RST`, `Checksum Errors`, `IPv4 TTL low or unexpected`, `IPv6 hop limit low or unexpected`.
   - Điều này có thể chỉ ra lỗi trong giao thức TCP hoặc các vấn đề liên quan đến TTL, lỗi checksum.

2. **Màu xanh lá cây nhạt (Light Green)**
   - **Gói tin HTTP hoặc SMB (Server Message Block)**.
   - Ví dụ: `HTTP`, `SMB`.
   - Đây là những gói tin liên quan đến dịch vụ Web hoặc chia sẻ file.

3. **Màu vàng (Yellow)**
   - **Các gói tin định tuyến (Routing Protocols)**.
   - Ví dụ: `HSRP`, `OSPF`, `BGP`, `EIGRP`, `CDP`, `VRRP`, `IGMP`.
   - Chúng giúp xác định và quản lý đường đi của dữ liệu trên mạng.

4. **Màu xanh nước biển nhạt (Light Blue)**
   - **Các gói tin TCP và UDP thông thường**.
   - Ví dụ: `TCP`, `UDP`, `TCP SYN/FIN`.
   - Màu này giúp phân biệt lưu lượng TCP/UDP chuẩn mà không có lỗi.

5. **Màu tím (Purple)**
   - **Sự kiện hệ thống (System Events)**.
   - Ví dụ: `System Event`, `systemd_journal`, `sysdig`.
   - Đây có thể là các thông điệp nhật ký từ hệ điều hành hoặc phần mềm giám sát hệ thống.

6. **Màu hồng nhạt (Pink)**
   - **Các gói tin ARP và ICMP (bao gồm ICMPv6)**.
   - Ví dụ: `ARP`, `ICMP`, `ICMP errors`.
   - Đây là các gói tin liên quan đến việc kiểm tra kết nối và xử lý địa chỉ mạng.

7. **Màu xanh đậm (Dark Blue)**
   - **Gói tin DCE/RPC (Distributed Computing Environment/Remote Procedure Calls)**.
   - Ví dụ: `DCERPC`.
   - Thường được sử dụng trong giao tiếp giữa các ứng dụng trên mạng.

**Tóm tắt**
- **Đỏ**: Gói tin lỗi nghiêm trọng.
- **Xanh lá cây nhạt**: Lưu lượng HTTP, SMB.
- **Vàng**: Gói tin định tuyến.
- **Xanh nước biển nhạt**: Gói tin TCP/UDP bình thường.
- **Tím**: Sự kiện hệ thống.
- **Hồng nhạt**: Gói tin ARP, ICMP.
- **Xanh đậm**: Giao thức RPC.

Để hiểu rõ hơn về ý nghĩa cụ thể của từng màu, bạn có thể truy cập mục View > Coloring Rules trong Wireshark. Ngoài ra, người dùng cũng có khả năng tự tùy chỉnh màu sắc theo ý muốn cá nhân thông qua cách thức Color Coding trong Wireshark.

![color coding](../Lab_2_Phân%20tích%20lưu%20lượng%20mạng%20máy%20tính%20bằng%20công%20cụ%20Wireshark/img/color_coding.png)

### Cách kiểm tra gói tin trong Wireshark

