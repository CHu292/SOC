# Hướng dẫn sử dụng WireShark

# WireShark là gì

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

# Cách dùng WireShark

## Cách bắt và dừng gói tin

Giao diện của WireShark:

![Giao diện](../Lab_2_Phân%20tích%20lưu%20lượng%20mạng%20máy%20tính%20bằng%20công%20cụ%20Wireshark/img/interface_wireshark.png)


Bắt đầu bắt gói tin:```Capture -> Start``` Hoặc bấm tổ hợp phím ```Ctrl + E```

![Bắt gói tin](../Lab_2_Phân%20tích%20lưu%20lượng%20mạng%20máy%20tính%20bằng%20công%20cụ%20Wireshark/img/batgoitin.png)

Dừng gói tin bằng cách bấm vào nút màu đỏ hoặc ```Capture -> Stop``` Hoặc bấm tổ hợp phím ```Ctrl + E```

![Dừng bắt gói tin](../Lab_2_Phân%20tích%20lưu%20lượng%20mạng%20máy%20tính%20bằng%20công%20cụ%20Wireshark/img/Dunggoitin.png)

## Giao diện WireShark

Giao diện gồm: Packet List, Packet Detail, Packet Byte

![Giao diện gồm: Packet List, Packet Detail, Packet Byte](../Lab_2_Phân%20tích%20lưu%20lượng%20mạng%20máy%20tính%20bằng%20công%20cụ%20Wireshark/img/giao_dien.png)

Giao diện chính của Wireshark được chia thành 3 phần:

- Packet List: Chứa danh sách toàn bộ packet của file capture hiện tại. Nó thể hiện số thứ tự của gói tin, thời gian mà mà gói tin được bắt, source và destination IP, protocol của packet, chiều dài gói tin và các thông tin tổng quan khác.

- Packet Details: Khi bạn chọn một gói tin ở phần Packet List, thông tin chi tiết của gói tin sẽ được thể hiện ở phần Packet Detail. Các thông tin chi tiết có thể được collapsed hoặc expanded bằng cách click vào mũi tên hình tam giác ở đầu dòng. 

- Packet Bytes: Thể hiện packet ở định dạng raw dưới dạng hex hoặc binary và thể hiện cách mà packet được truyền trên đường truyền. 

## Mở và lưu gói tin

Để mở gói tin bằng Wireshark, bạn chọn File > Open và tìm đến đường dẫn của file cần mở.

![Mở file](../Lab_2_Phân%20tích%20lưu%20lượng%20mạng%20máy%20tính%20bằng%20công%20cụ%20Wireshark/img/mo_file.png)

Để lưu gói tin đã capture, bạn click vào File > Save, sau đó chọn đường dẫn để lưu trữ, đặt tên cho file capture và định dạng sẽ lưu.

![Luu file](../Lab_2_Phân%20tích%20lưu%20lượng%20mạng%20máy%20tính%20bằng%20công%20cụ%20Wireshark/img/luu_file.png)


## Cách lọc các gói tin trong phần mềm Wireshark

> Một cách cơ bản để sử dụng Wireshark để lọc là nhập điều kiện vào hộp bộ lọc ở đầu cửa sổ và sau đó nhấp vào Apply hoặc nhấn Enter. Ví dụ, nếu bạn nhập dns vào bộ lọc, chỉ các gói tin DNS sẽ được hiển thị. Wireshark cung cấp chức năng tự động hoàn thành bộ lọc khi bạn bắt đầu nhập.

![Cách lọc gói tin](../Lab_2_Phân%20tích%20lưu%20lượng%20mạng%20máy%20tính%20bằng%20công%20cụ%20Wireshark/img/cach_loc_goi_tin.png)

> Ngoài ra, bạn cũng có thể truy cập Analyze > Display Filters để chọn các bộ lọc mặc định của Wireshark hoặc thêm bộ lọc mới và lưu chúng để sử dụng sau này.

