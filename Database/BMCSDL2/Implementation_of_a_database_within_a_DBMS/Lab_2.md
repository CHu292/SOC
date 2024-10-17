# 1. Chọn hệ quản trị cơ sở dữ liệu (DBMS)

- Sử dụng PostgreSQL
- Hỗ trợ chuẩn SQL, mạnh mẽ trong việc tối ưu hóa truy vấn và hỗ trợ các tính năng nâng cao.
- Lý do chọn PostgreSQL: Đây là hệ quản trị CSDL phổ biến, dễ sử dụng, có khả năng xử lý dữ liệu lớn, và đáp ứng các yêu cầu về bảo mật.

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
