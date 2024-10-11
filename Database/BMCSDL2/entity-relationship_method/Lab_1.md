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
  <img src="https://github.com/CHu292/SOC/blob/main/Database/BMCSDL2/entity-relationship_method/image/So_do_ER.png" alt="Sơ đồ ER" width="700">
</p>

# 3 Chuyển đổi ER-diagram sang mô hình quan hệ

- Mỗi thực thể trong ER-diagram sẽ được chuyển thành một bảng. Các thuộc tính của thực thể sẽ trở thành các cột của bảng, và khoá chính của thực thể sẽ trở thành khoá chính của bảng.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Database/BMCSDL2/entity-relationship_method/image/mo_hinh_quan_he.png" alt="Mô hình quan hệ" width="700">
</p>

# 4 Chuyển đổi quan hệ cơ sở dữ liệu sang 3NF.

**Để kiểm tra xem mô hình quan hệ đã đạt chuẩn 3NF (Third Normal Form) hay chưa, chúng ta cần xem xét các điều kiện của chuẩn 3NF:**

**- Đạt chuẩn 1NF:** Mỗi bảng trong mô hình phải có cấu trúc dạng bảng, với mỗi giá trị trong các cột phải là đơn trị (không có cột chứa các giá trị lặp hoặc nhóm giá trị lồng nhau). Đồng thời, bảng phải có khóa chính (Primary Key - PK) để đảm bảo mỗi dòng là duy nhất.

**- Đạt chuẩn 2NF:** Bảng phải đạt chuẩn 1NF và tất cả các thuộc tính không khóa phải phụ thuộc hoàn toàn vào khóa chính. Nói cách khác, không có thuộc tính không khóa nào phụ thuộc vào một phần của khóa chính (tránh phụ thuộc một phần).

**- Đạt chuẩn 3NF:** Bảng phải đạt chuẩn 2NF và không có phụ thuộc bắc cầu giữa các thuộc tính không khóa. Nghĩa là, tất cả các thuộc tính không khóa phải phụ thuộc trực tiếp vào khóa chính, không phụ thuộc vào các thuộc tính không khóa khác.

## Phân tích mô hình quan hệ để kiểm tra 3NF

Chúng ta sẽ xem xét từng bảng trong mô hình đã thiết kế để đảm bảo không vi phạm các điều kiện của chuẩn 3NF.

### 1 Bảng Employee

- Thuộc tính: Employee_ID (PK), Name, Position, Phone_Number, Email
- Phụ thuộc hàm: Tất cả các thuộc tính (Name, Position, Phone_Number, Email) đều phụ thuộc trực tiếp vào Employee_ID, và không có phụ thuộc bắc cầu.
- Kết luận: Đạt chuẩn 3NF.

### 2 Bảng Supplier

- Thuộc tính: Supplier_ID (PK), Name, Address, Phone_Number, Email
- Phụ thuộc hàm: Tất cả các thuộc tính (Name, Address, Phone_Number, Email) phụ thuộc trực tiếp vào Supplier_ID, không có phụ thuộc bắc cầu.
- Kết luận: Đạt chuẩn 3NF.

### 3 Bảng Product

- Thuộc tính: Product_ID (PK), Product_Category_Name, Price, Warehouse_ID (FK)
- Phụ thuộc hàm:
  -  Tất cả các thuộc tính (Product_Category_Name, Price, Warehouse_ID) đều phụ thuộc trực tiếp vào Product_ID.
  -  Không có thuộc tính nào phụ thuộc vào thuộc tính khác ngoài khóa chính.
-  Kết luận: Đạt chuẩn 3NF.

### 4 Bảng Customer

- Thuộc tính: Customer_ID (PK), Name, Phone_Number, Email
- Phụ thuộc hàm: Tất cả các thuộc tính phụ thuộc trực tiếp vào Customer_ID, không có phụ thuộc bắc cầu.
- Kết luận: Đạt chuẩn 3NF.

### 5 Bảng Order

- Thuộc tính: Order_ID (PK), Order_Date, Total_Amount, Customer_ID (FK), Employee_ID (FK)
- Phụ thuộc hàm:
  - Tất cả các thuộc tính (Order_Date, Total_Amount, Customer_ID, Employee_ID) đều phụ thuộc trực tiếp vào Order_ID.
  - Không có thuộc tính nào phụ thuộc vào thuộc tính khác ngoài khóa chính.
- Kết luận: Đạt chuẩn 3NF.

### 6 Bảng Bill

- Thuộc tính: Bill_ID (PK), Amount, Payment_Method, Order_ID (FK)
- Phụ thuộc hàm:
  - Tất cả các thuộc tính (Amount, Payment_Method, Order_ID) đều phụ thuộc trực tiếp vào Bill_ID.
  - Không có thuộc tính nào phụ thuộc vào thuộc tính khác ngoài khóa chính.
- Kết luận: Đạt chuẩn 3NF.

### 7 Bảng Warehouse

- Thuộc tính: Warehouse_ID (PK), Address, Status, Employee_ID (FK)
- Phụ thuộc hàm:
  - Tất cả các thuộc tính (Address, Status, Employee_ID) đều phụ thuộc trực tiếp vào Warehouse_ID.
  - Không có phụ thuộc bắc cầu.
- Kết luận: Đạt chuẩn 3NF.

### 8 Bảng trung gian Order_Product

- Thuộc tính: Order_ID (PK, FK), Product_ID (PK, FK)
- Không có thuộc tính không khóa, bảng này chỉ chứa các khóa ngoại liên kết, nên không cần kiểm tra thêm về 3NF.

### 9 Bảng trung gian Supplier_Product