![Chọn bộ lọc mặc định](../Lab_2_Phân%20tích%20lưu%20lượng%20mạng%20máy%20tính%20bằng%20công%20cụ%20Wireshark/img/chon_bo_loc_mac_dinh.png)

> Khi muốn xem chi tiết một cuộc trò chuyện TCP giữa máy khách và máy chủ, bạn có thể chuột phải vào một tệp và chọn Follow > TCP Stream. Điều này sẽ hiển thị cuộc trò chuyện TCP đầy đủ. Bạn cũng có thể theo dõi các cuộc trò chuyện của các giao thức khác để hiểu rõ hơn về cách chúng hoạt động.

![Theo dõi cuộc trò chuyện TCP đầy đủ](../Lab_2_Phân%20tích%20lưu%20lượng%20mạng%20máy%20tính%20bằng%20công%20cụ%20Wireshark/img/Theo_doi_TCP.png)

>Sau khi áp dụng bộ lọc, Wireshark sẽ tự động hiển thị các gói tin liên quan đến cuộc trò chuyện, giúp bạn hiểu rõ cách lọc gói tin trong Wireshark.

![Hiển thị các gói tin](../Lab_2_Phân%20tích%20lưu%20lượng%20mạng%20máy%20tính%20bằng%20công%20cụ%20Wireshark/img/hien_thi_goi_tin_sau_khi_ap_dung_bo_loc.png)

## Cách Color Coding trong Wireshark

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

## Cách kiểm tra gói tin trong Wireshark

> Để kiểm tra gói tin trong máy tính sử dụng Wireshark, chúng ta bắt đầu bằng cách nhấp chuột vào một gói tin cụ thể. Sau đó, để tạo một bộ lọc, chúng ta có thể nhấp chuột phải vào bất kỳ chi tiết nào trong gói tin và sử dụng menu con Apply as Filter để tạo bộ lọc dựa trên thông tin đó. Việc tự tạo bộ lọc giúp người dùng tập trung vào các gói tin cụ thể và thuận tiện trong quá trình phân tích dữ liệu mạng.

![Kiểm tra gói tin](../Lab_2_Phân%20tích%20lưu%20lượng%20mạng%20máy%20tính%20bằng%20công%20cụ%20Wireshark/img/Kiem_tra_goi_tin.png)

## Phân tích gói tin với Wireshark

### Tìm kiếm gói tin (Find Packet)

> Để tìm kiếm gói tin, chúng ta có thể sử dụng thanh công cụ Find Packet bằng cách bấm phím Ctrl + F, một hộp thoại mới sẽ xuất hiện nằm giữa thanh Filter và Packet List:

![Tìm gói tin](../Lab_2_Phân%20tích%20lưu%20lượng%20mạng%20máy%20tính%20bằng%20công%20cụ%20Wireshark/img/tim_goi_tin.png)

Chúng ta có thể tìm kiếm packet dựa vào:

- Display Filter: Nhập vào một biểu thức filter (expression-based filter), Wireshark sẽ tìm kiếm các gói tin khớp với biểu thức này.
- Hex value: Tìm kiếm dựa trên giá trị Hex.
- String: Tìm kiếm dựa trên chuỗi dữ liệu.
- Regular Expression: Tìm kiếm dựa trên biểu thức Regex.

![](../Lab_2_Phân%20tích%20lưu%20lượng%20mạng%20máy%20tính%20bằng%20công%20cụ%20Wireshark/img/tim_goi_tin_1.png)

> Tip: Sử dụng Ctrl + N để đi đến kết quả tiếp theo, Ctrl + B để lùi lại kết quả trước đó.

| Options            | Ví dụ                          |
|--------------------|--------------------------------|
| **Display filter** | `tcp.src port==80`<br>hoặc<br>`ip.src==192.168.1.1` |
| **Hex**           | `010108ffff`                   |
| **String**        | `web.telegram.org`<br>hoặc<br>`GET /` |
| **Regular Expression** | `GET .* HTTP`            |

