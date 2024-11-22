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

### 1.2.2 Xác định thực thể và xây dựng ERD

#### 1.2.2.1 Xác dựng các thực thể 

- Employee: Nhân viên
- Supplier: Nhà cung cấp
- Product: Sản phẩm
- Customer: Khách hàng
- Order: Đơn hàng
- Bill: Hóa đơn
- Warehouse: Kho hàng

#### 1.2.2.2 Mô tả thực thể

- Employee: Gồm ID, tên, chức vụ, số điện thoại và email.
- Supplier: Gồm ID, tên nhà cung cấp, địa chỉ, số điện thoại và email.
- Product: Gồm ID, tên loại sản phẩm, giá cả.
- Customer: Gồm ID, tên khách hàng, số điện thoại, email.
- Order: Gồm ID, ngày đặt hàng, tổng số tiền.
- Bill: Gồm ID, số tiền, phương thức thanh toán.
- Warehouse: Gồm ID, địa chỉ, trạng thái kho

#### 1.2.2.3 Các liên kết

1.  Nhân viên (Employee) và Đơn hàng (Order):

- Tên liên kết: "Xử lý" (Processes)
- Mô tả: Mỗi nhân viên có thể xử lý nhiều đơn hàng, nhưng mỗi đơn hàng chỉ được xử lý bởi một nhân viên duy nhất.
- Cardinality: 1 : N (Một nhân viên có thể xử lý nhiều đơn hàng, mỗi đơn hàng chỉ có một nhân viên).
- Nhân viên: Tham gia một phần (Partial Participation). Không phải tất cả nhân viên đều xử lý đơn hàng.
- Đơn hàng: Tham gia toàn phần (Total Participation). Mỗi đơn hàng đều phải được xử lý bởi một nhân viên.

2. Nhà cung cấp (Supplier) và Sản phẩm (Product):

- Tên liên kết: "Cung cấp" (Delivers)
- Mô tả: Một nhà cung cấp có thể cung cấp nhiều sản phẩm, và một sản phẩm có thể được cung cấp bởi nhiều nhà cung cấp.
- Cardinality: M : N (Nhiều nhà cung cấp có thể cung cấp nhiều sản phẩm, và nhiều sản phẩm có thể được cung cấp bởi nhiều nhà cung cấp).
- Nhà cung cấp: Tham gia một phần. Không phải nhà cung cấp nào cũng cung cấp tất cả các sản phẩm.
- Sản phẩm: Tham gia toàn phần. Mỗi sản phẩm cần có ít nhất một nhà cung cấp.

3. Sản phẩm (Product) và Đơn hàng (Order):

- Tên liên kết: "Bao gồm" (Includes)
- Mô tả: Một đơn hàng có thể bao gồm nhiều sản phẩm, và một sản phẩm có thể có trong nhiều đơn hàng.
- Cardinality: M : N (Một đơn hàng có thể chứa nhiều sản phẩm, và một sản phẩm có thể nằm trong nhiều đơn hàng).
- Sản phẩm: Tham gia toàn phần. Mỗi sản phẩm phải thuộc ít nhất một đơn hàng nếu nó đã được bán.
- Đơn hàng: Tham gia toàn phần. Mỗi đơn hàng phải chứa ít nhất một sản phẩm

4. Khách hàng (Customer) và Đơn hàng (Order):

- Tên liên kết: "Đặt hàng" (Places)
- Mô tả: Một khách hàng có thể đặt nhiều đơn hàng, nhưng mỗi đơn hàng chỉ thuộc về một khách hàng.
- Cardinality: 1 : N (Một khách hàng có thể có nhiều đơn hàng, nhưng mỗi đơn hàng chỉ thuộc về một khách hàng).
- Khách hàng: Tham gia một phần. Không phải khách hàng nào cũng đặt đơn hàng.
- Đơn hàng: Tham gia toàn phần. Mỗi đơn hàng phải thuộc về một khách hàng.

5. Đơn hàng (Order) và Hóa đơn (Bill):

- Tên liên kết: "Có" (Has)
- Mô tả: Mỗi đơn hàng chỉ có thể có nhiều hóa đơn, và mỗi hóa đơn chỉ liên quan đến một đơn hàng.
- Cardinality: 1 : N (Mỗi đơn hàng tương ứng với một hóa đơn và ngược lại).
- Đơn hàng: Tham gia toàn phần. Mỗi đơn hàng đều phải có một hoá đơn.
- Hoá đơn: Tham gia toàn phần. Mỗi hoá đơn phải gắn liền với một đơn hàng.

6. Kho hàng (Warehouse) và Sản phẩm (Product):

