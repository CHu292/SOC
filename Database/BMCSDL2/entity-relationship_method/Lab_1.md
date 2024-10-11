# 1. Chọn chủ đề: Hệ thống thông tin bán sản phẩm cà phê

# 2. Sử dụng phương pháp “thực thể-mối quan hệ”, xây dựng mô hình cơ sở dữ liệu cho hệ thống thông tin đã chọn.

## 2.1 Phân tích hệ thống của hệ thống thông tin.
### 2.1.1 Quá trình xử lý và nhiệm vụ cơ sở dữ liệu

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
  
### 2.1.2 Nguồn dữ liệu, định dạng và tần suất cập nhật 

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
  
### 2.1.3 Lớp người dùng

- Quản lý bán hàng: Truy cập dữ liệu khách hàng, đơn hàng, và trạng thái thanh toán.
- Nhân viên kho: Quản lý tình trạng hàng tồn kho và vị trí lưu trữ sản phẩm.

### 2.1.4 Hạn chế

- Mỗi đơn hàng chỉ có thể thuộc về một khách hàng, và một khách hàng có thể có nhiều đơn hàng.
- Một sản phẩm có thể liên quan đến nhiều nhà cung cấp, nhưng phải có ít nhất một nhà cung cấp.
- Mỗi kho phải có một nhân viên quản lý duy nhất.

## 2.2 Xác định thực thể và xây dựng ERD

### 2.2.1 Xác dựng các thực thể 

- Employee: Nhân viên
- Supplier: Nhà cung cấp
- Product: Sản phẩm
- Customer: Khách hàng
- Order: Đơn hàng
- Bill: Hóa đơn
- Warehouse: Kho hàng

### 2.2.2 Mô tả thực thể

- Employee: Gồm ID, tên, chức vụ, số điện thoại và email.
- Supplier: Gồm ID, tên nhà cung cấp, địa chỉ, số điện thoại và email.
- Product: Gồm ID, tên loại sản phẩm, giá cả.
- Customer: Gồm ID, tên khách hàng, số điện thoại, email.
- Order: Gồm ID, ngày đặt hàng, tổng số tiền.
- Bill: Gồm ID, số tiền, phương thức thanh toán.
- Warehouse: Gồm ID, địa chỉ, trạng thái kho

### 2.2.3 Các liên kết

#### Nhân viên (Employee) và Đơn hàng (Order):

- Tên liên kết: "Xử lý" (Processes)
- Mô tả: Mỗi nhân viên có thể xử lý nhiều đơn hàng, nhưng mỗi đơn hàng chỉ được xử lý bởi một nhân viên duy nhất.
- Cardinality: 1 : N (Một nhân viên có thể xử lý nhiều đơn hàng, mỗi đơn hàng chỉ có một nhân viên).
- Nhân viên: Tham gia một phần (Partial Participation). Không phải tất cả nhân viên đều xử lý đơn hàng.
- Đơn hàng: Tham gia toàn phần (Total Participation). Mỗi đơn hàng đều phải được xử lý bởi một nhân viên.

#### Nhà cung cấp (Supplier) và Sản phẩm (Product):

- Tên liên kết: "Cung cấp" (Delivers)
- Mô tả: Một nhà cung cấp có thể cung cấp nhiều sản phẩm, và một sản phẩm có thể được cung cấp bởi nhiều nhà cung cấp.
- Cardinality: M : N (Nhiều nhà cung cấp có thể cung cấp nhiều sản phẩm, và nhiều sản phẩm có thể được cung cấp bởi nhiều nhà cung cấp).
- Nhà cung cấp: Tham gia một phần. Không phải nhà cung cấp nào cũng cung cấp tất cả các sản phẩm.
- Sản phẩm: Tham gia toàn phần. Mỗi sản phẩm cần có ít nhất một nhà cung cấp.

#### Sản phẩm (Product) và Đơn hàng (Order):

