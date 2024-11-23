
# Bài tập 3. Phân tích lưu lượng mạng máy tính bằng công cụ Wireshark

## 3.1. Mục tiêu và đặc điểm ngắn gọn của công việc

**Mục tiêu công việc**:  
Nghiên cứu cấu trúc của các khối dữ liệu giao thức bằng cách phân tích lưu lượng thực tế trên máy tính của sinh viên, sử dụng công cụ Wireshark được phân phối miễn phí.

Trong quá trình thực hiện bài tập tại nhà, cần quan sát lưu lượng truyền từ máy tính của người dùng đến Internet và theo chiều ngược lại. Việc sử dụng công cụ chuyên dụng Wireshark cho phép quan sát cấu trúc của các khung dữ liệu, gói dữ liệu và đoạn dữ liệu của các giao thức mạng khác nhau. Khi thực hiện bài tập này, cần phân tích trình tự các lệnh và dữ liệu dịch vụ được sử dụng để tổ chức trao đổi dữ liệu trong các giao thức sau: ARP, DNS, FTP, HTTP, DHCP.

Khi xây dựng bài tập số 3, đã sử dụng tài liệu từ cuốn sách của J.F. Kurose “Computer Networking: A Top-Down Approach” (ấn bản thứ 6, 2012) và sự hỗ trợ trực tiếp của sinh viên thuộc khoa Viễn thông và Công nghệ Thông tin, Đại học ITMO, Polina Nuykina.



## 3.2. Thông tin lý thuyết

**Quá trình truyền dữ liệu qua mạng máy tính** là một tổ hợp phức tạp các quy trình, được thực hiện với sự tham gia của nhiều phương tiện phần mềm và phần cứng đa dạng. Để đơn giản hóa việc phân tích và thiết kế các hệ thống phức tạp như vậy, phương pháp phổ biến là phân rã (decomposition) quy trình phức tạp thành các mô-đun và/hoặc cấu trúc phân cấp.

Mục tiêu chính của phân rã là tạo ra các mô-đun độc lập, mỗi mô-đun thực hiện chức năng được giao mà không liên quan trực tiếp đến các mô-đun khác, chỉ truyền kết quả cuối cùng cho các mô-đun liền kề. Cách tiếp cận này cho phép thiết kế các mô-đun một cách độc lập, với mỗi nhóm kỹ sư chuyên môn hóa hẹp cho một mô-đun cụ thể. Ngoài ra, hệ thống với cấu trúc mô-đun có thể được sửa đổi nội bộ mà không ảnh hưởng đến các mô-đun khác.

Trong mạng máy tính, mô hình phổ biến để phân rã quy trình truyền dữ liệu là **mô hình OSI** (Open Systems Interconnection), được phát triển bởi tổ chức tiêu chuẩn hóa quốc tế. Mô hình OSI mô tả 7 lớp (layer), mỗi lớp thực hiện một tập hợp các hoạt động mạng liên quan, từ việc nhận dữ liệu từ người dùng cho đến việc phát tín hiệu vật lý (ví dụ: sóng radio) vào mạng. Các lớp này được kết nối tuần tự:

**“người dùng” ↔ Lớp 7 ↔ Lớp 6 ↔ Lớp 5 ↔ Lớp 4 ↔ Lớp 3 ↔ Lớp 2 ↔ Lớp 1 ↔ “mạng”**.

(Ở đây, các số chỉ số thứ tự của các lớp.) Điều này có nghĩa là các kết quả của một lớp chỉ được truyền đến lớp liền kề. Kết quả của các lớp này là các khối dữ liệu mã hóa (PDU - Protocol Data Unit). Trong quá trình từ “người dùng” đến “mạng”, mỗi lớp bổ sung PDU của nó với dữ liệu dịch vụ riêng. Kết quả là PDU của lớp 2 có cấu trúc sau (được biểu diễn dưới dạng biểu đồ hình chữ nhật với chiều dài tỷ lệ với số bit):

| SD2 | SD3 | SD4 | SD5 | SD6 | SD7 | DP |

- **SDi** là dữ liệu dịch vụ của lớp $$i$$,  
- **DP** là dữ liệu của người dùng muốn truyền qua mạng.  

Dữ liệu dịch vụ của một số lớp có thể được chia thành hai phần: phần tiêu đề và phần kết thúc. Trong trường hợp này, cấu trúc của PDU sẽ khác so với biểu đồ trên.