- Tên liên kết: "Lưu trữ" (Stores)
- Mô tả: Một kho có thể chứa nhiều sản phẩm, nhưng mỗi sản phẩm chỉ được lưu trữ tại một kho.
- Cardinality: 1 : N (Một kho có thể lưu trữ nhiều sản phẩm, mỗi sản phẩm chỉ lưu trữ tại một kho).
- Kho hàng: Tham gia một phần. Không phải tất cả các kho đều chứa sản phẩm.
- Sản phẩm: Tham gia toàn phần. Mỗi sản phẩm phải được lưu trữ tại một kho.

7. Nhân viên (Employee) và Kho hàng (Warehouse):

- Tên liên kết: "Quản lý" (Manages)
- Mô tả: Một nhân viên có thể quản lý nhiều kho, nhưng mỗi kho chỉ có một nhân viên quản lý.
- Cardinality: 1 : N (Một nhân viên có thể quản lý nhiều kho, nhưng mỗi kho chỉ có một nhân viên quản lý).
- Nhân viên: Tham gia một phần. Không phải tất cả nhân viên đều quản lý kho.
- Kho hàng: Tham gia toàn phần. Mỗi kho phải được quản lý bởi một nhân viên.

#### 1.2.2.4 Sơ đồ ER

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Database/BMCSDL2/entity-relationship_method/image/So_do_ER.png" alt="Sơ đồ ER" width="700">
</p>
<p align="center"><b>Bảng 1 - Sơ đồ ER</b></p>

## 1.3 Chuyển đổi ER-diagram sang mô hình quan hệ

### 1.3.1 Xác định các thực thể trong sơ đồ ER

Trong sơ đồ ER (Hình 1), các thực thể được xác định bao gồm:

Employee: Nhân viên

- Thuộc tính: Employee_ID, Name, Position, Phone_Number, Email.
- Khóa chính (Primary Key): Employee_ID.

Warehouse: Lưu trữ hàng hóa.

- Thuộc tính: Warehouse_ID, Address, Status.
- Khóa chính: Warehouse_ID.

Supplier: Nhà cung cấp hàng hóa.

- Thuộc tính: Supplier_ID, Name, Address, Phone_Number, Email.
- Khóa chính: Supplier_ID.

Product: Sản phẩm.

- Thuộc tính: Product_ID, Product_Category_Name, Price.
- Khóa chính: Product_ID.

Customer: Khách hàng.

- Thuộc tính: Customer_ID, Name, Phone_Number, Email.
- Khóa chính: Customer_ID.

Orders: Đơn hàng được đặt bởi khách hàng.

- Thuộc tính: Order_ID, Order_Date, Total_Amount.
- Khóa chính: Order_ID.

Bill: Hóa đơn gắn với đơn hàng.

- Thuộc tính: Bill_ID, Amount, Payment.
- Khóa chính: Bill_ID.

### 1.3.2 Chuyển đổi các mối quan hệ trong sơ đồ ER

Mối quan hệ giữa Employee và Warehouse:

- Mối quan hệ 1:N (Employee quản lý nhiều Warehouse).
- Giải pháp: Thêm khóa ngoại Employee_ID vào bảng Warehouse để tham chiếu đến bảng Employee.

Mối quan hệ giữa Warehouse và Product:

- Mối quan hệ 1:N (một Warehouse chứa nhiều Product).
- Giải pháp: Thêm khóa ngoại Warehouse_ID vào bảng Product để tham chiếu đến bảng Warehouse.

Mối quan hệ giữa Supplier và Product

- Mối quan hệ N:M (một Supplier cung cấp nhiều Product, một Product được cung cấp bởi nhiều Supplier).
- Giải pháp: Tạo bảng trung gian Supplier_Product với:
  - Thuộc tính: Supplier_ID, Product_ID.
  - Khóa chính là tổ hợp của Supplier_ID và Product_ID.
  - Cả hai cột này đều là khóa ngoại tham chiếu đến bảng Supplier và Product.

Mối quan hệ giữa Customer và Orders:

- Mối quan hệ 1:N (một Customer có thể đặt nhiều Orders).
- Giải pháp: Thêm khóa ngoại Customer_ID vào bảng Orders để tham chiếu đến bảng Customer.

Mối quan hệ giữa Orders và Product:

- Mối quan hệ N:M (một Order có thể bao gồm nhiều Product, một Product có thể thuộc nhiều Order).
- Giải pháp: Tạo bảng trung gian Order_Product với:
  - Thuộc tính: Order_ID, Product_ID.
  - Khóa chính là tổ hợp của Order_ID và Product_ID.
  - Cả hai cột này đều là khóa ngoại tham chiếu đến bảng Orders và Product.
 

Mối quan hệ giữa Orders và Bill:

- Mối quan hệ 1:1 (mỗi Order có một Bill tương ứng).
- Giải pháp: Thêm khóa ngoại Order_ID vào bảng Bill để tham chiếu đến bảng Orders.

