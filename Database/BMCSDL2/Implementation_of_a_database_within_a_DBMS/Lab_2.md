# 1. Chọn hệ quản trị cơ sở dữ liệu (DBMS)

- Sử dụng PostgreSQL
- Lý do sử dụng: PostgreSQL là một hệ quản trị cơ sở dữ liệu quan hệ mạnh mẽ, mã nguồn mở và tuân thủ chuẩn SQL. Nó có khả năng xử lý các cơ sở dữ liệu phức tạp, hỗ trợ đa người dùng và tích hợp tốt với các ngôn ngữ lập trình. PostgreSQL cũng được sử dụng rộng rãi trong các dự án thực tế nhờ khả năng mở rộng và bảo mật tốt.

# 2. Tạo cấu trúc cơ sở dữ liệu

## Kết nối cơ sở dữ liệu:

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
### Tạo cơ sở dữ liệu

```SQL
create database coffee_shop_db
with
owner = postgres
encoding = 'UTF8'
tablespace = pg_default
connection limit = -1
is_template = False;
```
1. CREATE DATABASE coffee_shop_db
CREATE DATABASE coffee_shop_db: Tạo cơ sở dữ liệu mới có tên là coffee_shop_db. Đây là tên của cơ sở dữ liệu mà bạn sẽ sử dụng để lưu trữ dữ liệu của mình.
2. OWNER = postgres
OWNER = postgres: Xác định người sở hữu (owner) của cơ sở dữ liệu là người dùng postgres. Người sở hữu có toàn quyền quản lý cơ sở dữ liệu này (tạo bảng, sửa bảng, quản lý dữ liệu, v.v.).
3. ENCODING = 'UTF8'
ENCODING = 'UTF8': Xác định mã hóa ký tự mà cơ sở dữ liệu sẽ sử dụng là UTF-8. UTF-8 là một chuẩn mã hóa ký tự phổ biến, hỗ trợ hầu hết các ngôn ngữ trên thế giới. Điều này đảm bảo rằng cơ sở dữ liệu có thể lưu trữ dữ liệu tiếng Việt, tiếng Anh, tiếng Nga và nhiều ngôn ngữ khác.
4. TABLESPACE = pg_default
TABLESPACE = pg_default: Xác định không gian lưu trữ (tablespace) mặc định là pg_default. Tablespace là nơi vật lý trên đĩa mà dữ liệu của cơ sở dữ liệu sẽ được lưu trữ. Trong trường hợp này, dữ liệu sẽ được lưu trong tablespace mặc định của PostgreSQL.
5. CONNECTION LIMIT = -1
CONNECTION LIMIT = -1: Giới hạn số lượng kết nối tối đa đến cơ sở dữ liệu này là -1, nghĩa là không giới hạn số lượng kết nối. Bất kỳ số lượng người dùng nào cũng có thể kết nối vào cơ sở dữ liệu, miễn là tài nguyên hệ thống cho phép.
6. IS_TEMPLATE = False
IS_TEMPLATE = False: Đặt thuộc tính IS_TEMPLATE thành False, nghĩa là cơ sở dữ liệu này không được sử dụng làm mẫu (template) để tạo các cơ sở dữ liệu khác. Nếu bạn đặt giá trị True, cơ sở dữ liệu này có thể được dùng làm mẫu để sao chép khi tạo các cơ sở dữ liệu mới.

```SQL
postgres=# \c coffee_shop_db 
You are now connected to database "coffee_shop_db" as user "postgres".
coffee_shop_db=# 
```

- Tạo schema
```sql
coffee_shop_db=# create schema coffee_shop_schema;
CREATE SCHEMA
coffee_shop_db=# \dn
            List of schemas
        Name        |       Owner       
--------------------+-------------------
 coffee_shop_schema | postgres
 public             | pg_database_owner
(2 rows)
```
- Chỉ định schema
```sql
coffee_shop_db=# set search_path to coffee_shop_schema;
SET
coffee_shop_db=# show search_path ;
    search_path     
--------------------
 coffee_shop_schema
```
### Tạo bảng
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
    Employee_ID INTEGER,
    FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID)
);
```

Bảng Product
```sql
CREATE TABLE Product (
    Product_ID SERIAL PRIMARY KEY,
    Product_Category_Name VARCHAR(100) NOT NULL,
    Price NUMERIC(10, 2) NOT NULL,
    Warehouse_ID INTEGER,
    FOREIGN KEY (Warehouse_ID) REFERENCES Warehouse(Warehouse_ID)
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
    Employee_ID INTEGER,
    FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID),
    FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID)
);
```
Bảng Bill
```sql
CREATE TABLE Bill (
    Bill_ID SERIAL PRIMARY KEY,
    Amount NUMERIC(10, 2) NOT NULL,
    Payment_Method VARCHAR(50) NOT NULL,
    Order_ID INTEGER,
    FOREIGN KEY (Order_ID) REFERENCES Orders(Order_ID)
);
```

Bảng liên kết giữa bảng Orders và bảng Product
```sql
CREATE TABLE Order_Product (
    Order_ID INTEGER,
    Product_ID INTEGER,
    PRIMARY KEY (Order_ID, Product_ID),
    FOREIGN KEY (Order_ID) REFERENCES "Order"(Order_ID),
    FOREIGN KEY (Product_ID) REFERENCES Product(Product_ID)
);
```

- Bảng liên kết giữa bảng Supplier và Product
```sql
CREATE TABLE Supplier_Product (
    Supplier_ID INTEGER,
    Product_ID INTEGER,
    PRIMARY KEY (Supplier_ID, Product_ID),
    FOREIGN KEY (Supplier_ID) REFERENCES Supplier(Supplier_ID),
    FOREIGN KEY (Product_ID) REFERENCES Product(Product_ID)
);
```
Ta có các bảng sau
```sql
coffee_shop_db=# \dt
                    List of relations
       Schema       |       Name       | Type  |  Owner   
--------------------+------------------+-------+----------
 coffee_shop_schema | bill             | table | postgres
 coffee_shop_schema | customer         | table | postgres
 coffee_shop_schema | employee         | table | postgres
 coffee_shop_schema | order_product    | table | postgres
 coffee_shop_schema | orders           | table | postgres
 coffee_shop_schema | product          | table | postgres
 coffee_shop_schema | supplier         | table | postgres
 coffee_shop_schema | supplier_product | table | postgres
 coffee_shop_schema | warehouse        | table | postgres
(9 rows)
```

---


Kiểm tra csdl trên PgAdmin

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Database/BMCSDL2/entity-relationship_method/image/mo_hinh_quan_he.png" alt="Mô hình quan hệ" width="700">
</p>
<p align="center"><b>Mô hình quan hệ</b></p>

### Sơ đồ

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Database/BMCSDL2/entity-relationship_method/image/mo_hinh_quan_he.png" alt="Mô hình quan hệ" width="700">
</p>
<p align="center"><b>Mô hình quan hệ</b></p>


### Tạo bảng

#### 
