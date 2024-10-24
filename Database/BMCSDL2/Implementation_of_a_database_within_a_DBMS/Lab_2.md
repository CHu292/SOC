# 1. Chọn hệ quản trị cơ sở dữ liệu (DBMS)

- Sử dụng PostgreSQL
- Lý do sử dụng: PostgreSQL là một hệ quản trị cơ sở dữ liệu quan hệ mạnh mẽ, mã nguồn mở và tuân thủ chuẩn SQL. Nó có khả năng xử lý các cơ sở dữ liệu phức tạp, hỗ trợ đa người dùng và tích hợp tốt với các ngôn ngữ lập trình. PostgreSQL cũng được sử dụng rộng rãi trong các dự án thực tế nhờ khả năng mở rộng và bảo mật tốt.
---
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
---
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
----
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
### Thêm dữ liệu vào các bảng
 Thêm dữ liệu vào bảng Emloyee
 
```sql
INSERT INTO employee (name, position, phone_number, email) 
VALUES 
    ('Nguyen Van A', 'supervisor', '9312828535', 'nguyenvana123@gmail.com'),
    ('Nguyen Thi B', 'salesperson', '92537563834', 'nb4214@gmail.com'),
    ('Artom', 'salesperson', '27582473683', 'artom33@mail.ru'),
    ('Irina', 'salesperson', '8925748253', 'irina8386@mail.ru'),
    ('Tran', 'salesperson', '92846363583', 'trantran4953@gmail.com');
```
Kết quả:
```sql
coffee_shop_db=# select * from employee;
 employee_id |     name     |  position   | phone_number |          email          
-------------+--------------+-------------+--------------+-------------------------
           1 | Nguyen Van A | supervisor  | 9312828535   | nguyenvana123@gmail.com
           2 | Nguyen Thi B | salesperson | 92537563834  | nb4214@gmail.com
           3 | Artom        | salesperson | 27582473683  | artom33@mail.ru
           4 | Irina        | salesperson | 8925748253   | irina8386@mail.ru
           5 | Tran         | salesperson | 92846363583  | trantran4953@gmail.com
(5 rows)
```

Thêm dữ liệu vào bảng Supplier
```sql
INSERT INTO supplier (name, address, phone_number, email) 
VALUES 
    ('Trung Nguyen Coffee', 'Dalat city', '03873532753', 'trungnguyencoffee@gmail.com'),
    ('King Coffee', 'Ho Chi Minh city', '0385636282', 'kingcoffee@gmail.com'),
    ('G7 Coffee', 'Ha Noi', '92834772843', 'g7coffee@gmail.com');
```
Kết quả:
```sql
coffee_shop_db=# select * from supplier;
 supplier_id |        name         |     address      | phone_number |            email            
-------------+---------------------+------------------+--------------+-----------------------------
           1 | Trung Nguyen Coffee | Dalat city       | 03873532753  | trungnguyencoffee@gmail.com
           2 | King Coffee         | Ho Chi Minh city | 0385636282   | kingcoffee@gmail.com
           3 | G7 Coffee           | Ha Noi           | 92834772843  | g7coffee@gmail.com
(3 rows)
```

Thêm dữ liệu cho bảng Warehouse
```sql
INSERT INTO warehouse (address, status, employee_id) 
VALUES 
    ('Lam Ha', 'In stock', 1),
    ('Tan Ha', 'In stock', 1),
    ('Dan Phuong', 'In stock', 1),
    ('Me Linh', 'In stock', 1);
```
Kết quả
```sql
coffee_shop_db=# select * from warehouse;
 warehouse_id |  address   |  status  | employee_id 
--------------+------------+----------+-------------
            1 | Lam Ha     | In stock |           1
            2 | Tan Ha     | In stock |           1
            3 | Dan Phuong | In stock |           1
            4 | Me Linh    | In stock |           1
(4 rows)
```

Thêm dữ liệu cho bảng Product
```sql
INSERT INTO product (product_category_name, price, warehouse_id) 
VALUES 
    ('Arabica', 100000, 1),
    ('Robusta', 90000, 2),
    ('Bourbon', 96000, 3),
    ('Typica', 92000, 4);
```
Kết quả:
```sql
coffee_shop_db=# select * from product;
 product_id | product_category_name |   price   | warehouse_id 
------------+-----------------------+-----------+--------------
          1 | Arabica               | 100000.00 |            1
          2 | Robusta               |  90000.00 |            2
          3 | Bourbon               |  96000.00 |            3
          4 | Typica                |  92000.00 |            4
(4 rows)
```

Thêm dữ liệu cho bảng Customer
```sql
INSERT INTO customer (name, phone_number, email) 
VALUES 
    ('Alex', '93842727543', 'alex8888@mail.ru'),
    ('Tom', '82736464383', 'tomi7749@mail.ru'),
    ('Anton', '827364646737', 'ton@mail.ru'),
    ('Karababy', '8283747654', 'baby@mail.ru');
```
Kết quả:
```sql
coffee_shop_db=# select * from customer;
 customer_id |   name   | phone_number |      email       
-------------+----------+--------------+------------------
           1 | Alex     | 93842727543  | alex8888@mail.ru
           2 | Tom      | 82736464383  | tomi7749@mail.ru
           3 | Anton    | 827364646737 | ton@mail.ru
           4 | Karababy | 8283747654   | baby@mail.ru
(4 rows)
```
Nhập dữ liệu cho bảng Orders
```sql
INSERT INTO orders (order_date, total_amount, employee_id, customer_id) 
VALUES 
    ('2024-10-12', 150000, 2, 1),
    ('2024-10-13', 599999, 2, 2),
    ('2024-10-13', 70000, 3, 3),
    ('2024-10-20', 6699999, 4, 4);
```
Kết quả
```sql
coffee_shop_db=# select * from orders;
 order_id | order_date | total_amount | employee_id | customer_id 
----------+------------+--------------+-------------+-------------
        1 | 2024-10-12 |    150000.00 |           2 |           1
        2 | 2024-10-13 |    599999.00 |           2 |           2
        3 | 2024-10-13 |     70000.00 |           3 |           3
        4 | 2024-10-20 |   6699999.00 |           4 |           4
(4 rows)
```
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