### Wireshark Filter

> Filter cho phép bạn lọc ra những packet nào sẽ dùng để phân tích. Sử dụng Wireshark filter bằng cách khai báo một biểu thức để quy định việc thêm vào (inclusion) hoặc loại bỏ (exclusion) các gói tin. Nếu có những gói tin bạn không cần phân tích, có thể viết filter để loại bỏ chúng. Ngược lại, có những gói tin quan trọng bạn muốn phân tích kỹ, có thể viết filter để lọc riêng chúng ra. Có hai loại filter chính:

- Capture Filters: Chỉ định các packet sẽ được capture và quá trình bắt gói tin chỉ capture những packet thỏa điều kiện này.
- Display filters: Áp dụng filter lên các gói tin đã được capture, mục tiêu là để ẩn đi những packet không cần thiết và chỉ thể hiện những packet thỏa điều kiện chỉ định

#### Capture Filter

> Được áp dụng trong quá trình bắt gói tin để giới hạn số lượng gói tin sẽ được bắt. Lý do chính để sử dụng filter này nhằm cải thiện performance và giới hạn số lượng dữ liệu capture được chỉ chứa các thông tin chúng ta quan tâm, giúp việc phân tích trở nên hiệu quả hơn. Điều này cực kỳ hữu ích khi áp dụng bắt gói tin bằng Wireshark trên các hệ thống có lưu lượng mạng cao, dữ liệu trao đổi lớn.

Chúng ta có thể khai báo biểu thức cho Capture Filter ở  Capture > Capture Filters hoặc khai báo ở phần …using this filter khi lựa chọn card mạng:

![Capture Filter](../Lab_2_Phân%20tích%20lưu%20lượng%20mạng%20máy%20tính%20bằng%20công%20cụ%20Wireshark/img/capture_filter.png)

Wireshark Capture Filter sử dụng cú pháp của Berkeley Packet Filter (BPF):

- Mỗi filter gọi là một expression.
- Mỗi expression chứa một hoặc nhiều primitives. Các primitives được kết hợp với nhau bằng các “Logical Operator” như AND (&&), OR (||) và NOT (!) .
- Mỗi primitives chứa một hoặc nhiều qualifiers, theo sau là một ID name hoặc number. Các BPF Qualifiers bao gồm:

| Qualifiers | Mô tả                                     | Ví dụ                          |
|------------|------------------------------------------|--------------------------------|
| **Type**   | Chỉ định ID name hoặc number ta sẽ tham chiếu | `host`, `net`, `port`         |
| **Dir**    | Chỉ định hướng của dữ liệu (transfer direction) | `src`, `dst`                 |
| **Proto**  | Protocol                                 | `ether`, `ip`, `tcp`, `udp`, `http`, `ftp` |


- Cú pháp tổng quan: Bắt các gói tin gửi đến host 192.168.0.10 và sử dụng giao thức TCP, port 80:

![Cú pháp bắt gói tin](../Lab_2_Phân%20tích%20lưu%20lượng%20mạng%20máy%20tính%20bằng%20công%20cụ%20Wireshark/img/Cu_phap_bat_goi_tin.png)


Một vài Wireshark Expression tham khảo cho phần Capture Filter:

| Expression | Ý nghĩa |
|------------|---------|
| `host 172.18.5.4` | Wireshark filter by IP: Bắt gói tin liên quan đến IP `172.18.5.4` |
| `src 192.168.0.10` | Wireshark filter source IP: Bắt các gói tin có source IP là `192.168.0.10` |
| `dst 192.168.0.1` | Wireshark filter destination IP: Bắt các gói tin có destination IP là `192.168.0.1` |
| `net 192.168.0.0/24`<br>hoặc:<br>`net 192.168.0.0 mask 255.255.255.0` | Bắt gói tin liên quan đến subnet `192.168.0.0/24` |
| `src net 192.168.0.0/24`<br>hoặc:<br>`src net 192.168.0.0 mask 255.255.255.0` | Bắt các gói tin có source IP thuộc subnet `192.168.0.0/24` |
| `dst net 192.168.0.0/24`<br>hoặc:<br>`dst net 192.168.0.0 mask 255.255.255.0` | Bắt các gói tin có destination IP thuộc subnet `192.168.0.0/24` |
| `port 53` | Wireshark port filter: Bắt gói tin DNS |
| `port 67 or port 68` | Bắt gói tin DHCP |
| `host 192.168.1.1 and not (port 80 or 443)`<br>hoặc:<br>`host 192.168.1.1 and not port 80 and not port 443` | Capture tất cả traffic liên quan đến IP `192.168.1.1` nhưng không phải traffic HTTP/HTTPS |
| `(tcp[0:2] > 1500 and tcp[0:2] < 1550) or (tcp[2:2] > 1500 and tcp[2:2] < 1550)`<br>hoặc:<br>`tcp portrange 1501-1549` | Capture các packet nằm trong range port từ `1501-1549` |
| `ip` | Wireshark IPv4 filter |
| `ip6` | Wireshark IPv6 filter |
| `tcp` | Bắt gói tin TCP |
| `udp` | Bắt gói tin UDP |
| `icmp` | Bắt gói tin ICMP |
| `http` | Wireshark HTTP filter |
| `https` | Wireshark HTTPS filter |
| `tcp[13] & 32 == 32` | TCP packets với cờ URG được bật |
| `tcp[13] & 16 == 16` | TCP packets với cờ ACK được bật |
| `tcp[13] & 8 == 8` | TCP packets với cờ PSH được bật |
| `tcp[13] & 4 == 4` | TCP packets với cờ RST được bật |
| `tcp[13] & 2 == 2` | TCP packets với cờ SYN được bật |
| `tcp[13] & 1 == 1` | TCP packets với cờ FIN được bật |
| `icmp[0:2] == 0x0301` | ICMP destination unreachable, host unreachable |

[Hoặc có thể tham khảo tại đây](https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html)

#### Display Filter

>Display Filter giúp lọc ra những packet thỏa điều kiện trong file capture để thể hiện lên cho người dùng. Display filter chỉ lọc và thể hiện packet thỏa điều kiện chứ không xóa bỏ những packet không thỏa điều kiện, dữ liệu trong file capture hoàn toàn không bị ảnh hưởng.

>Sử dụng Display Filter bằng cách nhập biểu thức (expression) vào Filter textbox phía trên phần Packet List. Bạn cũng có thể nhấp vào phần Expression để lựa chọn các pre-defined filters có sẵn ứng với từng giao thức.

![Display Filter](../Lab_2_Phân%20tích%20lưu%20lượng%20mạng%20máy%20tính%20bằng%20công%20cụ%20Wireshark/img/display_filter.png)


Wireshark Display Filter chủ yếu tuân theo cú pháp sau:

```
protocol.feature.subfeature COMPARISON_OPERATOR value LOGICAL_OPERATOR protocol.feature.subfeature COMPARISON_OPERATOR value
```

Trong đó:
- **`protocol`**: Giao thức được lọc (ví dụ: `ip`, `tcp`, `udp`, `icmp`, `http`).
- **`feature`**: Thuộc tính cụ thể của giao thức (ví dụ: `src`, `dst`, `port`, `flags`, `ttl`).
- **`subfeature`**: Một đặc tính cụ thể hơn (không phải lúc nào cũng cần thiết, ví dụ: `tcp.flags.syn`, `ip.ttl`).
- **`COMPARISON_OPERATOR`**: Toán tử so sánh 

