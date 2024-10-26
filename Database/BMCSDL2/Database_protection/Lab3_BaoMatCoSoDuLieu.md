
# Báo Cáo Bài Lab 3: Bảo Mật Cơ Sở Dữ Liệu

## 1. Giám Sát Cơ Sở Dữ Liệu (Database Monitoring)

Để giám sát cơ sở dữ liệu, ta tạo một bảng log để ghi lại các thay đổi trong cơ sở dữ liệu. Sử dụng trigger để tự động cập nhật log mỗi khi có thao tác thêm, sửa, hoặc xóa trong các bảng chính.

### Tạo Bảng Log

```sql
CREATE TABLE main_log (
    log_id SERIAL PRIMARY KEY,
    operation_type TEXT,
    operation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_operator TEXT,
    changed_data JSON
);
```
Cấu trúc bảng log:
- log_id: Khóa chính, tự động tăng.
- operation_type: Loại thao tác (INSERT, UPDATE, DELETE).
- operation_date: Ngày và giờ xảy ra thay đổi.
- user_operator: Người thực hiện thao tác (tên người dùng hoặc vai trò).
- changed_data: Dữ liệu đã thay đổi, lưu ở dạng JSON để dễ dàng lưu cả dữ liệu cũ và mới.

- Ví dụ:
```sql
lab3=# CREATE TABLE main_log (
    log_id SERIAL PRIMARY KEY,
    operation_type TEXT,
    operation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_operator TEXT,
    changed_data JSON
);
CREATE TABLE
lab3=# \dt
                    List of relations
       Schema       |       Name       | Type  |  Owner   
--------------------+------------------+-------+----------
 coffee_shop_schema | bill             | table | postgres
 coffee_shop_schema | customer         | table | postgres
 coffee_shop_schema | employee         | table | postgres
 coffee_shop_schema | main_log         | table | postgres
 coffee_shop_schema | order_product    | table | postgres
 coffee_shop_schema | orders           | table | postgres
 coffee_shop_schema | product          | table | postgres
 coffee_shop_schema | supplier         | table | postgres
 coffee_shop_schema | supplier_product | table | postgres
 coffee_shop_schema | warehouse        | table | postgres
(10 rows)
```


### Tạo Hàm Trigger

Hàm `logging()` dưới đây sẽ ghi lại thông tin vào bảng `main_log`.

```sql
CREATE OR REPLACE FUNCTION logging() RETURNS TRIGGER AS $logging$
BEGIN
    IF (TG_OP = 'DELETE') THEN
        INSERT INTO main_log (operation_type, user_operator, changed_data)
        VALUES ('D', current_user, row_to_json(OLD));
    ELSIF (TG_OP = 'UPDATE') THEN
        INSERT INTO main_log (operation_type, user_operator, changed_data)
        VALUES ('U', current_user, row_to_json(NEW));
    ELSIF (TG_OP = 'INSERT') THEN
        INSERT INTO main_log (operation_type, user_operator, changed_data)
        VALUES ('I', current_user, row_to_json(NEW));
    END IF;
    RETURN NULL;    
END;
$logging$ LANGUAGE plpgsql;
```
- Định nghĩa hàm trigger logging(): Hàm logging() là một hàm loại trigger (kích hoạt) được viết bằng ngôn ngữ plpgsql của PostgreSQL. Hàm này sẽ thực hiện khi có thao tác thêm (INSERT), cập nhật (UPDATE) hoặc xóa (DELETE) trên các bảng đã được liên kết với trigger.

```sql
CREATE OR REPLACE FUNCTION logging() RETURNS TRIGGER AS $logging$
```
    - RETURNS TRIGGER cho biết hàm sẽ được gọi dưới dạng trigger.
    - $logging$ được sử dụng để đánh dấu phần thân của hàm bắt đầu và kết thúc.

- Kiểm tra loại thao tác với TG_OP: Bên trong hàm, TG_OP là biến hệ thống dùng để xác định loại thao tác đã kích hoạt trigger:
    - DELETE': Xóa bản ghi
    - 'UPDATE': Cập nhật bản ghi
    - 'INSERT': Thêm mới bản ghi
 
- Dựa trên giá trị của TG_OP, hàm sẽ xử lý tương ứng và lưu dữ liệu phù hợp vào bảng log.
- Lưu dữ liệu vào bảng log main_log: Với mỗi loại thao tác, hàm sẽ thực hiện một câu lệnh INSERT vào bảng main_log. Cụ thể:
    - Khi xóa dữ liệu (TG_OP = 'DELETE'):
        - Lưu loại thao tác là DELETE.
        - Ghi lại tên người dùng hiện tại thực hiện thao tác (current_user).
        - Lưu dữ liệu của bản ghi bị xóa, sử dụng row_to_json(OLD) để chuyển dữ liệu của bản ghi cũ thành định dạng JSON.