- Tên liên kết: "Bao gồm" (Includes)
- Mô tả: Một đơn hàng có thể bao gồm nhiều sản phẩm, và một sản phẩm có thể có trong nhiều đơn hàng.
- Cardinality: M : N (Một đơn hàng có thể chứa nhiều sản phẩm, và một sản phẩm có thể nằm trong nhiều đơn hàng).
- Sản phẩm: Tham gia toàn phần. Mỗi sản phẩm phải thuộc ít nhất một đơn hàng nếu nó đã được bán.
- Đơn hàng: Tham gia toàn phần. Mỗi đơn hàng phải chứa ít nhất một sản phẩm

#### Khách hàng (Customer) và Đơn hàng (Order):

- Tên liên kết: "Đặt hàng" (Places)
- Mô tả: Một khách hàng có thể đặt nhiều đơn hàng, nhưng mỗi đơn hàng chỉ thuộc về một khách hàng.
- Cardinality: 1 : N (Một khách hàng có thể có nhiều đơn hàng, nhưng mỗi đơn hàng chỉ thuộc về một khách hàng).
- Khách hàng: Tham gia một phần. Không phải khách hàng nào cũng đặt đơn hàng.
- Đơn hàng: Tham gia toàn phần. Mỗi đơn hàng phải thuộc về một khách hàng.

#### Đơn hàng (Order) và Hóa đơn (Bill):

- Tên liên kết: "Có" (Has)
- Mô tả: Mỗi đơn hàng chỉ có một hóa đơn, và mỗi hóa đơn chỉ liên quan đến một đơn hàng.
- Cardinality: 1 : 1 (Mỗi đơn hàng tương ứng với một hóa đơn và ngược lại).
- Đơn hàng: Tham gia toàn phần. Mỗi đơn hàng đều phải có một hoá đơn.
- Hoá đơn: Tham gia toàn phần. Mỗi hoá đơn phải gắn liền với một đơn hàng.

#### Kho hàng (Warehouse) và Sản phẩm (Product):

- Tên liên kết: "Lưu trữ" (Stores)
- Mô tả: Một kho có thể chứa nhiều sản phẩm, nhưng mỗi sản phẩm chỉ được lưu trữ tại một kho.
- Cardinality: 1 : N (Một kho có thể lưu trữ nhiều sản phẩm, mỗi sản phẩm chỉ lưu trữ tại một kho).
- Kho hàng: Tham gia một phần. Không phải tất cả các kho đều chứa sản phẩm.
- Sản phẩm: Tham gia toàn phần. Mỗi sản phẩm phải được lưu trữ tại một kho.

#### Nhân viên (Employee) và Kho hàng (Warehouse):

- Tên liên kết: "Quản lý" (Manages)
- Mô tả: Một nhân viên có thể quản lý nhiều kho, nhưng mỗi kho chỉ có một nhân viên quản lý.
- Cardinality: 1 : N (Một nhân viên có thể quản lý nhiều kho, nhưng mỗi kho chỉ có một nhân viên quản lý).
- Nhân viên: Tham gia một phần. Không phải tất cả nhân viên đều quản lý kho.
- Kho hàng: Tham gia toàn phần. Mỗi kho phải được quản lý bởi một nhân viên.
  
# Ký hiệu Crow's foot

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Database/BMCSDL2/entity-relationship_method/image/ky_crow_foot.png" alt="Ký hiệu chân chim - Crow's foot" width="700">
</p>

### 2.2.4 Sơ đồ ER

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Database/BMCSDL2/entity-relationship_method/image/Mo_hinh_ER.png" alt="Sơ đồ ER" width="700">
</p>

# 3 Chuyển đổi ER-diagram sang mô hình quan hệ

- Mỗi thực thể trong ER-diagram sẽ được chuyển thành một bảng. Các thuộc tính của thực thể sẽ trở thành các cột của bảng, và khoá chính của thực thể sẽ trở thành khoá chính của bảng.
  