| Operator | Ý nghĩa |
|----------|---------|
| `==`     | Bằng (equal to) |
| `!=`     | Không bằng (not equal to) |
| `>`      | Lớn hơn (greater than) |
| `<`      | Nhỏ hơn (less than) |
| `>=`     | Lớn hơn hoặc bằng (greater than or equal) |
| `<=`     | Nhỏ hơn hoặc bằng (less than or equal) |

- **`value`**: Giá trị để so sánh (ví dụ: `80`, `192.168.1.1`, `5`).
- **`LOGICAL_OPERATOR`**: Toán tử logic để kết hợp nhiều điều kiện.

| Operator | Ý nghĩa |
|----------|----------------------------------|
| `and`    | tất cả các điều kiện phải được thỏa mãn |
| `or`     | một trong các điều kiện được thỏa mãn |
| `xor`    | một và chỉ một điều kiện được thỏa mãn |
| `not`    | không điều kiện nào được phép thỏa mãn |

---
Một vài Wireshark Expression tham khảo cho phần Display Filter:

| Expression | Ý nghĩa |
|------------|---------|
| `tcp.port eq 25 or icmp` | Lọc gói tin TCP liên quan port 25 hoặc sử dụng giao thức ICMP |
| `ip.src==192.168.0.0/16 and ip.dst==192.168.0.0/16` | Lọc traffic trao đổi trong mạng LAN của subnet `192.168.0.0/16` |
| `tcp.window_size == 0 && tcp.flags.reset != 1` | TCP buffer full và source kết nối báo hiệu cho Destination ngừng gửi dữ liệu |
| `udp contains 81:60:03` | UDP packet chứa 3 bytes `81:60:03` ở vị trí bất kỳ trong header hoặc payload |
| `http.request.uri matches “gl=se$”` | HTTP request có URL tận cùng bằng chuỗi `"gl=se"` |
| `ip.addr == 192.168.0.1`<br>hoặc:<br>`ip.src == 192.168.0.1 or ip.dst == 192.168.0.1` | Wireshark filter by IP: Lọc tất cả traffic liên quan đến IP `192.168.0.1` |
| `! ( ip.addr == 192.168.0.1 )`<br>hoặc:<br>`! (ip.src == 192.168.0.1 or ip.dst == 192.168.0.1)` | Lọc tất cả traffic **KHÔNG** liên quan đến IP `192.168.0.1` |
| `tcp.flags.syn == 1` | Các gói tin TCP có cờ SYN được bật |
| `tcp.flags.syn == 1 && tcp.flags.ack == 1` | Các gói tin TCP có cờ SYN/ACK được bật |
| `http.host == “quantrilinux.vn”` | HTTP request có Host header là `"quantrilinux.vn"` |
| `http.response.code == 404` | Các HTTP request có response status code là `404` |
| `smtp || imap || pop` | Traffic liên quan đến email (SMTP, IMAP, POP) |
| `! tcp.port == 22` | Loại bỏ traffic SSH |
| `! arp` | Loại bỏ traffic ARP |
| `ip.version == 4` | Wireshark IPv4 filter: Lọc tất cả các gói tin IP version 4 |
| `tcp.srcport == 80` | Wireshark port filter: Lọc tất cả gói tin TCP có source port là `80` |
| `tcp.port == 80` | Lọc tất cả các gói tin có liên quan đến port `80` |
| `udp.port == 67 or udp.port == 68` | Traffic DHCP |
| `dns` | Filter traffic liên quan DNS |
| `http` | Wireshark HTTP filter |
| `https` | Wireshark HTTPS filter |
| `ip.src == 192.168.0.1` | Wireshark filter source IP |
| `ip.dst == 192.168.0.1` | Wireshark filter destination IP |
| `tcp.analysis.flags && !tcp.analysis.window_update` | Lọc tất cả các lỗi TCP |
| `tcp.analysis.retransmission` | Lọc các gói tin TCP retransmissions (gửi lại do lỗi) |
| `tcp.analysis.fast_retransmission` | Lọc các gói tin TCP fast retransmissions |
| `tcp.analysis.duplicate_ack` | Lọc các gói tin TCP duplicate ACKs (ACK trùng lặp) |
| `icmp` | Lọc tất cả traffic ICMP (ping, lỗi mạng, unreachable...) |
| `icmp.type == 3` | Lọc ICMP Destination Unreachable |
| `icmp.type == 8` | Lọc ICMP Echo Request (Ping Request) |
| `icmp.type == 0` | Lọc ICMP Echo Reply (Ping Reply) |
| `ether.src == 00:1A:2B:3C:4D:5E` | Lọc tất cả các gói tin có địa chỉ MAC nguồn `00:1A:2B:3C:4D:5E` |
| `ether.dst == 00:1A:2B:3C:4D:5E` | Lọc tất cả các gói tin có địa chỉ MAC đích `00:1A:2B:3C:4D:5E` |
| `ip.ttl < 10` | Lọc tất cả các gói tin có giá trị TTL nhỏ hơn 10 |
| `frame.len > 1000` | Lọc tất cả các gói tin có kích thước lớn hơn 1000 byte |
| `ip.flags.mf == 1` | Lọc các gói tin bị phân mảnh (More Fragments flag bật) |
| `ip.frag_offset > 0` | Lọc tất cả các gói tin là phần tiếp theo của gói tin bị phân mảnh |
| `tcp.seq == 1` | Lọc các gói tin TCP có số sequence là 1 |
| `tcp.options.mss_val < 1460` | Lọc tất cả các gói tin TCP có giá trị MSS nhỏ hơn 1460 |
| `ssl` | Lọc tất cả traffic liên quan đến SSL/TLS |
| `tls.handshake.type == 1` | Lọc tất cả các gói tin TLS Client Hello |
| `tls.handshake.type == 2` | Lọc tất cả các gói tin TLS Server Hello |
| `tls.handshake.type == 11` | Lọc tất cả các gói tin TLS Certificate |
| `tls.handshake.type == 16` | Lọc tất cả các gói tin TLS Client Key Exchange |
| `dns.qry.name == "example.com"` | Lọc tất cả các truy vấn DNS tới `example.com` |
| `dhcp.option.dhcp == 1` | Lọc các gói tin DHCP Discover |
| `dhcp.option.dhcp == 2` | Lọc các gói tin DHCP Offer |
| `dhcp.option.dhcp == 3` | Lọc các gói tin DHCP Request |
| `dhcp.option.dhcp == 5` | Lọc các gói tin DHCP ACK |
| `ftp` | Lọc tất cả traffic liên quan đến FTP |
| `ftp.command == "USER"` | Lọc tất cả các gói tin FTP chứa lệnh `USER` (đăng nhập) |
| `ftp.response.code == 530` | Lọc tất cả các phản hồi FTP có mã `530` (Login incorrect) |
| `ppp` | Lọc tất cả các gói tin PPP (Point-to-Point Protocol) |
| `smb` | Lọc tất cả traffic liên quan đến SMB (Server Message Block) |
| `ntlmssp` | Lọc tất cả traffic liên quan đến NTLM authentication |
| `kerberos` | Lọc tất cả traffic liên quan đến Kerberos authentication |
| `dhcp` | Lọc tất cả traffic liên quan đến DHCP |
| `stp` | Lọc tất cả traffic liên quan đến Spanning Tree Protocol |
| `ospf` | Lọc tất cả traffic liên quan đến OSPF (Open Shortest Path First) |
| `bgp` | Lọc tất cả traffic liên quan đến BGP (Border Gateway Protocol) |
| `h323` | Lọc tất cả traffic liên quan đến giao thức VoIP H.323 |
| `sip` | Lọc tất cả traffic liên quan đến giao thức VoIP SIP |

