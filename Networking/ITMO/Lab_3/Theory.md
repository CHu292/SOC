# Nhiệm vụ 4. Cơ bản về quản trị mạng máy tính có định tuyến

## 4.1. Mục tiêu và đặc điểm ngắn gọn của nhiệm vụ

Mục tiêu của nhiệm vụ là nghiên cứu các phương pháp cơ bản để cấu hình mạng máy tính có định tuyến thông qua ví dụ về một mạng gồm các máy tính chạy hệ điều hành Linux.

Trong quá trình thực hiện nhiệm vụ, sẽ nghiên cứu tầng mạng của mô hình OSI. Thực hiện cấu hình cơ bản kết nối trong mạng, quản lý các bảng định tuyến và các quy tắc chuyển đổi địa chỉ mạng. Sử dụng tiện ích *tcpdump* để theo dõi quá trình truyền tải lưu lượng qua các kênh kết nối trong mạng máy tính có định tuyến. 

Việc sử dụng tiện ích *tcpdump* cho phép theo dõi trực tiếp trong terminal (đây là phương pháp quản lý thiết bị mạng cơ bản) các gói dữ liệu đi qua giao diện mạng của máy tính và nghiên cứu lưu lượng nội bộ của mạng.

Trong nhiệm vụ này, sẽ nghiên cứu các phương pháp định tuyến trong các mạng IPv4 và IPv6, cũng như công nghệ NAT vốn phổ biến rộng rãi trong các mạng máy tính.


---

## 4.2. Tham khảo lý thuyết

Quá trình định tuyến gói tin tại mỗi nút mạng máy tính là một quá trình nhiều giai đoạn. Ở mỗi giai đoạn, các điều kiện khác nhau được kiểm tra để xác định các hành động tiếp theo với gói tin được định tuyến.

Trong Linux, quá trình định tuyến được chia thành các giai đoạn sau:
1. **Lọc và xử lý ban đầu** các gói tin được gửi đến bộ định tuyến.
2. **Xác định bảng định tuyến**, nơi sẽ tìm kiếm tuyến đường phù hợp cho gói tin.
3. **Tìm kiếm trong bảng định tuyến** và quyết định cách xử lý gói tin.
4. **Lọc và thay đổi gói tin được định tuyến**, dựa trên thông tin về việc di chuyển gói tin.

Chúng ta sẽ xem xét chi tiết từng giai đoạn này.

---

Mặc định trong Linux tồn tại 3 bảng định tuyến: `local`, `main`, và `default`. Đối với mỗi gói tin, việc tìm kiếm tuyến đường sẽ được thực hiện lần lượt trong từng bảng định tuyến cho đến khi tìm được tuyến đường phù hợp hoặc tất cả các tuyến đường đã được kiểm tra.

- **Bảng `local`** chứa các tuyến đường thuộc về giao diện mạng của bộ định tuyến (ví dụ: địa chỉ multicast, địa chỉ của các mạng con kết nối, hoặc địa chỉ gán cho giao diện của bộ định tuyến). Nếu gói tin phù hợp với một tuyến trong bảng này, nó sẽ được xử lý ở tầng giao thức tiếp theo.

- **Bảng `main`** chứa các tuyến đường chính, được sử dụng để thực hiện định tuyến trên máy tính. Nếu tìm thấy một quy tắc phù hợp, gói tin sẽ được chuyển tiếp qua giao diện mạng tương ứng.

- **Bảng `default`** được sử dụng để chỉ định tuyến đường cho các gói tin không được xử lý trong hai bảng trước đó. Thông thường, bảng này trống.

Nếu không tìm thấy tuyến đường trong bất kỳ bảng nào, gói tin sẽ bị loại bỏ. Trong trường hợp này, một thông báo ICMP về lỗi “Destination host unreachable” sẽ được gửi đến địa chỉ nguồn của gói tin.