- Thuộc tính: Supplier_ID (PK, FK), Product_ID (PK, FK)
- Không có thuộc tính không khóa, bảng này chỉ chứa các khóa ngoại liên kết, nên không cần kiểm tra thêm về 3NF.

**Tổng kết**

Tất cả các bảng trong mô hình quan hệ trên đều đạt chuẩn 3NF. Không có bảng nào vi phạm điều kiện của chuẩn 3NF như phụ thuộc bắc cầu hoặc phụ thuộc một phần vào khóa chính.

# 5 Tạo chế độ xem

## 5.1. View dành cho Nhân viên bán hàng (Sales Employee View)

**Mục đích:**

Chế độ xem này cung cấp cho nhân viên bán hàng thông tin về các đơn hàng mà họ đã xử lý, bao gồm thông tin chi tiết về khách hàng, ngày đặt hàng, tổng số tiền đơn hàng, và trạng thái của đơn hàng. Nhân viên bán hàng có thể dùng view này để theo dõi tiến độ của các đơn hàng và liên hệ khách hàng nếu cần thiết.

**Chi tiết truy vấn:**

```SQL
CREATE VIEW Sales_Employee_View AS
SELECT 
    e.Employee_ID,
    e.Name AS Employee_Name,
    o.Order_ID,
    o.Order_Date,
    o.Total_Amount,
    c.Customer_ID,
    c.Name AS Customer_Name,
    c.Phone_Number AS Customer_Phone,
    c.Email AS Customer_Email
FROM 
    Employee e
JOIN 
    [Order] o ON e.Employee_ID = o.Employee_ID
JOIN 
    Customer c ON o.Customer_ID = c.Customer_ID;
```

**Dữ liệu hiển thị:**

- Employee_ID, Employee_Name: ID và tên của nhân viên bán hàng.
- Order_ID, Order_Date, Total_Amount: ID của đơn hàng, ngày đặt hàng, và tổng số tiền của đơn hàng.
- Customer_ID, Customer_Name, Customer_Phone, Customer_Email: ID, tên, số điện thoại và email của khách hàng.

## 5.2. View dành cho Quản lý kho (Warehouse Manager View)

**Mục đích:**

Chế độ xem này cho phép quản lý kho theo dõi thông tin về các sản phẩm đang được lưu trữ trong kho và tình trạng của kho. View này giúp họ kiểm soát hiệu quả việc quản lý hàng tồn kho và đánh giá tình trạng lưu trữ của sản phẩm.

**Chi tiết truy vấn:**

```SQL

CREATE VIEW Warehouse_Manager_View AS
SELECT 
    w.Warehouse_ID,
    w.Address AS Warehouse_Address,
    w.Status AS Warehouse_Status,
    p.Product_ID,
    p.Product_Category_Name,
    p.Price
FROM 
    Warehouse w
JOIN 
    Product p ON w.Warehouse_ID = p.Warehouse_ID;
```

**Dữ liệu hiển thị:**

- Warehouse_ID, Warehouse_Address, Warehouse_Status: ID, địa chỉ và trạng thái của kho hàng.
- Product_ID, Product_Category_Name, Price: ID sản phẩm, tên danh mục sản phẩm, và giá sản phẩm.


## 5.3 View dành cho Khách hàng (Customer View)

**Mục đích:**

View này cho phép khách hàng xem lịch sử mua hàng của họ, bao gồm thông tin về các đơn hàng đã đặt và chi tiết hóa đơn tương ứng. Nó giúp khách hàng theo dõi các giao dịch đã thực hiện và các phương thức thanh toán.

**Chi tiết truy vấn:**

```SQL
CREATE VIEW Customer_Order_View AS
SELECT 
    c.Customer_ID,
    c.Name AS Customer_Name,
    o.Order_ID,
    o.Order_Date,
    o.Total_Amount,
    b.Bill_ID,
    b.Amount AS Bill_Amount,
    b.Payment_Method
FROM 
    Customer c
JOIN 
    [Order] o ON c.Customer_ID = o.Customer_ID
JOIN 
    Bill b ON o.Order_ID = b.Order_ID;
```

**Dữ liệu hiển thị:**

- Customer_ID, Customer_Name: ID và tên của khách hàng.
- Order_ID, Order_Date, Total_Amount: ID đơn hàng, ngày đặt hàng, và tổng số tiền của đơn hàng.
- Bill_ID, Bill_Amount, Payment_Method: ID hóa đơn, số tiền hóa đơn, và phương thức thanh toán.

## 5.4 View dành cho Quản lý nhà cung cấp (Supplier Manager View)

**Mục đích:**

View này cho phép quản lý nhà cung cấp theo dõi thông tin về các nhà cung cấp và sản phẩm mà họ cung cấp. Quản lý nhà cung cấp có thể sử dụng view này để kiểm tra thông tin về các nhà cung cấp và sản phẩm đang được nhập từ các đối tác.

**Chi tiết truy vấn:**

```SQL
CREATE VIEW Supplier_Product_View AS
SELECT 
    s.Supplier_ID,
    s.Name AS Supplier_Name,
    s.Phone_Number AS Supplier_Phone,
    p.Product_ID,
    p.Product_Category_Name,
    p.Price
FROM 
    Supplier s
JOIN 
    Supplier_Product sp ON s.Supplier_ID = sp.Supplier_ID
JOIN 
    Product p ON sp.Product_ID = p.Product_ID;
```

**Dữ liệu hiển thị:**

- Supplier_ID, Supplier_Name, Supplier_Phone: ID, tên và số điện thoại của nhà cung cấp.
- Product_ID, Product_Category_Name, Price: ID sản phẩm, danh mục sản phẩm, và giá sản phẩm mà nhà cung cấp cung cấp.