```sql
INSERT INTO main_log (operation_type, user_operator, changed_data)
VALUES ('DELETE', current_user, row_to_json(OLD));

```
- Các thao tác còn lại tương tự
- Hoàn tất hàm và trả về kết quả: Hàm logging() kết thúc bằng RETURN NULL;, để chỉ ra rằng trigger không thay đổi nội dung của bản ghi trong bảng gốc. Cuối cùng, đóng phần thân hàm với $logging$ LANGUAGE plpgsql;.
```sql
RETURN NULL;
END;
$logging$ LANGUAGE plpgsql;
```
Ví dụ:
```sql
lab3=# CREATE OR REPLACE FUNCTION logging() RETURNS TRIGGER AS $logging$
BEGIN
    IF (TG_OP = 'DELETE') THEN
        INSERT INTO main_log (operation_type, user_operator, changed_data)
        VALUES ('D', current_user, row_to_json(OLD));
    ELSIF (TG_OP = 'UPDATE') THEN
        INSERT INTO main_log (operation_type, user_operator, changed_data)
        VALUES ('U', current_user, row_to_json(NEW));
    ELSIF (TG_OP = 'INSERT') THEN
        INSERT INTO main_log (operation_type, user_operator, changed_data)
        VALUES ('I', current_user, row_to_json(NEW));
    END IF;
    RETURN NULL;    
END;
$logging$ LANGUAGE plpgsql;
CREATE FUNCTION
lab3=# \df
                              List of functions
       Schema       |  Name   | Result data type | Argument data types | Type 
--------------------+---------+------------------+---------------------+------
 coffee_shop_schema | logging | trigger          |                     | func
(1 row)

```



### Áp Dụng Trigger Cho Các Bảng

Áp dụng trigger cho bảng `Product`.

```sql
CREATE TRIGGER product_logging
AFTER INSERT OR UPDATE OR DELETE ON Product
FOR EACH ROW EXECUTE FUNCTION logging();
```

Áp dụng trigger cho bảng `Bill`.

```sql
CREATE TRIGGER bill_logging
AFTER INSERT OR UPDATE OR DELETE ON Product
FOR EACH ROW EXECUTE FUNCTION logging();
```

Áp dụng trigger cho bảng `Orders`.

```sql
CREATE TRIGGER order_logging
AFTER INSERT OR UPDATE OR DELETE ON Product
FOR EACH ROW EXECUTE FUNCTION logging();
```

Áp dụng trigger cho bảng `Customer`.

```sql
CREATE TRIGGER customer_logging
AFTER INSERT OR UPDATE OR DELETE ON Product
FOR EACH ROW EXECUTE FUNCTION logging();
```

Áp dụng trigger cho bảng `Employee`.

```sql
CREATE TRIGGER employee_logging
AFTER INSERT OR UPDATE OR DELETE ON Product
FOR EACH ROW EXECUTE FUNCTION logging();
```

Áp dụng trigger cho bảng `Warehouse`.

```sql
CREATE TRIGGER warehouse_logging
AFTER INSERT OR UPDATE OR DELETE ON Product
FOR EACH ROW EXECUTE FUNCTION logging();
```

Áp dụng trigger cho bảng `Supplier`.

```sql
CREATE TRIGGER supplier_logging
AFTER INSERT OR UPDATE OR DELETE ON Product
FOR EACH ROW EXECUTE FUNCTION logging();
```


## 2. Mã Hóa Dữ Liệu Nhạy Cảm (Data Encryption)

Để bảo mật dữ liệu nhạy cảm, ta sử dụng mã hóa đối xứng AES-256 và tạo khóa mã hóa bằng hàm băm SHA-256 từ mật khẩu.

### Tạo Bảng Chứa Dữ Liệu Nhạy Cảm

```sql
CREATE TABLE secret_data (
    id SERIAL PRIMARY KEY,
    username TEXT,
    secret_token TEXT
);
```

### Mã Hóa Dữ Liệu Sử Dụng pgcrypto

```sql
-- Tải mô-đun pgcrypto (chỉ cần làm một lần)
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- Mã hóa dữ liệu với khóa mã hóa được tạo từ mật khẩu đã băm
INSERT INTO secret_data (username, secret_token) VALUES 
    (pgp_sym_encrypt('nguyen_van_a', '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08'), 
     pgp_sym_encrypt('token_secret', '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08'));
```

## 3. Kiểm Soát Truy Cập (Access Control)

Tạo các vai trò và phân quyền cho từng vai trò dựa trên nguyên tắc quyền hạn tối thiểu.

### Tạo Vai Trò

```sql
CREATE ROLE sales_role NOLOGIN;
CREATE ROLE warehouse_role NOLOGIN;
CREATE ROLE admin_role NOLOGIN;
```

### Phân Quyền

Phân quyền truy cập cho `sales_role` vào bảng `Orders` và `Customer`.

```sql
GRANT SELECT ON Orders TO sales_role;
GRANT SELECT ON Customer TO sales_role;
```

Phân quyền truy cập cho `warehouse_role` vào bảng `Product` và `Warehouse`.

```sql
GRANT SELECT ON Product TO warehouse_role;
GRANT SELECT ON Warehouse TO warehouse_role;
```

Phân quyền toàn quyền cho `admin_role`.

```sql
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO admin_role;
```

### Tạo Người Dùng và Gán Vai Trò

```sql
CREATE ROLE user_sales LOGIN PASSWORD 'strong_password';
GRANT sales_role TO user_sales;

CREATE ROLE user_warehouse LOGIN PASSWORD 'secure_password';
GRANT warehouse_role TO user_warehouse;

CREATE ROLE admin_user LOGIN PASSWORD 'admin_password';
GRANT admin_role TO admin_user;
```

## Kết Luận

Qua các bước trên, chúng ta đã hoàn thành việc thiết lập hệ thống bảo mật cơ sở dữ liệu với chức năng giám sát thay đổi, mã hóa dữ liệu nhạy cảm, và phân quyền truy cập.
