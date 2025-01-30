![image](https://github.com/user-attachments/assets/75e428ad-4ab4-4188-bd60-abf5905d00f5)# Active Directory Basics

> Phòng này sẽ giới thiệu các khái niệm và chức năng cơ bản được cung cấp bởi Active Directory.

## Mục Lục

1. [Task 1: Introduction](#task-1-introduction)

2. [Task 2: Windows Domains](#task-2-windows-domains)

3. [Task 3: Active Directory](#task-3-active-directory)

4. [Task 4: Managing Users in AD](#task-4-managing-users-in-ad)

5. [Task 5: Managing Computers in AD](#task-5-managing-computers-in-ad)

6. [Task 6: Group Policies](#task-6-group-policies)

7. [Task 7: Authentication Methods](#task-7-authentication-methods)

8. [Task 8: Trees, Forests and Trusts](#task-8-trees-forests-and-trusts)

9. [Task 9: Conclusion](#task-9-conclusion)

## Nội dung

# Task 1: Introduction

Microsoft Active Directory là xương sống của thế giới doanh nghiệp. Nó đơn giản hóa việc quản lý các thiết bị và người dùng trong một môi trường doanh nghiệp. Trong phòng này, chúng ta sẽ đi sâu vào các thành phần quan trọng của Active Directory.

#### Mục tiêu của phòng:

Trong phòng này, chúng ta sẽ học về Active Directory và làm quen với các chủ đề sau:
- Active Directory là gì
- Miền (Domain) của Active Directory là gì
- Các thành phần trong một miền Active Directory
- Rừng (Forests) và mối quan hệ tin cậy giữa các miền (Domain Trust)
- Và nhiều nội dung khác!

#### Yêu cầu đầu vào:
- Hiểu biết cơ bản về Windows. Hãy kiểm tra [Windows Fundamentals module](https://github.com/CHu292/SOC/tree/main/Try_Hack_Me/Pre_Security/5_Windows_Fundamentals) để biết thêm thông tin về điều này.

# Task 2: Windows Domains

Hãy tưởng tượng bạn đang quản lý một mạng của một doanh nghiệp nhỏ chỉ với năm máy tính và năm nhân viên. Trong một mạng nhỏ như vậy, bạn có thể cấu hình từng máy tính một cách riêng lẻ mà không gặp vấn đề gì. Bạn sẽ đăng nhập thủ công vào từng máy tính, tạo người dùng cho những ai cần sử dụng chúng và thực hiện các cấu hình cụ thể cho từng tài khoản nhân viên. Nếu máy tính của một người dùng gặp sự cố, bạn có thể đến chỗ họ và sửa máy tính tại chỗ.

Mặc dù điều này nghe có vẻ như một cuộc sống rất thư thả, nhưng giả sử doanh nghiệp của bạn đột nhiên phát triển và bây giờ có 157 máy tính và 320 người dùng khác nhau, nằm rải rác tại bốn văn phòng khác nhau. Liệu bạn có thể tiếp tục quản lý từng máy tính như một thực thể riêng biệt, cấu hình thủ công các chính sách cho từng người dùng trên toàn bộ mạng và cung cấp hỗ trợ tại chỗ cho tất cả mọi người? Câu trả lời có khả năng cao là không.

Để vượt qua những hạn chế này, chúng ta có thể sử dụng một miền Windows (Windows domain). Nói đơn giản, một **miền Windows** là một nhóm người dùng và máy tính dưới sự quản lý của một doanh nghiệp nhất định. Ý tưởng chính của một miền là tập trung hóa việc quản trị các thành phần chung của một mạng máy tính Windows trong một kho lưu trữ duy nhất gọi là **Active Directory (AD)**. Máy chủ chạy dịch vụ Active Directory được gọi là **Domain Controller (DC)**. 

![windows domains](./img/2.1.png)

Những lợi ích chính của việc có một miền Windows được cấu hình bao gồm:

- **Quản lý danh tính tập trung:** Tất cả người dùng trên mạng có thể được cấu hình từ Active Directory với nỗ lực tối thiểu.  
- **Quản lý chính sách bảo mật:** Bạn có thể cấu hình các chính sách bảo mật trực tiếp từ Active Directory và áp dụng chúng cho người dùng và máy tính trên toàn mạng khi cần.

## Một ví dụ thực tế

Nếu điều này nghe có vẻ hơi khó hiểu, có khả năng bạn đã từng tương tác với một miền Windows ở trường học, đại học hoặc nơi làm việc của bạn.

Trong mạng lưới trường học/đại học, bạn thường sẽ được cung cấp một tên người dùng và mật khẩu mà bạn có thể sử dụng trên bất kỳ máy tính nào có sẵn trong khuôn viên. Thông tin xác thực của bạn hợp lệ cho tất cả các máy vì bất cứ khi nào bạn nhập chúng vào một máy, quá trình xác thực sẽ được chuyển đến Active Directory, nơi thông tin xác thực của bạn sẽ được kiểm tra. Nhờ Active Directory, thông tin xác thực của bạn không cần tồn tại trên từng máy riêng lẻ mà vẫn có thể sử dụng được trên toàn mạng.

Active Directory cũng là thành phần cho phép trường học/đại học của bạn hạn chế bạn truy cập vào bảng điều khiển (control panel) trên các máy của trường học/đại học. Các chính sách thường sẽ được triển khai trên toàn mạng để bạn không có quyền quản trị trên các máy tính đó.

## Chào mừng đến với THM Inc.

Trong nhiệm vụ này, chúng ta sẽ đảm nhận vai trò của một quản trị viên IT mới tại THM Inc. Nhiệm vụ đầu tiên của chúng ta là xem xét miền hiện tại "THM.local" và thực hiện một số cấu hình bổ sung. Bạn sẽ có thông tin đăng nhập quản trị để truy cập Domain Controller (DC) đã được cấu hình sẵn để thực hiện các nhiệm vụ.

Nếu bạn muốn kết nối với máy này qua **RDP**, bạn có thể sử dụng thông tin đăng nhập sau đây: 

![windows domains](./img/2.2.png)

**Lưu ý:** Khi kết nối qua **RDP**, sử dụng **THM\Administrator** làm tên người dùng để chỉ định rằng bạn muốn đăng nhập với tài khoản **Administrator** trong miền **THM**.

Vì chúng ta sẽ kết nối đến máy mục tiêu qua **RDP**, đây cũng là thời điểm thích hợp để khởi động **AttackBox** (trừ khi bạn đang sử dụng máy của chính mình). 

**Câu hỏi 1: Trong một miền Windows, thông tin xác thực được lưu trữ trong kho lưu trữ tập trung được gọi là gì?**  
<details>  
<summary>Hiển thị đáp án</summary>  
Đáp án: Active Directory  
</details>  

**Câu hỏi 2: Máy chủ chịu trách nhiệm vận hành các dịch vụ Active Directory được gọi là gì?**  
<details>  
<summary>Hiển thị đáp án</summary>  
Đáp án: Domain Controller  
</details>  

# Task 3: Active Directory

Trung tâm của bất kỳ Miền Windows nào là **Active Directory Domain Service (AD DS)**. Dịch vụ này hoạt động như một danh mục chứa thông tin về tất cả các "đối tượng" tồn tại trên mạng của bạn. Trong số nhiều đối tượng được hỗ trợ bởi **AD**, chúng ta có người dùng, nhóm, máy tính, máy in, chia sẻ và nhiều đối tượng khác. Hãy xem một số trong số đó:

## Người dùng (Users)  

Người dùng là một trong những loại đối tượng phổ biến nhất trong Active Directory. Người dùng là một trong những đối tượng được gọi là **security principals** (nguyên tắc bảo mật), có nghĩa là họ có thể được xác thực bởi miền và có thể được cấp quyền đối với **resources** (tài nguyên) như tệp hoặc máy in. Bạn có thể nói rằng một nguyên tắc bảo mật là một đối tượng có thể hành động trên các tài nguyên trong mạng.

Người dùng có thể được sử dụng để đại diện cho hai loại thực thể:  

- **People**: Người dùng thường đại diện cho các cá nhân trong tổ chức của bạn cần truy cập vào mạng, chẳng hạn như nhân viên.  
- **Services**: Bạn cũng có thể xác định người dùng để được sử dụng bởi các dịch vụ như IIS hoặc MSSQL. Mỗi dịch vụ riêng lẻ yêu cầu một người dùng để chạy, nhưng người dùng dịch vụ khác với người dùng thông thường vì họ chỉ có quyền cần thiết để chạy dịch vụ cụ thể của họ.  

## Máy tính (Machines)  

Máy tính là một loại đối tượng khác trong Active Directory; đối với mỗi máy tính tham gia miền Active Directory, một đối tượng máy tính sẽ được tạo. Máy tính cũng được xem là **"security principals"** (nguyên tắc bảo mật) và được chỉ định một tài khoản giống như bất kỳ người dùng thông thường nào. Tài khoản này có quyền hạn chế hơn trong chính miền đó.

Bản thân tài khoản máy tính là quản trị viên cục bộ trên máy tính được chỉ định, chúng thường không được phép truy cập bởi bất kỳ ai ngoài chính máy tính, nhưng giống như bất kỳ tài khoản nào khác, nếu bạn có mật khẩu, bạn có thể sử dụng nó để đăng nhập.

**Lưu ý**: Mật khẩu của tài khoản máy tính được tự động thay đổi và thường bao gồm 120 ký tự ngẫu nhiên.  

Việc xác định tài khoản máy tính tương đối đơn giản. Chúng tuân theo một quy ước đặt tên cụ thể. Tên tài khoản máy tính là tên của máy tính, theo sau là ký hiệu đô la ($). Ví dụ: một máy tính có tên **DC01** sẽ có tài khoản máy tính được gọi là **DC01$**.  

## Nhóm bảo mật (Security Groups)

Nếu bạn quen thuộc với Windows, bạn có thể biết rằng bạn có thể định nghĩa các nhóm người dùng để gán quyền truy cập vào tệp hoặc tài nguyên khác cho toàn bộ nhóm thay vì từng người dùng. Điều này giúp quản lý dễ dàng hơn vì bạn có thể thêm người dùng vào một nhóm hiện có, và họ sẽ tự động kế thừa tất cả các quyền của nhóm đó. Nhóm bảo mật cũng được xem là **security principals** (nguyên tắc bảo mật) và, do đó, có thể có quyền đối với các tài nguyên trong mạng.

Các nhóm có thể có cả người dùng và máy tính làm thành viên. Nếu cần, nhóm có thể bao gồm các nhóm khác.

Một số nhóm được tạo mặc định trong một miền có thể được sử dụng để cấp các quyền cụ thể cho người dùng. Ví dụ, dưới đây là một số nhóm quan trọng nhất trong một miền:

| **Nhóm bảo mật (Security Group)** | **Mô tả (Description)** |
|----------------------------------|--------------------------|
| **Domain Admins**               | Người dùng trong nhóm này có quyền quản trị trên toàn bộ miền. Theo mặc định, họ có thể quản trị bất kỳ máy tính nào trong miền, bao gồm cả Domain Controllers (DCs). |
| **Server Operators**            | Người dùng trong nhóm này có thể quản trị Domain Controllers. Họ không thể thay đổi tư cách thành viên của các nhóm quản trị. |
| **Backup Operators**            | Người dùng trong nhóm này được phép truy cập bất kỳ tệp nào, bất kể quyền hạn. Họ được sử dụng để thực hiện sao lưu dữ liệu trên máy tính. |
| **Account Operators**           | Người dùng trong nhóm này có thể tạo hoặc sửa đổi các tài khoản khác trong miền. |
| **Domain Users**                | Bao gồm tất cả tài khoản người dùng hiện có trong miền. |
| **Domain Computers**            | Bao gồm tất cả máy tính hiện có trong miền. |
| **Domain Controllers**          | Bao gồm tất cả các Domain Controllers (DCs) hiện có trong miền. |

Bạn có thể tham khảo danh sách đầy đủ các nhóm bảo mật mặc định từ [tài liệu của Microsoft](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups).

## **Active Directory Users and Computers**

Để cấu hình người dùng, nhóm hoặc máy tính trong Active Directory, chúng ta cần đăng nhập vào Domain Controller và chạy **"Active Directory Users and Computers"** từ menu Start.

![Người dùng và máy tính Active Directory](./img/3.1.png)

Điều này sẽ mở một cửa sổ nơi bạn có thể thấy được hệ thống phân cấp của người dùng, máy tính và nhóm tồn tại trong miền. Các đối tượng này được tổ chức trong **Organizational Units (OUs)**, là các đối tượng chứa (**container objects**) cho phép bạn phân loại người dùng và máy tính. OUs chủ yếu được sử dụng để định nghĩa các nhóm người dùng với các yêu cầu chính sách tương tự. Ví dụ, nhân viên trong bộ phận Kinh doanh của tổ chức bạn có thể có một bộ chính sách khác với những người trong bộ phận IT. Lưu ý rằng một người dùng chỉ có thể thuộc một OU duy nhất tại một thời điểm.

Kiểm tra máy của chúng ta, ta có thể thấy đã có một OU được gọi là **THM** với bốn OU (Organizational Unit) con cho các bộ phận IT, Quản lý, Tiếp thị và Kinh doanh. Đây là một mô hình phổ biến vì nó cho phép triển khai hiệu quả các chính sách cơ bản áp dụng cho toàn bộ các phòng ban. Hãy nhớ rằng, mặc dù đây sẽ là mô hình dự kiến hầu hết thời gian, bạn cũng có thể định nghĩa OUs theo ý muốn. Cứ thoải mái nhấp chuột phải vào OU **THM** và tạo một OU mới bên trong gọi là **Students** chỉ để thử nghiệm. 

![Người dùng và máy tính Active Directory](./img/3.2.png)

Nếu bạn mở bất kỳ OU nào, bạn có thể thấy người dùng mà chúng chứa và thực hiện các tác vụ đơn giản như tạo, xóa hoặc chỉnh sửa chúng khi cần thiết. Bạn cũng có thể đặt lại mật khẩu nếu cần (rất hữu ích cho bộ phận hỗ trợ kỹ thuật).

Chắc hẳn bạn đã nhận ra rằng có một số container mặc định khác ngoài OU **THM**. Những container này được Windows tự động tạo ra và bao gồm các nội dung sau:

- **Builtin**: Chứa các nhóm mặc định có sẵn trên bất kỳ máy chủ Windows nào.
- **Computers**: Bất kỳ máy nào tham gia vào mạng sẽ được đưa vào đây theo mặc định. Bạn có thể di chuyển chúng nếu cần.
- **Domain Controllers**: OU mặc định chứa các DC (Domain Controller) trong mạng của bạn.
- **Users**: Người dùng và nhóm mặc định áp dụng trong toàn bộ bối cảnh của miền (domain-wide).
- **Managed Service Accounts**: Chứa các tài khoản được sử dụng bởi các dịch vụ trong miền Windows của bạn.

## So sánh giữa Security Groups và OUs

Có lẽ bạn đang tự hỏi tại sao lại có cả **nhóm bảo mật** (Security Groups) và **OUs**. Mặc dù cả hai đều được sử dụng để phân loại người dùng và máy tính, mục đích của chúng hoàn toàn khác nhau:

- **OUs** rất hữu ích để **áp dụng chính sách** cho người dùng và máy tính, bao gồm các cấu hình cụ thể áp dụng cho các nhóm người dùng dựa trên vai trò của họ trong doanh nghiệp. Lưu ý rằng, một người dùng chỉ có thể là thành viên của **một OU duy nhất** tại một thời điểm, vì không có lý do hợp lý để áp dụng hai tập hợp chính sách khác nhau cho một người dùng duy nhất.

- **Security Groups**, mặt khác, được sử dụng để **cấp quyền truy cập vào các tài nguyên**. Ví dụ: bạn sẽ sử dụng các nhóm nếu bạn muốn một số người dùng có quyền truy cập vào một thư mục được chia sẻ hoặc một máy in mạng. Một người dùng có thể là thành viên của nhiều nhóm, điều này rất cần thiết để cấp quyền truy cập vào nhiều tài nguyên khác nhau.

**Câu hỏi:**

---

**Câu hỏi 1: Nhóm nào thường quản lý tất cả các máy tính và tài nguyên trong một miền?**  
<details>  
<summary>Hiển thị đáp án</summary>  
Đáp án: Domain Admins  
</details>  

---

**Câu hỏi 2: Tên của tài khoản máy được liên kết với một máy có tên TOM-PC sẽ là gì?**  
<details>  
<summary>Hiển thị đáp án</summary>  
Đáp án: TOM-PC$  
</details>  

Trong môi trường **Active Directory (AD)**, tài khoản máy tính (**machine account**) được tạo tự động khi một máy tính được tham gia vào miền (**domain**). Tên của tài khoản máy tính thường tuân theo quy tắc:  

**Tên máy + ký tự "$"**  

**Tài khoản máy tính dùng để làm gì?**
1. **Xác thực (Authentication)** – Máy tính sử dụng tài khoản này để xác thực với bộ điều khiển miền (**Domain Controller**).  
2. **Áp dụng Group Policy** – Cho phép máy tính nhận các chính sách bảo mật và cấu hình từ hệ thống.  
3. **Giao tiếp bảo mật** – Đảm bảo kết nối an toàn giữa máy tính và các dịch vụ trên mạng nội bộ.

---

**Câu hỏi 3: Giả sử công ty chúng ta tạo một bộ phận mới dành cho Đảm bảo Chất lượng (Quality Assurance). Chúng ta nên sử dụng loại container nào để nhóm tất cả người dùng Quality Assurance sao cho chính sách có thể được áp dụng nhất quán với họ?**  
<details>  
<summary>Hiển thị đáp án</summary>  
Đáp án: Organizational Units  
</details>  

Để nhóm tất cả người dùng thuộc bộ phận **Đảm bảo Chất lượng (Quality Assurance - QA)** và áp dụng chính sách một cách nhất quán, bạn nên sử dụng **Đơn vị Tổ chức (Organizational Units - OUs)** trong **Active Directory (AD)** hoặc **Azure AD** nếu sử dụng môi trường đám mây.  

**Tại sao nên sử dụng Đơn vị Tổ chức (OU)?**

1. **Áp dụng chính sách nhất quán** – OUs cho phép bạn triển khai **Chính sách Nhóm (Group Policies - GPOs)** trong Active Directory, đảm bảo rằng tất cả người dùng QA đều có chung cài đặt bảo mật, quyền truy cập và tuân thủ quy định.  
2. **Quản lý tập trung** – Quản trị viên có thể dễ dàng quản lý tài khoản người dùng, quyền hạn và cài đặt bảo mật cho toàn bộ nhóm QA trong một vị trí duy nhất.  
3. **Phân quyền quản trị** – Nếu trưởng nhóm QA hoặc nhân viên IT cần quyền kiểm soát cụ thể đối với người dùng QA, có thể cấp quyền quản lý trực tiếp trên OU.  
4. **Khả năng mở rộng** – Khi bộ phận QA phát triển, bạn chỉ cần thêm người dùng mới vào OU và họ sẽ tự động kế thừa các chính sách đã thiết lập.  

**Các phương pháp thay thế**

- **Nhóm Bảo mật (Security Groups)**: Hữu ích để kiểm soát quyền truy cập vào tài nguyên hệ thống và ứng dụng.  
- **Nhóm Động (Dynamic Groups - Azure AD)**: Nếu sử dụng môi trường đám mây, có thể thiết lập nhóm động để tự động thêm người dùng vào nhóm QA dựa trên thông tin như chức danh công việc hoặc phòng ban.  
---

# Task 4: Managing Users in AD

**Quản lý Người dùng trong Active Directory (AD)**

Nhiệm vụ đầu tiên của bạn với tư cách là quản trị viên miền mới là kiểm tra các OU (Organizational Units) và người dùng hiện có trong **Active Directory (AD)**, vì một số thay đổi gần đây đã xảy ra trong doanh nghiệp. Bạn đã được cung cấp sơ đồ tổ chức sau đây và dự kiến sẽ thực hiện các thay đổi trong **AD** để phù hợp với nó.

> **Active Directory** là một dịch vụ thư mục được Microsoft phát triển cho các mạng miền Windows. Nó lưu trữ thông tin về các đối tượng trong mạng như máy tính, người dùng và nhóm. Dịch vụ này cung cấp khả năng xác thực và ủy quyền, đồng thời cho phép quản trị viên quản lý tài nguyên mạng tập trung.

![Active Directory](./img/4.1.png)

## Xóa các OU và người dùng dư thừa

Điều đầu tiên bạn nên nhận thấy là có một **OU (Organizational Unit)** bổ sung trong cấu hình **AD (Active Directory)** hiện tại của bạn mà không xuất hiện trong sơ đồ tổ chức. Chúng tôi được thông báo rằng bộ phận này đã bị đóng do cắt giảm ngân sách và cần được xóa khỏi miền. Nếu bạn cố nhấp chuột phải và xóa **OU**, bạn sẽ gặp lỗi sau:

![xóa OU](./img/4.2.png)

> Trong các miền Windows, **Organizational Unit (OU)** đề cập đến các **container** chứa người dùng, nhóm và máy tính mà các chính sách tương tự nên được áp dụng.  
Trong hầu hết các trường hợp, **OU** sẽ tương ứng với các **phòng ban** trong một doanh nghiệp.

Theo mặc định, các **OU** được bảo vệ khỏi việc xóa nhầm. Để xóa **OU**, chúng ta cần kích hoạt **Advanced Features** trong menu **View**.

![xóa OU](./img/4.3.png)

Điều này sẽ hiển thị cho bạn một số container bổ sung và cho phép bạn tắt tính năng bảo vệ khỏi việc xóa nhầm. Để thực hiện, nhấp chuột phải vào **OU**, chọn **Properties**. Bạn sẽ tìm thấy một hộp kiểm trong tab **Object** để tắt bảo vệ.

![xóa OU](./img/4.4.png)

Hãy chắc chắn bỏ chọn hộp kiểm và thử xóa lại **OU**. Bạn sẽ được nhắc xác nhận rằng bạn muốn xóa **OU**, và kết quả là, bất kỳ người dùng, nhóm hoặc **OU** nào bên dưới nó cũng sẽ bị xóa.

Sau khi xóa **OU** dư thừa, bạn nên nhận thấy rằng đối với một số phòng ban, người dùng trong **AD** không khớp với những người trong sơ đồ tổ chức của chúng ta. Hãy tạo và xóa người dùng khi cần để khớp với sơ đồ.

## **Ủy quyền (Delegation)**

Một trong những điều hữu ích mà bạn có thể làm trong **AD** là cấp quyền kiểm soát một số **OU** nhất định cho một số người dùng cụ thể. Quá trình này được gọi là **ủy quyền (delegation)** và cho phép bạn cấp quyền đặc biệt để thực hiện các tác vụ nâng cao trên **OU** mà không cần Quản trị viên miền (Domain Administrator) can thiệp.

Một trong những trường hợp sử dụng phổ biến nhất cho điều này là cấp quyền cho nhóm **IT support** để đặt lại mật khẩu của người dùng có quyền hạn thấp hơn. Theo sơ đồ tổ chức của chúng ta, Phillip phụ trách **IT support**, vì vậy có thể chúng ta sẽ muốn ủy quyền kiểm soát việc đặt lại mật khẩu cho các **OU** của bộ phận **Sales, Marketing và Management** cho anh ta.

Trong ví dụ này, chúng ta sẽ ủy quyền kiểm soát **OU Sales** cho Phillip. Để ủy quyền kiểm soát một **OU**, bạn có thể nhấp chuột phải vào nó và chọn **Delegate Control**.

![Delegation](./img/4.5.png)

Điều này sẽ mở một cửa sổ mới, nơi bạn sẽ được yêu cầu chọn người dùng mà bạn muốn ủy quyền kiểm soát:

**Lưu ý:** Để tránh nhập sai tên người dùng, hãy nhập **"phillip"** và nhấp vào nút **Check Names**. Windows sẽ tự động hoàn thành tên người dùng cho bạn.

![Delegation](./img/4.6.png)

Nhấp vào **OK**, và trong bước tiếp theo, chọn tùy chọn sau:

![Delegation](./img/4.7.png)

Nhấp vào **Next** vài lần, và bây giờ Phillip sẽ có thể đặt lại mật khẩu cho bất kỳ người dùng nào trong bộ phận bán hàng. Mặc dù bạn có thể muốn lặp lại các bước này để ủy quyền đặt lại mật khẩu cho các bộ phận Marketing và Quản lý, nhưng chúng ta sẽ dừng lại ở đây cho nhiệm vụ này. Bạn có thể tiếp tục cấu hình phần còn lại của các **OU** nếu muốn.

Bây giờ hãy sử dụng tài khoản của Phillip để thử đặt lại mật khẩu của Sophie. Dưới đây là thông tin đăng nhập của Phillip để bạn đăng nhập qua **RDP**:

![Delegation](./img/4.8.png)

**Lưu ý:** Khi kết nối qua **RDP**, sử dụng `THM\phillip` làm tên người dùng để đăng nhập bằng tài khoản **phillip** trên miền **THM**.

Mặc dù bạn có thể muốn mở **Active Directory Users and Computers** để kiểm tra các quyền mới của Phillip, nhưng thực tế anh ta không có đủ quyền để mở nó. Vì vậy, bạn sẽ cần sử dụng phương pháp khác để đặt lại mật khẩu. Trong trường hợp này, chúng ta sẽ sử dụng **Powershell** để thực hiện:

![Delegation](./img/4.9.png)

Vì chúng ta không muốn Sophie tiếp tục sử dụng một mật khẩu mà chúng ta biết, nên chúng ta cũng có thể ép buộc đặt lại mật khẩu vào lần đăng nhập tiếp theo bằng lệnh sau:

![Delegation](./img/4.10.png)

**Lưu ý:** Khi kết nối qua **RDP**, sử dụng **THM\sophie** làm tên người dùng để xác định bạn muốn đăng nhập bằng người dùng **sophie** trên miền **THM**.