- Mỗi thực thể trong ER-diagram sẽ được chuyển thành một bảng. Các thuộc tính của thực thể sẽ trở thành các cột của bảng, và khoá chính của thực thể sẽ trở thành khoá chính của bảng.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Database/BMCSDL2/entity-relationship_method/image/mo_hinh_quan_he.png" alt="Mô hình quan hệ" width="700">
</p>
<p align="center"><b>Bảng 2 - Mô hình quan hệ</b></p>


## 1.4 Chuyển đổi quan hệ cơ sở dữ liệu sang 3NF.

**Để kiểm tra xem mô hình quan hệ đã đạt chuẩn 3NF (Third Normal Form) hay chưa, chúng ta cần xem xét các điều kiện của chuẩn 3NF:**

**- Đạt chuẩn 1NF:** Mỗi bảng trong mô hình phải có cấu trúc dạng bảng, với mỗi giá trị trong các cột phải là đơn trị (không có cột chứa các giá trị lặp hoặc nhóm giá trị lồng nhau). Đồng thời, bảng phải có khóa chính (Primary Key - PK) để đảm bảo mỗi dòng là duy nhất.

**- Đạt chuẩn 2NF:** Bảng phải đạt chuẩn 1NF và tất cả các thuộc tính không khóa phải phụ thuộc hoàn toàn vào khóa chính. Nói cách khác, không có thuộc tính không khóa nào phụ thuộc vào một phần của khóa chính (tránh phụ thuộc một phần).

**- Đạt chuẩn 3NF:** Bảng phải đạt chuẩn 2NF và không có phụ thuộc bắc cầu giữa các thuộc tính không khóa. Nghĩa là, tất cả các thuộc tính không khóa phải phụ thuộc trực tiếp vào khóa chính, không phụ thuộc vào các thuộc tính không khóa khác.

 Phân tích mô hình quan hệ để kiểm tra 3NF

Chúng ta sẽ xem xét từng bảng trong mô hình đã thiết kế để đảm bảo không vi phạm các điều kiện của chuẩn 3NF.

1. Bảng Employee

- Thuộc tính: Employee_ID (PK), Name, Position, Phone_Number, Email
- Phụ thuộc hàm: Tất cả các thuộc tính (Name, Position, Phone_Number, Email) đều phụ thuộc trực tiếp vào Employee_ID, và không có phụ thuộc bắc cầu.
- Kết luận: Đạt chuẩn 3NF.

2. Bảng Supplier

- Thuộc tính: Supplier_ID (PK), Name, Address, Phone_Number, Email
- Phụ thuộc hàm: Tất cả các thuộc tính (Name, Address, Phone_Number, Email) phụ thuộc trực tiếp vào Supplier_ID, không có phụ thuộc bắc cầu.
- Kết luận: Đạt chuẩn 3NF.

3. Bảng Product

- Thuộc tính: Product_ID (PK), Product_Category_Name, Price, Warehouse_ID (FK)
- Phụ thuộc hàm:
  -  Tất cả các thuộc tính (Product_Category_Name, Price, Warehouse_ID) đều phụ thuộc trực tiếp vào Product_ID.
  -  Không có thuộc tính nào phụ thuộc vào thuộc tính khác ngoài khóa chính.
-  Kết luận: Đạt chuẩn 3NF.

4. Bảng Customer

- Thuộc tính: Customer_ID (PK), Name, Phone_Number, Email
- Phụ thuộc hàm: Tất cả các thuộc tính phụ thuộc trực tiếp vào Customer_ID, không có phụ thuộc bắc cầu.
- Kết luận: Đạt chuẩn 3NF.

5.  Bảng Order

- Thuộc tính: Order_ID (PK), Order_Date, Total_Amount, Customer_ID (FK), Employee_ID (FK)
- Phụ thuộc hàm:
  - Tất cả các thuộc tính (Order_Date, Total_Amount, Customer_ID, Employee_ID) đều phụ thuộc trực tiếp vào Order_ID.
  - Không có thuộc tính nào phụ thuộc vào thuộc tính khác ngoài khóa chính.
- Kết luận: Đạt chuẩn 3NF.

6. Bảng Bill

- Thuộc tính: Bill_ID (PK), Amount, Payment_Method, Order_ID (FK)
- Phụ thuộc hàm:
  - Tất cả các thuộc tính (Amount, Payment_Method, Order_ID) đều phụ thuộc trực tiếp vào Bill_ID.
  - Không có thuộc tính nào phụ thuộc vào thuộc tính khác ngoài khóa chính.
- Kết luận: Đạt chuẩn 3NF.

7. Bảng Warehouse