**Quy trình ngược lại trong mô hình OSI** (từ “mạng” đến “người dùng”):  
Mỗi lớp trước tiên sử dụng dữ liệu dịch vụ tương ứng để thực hiện các chức năng mạng cần thiết, sau đó loại bỏ chúng khi truyền sang lớp liền kề tiếp theo. Cách tiếp cận này đảm bảo các lớp hoạt động độc lập với nhau, duy trì tính mô-đun, nhưng đồng thời yêu cầu lượng lớn dữ liệu dịch vụ, dẫn đến tăng chi phí truyền dữ liệu hữu ích.

Dưới đây là bản dịch nội dung từ hình ảnh bạn cung cấp:

---

Trong một số trường hợp, quy tắc của lớp có thể áp đặt giới hạn lên kích thước của PDU (Protocol Data Unit), để nó có thể được xử lý đúng bởi lớp đó. Trong trường hợp này, khi cố gắng truyền một PDU có kích thước lớn hơn giới hạn, PDU sẽ bị từ chối kèm theo thông báo lỗi hoặc bị phân mảnh thành nhiều phần, mỗi phần được truyền độc lập. Khi sử dụng phân mảnh, cần đảm bảo rằng phía nhận có thể ghép lại các mảnh để khôi phục thành một PDU hoàn chỉnh.

Giả sử PDU của lớp 4 có kích thước vượt quá giới hạn cho phép của PDU lớp 3 (PDU-3 MAX) là $$B$$ byte:

| SD4 | SD5 | SD6 | SD7 | DP |

<-------- PDU-3 MAX --------> <---- B ---->

Trong trường hợp này, đầu vào của lớp 2, thay vì nhận một PDU duy nhất, sẽ nhận được nhiều PDU lớp 3, mỗi cái là một phần (fragment) của PDU ban đầu. Các phần này sẽ có kích thước tối đa là giới hạn của lớp 3:

**Fragment 1:**

| SD3 | SD4 | SD5 | SD6 | SD7 | DP1 |

<-------- PDU-3 MAX -------->

**Fragment 2:**

| SD3 | DP2 |

<-------- B -------->

Trong trường hợp được mô tả, PDU của lớp 4 được chia thành hai PDU lớp 3. Dữ liệu người dùng bị "chia nhỏ" thành hai phần: DP1 và DP2. Tổng kích thước của DP1 và DP2 đương nhiên bằng kích thước của DP ban đầu. Tuy nhiên, khi phân mảnh, cần thêm SD3 vào cả hai fragment, dẫn đến tăng chi phí truyền thông điệp. Điều này là cần thiết để đảm bảo rằng PDU lớp 4 có thể được khôi phục từ các fragment ở phía nhận.

Cuối cùng, mô tả ngắn gọn về từng lớp trong 7 lớp của mô hình OSI sẽ được cung cấp, đi từ hướng người dùng đến mạng (xem chi tiết hơn trong tài liệu tham khảo [1]).



**Lớp ứng dụng (Application Layer, L7)** mô tả cách quá trình truyền dữ liệu được nhìn nhận từ góc độ của người dùng cuối hoặc ứng dụng. L7 cung cấp cho người dùng các "công cụ" cấp cao để truy cập các dịch vụ của các lớp từ L1 đến L6. Người dùng cuối hoặc ứng dụng khi làm việc với mạng chỉ tương tác với L7, trong khi tất cả các lớp bên dưới đều bị ẩn đi, tức là chúng được đóng gói bên trong L7.  

Lớp này có ranh giới không rõ ràng, bởi nó không chỉ mô tả các chức năng của ứng dụng mạng mà còn mô tả các hành động có thể của người dùng. Ở lớp L7 có thể bao gồm:  

- **Ủy quyền và xác thực người dùng;**  
- **Kiểm soát tính toàn vẹn của dữ liệu người dùng cuối nhận từ mạng;**  
- **Đồng bộ hóa các hành động hoặc tệp tin của người dùng tương tác qua mạng** (ví dụ: khi chỉnh sửa đồng thời một tệp tin bởi nhiều người dùng);  
- Và bất kỳ chức năng nào của các lớp từ L2 đến L6 (xem chi tiết bên dưới) nếu chúng không được thực hiện ở L2-L6, hoặc được triển khai không đầy đủ tùy theo nhu cầu của ứng dụng hoặc người dùng.


**Lớp trình bày (Presentation Layer, L6)** mô tả cách các bên tham gia tương tác "thỏa thuận" về định dạng mà trong đó dữ liệu của người dùng sẽ được biểu diễn khi truyền qua mạng. Ở lớp này có thể mô tả:

- **Thủ tục thỏa thuận định dạng biểu diễn dữ liệu tại giai đoạn thiết lập kết nối** (ví dụ: lựa chọn mã hóa UTF-8 cho văn bản người dùng hoặc chọn thuật toán nén cùng các tham số của nó, v.v.);
  
- **Quy tắc thay đổi định dạng biểu diễn dữ liệu hiện tại trong một kết nối đã được thiết lập** (ví dụ: thay đổi codec nén luồng âm thanh trong cuộc gọi VoIP khi phát hiện kênh truyền bị quá tải);
  
- **Mô tả cú pháp của định dạng biểu diễn dữ liệu đã chọn**, nếu nó không phải là tiêu chuẩn phổ biến và không thể được mô tả đơn giản bằng cách tham chiếu đến tiêu chuẩn (ví dụ: thuật toán nén mới được cấp bằng sáng chế hoặc một thứ tự byte đặc biệt khác với Big Endian và Little Endian).



**Lớp phiên (Session Layer, L5)** mô tả quá trình thiết lập, chấm dứt và duy trì kết nối. Ở lớp này có thể bao gồm:

- **Thủ tục thiết lập kết nối và thỏa thuận các tham số kết nối** (ví dụ: yêu cầu QoS - xem chi tiết bên dưới), trong đó việc thực hiện thực tế các yêu cầu đã được thỏa thuận được xử lý tại lớp L4;  

- **Thủ tục chấm dứt kết nối** khi có yêu cầu rõ ràng từ người dùng hoặc khi nhận được thông báo từ lớp L4 về việc không thể đáp ứng các yêu cầu QoS (có thể bao gồm quá trình ngắt kết nối thông thường mà không làm mất dữ liệu người dùng và/hoặc ngắt kết nối nhanh có "cứng" với rủi ro mất dữ liệu);  

- **Thủ tục đồng bộ hóa (re-synchronization) trạng thái kết nối**, cho phép kết nối được đồng bộ hóa lại khi xảy ra lỗi trong mạng, trong trường hợp chuyển thời gian hoặc vị trí vượt qua ranh giới của cửa sổ truyền dữ liệu, v.v.



**Lớp vận chuyển (Transport Layer, L4)** mô tả quá trình truyền dữ liệu từ đầu cuối đến đầu cuối (end-to-end) qua mạng, nghĩa là truyền từ góc nhìn của người quan sát, trong đó tất cả các thiết bị mạng trung gian giữa các thuê bao được coi là một "hộp đen" với cấu trúc không xác định. Ở lớp này có thể mô tả:

- **Thủ tục thiết lập/duy trì/chấm dứt kết nối và truyền dữ liệu tuân thủ các yêu cầu QoS**, nhận từ lớp L5 (ví dụ: có thể cần thiết lập ngay nhiều kết nối L4 hoặc chọn các tham số L4 đảm bảo tuân thủ yêu cầu QoS với độ tin cậy cao do thiếu khả năng điều chỉnh chính xác);

- **Thủ tục phản ứng khi phát hiện dữ liệu bị méo hoặc mất gói tin** (cần phải lặp lại truyền dữ liệu hay có thể bỏ qua mất mát/méo mó?);

- **Thủ tục đảm bảo thứ tự chính xác của PDU (Protocol Data Unit) đến thuê bao cuối**, (PDU được đánh số thứ tự và có thể cần bộ đệm tạm thời để lưu trữ các PDU nhận không theo thứ tự);

- **Thủ tục thao tác kích thước PDU**: ghép kênh dòng, chia nhỏ các PDU lớn thành các PDU nhỏ hơn, hợp nhất các PDU nhỏ thành các PDU lớn, v.v.


**Lớp mạng (Network Layer, L3)** mô tả quá trình truyền PDU qua các nút trung gian của mạng, bao gồm việc lựa chọn lộ trình di chuyển khi có nhiều tuyến đường. Trong trường hợp này, tuyến truyền có thể đi qua nhiều mạng khác loại được kết nối với nhau.  

Lớp mạng hoàn toàn che giấu khỏi các lớp phía trên (L4–L7) các đặc tính của định tuyến và truyền PDU qua các mạng khác loại, vì nó thực hiện độc lập hoặc thông qua các phương tiện của lớp L2. Ở lớp L3 có thể mô tả:

- **Thiết lập/duy trì/chấm dứt kết nối** trong điều kiện cần vượt qua biên giới của nhiều mạng (ví dụ: khi vượt qua biên giới giữa các mạng của các nhà cung cấp khác nhau, có thể cần thiết lập kết nối độc lập mà không phụ thuộc vào kết nối end-to-end trên L5);

