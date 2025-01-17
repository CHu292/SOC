# DNS in detail

> Chi tiết về DNS: Tìm hiểu cách DNS hoạt động và cách nó hỗ trợ bạn truy cập các dịch vụ trên Internet.

## Mục lục

1. [Task 1: What is DNS?](#task-1-what-is-dns)  
2. [Task 2: Domain Hierarchy](#task-2-domain-hierarchy)  
3. [Task 3: Record Types](#task-3-record-types)  
4. [Task 4: Making A Request](#task-4-making-a-request)  
5. [Task 5: Practical](#task-5-practical)

## Nội dung

# Task 1: What is DNS?

 **DNS là gì?**

**DNS (Domain Name System)** cung cấp một cách đơn giản để chúng ta giao tiếp với các thiết bị trên Internet mà không cần nhớ những con số phức tạp. Giống như mỗi ngôi nhà có một địa chỉ duy nhất để gửi thư trực tiếp, mỗi máy tính trên Internet cũng có một địa chỉ duy nhất để giao tiếp, được gọi là **địa chỉ IP**.  

Một địa chỉ IP trông như sau: **104.26.10.229**, bao gồm 4 nhóm số trong khoảng từ **0 - 255**, được ngăn cách bằng dấu chấm. Khi bạn muốn truy cập một trang web, việc nhớ một dãy số phức tạp như vậy không hề thuận tiện, và đó là lúc **DNS** giúp ích.  

Thay vì phải nhớ **104.26.10.229**, bạn chỉ cần nhớ **tryhackme.com**.

![DNS](./img/1_DNS_in_detail/1.1.png)

**Câu hỏi:** DNS viết tắt của?

<details>  
  <summary>Hiển thị đáp án</summary>  
  Đáp án: Domain Name System.  
</details>  

# Task 2: Domain Hierarchy

## **Hệ thống phân cấp miền**

![Hệ thống phân cấp miền](./img/1_DNS_in_detail/2.1.png)

## TLD (Top-Level Domain)  
TLD là phần nằm ở bên phải nhất của một tên miền. Ví dụ, trong **tryhackme.com**, TLD là **.com**. Có hai loại TLD:  
- **gTLD (Generic Top Level Domain)**: Được sử dụng cho mục đích cụ thể, ví dụ: **.com** cho mục đích thương mại, **.org** cho tổ chức, **.edu** cho giáo dục và **.gov** cho chính phủ.  
- **ccTLD (Country Code Top Level Domain)**: Được sử dụng cho các mục đích địa lý, ví dụ: **.ca** cho Canada, **.co.uk** cho Vương quốc Anh, v.v.  

Do nhu cầu lớn, hiện nay có sự gia tăng về số lượng gTLD mới, ví dụ: **.online**, **.club**, **.website**, **.biz**, và nhiều loại khác.  

[Xem thêm các tên miền TLD tại đây](https://data.iana.org/TLD/tlds-alpha-by-domain.txt)

## Second-Level Domain  
Sử dụng ví dụ **tryhackme.com**, phần **.com** là TLD, và **tryhackme** là Second-Level Domain (Tên miền cấp hai). Khi đăng ký một tên miền, **Second-Level Domain** bị giới hạn tối đa 63 ký tự (bao gồm cả TLD) và chỉ được sử dụng các ký tự **a-z, 0-9** và **dấu gạch ngang (-)** (không được bắt đầu, kết thúc bằng dấu gạch ngang, hoặc có các gạch ngang liền nhau).

## Subdomain  
Subdomain nằm bên trái của **Second-Level Domain** và được tách ra bằng dấu chấm. Ví dụ: trong **admin.tryhackme.com**, phần **admin** là subdomain.  

Tên subdomain có các hạn chế tương tự như Second-Level Domain:  
- Giới hạn tối đa 63 ký tự, chỉ sử dụng các ký tự **a-z, 0-9** và **dấu gạch ngang (-)** (không được bắt đầu, kết thúc bằng dấu gạch ngang, hoặc có các gạch ngang liền nhau).  
- Có thể sử dụng nhiều subdomain được ngăn cách bằng dấu chấm để tạo tên dài hơn, ví dụ: **jupiter.servers.tryhackme.com**.  

Tuy nhiên, độ dài tối đa phải dưới **253 ký tự**. Không có giới hạn về số lượng subdomain bạn có thể tạo cho tên miền của mình.

**Trả lời các câu hỏi dưới đây:**

1. **Độ dài tối đa của một subdomain là bao nhiêu?**  
   <details>
   <summary>Hiển thị đáp án</summary>
   Đáp án: 63
   </details>

2. **Ký tự nào sau đây không thể sử dụng trong subdomain (3 b _ - )?**  
   <details>
   <summary>Hiển thị đáp án</summary>
   Đáp án: _ (dấu gạch dưới)
   </details>

3. **Độ dài tối đa của một tên miền là bao nhiêu?**  
   <details>
   <summary>Hiển thị đáp án</summary>
   Đáp án: 253
   </details>

4. **TLD của .co.uk thuộc loại nào?**  
   <details>
   <summary>Hiển thị đáp án</summary>
   Đáp án: ccTLD
   </details>

# Task 3: Record Types

 **Các loại bản ghi DNS**

## **Bản ghi A**
Những bản ghi này ánh xạ tới địa chỉ IPv4, ví dụ: 104.26.10.229.

## **Bản ghi AAAA**
Những bản ghi này ánh xạ tới địa chỉ IPv6, ví dụ: 2606:4700:20::681a:be5.

## **Bản ghi CNAME**
Những bản ghi này ánh xạ tới một tên miền khác, ví dụ: cửa hàng trực tuyến của TryHackMe có tên miền phụ `store.tryhackme.com`, ánh xạ tới bản ghi CNAME `shops.shopify.com`. Một yêu cầu DNS khác sau đó sẽ được thực hiện để tìm địa chỉ IP.

## **Bản ghi MX**
Những bản ghi này ánh xạ tới địa chỉ của các máy chủ xử lý email cho tên miền bạn truy vấn, ví dụ: một phản hồi bản ghi MX cho `tryhackme.com` có thể giống như `alt1.aspmx.l.google.com`. Những bản ghi này cũng đi kèm với cờ ưu tiên. Điều này cho biết khách hàng nên thử các máy chủ theo thứ tự nào, rất hữu ích nếu máy chủ chính bị lỗi và email cần được gửi tới máy chủ dự phòng.

## **Bản ghi TXT**
Bản ghi TXT là các trường văn bản tự do nơi dữ liệu dựa trên văn bản có thể được lưu trữ. Các bản ghi TXT có nhiều ứng dụng, một số trong đó là liệt kê các máy chủ có thẩm quyền gửi email thay mặt cho tên miền (hữu ích trong việc chống lại thư rác và email giả mạo). Chúng cũng có thể được sử dụng để xác minh quyền sở hữu tên miền khi đăng ký các dịch vụ bên thứ ba.

**Câu hỏi:**

**Câu 1:** Loại bản ghi nào được sử dụng để xác định nơi gửi email?  
<details>  
  <summary>Hiển thị đáp án</summary>  
  Đáp án: MX  
</details>  

**Câu 2:** Loại bản ghi nào xử lý các địa chỉ IPv6?  
<details>  
  <summary>Hiển thị đáp án</summary>  
  Đáp án: AAAA  
</details>  

# Task 4: Making A Request

**Điều gì xảy ra khi bạn thực hiện một yêu cầu DNS**

**1.** Khi bạn yêu cầu một tên miền, máy tính của bạn sẽ kiểm tra bộ nhớ đệm cục bộ để xem liệu bạn đã tra cứu địa chỉ này gần đây hay chưa. Nếu không, một yêu cầu sẽ được gửi đến Máy chủ DNS Đệ quy (Recursive DNS Server) của bạn.

**2.** Máy chủ DNS Đệ quy thường được cung cấp bởi nhà cung cấp dịch vụ Internet (ISP -  Internet Service Provider) của bạn, nhưng bạn cũng có thể chọn máy chủ riêng của mình. Máy chủ này cũng có bộ nhớ đệm cục bộ chứa các tên miền đã được tra cứu gần đây. Nếu kết quả được tìm thấy trong bộ nhớ đệm cục bộ, kết quả này sẽ được gửi lại cho máy tính của bạn và yêu cầu của bạn kết thúc tại đây (điều này thường xảy ra với các dịch vụ phổ biến và có nhiều yêu cầu như Google, Facebook, Twitter). Nếu không tìm thấy kết quả trong bộ nhớ cục bộ, một hành trình sẽ bắt đầu để tìm câu trả lời chính xác, bắt đầu từ các máy chủ DNS gốc của internet.

**3.** Các máy chủ gốc (root servers) hoạt động như xương sống DNS của internet; nhiệm vụ của chúng là chuyển hướng bạn đến Máy chủ Miền Cấp Cao Nhất (Top Level Domain Server) phù hợp, tùy thuộc vào yêu cầu của bạn. Ví dụ: nếu bạn yêu cầu **www.tryhackme.com**, máy chủ gốc sẽ nhận ra Tên Miền Cấp Cao Nhất là **.com** và chuyển bạn đến máy chủ TLD phù hợp xử lý các địa chỉ **.com**.

**4.** Máy chủ TLD lưu trữ các bản ghi chỉ dẫn nơi tìm thấy máy chủ có thẩm quyền (authoritative server) để trả lời yêu cầu DNS. Máy chủ có thẩm quyền thường được gọi là nameserver của tên miền. Ví dụ: nameserver cho **tryhackme.com** là **kip.ns.cloudflare.com** và **uma.ns.cloudflare.com**. Bạn thường thấy nhiều nameserver cho một tên miền để hoạt động như bản sao lưu trong trường hợp một máy chủ gặp sự cố.

**5.** Máy chủ DNS có thẩm quyền (authoritative DNS server) là máy chủ chịu trách nhiệm lưu trữ các bản ghi DNS cho một tên miền cụ thể và nơi thực hiện bất kỳ cập nhật nào đối với các bản ghi DNS của tên miền đó. Tùy thuộc vào loại bản ghi, bản ghi DNS sau đó được gửi lại tới Máy chủ DNS Đệ quy (Recursive DNS Server), nơi một bản sao cục bộ sẽ được lưu trữ tạm thời (cached) để sử dụng cho các yêu cầu trong tương lai và sau đó được chuyển tiếp lại tới máy khách ban đầu đã thực hiện yêu cầu.

Các bản ghi DNS đều đi kèm với một giá trị TTL (Time To Live). Giá trị này được biểu diễn bằng số giây mà phản hồi sẽ được lưu trữ cục bộ cho đến khi bạn cần tra cứu lại. Việc lưu trữ tạm thời (caching) giúp giảm nhu cầu phải gửi yêu cầu DNS mỗi khi bạn giao tiếp với một máy chủ.

![DNS request](./img/1_DNS_in_detail/4.1.png)

**Câu hỏi:**

**Câu hỏi 1:** Trường nào xác định thời gian một bản ghi DNS được lưu trong bộ nhớ đệm?  
<details>  
<summary>Hiển thị đáp án</summary>  
Đáp án: TTL  
</details>  

**Câu hỏi 2:** Loại máy chủ DNS nào thường được nhà cung cấp dịch vụ Internet (ISP) cung cấp?  
<details>  
<summary>Hiển thị đáp án</summary>  
Đáp án: recursive  
</details>  

**Câu hỏi 3:** Loại máy chủ nào lưu trữ tất cả các bản ghi cho một tên miền?  
<details>  
<summary>Hiển thị đáp án</summary>  
Đáp án: authoritative  
</details>  