- Thuộc tính: Warehouse_ID (PK), Address, Status, Employee_ID (FK)
- Phụ thuộc hàm:
  - Tất cả các thuộc tính (Address, Status, Employee_ID) đều phụ thuộc trực tiếp vào Warehouse_ID.
  - Không có phụ thuộc bắc cầu.
- Kết luận: Đạt chuẩn 3NF.

8. Bảng trung gian Order_Product

- Thuộc tính: Order_ID (PK, FK), Product_ID (PK, FK)
- Không có thuộc tính không khóa, bảng này chỉ chứa các khóa ngoại liên kết, nên không cần kiểm tra thêm về 3NF.

9. Bảng trung gian Supplier_Product

- Thuộc tính: Supplier_ID (PK, FK), Product_ID (PK, FK)
- Không có thuộc tính không khóa, bảng này chỉ chứa các khóa ngoại liên kết, nên không cần kiểm tra thêm về 3NF.

**Tổng kết**

Tất cả các bảng trong mô hình quan hệ trên đều đạt chuẩn 3NF. Không có bảng nào vi phạm điều kiện của chuẩn 3NF như phụ thuộc bắc cầu hoặc phụ thuộc một phần vào khóa chính.

## 1.5 Tạo chế độ xem

### 1.5.1 View dành cho Nhân viên bán hàng (Sales Employee View)

**Mục đích:**

Chế độ xem này cung cấp cho nhân viên bán hàng thông tin về các đơn hàng mà họ đã xử lý, bao gồm thông tin chi tiết về khách hàng, ngày đặt hàng, tổng số tiền đơn hàng, và trạng thái của đơn hàng. Nhân viên bán hàng có thể dùng view này để theo dõi tiến độ của các đơn hàng và liên hệ khách hàng nếu cần thiết.

*Dữ liệu hiển thị:**

- Employee_ID, Employee_Name: ID và tên của nhân viên bán hàng.
- Order_ID, Order_Date, Total_Amount: ID của đơn hàng, ngày đặt hàng, và tổng số tiền của đơn hàng.
- Customer_ID, Customer_Name, Customer_Phone, Customer_Email: ID, tên, số điện thoại và email của khách hàng.

### 1.5.2. View dành cho Quản lý kho (Warehouse Manager View)

**Mục đích:**

Chế độ xem này cho phép quản lý kho theo dõi thông tin về các sản phẩm đang được lưu trữ trong kho và tình trạng của kho. View này giúp họ kiểm soát hiệu quả việc quản lý hàng tồn kho và đánh giá tình trạng lưu trữ của sản phẩm.

**Dữ liệu hiển thị:**

- Warehouse_ID, Warehouse_Address, Warehouse_Status: ID, địa chỉ và trạng thái của kho hàng.
- Product_ID, Product_Category_Name, Price: ID sản phẩm, tên danh mục sản phẩm, và giá sản phẩm.

### 1.5.3 View dành cho Khách hàng (Customer View)

**Mục đích:**

View này cho phép khách hàng xem lịch sử mua hàng của họ, bao gồm thông tin về các đơn hàng đã đặt và chi tiết hóa đơn tương ứng. Nó giúp khách hàng theo dõi các giao dịch đã thực hiện và các phương thức thanh toán.

**Dữ liệu hiển thị:**

- Customer_ID, Customer_Name: ID và tên của khách hàng.
- Order_ID, Order_Date, Total_Amount: ID đơn hàng, ngày đặt hàng, và tổng số tiền của đơn hàng.
- Bill_ID, Bill_Amount, Payment_Method: ID hóa đơn, số tiền hóa đơn, và phương thức thanh toán.

### 1.5.4 View dành cho Quản lý nhà cung cấp (Supplier Manager View)

**Mục đích:**

View này cho phép quản lý nhà cung cấp theo dõi thông tin về các nhà cung cấp và sản phẩm mà họ cung cấp. Quản lý nhà cung cấp có thể sử dụng view này để kiểm tra thông tin về các nhà cung cấp và sản phẩm đang được nhập từ các đối tác.

**Dữ liệu hiển thị:**

- Supplier_ID, Supplier_Name, Supplier_Phone: ID, tên và số điện thoại của nhà cung cấp.
- Product_ID, Product_Category_Name, Price: ID sản phẩm, danh mục sản phẩm, và giá sản phẩm mà nhà cung cấp cung cấp.

# 2. Triển khai cơ sở dữ liệu trong DBMS

## 2.1 Chọn hệ quản trị cơ sở dữ liệu (DBMS)

- Sử dụng PostgreSQL
- Lý do sử dụng: PostgreSQL là một hệ quản trị cơ sở dữ liệu quan hệ mạnh mẽ, mã nguồn mở và tuân thủ chuẩn SQL. Nó có khả năng xử lý các cơ sở dữ liệu phức tạp, hỗ trợ đa người dùng và tích hợp tốt với các ngôn ngữ lập trình. PostgreSQL cũng được sử dụng rộng rãi trong các dự án thực tế nhờ khả năng mở rộng và bảo mật tốt.

