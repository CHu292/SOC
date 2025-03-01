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

![Giao diện gồm: Packet List, Packet Detail, Packet Byte](../Lab_2_Phân%20tích%20lưu%20lượng%20mạng%20máy%20tính%20bằng%20công%20cụ%20Wireshark/img/1.png)

Giao diện chính của Wireshark được chia thành 3 phần:

- Packet List: Chứa danh sách toàn bộ packet của file capture hiện tại. Nó thể hiện số thứ tự của gói tin, thời gian mà mà gói tin được bắt, source và destination IP, protocol của packet, chiều dài gói tin và các thông tin tổng quan khác.

- Packet Details: Khi bạn chọn một gói tin ở phần Packet List, thông tin chi tiết của gói tin sẽ được thể hiện ở phần Packet Detail. Các thông tin chi tiết có thể được collapsed hoặc expanded bằng cách click vào mũi tên hình tam giác ở đầu dòng. 

- Packet Bytes: Thể hiện packet ở định dạng raw dưới dạng hex hoặc binary và thể hiện cách mà packet được truyền trên đường truyền. 