- **Thủ tục duy trì thứ tự chính xác của PDU tại ranh giới mạng** (so sánh với mục tương tự ở lớp L3);

- **Quy tắc định tuyến và xây dựng bảng định tuyến khi vượt qua biên giới mạng**;

- **Thủ tục thao tác kích thước PDU** (xem L4);

- **Quy tắc xác nhận việc nhận PDU từ phía nhận**.


**Lớp liên kết dữ liệu (Data Link Layer, L2)** mô tả các quy tắc logic để truyền PDU trong phạm vi một mạng đơn giản, được xây dựng trên một công nghệ duy nhất với các đường truyền cùng loại. L2 che giấu khỏi các lớp phía trên các đặc điểm vật lý của mạng. Ở lớp này có thể mô tả:

- **Thiết lập, duy trì và chấm dứt kết nối trong phạm vi một mạng cục bộ**, có khả năng điều chỉnh tham số truyền giữa các nút (ví dụ: khi kết nối Wi-Fi, cần thiết lập kết nối L2 với trạm gốc Wi-Fi mà không phụ thuộc vào việc thiết lập kết nối tại L3 và L5);

- **Thủ tục phản ứng khi phát hiện gói tin bị méo hoặc mất** (so sánh với L4);

- **Đồng bộ hóa các thiết bị nhận và truyền của mạng để nhận dạng đúng ranh giới của PDU** (ví dụ: gửi một khối dữ liệu có độ dài đã biết với chuỗi xen kẽ 0 và 1: "01010101..."; hoặc sử dụng các tín hiệu cấm như J, K);

- **Thủ tục duy trì thứ tự chính xác của PDU trong mạng nội bộ** (so sánh với mục tương tự ở L3 và L4);

- **Quy tắc chia luồng PDU thành các luồng con** để có thể truyền đồng thời qua nhiều đường truyền vật lý (ví dụ: sử dụng nhiều kênh vô tuyến với các dải tần khác nhau);

- **Quy tắc định tuyến và xây dựng bảng định tuyến trong mạng nội bộ** (so sánh với mục tương tự ở L3; thông thường trong mạng L2 không cần định tuyến vì luôn chỉ có một tuyến duy nhất).


**Lớp vật lý (Physical Layer, L1)** mô tả từ góc độ vật lý quá trình truyền PDU qua một đường truyền cụ thể. Trong đó bao gồm các thông số vật lý sau:  

- **Môi trường truyền dẫn**: băng thông của kênh vô tuyến tính bằng MHz, chiều dài tối đa của cáp khi truyền qua cặp xoắn hoặc sợi quang, số lượng và mục đích của các dây dẫn hoặc sợi trong cáp, v.v.;  

- **Tín hiệu truyền tải**: các bước sóng hoặc điện áp sử dụng, phương pháp mã hóa bit ở mức tín hiệu cụ thể, thời gian truyền một bit hoặc một nhóm bit, ghép kênh nhiều tín hiệu vật lý trong cùng một đường truyền, các chỉ số QoS của đường truyền (độ trễ lan truyền tín hiệu, tỷ lệ lỗi bit - BER, tốc độ truyền dữ liệu tính bằng baud, v.v.);  

- **Thiết bị mạng**: số lượng và mục đích của các chân cắm trong đầu nối của card mạng hoặc router, số lượng và cấu hình vật lý của anten trong bộ phát sóng vô tuyến, phương thức truyền tải (full-duplex, half-duplex, simplex), phương pháp kích hoạt đường truyền khi khởi động hoặc bắt đầu truyền dữ liệu, v.v.

Ngoài ra, có một số chức năng phổ quát được thực hiện gần như ở tất cả các lớp của mô hình OSI. Các chức năng này bao gồm:


- **Định địa chỉ (Addressing):** Ở mỗi lớp (ngoại trừ L6), để xác định các bên tham gia tương tác, một địa chỉ cụ thể có thể được sử dụng.  
  - Ở L2, địa chỉ có thể là địa chỉ vật lý của thiết bị mạng, đặc thù cho một công nghệ mạng cụ thể.  
  - Ở L3, địa chỉ là địa chỉ liên mạng phổ quát, phù hợp để truyền tải qua các mạng khác loại.  
  - Ở L5, địa chỉ có thể là số cổng kết nối.  
  - Ở L7, địa chỉ có thể là tên người dùng hoặc địa chỉ văn bản thân thiện với con người.  

  Tổng cộng, tại thời điểm hình thành PDU ở L1, gói dữ liệu có thể chứa tới 6 loại địa chỉ nhận dạng khác nhau.