## 2.2 Tạo cấu trúc cơ sở dữ liệu

Kết nối cơ sở dữ liệu:

```bash
sudo systemctl enable --now postgresql.service
[sudo] password for chu: 
Synchronizing state of postgresql.service with SysV service script with /lib/systemd/systemd-sysv-install.
Executing: /lib/systemd/systemd-sysv-install enable postgresql
```

```bash
sudo su postgres -c psql
psql (16.4 (Ubuntu 16.4-1.pgdg22.04+1))
```

Tạo cơ sở dữ liệu

```SQL
create database coffee_shop_db
with
owner = postgres
encoding = 'UTF8'
tablespace = pg_default
connection limit = -1
is_template = False;
```

```SQL
postgres=# \c coffee_shop_db 
You are now connected to database "coffee_shop_db" as user "postgres".
coffee_shop_db=# 
```

### 2.2.1 Code tạo các bảng 

Bảng nhân viên

```sql
CREATE TABLE Employee (
    Employee_ID SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Position VARCHAR(50) NOT NULL,
    Phone_Number VARCHAR(13),
    Email VARCHAR(100)
);
```

Bảng Supplier
```sql
CREATE TABLE Supplier (
    Supplier_ID SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Address VARCHAR(255),
    Phone_Number VARCHAR(13),
    Email VARCHAR(100)
);
```
Bảng Warehouse
```sql
CREATE TABLE Warehouse (
    Warehouse_ID SERIAL PRIMARY KEY,
    Address VARCHAR(255) NOT NULL,
    Status VARCHAR(50),
    Employee_ID INTEGER
);
```

Bảng Product
```sql
CREATE TABLE Product (
    Product_ID SERIAL PRIMARY KEY,
    Product_Category_Name VARCHAR(100) NOT NULL,
    Price NUMERIC(10, 2) NOT NULL,
    Warehouse_ID INTEGER
);
```
Bảng Customer
```sql
CREATE TABLE Customer (
    Customer_ID SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Phone_Number VARCHAR(15),
    Email VARCHAR(100)
);
```

Bảng Orders
```sql
CREATE TABLE Orders(
    Order_ID SERIAL PRIMARY KEY,
    Order_Date DATE NOT NULL,
    Total_Amount NUMERIC(10, 2) NOT NULL,
    Customer_ID INTEGER,
    Employee_ID INTEGER
);
```
Bảng Bill
```sql
CREATE TABLE Bill (
    Bill_ID SERIAL PRIMARY KEY,
    Amount NUMERIC(10, 2) NOT NULL,
    Payment_Method VARCHAR(50) NOT NULL,
    Order_ID INTEGER
);
```

Bảng liên kết giữa bảng Orders và bảng Product
```sql
CREATE TABLE Order_Product (
    Order_ID INTEGER,
    Product_ID INTEGER,
    PRIMARY KEY (Order_ID, Product_ID)
);
```

- Bảng liên kết giữa bảng Supplier và Product
```sql
CREATE TABLE Supplier_Product (
    Supplier_ID INTEGER,
    Product_ID INTEGER,
    PRIMARY KEY (Supplier_ID, Product_ID)
);
```

Ta có các bảng như sau:

```sql
coffee_shop_db=# \dt
              List of relations
 Schema |       Name       | Type  |  Owner   
--------+------------------+-------+----------
 public | bill             | table | postgres
 public | customer         | table | postgres
 public | employee         | table | postgres
 public | order_product    | table | postgres
 public | orders           | table | postgres
 public | product          | table | postgres
 public | supplier         | table | postgres
 public | supplier_product | table | postgres
 public | warehouse        | table | postgres
(9 rows)
```

### 2.2.2 Code nhập dữ liệu vào bảng

- Bảng employee

```sql
INSERT INTO Employee (Name, Position, Phone_Number, Email) VALUES
('Алексей Иванов', 'Sales Staff', '+84410621704', 'alekseyivanov@mail.ru'),
('Дмитрий Соколов', 'Sales Staff', '+84804504364', 'dmitriysokolov@mail.ru'),
('Екатерина Смирнова', 'Sales Staff', '+84637892756', 'ekaterinasmirnova@mail.ru'),
('Анна Петрова', 'Sales Staff', '+84116278986', 'annapetrova@mail.ru'),
('Иван Васильев', 'Sales Staff', '+84463544856', 'ivanvasilev@mail.ru'),
('Мария Кузнецова', 'Sales Staff', '+84726549107', 'mariyakuznetsova@mail.ru'),
('Ольга Попова', 'Sales Staff', '+84913287564', 'olgapopova@mail.ru'),
('Сергей Федоров', 'Warehouse Manager', '+84892657481', 'sergeyfedorov@mail.ru'),
('Николай Григорьев', 'Warehouse Manager', '+84652718462', 'nikolaygrigoriev@mail.ru'),
('Владимир Николаев', 'Warehouse Manager', '+84187365942', 'vladimirnikolaev@mail.ru');
```

