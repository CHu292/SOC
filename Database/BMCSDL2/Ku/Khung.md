# 1. Mô hình hóa thông tin cơ sở dữ liệu bằng phương pháp “mối quan hệ thực thể”
## 1.1 Lựa chọn chủ đề

Chủ đề: Hệ thống thông tin bán sản phẩm cà phê
Lý do chọn chủ đề: Nơi tôi sống ở Việt Nam họ trồng rất nhiều cà phê. Vì vậy tôi chọn đề tài:
“Hệ thống thông tin bán sản phẩm cà phê”

## 1.2 Sử dụng phương pháp “thực thể-mối quan hệ”, xây dựng mô hình cơ sở dữ liệu cho hệ thống thông tin đã chọn.

### 1.2.1 Phân tích hệ thống của hệ thống thông tin. 

#### 1.2.1.1 Quá trình xử lý và nhiệm vụ cơ sở dữ liệu

**Cơ sở dữ liệu sẽ hỗ trợ các quy trình chính sau:**

- Quản lý sản phẩm: Theo dõi thông tin về các loại cà phê, giá cả, kho hàng và nhà cung cấp.
- Quản lý đơn hàng: Đăng ký và xử lý đơn đặt hàng của khách hàng, bao gồm chi tiết sản phẩm, tổng giá trị và trạng thái đơn hàng.
- Quản lý khách hàng: Lưu trữ thông tin khách hàng và lịch sử mua hàng.
- Quản lý nhà cung cấp: Theo dõi các nhà cung cấp và các sản phẩm họ cung cấp.
- Quản lý kho: Quản lý vị trí kho và tình trạng lưu trữ hàng hóa.. 

**Nhiệm vụ cần giải quyết:**

- Quản lý hiệu quả hàng tồn kho.
- Tự động hóa xử lý đơn hàng và theo dõi.
- Đơn giản hóa quản lý quan hệ khách hàng và nhà cung cấp.
- Tối ưu hóa công việc nhân viên qua việc phân chia nhiệm vụ.

#### 1.2.1.2 Nguồn dữ liệu, định dạng và tần suất cập nhật 

**Nguồn dữ liệu:**

- Đơn hàng: Lấy từ hệ thống bán hàng hoặc cửa hàng trực tuyến.
- Thông tin sản phẩm: Cập nhật bởi nhà cung cấp.
- Thông tin khách hàng: Nhập liệu bởi nhân viên hoặc qua biểu mẫu đăng ký.
- Thông tin kho: Từ hệ thống quản lý kho.

**Định dạng dữ liệu:**

- Đơn hàng: Dữ liệu đơn hàng được lưu trữ trong các bản ghi có cấu trúc bao gồm sản phẩm, số lượng, giá cả và thông tin khách hàng. 
- Sản phẩm và nhà cung cấp: thông tin được trình bày dưới dạng bảng với các thuộc tính chính (tên, giá, số lượng, chi tiết liên hệ của nhà cung cấp). 

**Tần suất cập nhật:**

- Đơn hàng: Cập nhật theo thời gian thực.
- Sản phẩm và kho: Cập nhật hàng ngày hoặc khi có thay đổi.
- Khách hàng: Cập nhật khi có khách hàng mới hoặc thay đổi thông tin.

#### 1.2.1.3 Lớp người dùng

- Quản lý bán hàng: Truy cập dữ liệu khách hàng, đơn hàng, và trạng thái thanh toán.
- Nhân viên kho: Quản lý tình trạng hàng tồn kho và vị trí lưu trữ sản phẩm.

#### 1.2.1.4 Hạn chế

- Mỗi đơn hàng chỉ có thể thuộc về một khách hàng, và một khách hàng có thể có nhiều đơn hàng.
- Một sản phẩm có thể liên quan đến nhiều nhà cung cấp, nhưng phải có ít nhất một nhà cung cấp.
- Mỗi kho phải có một nhân viên quản lý duy nhất.

