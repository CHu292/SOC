# Windows Fundamentals 1

> Trong phần 1 của mô-đun Cơ bản về Windows, chúng ta sẽ bắt đầu hành trình tìm hiểu về màn hình nền Windows, hệ thống tệp NTFS, UAC, Bảng điều khiển và nhiều nội dung khác.

## Mục Lục

1. [Task 1: Introduction to Windows](#task-1-introduction-to-windows)

2. [Task 2: Windows Editions](#task-2-windows-editions)

3. [Task 3: The Desktop (GUI)](#task-3-the-desktop-gui)

4. [Task 4: The File System](#task-4-the-file-system)

5. [Task 5: The Windows\System32 Folders](#task-5-the-windows-system32-folders)

6. [Task 6: User Accounts, Profiles, and Permissions](#task-6-user-accounts-profiles-and-permissions)

7. [Task 7: User Account Control](#task-7-user-account-control)

8. [Task 8: Settings and the Control Panel](#task-8-settings-and-the-control-panel)

9. [Task 9: Task Manager](#task-9-task-manager)

10. [Task 10: Conclusion](#task-10-conclusion)

## Nội dung

# Task 1: Introduction to Windows

Hệ điều hành (OS) Windows là một sản phẩm phức tạp với nhiều tệp hệ thống, tiện ích, cài đặt, tính năng, v.v.

Mô-đun này sẽ cố gắng cung cấp tổng quan chung về một số ít thành phần tạo nên HĐH Windows, điều hướng giao diện người dùng, thực hiện thay đổi cho hệ thống, v.v. Nội dung này hướng đến những người muốn hiểu và sử dụng HĐH Windows ở mức độ thoải mái hơn.

Máy ảo sẽ mở trong trình duyệt web của bạn.

Nếu bạn muốn truy cập máy ảo qua Remote Desktop, hãy sử dụng thông tin đăng nhập bên dưới.

Machine IP: MACHINE_IP

User: administrator

Password: letmein123!

![remote desktop](./img/1_Windows_Fundamentals_1/1.1.png)

Chấp nhận Chứng chỉ khi được nhắc và bạn sẽ được đăng nhập vào hệ thống từ xa ngay bây giờ.

Lưu ý: Máy ảo có thể mất tới 3 phút để tải.

# Task 2: Windows Editions

Hệ điều hành Windows có một lịch sử lâu dài, bắt đầu từ năm 1985, và hiện nay, nó là hệ điều hành chiếm ưu thế trong cả việc sử dụng tại gia và trong các mạng lưới công ty. Vì lý do này, Windows luôn là mục tiêu của các hacker và những kẻ viết phần mềm độc hại.

Windows XP là một phiên bản Windows phổ biến và hoạt động lâu dài. Microsoft đã công bố Windows Vista, đây là một cuộc đại tu hoàn toàn của hệ điều hành Windows. Tuy nhiên, Vista gặp phải nhiều vấn đề. Người dùng Windows không đón nhận Vista tốt, và nó nhanh chóng bị loại bỏ.

Khi Microsoft thông báo ngày kết thúc vòng đời của Windows XP, nhiều khách hàng hoảng sợ. Các tập đoàn, bệnh viện, v.v., phải gấp rút thử nghiệm và chuyển sang phiên bản Windows khả dụng tiếp theo, đó là Windows 7, cùng với nhiều phần cứng và thiết bị khác. Các nhà cung cấp phải làm việc hết tốc lực để đảm bảo sản phẩm của họ hoạt động với Windows 7 cho khách hàng của mình. Nếu họ không làm được, khách hàng buộc phải phá vỡ thỏa thuận và tìm nhà cung cấp khác nâng cấp sản phẩm để hoạt động với Windows 7. Điều này là một cơn ác mộng đối với nhiều người, và Microsoft đã lưu ý đến điều này.

Windows 7, được phát hành nhanh chóng ngay sau đó, đã được đánh dấu với một ngày kết thúc hỗ trợ. Windows 8.x xuất hiện và biến mất nhanh chóng, giống như Vista.

Sau đó, [Windows 10](https://www.microsoft.com/en-us/windows/tips?activetab=NewPopular?activetab=NewPopular) ra đời, là phiên bản hệ điều hành Windows hiện tại cho máy tính để bàn.

Windows 10 có hai phiên bản: Home và Pro. Bạn có thể đọc sự khác biệt giữa chúng [tại đây](https://www.microsoft.com/en-us/windows/?r=1).

Mặc dù chúng ta không nói về các máy chủ, phiên bản hệ điều hành Windows hiện tại cho máy chủ là **[Windows Server 2019](https://www.microsoft.com/en-us/windows-server)**.

Nhiều nhà phê bình chỉ trích Microsoft, nhưng họ đã có những bước tiến dài trong việc cải thiện tính khả dụng và bảo mật với mỗi phiên bản mới của Windows.

**Lưu ý:** Phiên bản Windows của máy ảo (VM) đính kèm là Windows Server 2019 Standard, như được thấy trong **System Information**.

**Cập nhật:** Từ tháng 6 năm 2021, Microsoft đã công bố ngày ngừng hỗ trợ cho Windows 10 [tại đây](https://learn.microsoft.com/en-us/lifecycle/products/windows-10-home-and-pro?ranMID=24542&ranEAID=kXQk6*ivFEQ&ranSiteID=kXQk6.ivFEQ-4cKUPfbv9lM_IR2EX7K_hw&epi=kXQk6.ivFEQ-4cKUPfbv9lM_IR2EX7K_hw&irgwc=1&OCID=AID2000142_aff_7593_1243925&tduid=(ir__feexvhocigkfqna9kk0sohznb32xutanagupypus00)(7593)(1243925)(kXQk6.ivFEQ-4cKUPfbv9lM_IR2EX7K_hw)()&irclickid=_feexvhocigkfqna9kk0sohznb32xutanagupypus00).

“Microsoft sẽ tiếp tục hỗ trợ ít nhất một phiên bản Windows 10 Semi-Annual Channel đến ngày 14 tháng 10 năm 2025.”

Kể từ ngày 5 tháng 10 năm 2021 - Windows 11 hiện là hệ điều hành Windows dành cho người dùng cuối. Đọc thêm về Windows 11 [tại đây](https://www.microsoft.com/en-us/windows?wa=wsignin1.0&r=1).

**Câu hỏi: Bạn có thể bật loại mã hóa nào trên Pro mà không thể bật trên Home?**

<details>  
<summary>Hiển thị đáp án</summary>  
Đáp án: BitLocker
</details>  

Sự khác biệt chính về khả năng mã hóa giữa Windows **Pro** và **Home** nằm ở tính năng hỗ trợ **BitLocker**:

**Windows Pro:**

- **BitLocker Drive Encryption:** Có sẵn và có thể kích hoạt. BitLocker cung cấp mã hóa toàn bộ ổ đĩa, bảo vệ dữ liệu của bạn ngay cả khi ổ đĩa bị tháo ra khỏi thiết bị. Ngoài ra, BitLocker còn hỗ trợ các tính năng như **BitLocker To Go** (mã hóa USB) và quản lý qua **Group Policy**.

**Windows Home:**

- **BitLocker Drive Encryption:** Không được hỗ trợ một cách chính thức. Tuy nhiên, Windows Home có thể hỗ trợ một dạng mã hóa đơn giản hơn gọi là **Device Encryption** (Mã hóa thiết bị), nếu phần cứng của bạn hỗ trợ. Tính năng này ít tùy chọn và không mạnh mẽ bằng BitLocker.
- Để sử dụng tính năng mã hóa đầy đủ như BitLocker, bạn cần nâng cấp lên phiên bản Windows Pro hoặc sử dụng các công cụ mã hóa của bên thứ ba.

Nếu bạn cần một giải pháp mã hóa mạnh mẽ với khả năng quản lý nâng cao (ví dụ: quản lý qua Group Policy, tích hợp với Active Directory, hoặc mã hóa đồng loạt nhiều ổ đĩa), thì **Windows Pro** là lựa chọn phù hợp hơn.