- Bảng supplier

```sql
INSERT INTO Supplier (Name, Address, Phone_Number, Email) VALUES
('ООО РусКофе', 'ул. 80-15, Москва, Россия', '+84867010843', 'oooruskofe@mail.ru'),
('ЗАО ЧайКофе', 'ул. 100-16, Москва, Россия', '+84625548793', 'zaochaykofe@mail.ru'),
('ИП Васильев Торг', 'ул. 25-5, Москва, Россия', '+84534269602', 'ipvasilevtorg@mail.ru'),
('ТД Бариста', 'ул. 18-45, Москва, Россия', '+84919114853', 'tdbarista@mail.ru'),
('КофеТрейд', 'ул. 97-24, Москва, Россия', '+84992880427', 'kofetreyd@mail.ru'),
('СоюзКофе', 'ул. 59-42, Москва, Россия', '+84731450928', 'soyuzkofe@mail.ru'),
('МирКофе', 'ул. 38-35, Москва, Россия', '+84713090284', 'mirkofe@mail.ru'),
('ЭспрессоЭкспорт', 'ул. 47-9, Москва, Россия', '+84890236452', 'espressoeksport@mail.ru'),
('ЗАО Черный Жемчуг', 'ул. 64-17, Москва, Россия', '+84938572461', 'zaochernyjzhemchug@mail.ru'),
('Кофейный Дом', 'ул. 29-31, Москва, Россия', '+84719530678', 'kofejnyjdom@mail.ru');
```

- Bảng warehouse

```sql
INSERT INTO Warehouse (Address, Status, Employee_ID) VALUES
('ул. 97-4, Москва, Россия', 'Inactive', 9),
('ул. 38-11, Москва, Россия', 'Active', 9),
('ул. 97-13, Москва, Россия', 'Inactive', 8),
('ул. 24-37, Москва, Россия', 'Inactive', 10),
('ул. 58-40, Москва, Россия', 'Active', 10);
```

- Bảng product

```sql
INSERT INTO Product (Product_Category_Name, Price, Warehouse_ID) VALUES
('Арабика', 481.21, 1),
('Капучино', 549.51, 1),
('Латте', 778.31, 5),
('Капучино', 114.89, 5),
('Робуста', 465.66, 5),
('Эспрессо', 982.47, 3),
('Робуста', 347.12, 2),
('Капучино', 853.89, 1),
('Арабика', 616.37, 4),
('Латте', 239.44, 3);
```

- Bảng customer

```sql
INSERT INTO Customer (Name, Phone_Number, Email) VALUES
('Иван Иванов', '+84347792080', 'ivanivanov@mail.ru'),
('Петр Петров', '+84725742192', 'petrpetrov@mail.ru'),
('Светлана Смирнова', '+84498734272', 'svetlanasmirnova@mail.ru'),
('Елена Кузнецова', '+84451098251', 'elenakuznetsova@mail.ru'),
('Александр Соколов', '+84479531226', 'aleksandrsokolov@mail.ru'),
('Мария Попова', '+84712349852', 'mariyapopova@mail.ru'),
('Николай Федоров', '+84396571482', 'nikolayfedorov@mail.ru'),
('Анна Васильева', '+84578321940', 'annavasilyeva@mail.ru'),
('Дмитрий Григорьев', '+84410239854', 'dmitriygrigorev@mail.ru'),
('Ольга Николаева', '+84765849320', 'olganikolaeva@mail.ru');
```

- Bảng orders

```sql
INSERT INTO Orders (Order_Date, Total_Amount, Customer_ID, Employee_ID) VALUES
('2024-11-08', 1039.79, 9, 5),
('2024-10-28', 1316.75, 9, 4),
('2024-10-31', 3327.25, 10, 4),
('2024-10-24', 3579.22, 9, 3),
('2024-11-08', 2161.28, 6, 6),
('2024-10-26', 3024.59, 2, 6),
('2024-11-06', 4376.18, 7, 5),
('2024-10-29', 2891.04, 3, 1),
('2024-11-04', 3561.47, 1, 7),
('2024-10-30', 4589.87, 5, 3);
```

- Bảng bill