Danh sách kiểm tra bảng định tuyến được định nghĩa bằng một tập hợp các quy tắc. Mặc định, tập hợp này trông như sau (lệnh `ip rule list`):
```
0:    from all lookup local
32766: from all lookup main
32767: from all lookup default
```
Tất cả các quy tắc được xử lý theo thứ tự tăng dần của chỉ số. Sau ký hiệu `:` là quy tắc chỉ định hành động cần thực hiện cho gói tin hiện tại. Sau từ khóa `lookup` là bảng định tuyến mà sẽ được tìm kiếm tuyến đường phù hợp cho gói tin hiện tại.

Ví dụ, quy tắc đầu tiên (`from all`) có nghĩa là tất cả các gói tin từ bất kỳ nguồn nào đều được xử lý.

---

Trong quá trình xử lý gói tin qua bộ định tuyến, các bước kiểm tra gói tin được thực hiện tại các giai đoạn khác nhau (định tuyến, chuyển đổi trường dữ liệu, hoặc NAT). Trong thuật ngữ của Linux, các giai đoạn này tương ứng với các bảng sau:

- **Mangle**: Thay đổi các trường như ToS, TTL, hoặc thêm nhãn đặc biệt vào gói tin để sử dụng ở các bảng khác.
- **NAT**: Thực hiện chuyển đổi địa chỉ IP và cổng UDP/TCP.
- **Filter**: Lọc các gói tin (tính năng chính của firewall) để ngăn chặn các gói không mong muốn.
- **Raw** và **Security**: Các bảng này được sử dụng trong các trường hợp cụ thể, không được xem xét ở đây.

---

Trong mỗi bảng, có các chuỗi quy tắc được kích hoạt ở các giai đoạn xử lý gói tin (PREROUTING, INPUT, FORWARD, OUTPUT, POSTROUTING). Theo mặc định, tất cả các bảng đều rỗng, nên cần phải cấu hình các quy tắc để thực hiện hành động cụ thể.

---

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/1_Basic_concepts_of_network_technologies/image/Notations_used_in_the_course.png" alt="Hình 4.1. Sơ đồ đơn giản hóa về quá trình xử lý gói tin qua các chuỗi trong bảng của tường lửa Linux." width="800">
</p>

<p align="center"><b>Hình 4.1. Sơ đồ đơn giản hóa về quá trình xử lý gói tin qua các chuỗi trong bảng của tường lửa Linux.</b></p>

Có thể dường như việc một số bảng (ví dụ: *mangle*) xuất hiện đồng thời trong nhiều chuỗi là dư thừa. Tuy nhiên, sự dư thừa này cho phép linh hoạt đặt quy tắc xử lý gói tin. Ví dụ: nếu thêm quy tắc vào bảng *mangle* trong chuỗi *FORWARD*, quy tắc này sẽ chỉ áp dụng cho các gói tin được chuyển tiếp trong kịch bản 2, nhưng không áp dụng cho các gói tin trong kịch bản 1 và 3. Ngược lại, nếu thêm quy tắc vào chuỗi *POSTROUTING* trong cùng bảng *mangle*, quy tắc đó sẽ được áp dụng cho tất cả gói tin trong kịch bản 2 và 3, nhưng không áp dụng cho kịch bản 1 (điều này được minh họa bằng đường nét đứt trong Hình 4.1). 

Lưu ý rằng trong mỗi kịch bản đều có một chuỗi riêng biệt mà không có ở các chuỗi khác. Điều này cho phép thực hiện logic xử lý độc lập đối với bất kỳ loại gói tin nào trong mỗi kịch bản.

Chữ cái "d" trong ngoặc trước bảng *nat* chỉ ra rằng trong chuỗi tương ứng trong khuôn khổ công nghệ NAT, việc thay đổi chỉ áp dụng cho địa chỉ đích (*destination*). Điều này được giải thích bởi thực tế là thay đổi địa chỉ đích là cần thiết để tìm tuyến đường trong quá trình truyền tải (tên chuỗi *PREROUTING* được hiểu theo nghĩa đen là "trước định tuyến"). Tương tự, chữ "s" trong ngoặc chỉ ra rằng trong bảng tương ứng, chỉ cần thay đổi địa chỉ nguồn (*source*).


