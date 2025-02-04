## Mục lục

# Phần I: Cơ bản về mạng truyền dữ liệu
- [Chương 1: Sự phát triển của mạng máy tính](#chuong-1-su-phat-trien-cua-mang-may-tinh)
- [Chương 2: Các nguyên tắc chung trong xây dựng mạng](#chuong-2-cac-nguyen-tac-chung-trong-xay-dung-mang)
- [Chương 3: Chuyển mạch kênh và chuyển mạch gói](#chuong-3-chuyen-mach-kenh-va-chuyen-mach-goi)
- [Chương 4: Chuẩn hóa và phân loại mạng](#chuong-4-chuan-hoa-va-phan-loai-mang)
- [Chương 5: Các đặc tính mạng và chất lượng dịch vụ](#chuong-5-cac-dac-tinh-mang-va-chat-luong-dich-vu)
- [Câu hỏi cho Phần I](#cau-hoi-cho-phan-i)

## Nội dung

<h1 id="chuong-1-su-phat-trien-cua-mang-may-tinh">CHƯƠNG 1: Sự phát triển của mạng máy tính</h1>

## 1.1 Hai nguồn gốc của mạng máy tính
 
- **Mạng máy tính** là kết quả phát triển từ hai ngành quan trọng: **kỹ thuật tính toán (computing technology)** và **viễn thông (telecommunications technology)**.  
- Chúng có hai vai trò chính:  
  1. **Hệ thống máy tính liên kết (interconnected computer system)** giúp trao đổi dữ liệu và thực hiện các nhiệm vụ tự động.  
  2. **Phương tiện truyền thông tin (information transmission medium)** giúp mã hóa, truyền và xử lý dữ liệu trong các hệ thống viễn thông như mạng điện thoại.

![Nguồn gốc của mạng máy tính](./img/1.1.png)

Hình 1.1. Sự tiến hóa của mạng máy tính tại giao điểm của công nghệ tính toán và công nghệ viễn thông.

## 1.2 Những mạng máy tính đầu tiên

### 1.2.1 Hệ thống xử lý theo lô

- **Hệ thống xử lý theo lô (batch processing systems)** dựa trên **máy tính lớn (mainframe)**, nơi người dùng chuẩn bị **thẻ đục lỗ (punched cards)** chứa dữ liệu và chương trình, sau đó gửi vào trung tâm tính toán (computing center).  
- Tác vụ của nhiều người dùng được nhóm thành **gói (batch)** và xử lý tuần tự, tối ưu hóa việc sử dụng bộ xử lý .  
- Người dùng nhận kết quả sau một chu kỳ xử lý, gây độ trễ cao.  
- Chế độ tương tác chưa phổ biến do ưu tiên hiệu suất bộ xử lý hơn trải nghiệm người dùng.

![Hệ thống xử lý theo lô](./img/1.2.png)

Hình 1.2. Hệ thống tập trung dựa trên máy tính trung tâm (mainframe).

### 1.2.2 Hệ thống đa thiết bị đầu cuối — hình mẫu của mạng

- **Hệ thống đa thiết bị đầu cuối (multi-terminal systems)** với **chế độ chia sẻ thời gian (time-sharing mode)** cho phép mỗi người dùng có phiên làm việc riêng, giúp tương tác trực tiếp với mainframe.  
- Bộ xử lý phân chia tài nguyên theo thời gian, đảm bảo người dùng không nhận thấy độ trễ do chia sẻ hệ thống.  
- **Thiết bị đầu cuối (terminals)** mở rộng ra ngoài trung tâm tính toán, phân tán trong doanh nghiệp, trong khi khả năng tính toán vẫn tập trung.  
- Một số chức năng như **nhập/xuất dữ liệu (data input/output)** trở thành **hệ thống phân tán (distributed system)**.  
- Người dùng có thể  truy cập file và chạy chương trình từ bất kỳ thiết bị nào mà không cần thiết bị lưu trữ cá nhân.  
- Hệ thống này trở thành tiền đề cho **mạng máy tính cục bộ (local computer networks - LANs)**.

![Hệ thống đa thiết bị đầu cuối — hình mẫu của mạng](./img/1.3.png)

Hình 1.3. Hệ thống đa thiết bị đầu cuối — hình mẫu của mạng tính toán

### 1.2.3 Những mạng toàn cầu đầu tiên

- **Mạng diện rộng hay còn gọi là mạng toàn cầu (Wide Area Network - WAN)** kết nối các máy tính phân tán về mặt địa lý, ban đầu thông qua mạng điện thoại và **modem**.  
- Hệ thống phát triển từ **kết nối thiết bị đầu cuối - máy tính (terminal-computer)** sang **kết nối máy tính - máy tính (computer-computer)**, cho phép trao đổi dữ liệu tự động.  
- Các dịch vụ ban đầu bao gồm chia sẻ tệp tin, **đồng bộ hóa cơ sở dữ liệu (database synchronization)** và **thư điện tử (email)**.  
- Giao thức mạng phát triển với mô hình truyền gói tin thay thế **chuyển mạch kênh (circuit switching)**, giúp tối ưu băng thông và giảm chi phí.  
- Ban đầu, **kênh truyền (communication channels)** có tốc độ thấp (~kbit/s), chủ yếu hỗ trợ truyền file và email, nhưng dần nâng cấp với các tiêu chuẩn như **X.25** vào thập niên 1970.  
- **ARPANET**, phát triển bởi Bộ Quốc phòng Mỹ năm 1969, là tiền thân của **Internet**, áp dụng **hệ điều hành mạng (network operating systems)** để quản lý tài nguyên phân tán và **giao thức truyền thông (communication protocols)**.  
- **Số hóa thoại (digital voice transmission)** trong mạng điện thoại thúc đẩy sự phát triển của **mạng số tốc độ cao (high-speed digital networks)**, giúp **mạng WAN** đạt chất lượng dịch vụ ngang tầm **mạng LAN**.

### 1.2.4 Những mạng cục bộ đầu tiên

- **Mạng cục bộ (Local Area Networks - LANs)** phát triển từ đầu những năm 1970 nhờ sự ra đời của **mạch tích hợp quy mô lớn (Large Scale Integrated Circuits - LSI)**, giúp giảm giá thành và tăng khả năng của máy tính mini.  
- **Máy tính mini** trở thành đối thủ cạnh tranh với **máy tính lớn (mainframes)**, phá vỡ quy luật Grosch khi nhiều **máy tính nhỏ** có thể thay thế một **máy tính lớn** với cùng chi phí nhưng hiệu suất tốt hơn cho **tác vụ song song (parallel tasks)**.  
- Các bộ phận trong doanh nghiệp có thể sở hữu máy tính riêng để quản lý sản xuất, kho bãi và vận hành công nghệ.  
- **Tài nguyên tính toán (computing resources)** phân bố trên toàn doanh nghiệp, nhưng vẫn hoạt động độc lập , chưa có liên kết mạng thực sự.

![Hình 1.4. Sử dụng độc lập nhiều máy tính mini trong một doanh nghiệp](./img/1.4.png)

Hình 1.4. Sử dụng độc lập nhiều máy tính mini trong một doanh nghiệp

- **Mạng cục bộ (Local Area Network - LAN)** kết nối các máy tính trong phạm vi nhỏ (~1-2 km), thường thuộc về một tổ chức.  
- Ban đầu, các máy tính mini kết nối với nhau qua **bộ ghép nối (interface devices)** để trao đổi dữ liệu tự động giữa các bộ phận doanh nghiệp.  
- **Mạng Ethernet tiêu chuẩn (Standard Ethernet networks)** dần thay thế các giải pháp riêng lẻ, tạo ra nền tảng chung cho việc kết nối **máy tính cá nhân (PCs)** với nhau và với máy chủ.  
- **Công nghệ chuyển mạch gói (packet switching technology)** từ mạng diện rộng được áp dụng vào LANs, giúp cải thiện hiệu suất truyền dữ liệu.  
- Cuối thập niên 1980, các **chuẩn mạng LAN (LAN standards)** gồm **Ethernet, Token Ring, Arcnet, FDDI** ra đời, nhưng Ethernet trở thành lựa chọn phổ biến nhất.  
- **Máy tính cá nhân (PCs)** thay thế **máy tính mini**, trở thành nền tảng chính của LANs, hoạt động như **máy khách (clients)** và **máy chủ (servers)**.  
- **Kết nối đơn giản (plug-and-play connectivity)** giúp LANs dễ triển khai, thúc đẩy sự phổ biến của máy tính trong doanh nghiệp và hộ gia đình.  
- Cuối thập niên 1990, **Ethernet 10 Mbps, Fast Ethernet 100 Mbps và Gigabit Ethernet 1 Gbps** trở thành tiêu chuẩn, nhờ hiệu suất cao và chi phí thấp.

![Hình 1.5. Các loại kết nối khác nhau trong mạng cục bộ đầu tiên](./img/1.5.png)

Hình 1.5. Các loại kết nối khác nhau trong mạng cục bộ đầu tiên

## 1.3 Hội tụ mạng

### 1.3.1 Hội tụ giữa mạng cục bộ và mạng toàn cầu

- **Sự hội tụ giữa mạng LAN và WAN (Convergence of LANs and WANs)** trở nên rõ ràng vào cuối thập niên 1980 do sự khác biệt giảm dần về **độ tin cậy (reliability)**, phương thức truyền dữ liệu, **tốc độ (speed)** và dịch vụ.  
- **LANs** sử dụng **kết nối cự ly ngắn (short-distance connections)** với **băng thông cao (high bandwidth)**, trong khi **WANs** phải tối ưu hóa cho **kênh truyền xa (long-distance links)** có **độ trễ cao (high latency)**.  
- **Mạng WAN nâng cấp** nhờ **Frame Relay, ATM**, cải thiện truyền gói tin với độ trễ thấp hơn, giảm mất gói.  
- **Internet phát triển mạnh** từ thập niên 1990, hợp nhất nhiều công nghệ mạng vào mô hình IP.  
- **Mạng diện rộng đô thị (Metropolitan Area Networks - MANs)** xuất hiện, kết nối **mạng LAN quy mô lớn** với tốc độ **hàng trăm Mbps đến Gbps**.  
- **Ethernet mở rộng ra mạng WAN** với Ethernet qua quang, giúp LAN và WAN hoạt động trên nền IP đồng nhất.

### 1.3.2 Hội tụ giữa mạng máy tính và mạng viễn thông

- **Mạng hội tụ (Converged Networks)** xuất hiện từ thập niên 1980 với mục tiêu hợp nhất mạng máy tính  và mạng viễn thông, hình thành **mạng đa dịch vụ (multiservice networks)**.  
- **Mạng viễn thông** truyền thống bao gồm **radio, điện thoại, truyền hình**, trong khi **mạng máy tính** tập trung vào truyền dữ liệu.  
- Hội tụ dữ liệu và đa phương tiện cho phép truyền cả thông tin thoại (voice), video và dữ liệu trên nền tảng chung.  
- **ISDN (Integrated Services Digital Network)** là một trong những công nghệ đầu tiên kết hợp thoại và dữ liệu nhưng bị thay thế bởi **Internet** và **IP-based services**.  
- **Internet trở thành nền tảng chính** cho **IP telephony, video streaming, cloud computing**, làm mờ ranh giới giữa **mạng viễn thông và mạng máy tính**.  
- **Công nghệ di động (Mobile Technologies - 3G, 4G, 5G)** hỗ trợ dịch vụ IP, giúp **mạng điện thoại và mạng dữ liệu hội tụ hoàn toàn**.  
- **Chuyển mạch gói (Packet switching)** thay thế **chuyển mạch kênh (Circuit switching)** trong viễn thông, tối ưu hóa băng thông và hỗ trợ **QoS (Quality of Service)** để đảm bảo độ trễ thấp cho dịch vụ thời gian thực.

## 1.4 Internet như một yếu tố phát triển công nghệ mạng

- Internet là đỉnh cao của mạng viễn thông, phát triển mạnh mẽ từ thập niên 1980 và tiếp tục mở rộng.  
- Chỉ số phát triển Internet gồm số lượng người dùng, thiết bị đầu cuối, lưu lượng dữ liệu.  
- Thiết bị Internet tăng từ 1000 host (1980) → 1 triệu (1991) → 100 triệu (2000) → hơn 1 tỷ (2018), với 23 tỷ thiết bị kết nối.  
- Lưu lượng dữ liệu tăng theo cấp số nhân:  
  - **1990: 1 TB → 2000: 84 PB → 2013: 50 EB → 2018: 129 EB**  
- Máy tính cá nhân (PCs) giảm dần, thay thế bởi thiết bị di động (smartphones, tablets) và thiết bị IoT (Internet of Things).  
- Dịch vụ Internet chuyển từ tải file sang truyền phát video , với nội dung theo yêu cầu dẫn đầu từ 2010.  
- **Điện toán đám mây (cloud computing)** đẩy mạnh xử lý dữ liệu từ xa thay vì lưu trữ cục bộ.  
- Ô tô tự hành cần kết nối Internet tốc độ cao và độ trễ thấp để xử lý dữ liệu AI theo thời gian thực.  
- Tăng trưởng và biến đổi liên tục của Internet buộc công nghệ mạng phải thích ứng, phát triển kiến trúc điện toán biên để đáp ứng yêu cầu độ trễ thấp. 

![Hình 1.6. Sự tăng trưởng số lượng người dùng và lưu lượng truy cập Internet.](./img/1.5.png)

Hình 1.6. Sự tăng trưởng số lượng người dùng và lưu lượng truy cập Internet.