- **Phát hiện lỗi (Error Detection):** Mỗi lớp đều có đặc thù riêng trong việc phát hiện lỗi.  
  - Ở L1, lỗi có thể được báo hiệu bởi các giá trị điện áp không hợp lệ hoặc chuỗi tín hiệu vô tuyến không chính xác.  
  - Ở các lớp cao hơn, nhiều loại checksum (tổng kiểm tra) khác nhau có thể được sử dụng để phát hiện và sửa lỗi (ví dụ: mã Hamming).  
  - Ở L3, lỗi có thể được phát hiện tại các nút trung gian khi vượt qua biên giới mạng.  
  - Ở L4, kiểm tra lỗi chỉ thực hiện được tại điểm cuối nhận.  

  Một loại lỗi khác có liên quan đến việc vi phạm các quy tắc logic của giao thức trao đổi dữ liệu, ví dụ: nếu thuê bao gửi gói dữ liệu đầu tiên trước khi hoàn thành thủ tục thiết lập kết nối tại L5.

- **Chỉ số QoS (Quality of Service):** Đây là các số liệu để đo chất lượng truyền dữ liệu qua mạng, như độ trễ truyền tải, thời gian thiết lập kết nối, tỷ lệ mất gói tin, v.v.  
  - Ở L1, QoS đo chất lượng truyền tải qua một đường truyền cụ thể (ví dụ: cường độ tín hiệu tại trạm Wi-Fi).  
  - Ở L2, QoS được kiểm soát trong phạm vi mạng cục bộ.  
  - Ở L3, QoS được mô tả khi vượt qua biên giới mạng.  
  - Ở L4, QoS được kiểm soát trong quá trình truyền end-to-end.  
  - Ở L5, QoS liên quan đến thỏa thuận về các tham số giữa các thuê bao khi thiết lập kết nối.  
  - Ở L7, người dùng có thể yêu cầu tốc độ bit cần thiết để đảm bảo chất lượng truyền phát video mạng hoặc các ứng dụng khác.

- **Thiết lập kết nối (Connection Establishment):** Khi mô tả các chức năng của L2, L3 và L5 (như đã thấy ở trên), rõ ràng rằng trong quá trình truyền dữ liệu, có thể cần thực hiện một loạt các thủ tục độc lập để thiết lập kết nối. Ví dụ:  
  - Kết nối L2 với điểm truy cập Wi-Fi;  
  - Kết nối L3 với nhà cung cấp dịch vụ Internet;  
  - Kết nối L5 với một máy chủ FTP công khai trên Internet (tức là với một địa chỉ cụ thể).


**Các triển khai hiện tại của mô hình OSI**

Tiêu chuẩn mô tả mô hình OSI được công bố vào năm 1984, nhưng từ đó đến nay không có công nghệ mạng phổ biến nào hoàn toàn tuân theo mô hình này. Ngăn xếp mạng phổ biến nhất là TCP/IP, được phát triển trước khi mô hình OSI được công bố, chỉ có thể được so sánh với các lớp của OSI với một số điều chỉnh:

- **Lớp liên kết TCP/IP:** Xấp xỉ thực hiện các chức năng của L1 và L2.  
  - Tại lớp này, địa chỉ được sử dụng là địa chỉ MAC của thiết bị mạng, và PDU của lớp này được gọi là khung (frame).  
  - Lớp này mô tả quá trình truyền dữ liệu trong phạm vi mạng cục bộ.

- **Lớp mạng TCP/IP:** Xấp xỉ tương ứng với L3.  
  - Địa chỉ tại lớp này là địa chỉ IP, và PDU được gọi là gói (packet).  
  - Lớp này mô tả quá trình truyền dữ liệu qua các mạng cục bộ khác loại đã được kết nối.

- **Lớp vận chuyển TCP/IP:** Xấp xỉ thực hiện các chức năng của L4 và L5.  
  - Tại lớp này, địa chỉ là cặp số xác định duy nhất kết nối: cổng gửi và cổng nhận (ví dụ: cổng UDP), và PDU của lớp này được gọi là đoạn (segment) hoặc datagram.

- **Lớp ứng dụng TCP/IP:** Xấp xỉ thực hiện các chức năng của L5, L6 và L7.  
  - (Lưu ý: L5 được liệt kê hai lần, ở cả lớp ứng dụng và lớp vận chuyển trong TCP/IP).  
  - Địa chỉ tại lớp này bao gồm URL trang web, tên DNS của máy chủ, tên người dùng, địa chỉ email, v.v.

