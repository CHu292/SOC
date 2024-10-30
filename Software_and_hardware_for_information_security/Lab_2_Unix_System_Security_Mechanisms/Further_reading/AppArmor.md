# AppArmor

## Giới thiệu
AppArmor là một hệ thống bảo mật Kiểm Soát Truy Cập Bắt Buộc (MAC). Mục tiêu của AppArmor là cung cấp một hệ thống bảo mật dễ sử dụng, tập trung vào việc bảo vệ các ứng dụng riêng lẻ bằng cách xác định và giới hạn những tài nguyên mà một ứng dụng có thể truy cập và chia sẻ. Khác với các công nghệ container khác (chroot, lxc containers), AppArmor tập trung vào việc chia sẻ và kiểm soát tại chỗ để thực thi bảo mật, thay vì sao chép toàn bộ hệ thống nhằm đạt được sự cách ly hoàn toàn. Ngoài việc kiểm soát các tài nguyên hệ thống tiêu chuẩn (tệp, mạng, các quyền hạn,...), AppArmor còn mở rộng đến các dịch vụ và daemon của hệ thống (như dbus, gsettings, X,...) cho phép tích hợp thực thi chính sách vượt qua giới hạn mà sự cách ly mang lại. 

Cụ thể, AppArmor là một biến thể của Domain Type Enforcement (DTE), vốn là một biến thể của Type Enforcement (TE). AppArmor 4 mở rộng AppArmor thành một dạng lai giữa DTE và hệ thống quyền hạn. Dù AppArmor có khả năng cung cấp chính sách toàn hệ thống, chính sách của nó được thiết kế và tập trung xung quanh mô hình ứng dụng (domain), cho phép dễ dàng nhắm mục tiêu đến các ứng dụng hoặc người dùng cụ thể. Do không yêu cầu chính sách toàn hệ thống, AppArmor dễ dàng triển khai chọn lọc chỉ trong vài giờ.

Đơn vị cơ bản của sự hạn chế trong AppArmor là hồ sơ (profile), là một tệp văn bản mô tả quyền và truy cập mà một ứng dụng hoặc dịch vụ có được, dưới dạng danh sách trắng. Tệp văn bản hồ sơ này được biên dịch bởi trình biên dịch chính sách (apparmor_parser) và được tải vào nhân, nơi mô-đun bảo mật AppArmor (một mô-đun Bảo Mật Linux) thực thi tất cả các quyền hạn dựa trên nhân. Mô-đun nhân AppArmor cung cấp giao diện và API để các Trusted Helpers (dịch vụ hệ thống hỗ trợ thực thi chính sách của AppArmor) có thể thực thi phần chính sách mà họ chịu trách nhiệm.

AppArmor cho phép các hồ sơ có chế độ khác nhau được kết hợp, cho phép một số hồ sơ thực thi chính sách trong khi một số khác đang được phát triển ở chế độ phàn nàn (complain mode). AppArmor sử dụng các tệp bao gồm (include files) để dễ dàng phát triển và có rào cản gia nhập thấp hơn nhiều so với các hệ thống MAC phổ biến khác. 

Các đặc điểm của AppArmor bao gồm:

- Hồ sơ là các tệp văn bản đơn giản.
- Hỗ trợ ghi chú trong hồ sơ.
- Các đường dẫn tuyệt đối và khả năng sử dụng ký tự đại diện cho phép khi chỉ định truy cập tệp.
- Có các kiểm soát truy cập khác nhau cho tệp.
- Kiểm soát truy cập cho mạng.
- Cụ thể trong việc khớp quy tắc, ví dụ, quy tắc cụ thể nhất sẽ được áp dụng.
- Hỗ trợ tệp bao gồm để đơn giản hóa và phát triển hồ sơ.
- Biến có thể được định nghĩa và điều chỉnh ngoài hồ sơ.
- Hồ sơ AppArmor dễ đọc và kiểm tra.
- Chính sách AppArmor có thể được đọc và kiểm tra trên cơ sở từng hồ sơ ứng dụng.

AppArmor là một công nghệ đã được thiết lập, lần đầu tiên xuất hiện trong Immunix và sau đó được tích hợp vào Ubuntu, Novell/SUSE, và Mandriva. Chức năng cốt lõi của AppArmor đã có trong nhân Linux chính từ phiên bản 2.6.36 trở đi; công việc vẫn đang được AppArmor, Ubuntu và các nhà phát triển khác tiếp tục để hợp nhất thêm các tính năng của AppArmor vào nhân chính. Tập hợp chính xác các tính năng và quyền có sẵn sẽ thay đổi theo phiên bản AppArmor được cài đặt, phiên bản của nhân Linux, và những dịch vụ hệ thống mà bản phân phối Linux đã kích hoạt (ví dụ: Để thực thi trung gian dbus của AppArmor, tùy chọn này phải được kích hoạt trong daemon dbus của bản phân phối).