```sql
INSERT INTO Bill (Bill_ID, Amount, Payment_Method, Order_ID) VALUES
(1, 1039.79, 'Bank Transfer', 1),
(2, 1316.75, 'Bank Transfer', 2),
(3, 3327.25, 'Credit Card', 3),
(4, 3579.22, 'Credit Card', 4),
(5, 2161.28, 'Bank Transfer', 5),
(6, 3024.59, 'Cash', 6),
(7, 4376.18, 'Credit Card', 7),
(8, 2891.04, 'Cash', 8),
(9, 3561.47, 'Credit Card', 9),
(10, 4589.87, 'Bank Transfer', 10);
```

- Bảng liên kết giữa bảng Orders và bảng Product

```sql
INSERT INTO Order_Product (Order_ID, Product_ID) VALUES
(1, 2),
(1, 4),
(2, 5),
(2, 1),
(2, 9),
(3, 7),
(3, 3),
(3, 8),
(4, 10),
(4, 6),
(4, 2),
(5, 4),
(5, 1),
(6, 3),
(6, 8),
(6, 5),
(7, 9),
(7, 2),
(7, 10),
(8, 1),
(8, 7),
(9, 6),
(9, 5),
(10, 4),
(10, 3);
```

- Bảng liên kết giữa bảng Supplier và Product

```sql
INSERT INTO Supplier_Product (Supplier_ID, Product_ID) VALUES
(1, 7),
(1, 1),
(1, 10),
(2, 7),
(2, 9),
(2, 2),
(2, 5),
(3, 8),
(3, 4),
(3, 6),
(4, 3),
(4, 1),
(4, 5),
(4, 10),
(5, 9),
(5, 4),
(5, 2),
(5, 6),
(5, 8);
```

## 2.3 Tạo index

 **Liên kết bảng** (JOIN): Thông thường là các cột `Primary Key` và `Foreign Key`.
 **Tìm kiếm hoặc lọc dữ liệu**: Các cột thường xuyên được sử dụng trong các mệnh đề `WHERE`, `ORDER BY`, hoặc `GROUP BY`.



1. Index bảng `Employee`
- **Mục tiêu**: Tăng tốc tìm kiếm theo `Employee_ID`.

```sql
CREATE INDEX idx_employee_id ON Employee (Employee_ID);
CREATE INDEX idx_employee_email ON Employee (Email);
```


2. Index bảng `Supplier`
- **Mục tiêu**: Tăng tốc truy vấn theo `Supplier_ID` và tìm kiếm qua `Name`.

```sql
CREATE INDEX idx_supplier_id ON Supplier (Supplier_ID);
CREATE INDEX idx_supplier_name ON Supplier (Name);
```


3. Index bảng `Warehouse`
- **Mục tiêu**: Tăng tốc liên kết và lọc dữ liệu theo `Employee_ID` và `Warehouse_ID`.

```sql
CREATE INDEX idx_warehouse_id ON Warehouse (Warehouse_ID);
CREATE INDEX idx_warehouse_employee_id ON Warehouse (Employee_ID);
```


4. Index bảng `Product`
- **Mục tiêu**: Tăng tốc tìm kiếm theo `Product_ID`, `Warehouse_ID`, và lọc dữ liệu theo `Price`.

```sql
CREATE INDEX idx_product_id ON Product (Product_ID);
CREATE INDEX idx_product_warehouse_id ON Product (Warehouse_ID);
CREATE INDEX idx_product_price ON Product (Price);
```


5. Index bảng `Customer`
- **Mục tiêu**: Tăng tốc tìm kiếm theo `Customer_ID` và email khách hàng.

```sql
CREATE INDEX idx_customer_id ON Customer (Customer_ID);
CREATE INDEX idx_customer_email ON Customer (Email);
```


6. Index bảng `Orders`
- **Mục tiêu**: Tăng tốc liên kết và lọc dữ liệu theo `Order_ID`, `Customer_ID`, và `Employee_ID`.

```sql
CREATE INDEX idx_orders_id ON Orders (Order_ID);
CREATE INDEX idx_orders_customer_id ON Orders (Customer_ID);
CREATE INDEX idx_orders_employee_id ON Orders (Employee_ID);
```


7. Index bảng `Bill`
- **Mục tiêu**: Tăng tốc liên kết với bảng `Orders` và tìm kiếm theo `Payment_Method`.

```sql
CREATE INDEX idx_bill_id ON Bill (Bill_ID);
CREATE INDEX idx_bill_order_id ON Bill (Order_ID);
CREATE INDEX idx_bill_payment_method ON Bill (Payment_Method);
```

8. Index bảng `Order_Product`
- **Mục tiêu**: Tăng tốc liên kết giữa `Orders` và `Product`.

```sql
CREATE INDEX idx_order_product_order_id ON Order_Product (Order_ID);
CREATE INDEX idx_order_product_product_id ON Order_Product (Product_ID);
```


9. Index bảng `Supplier_Product`
- **Mục tiêu**: Tăng tốc liên kết giữa `Supplier` và `Product`.

```sql
CREATE INDEX idx_supplier_product_supplier_id ON Supplier_Product (Supplier_ID);
CREATE INDEX idx_supplier_product_product_id ON Supplier_Product (Product_ID);
```

## 2.4 Thiết lập mối quan hệ giữa các bảng

Để thiết lập mối quan hệ giữa các bảng trong cơ sở dữ liệu PostgreSQL, chúng ta sẽ sử dụng các **Foreign Key** (khóa ngoại). Điều này giúp duy trì tính toàn vẹn dữ liệu và thể hiện các mối quan hệ giữa các bảng.


1. Mối quan hệ giữa `Warehouse` và `Employee`
- **Mô tả**: Một nhân viên (`Employee`) quản lý một hoặc nhiều kho (`Warehouse`).
- **Mối quan hệ**: 1:N.

```sql
ALTER TABLE Warehouse
ADD CONSTRAINT fk_warehouse_employee
FOREIGN KEY (Employee_ID)
REFERENCES Employee (Employee_ID)
ON DELETE SET NULL;
```


2. Mối quan hệ giữa `Product` và `Warehouse`
- **Mô tả**: Một sản phẩm (`Product`) được lưu trữ trong một kho (`Warehouse`).
- **Mối quan hệ**: 1:N.

```sql
ALTER TABLE Product
ADD CONSTRAINT fk_product_warehouse
FOREIGN KEY (Warehouse_ID)
REFERENCES Warehouse (Warehouse_ID)
ON DELETE CASCADE;
```


3. Mối quan hệ giữa `Orders` và `Customer`
- **Mô tả**: Một khách hàng (`Customer`) có thể đặt nhiều đơn hàng (`Orders`).
- **Mối quan hệ**: 1:N.

```sql
ALTER TABLE Orders
ADD CONSTRAINT fk_orders_customer
FOREIGN KEY (Customer_ID)
REFERENCES Customer (Customer_ID)
ON DELETE CASCADE;
```


4. Mối quan hệ giữa `Orders` và `Employee`
- **Mô tả**: Một nhân viên (`Employee`) xử lý nhiều đơn hàng (`Orders`).
- **Mối quan hệ**: 1:N.

```sql
ALTER TABLE Orders
ADD CONSTRAINT fk_orders_employee
FOREIGN KEY (Employee_ID)
REFERENCES Employee (Employee_ID)
ON DELETE SET NULL;
```


5. Mối quan hệ giữa `Bill` và `Orders`
- **Mô tả**: Một hóa đơn (`Bill`) thuộc về một đơn hàng (`Orders`).
- **Mối quan hệ**: 1:1.

```sql
ALTER TABLE Bill
ADD CONSTRAINT fk_bill_order
FOREIGN KEY (Order_ID)
REFERENCES Orders (Order_ID)
ON DELETE CASCADE;
```


6. Mối quan hệ giữa `Order_Product` và `Orders`, `Product`
- **Mô tả**: Liên kết giữa các đơn hàng (`Orders`) và sản phẩm (`Product`) thông qua bảng trung gian `Order_Product`.
- **Mối quan hệ**: N:M.

```sql
ALTER TABLE Order_Product
ADD CONSTRAINT fk_order_product_order
FOREIGN KEY (Order_ID)
REFERENCES Orders (Order_ID)
ON DELETE CASCADE;

ALTER TABLE Order_Product
ADD CONSTRAINT fk_order_product_product
FOREIGN KEY (Product_ID)
REFERENCES Product (Product_ID)
ON DELETE CASCADE;
```


7. Mối quan hệ giữa `Supplier_Product` và `Supplier`, `Product`
- **Mô tả**: Liên kết giữa các nhà cung cấp (`Supplier`) và sản phẩm (`Product`) thông qua bảng trung gian `Supplier_Product`.
- **Mối quan hệ**: N:M.

```sql
ALTER TABLE Supplier_Product
ADD CONSTRAINT fk_supplier_product_supplier
FOREIGN KEY (Supplier_ID)
REFERENCES Supplier (Supplier_ID)
ON DELETE CASCADE;

ALTER TABLE Supplier_Product
ADD CONSTRAINT fk_supplier_product_product
FOREIGN KEY (Product_ID)
REFERENCES Product (Product_ID)
ON DELETE CASCADE;
```


Ghi chú:
- **`ON DELETE CASCADE`**: Khi dữ liệu trong bảng cha bị xóa, các bản ghi liên quan trong bảng con cũng sẽ bị xóa.
- **`ON DELETE SET NULL`**: Khi dữ liệu trong bảng cha bị xóa, cột khóa ngoại trong bảng con sẽ được đặt thành `NULL`.


