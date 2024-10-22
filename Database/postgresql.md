# 1. Kết nối dữ liệu bằng máy khách psql

```bash
sudo systemctl enable --now postgresql.service
```

```bash
sudo su postgres -c psql
```
**Giải thích tập lệnh:**
- Câu lệnh "sudo systemctl enable --now postgresql.service" được sử dụng để cài đặt và kích hoạt dịch vụ "PostgreSQL", đồng thời đảm bảo rằng dịch vụ này sẽ được khởi động tự động ngay lập tức và sau mỗi lần khởi động hệ thống.
- sudo: Được sử dụng để thực thi câu lệnh với quyền hạn của người dùng root hoặc một người dùng khác có quyền hạn tương đương.
- systemctl: Là một công cụ trong hệ thống systemd để quản lý các dịch vụ, thiết bị và các thành phần hệ thống khác.
- enable: Kích hoạt dịch vụ để khởi động cùng với hệ thống. Nó thêm một liên kết tới dịch vụ trong các thư mục systemd để đảm bảo rằng dịch vụ sẽ được khởi động tự động khi hệ thống khởi động.
- --now: Khi kết hợp với enable, sự kết hợp này đảm bảo rằng dịch vụ sẽ được khởi động ngay lập tức sau khi được kích hoạt.
- postgresql.service: Là tên của dịch vụ PostgreSQL. Trong trường hợp này, câu lệnh đang làm việc với dịch vụ PostgreSQL, có thể là một cơ sở dữ liệu quan hệ mạnh mẽ và phổ biến được sử dụng trong nhiều ứng dụng.
- su postgres: Lệnh này thay đổi người dùng hiện tại thành postgres.
- -c psql: Lệnh này chạy chương trình psql với các quyền của người dùng postgres.

# 2. Thao tác với cơ sở dữ liệu:

#### Tạo cơ sở dữ liệu

```bash
CREATE DATABASE <tên_cơ_sở_dữ_liệu>;
```

```bash
postgres=# create database n3347_22;
CREATE DATABASE
```

#### Xóa cơ sở dữ liệu

```sql
DROP DATABASE <tên_cơ_sở_dữ_liệu>;
```
#### Đổi tên cơ sở dữ liệu

```sql
ALTER DATABASE <tên_cơ_sở_dữ_liệu_cũ> RENAME TO <tên_cơ_sở_dữ_liệu_mới>;
```

#### Liệt kê tất cả các sơ sở dữ liệu

```\l```

*tùy chọn \l trong PostgreSQL là một lệnh được sử dụng để hiển thị danh sách các đối tượng trong cơ sở dữ liệu hiện tại, bao gồm bảng, lược đồ, view, v.v.*

``` bash
postgres=# \l
                                                          List of databases
      Name      |  Owner   | Encoding | Locale Provider |   Collate   |    Ctype    | ICU Locale | ICU Rules |   Access privileges   
----------------+----------+----------+-----------------+-------------+-------------+------------+-----------+-----------------------
 coffee_shop_db | postgres | UTF8     | libc            | en_US.UTF-8 | en_US.UTF-8 |            |           | 
 my_data        | postgres | UTF8     | libc            | en_US.UTF-8 | en_US.UTF-8 |            |           | =Tc/postgres         +
                |          |          |                 |             |             |            |           | postgres=CTc/postgres+
                |          |          |                 |             |             |            |           | chu=CTc/postgres
 n3347_22       | postgres | UTF8     | libc            | en_US.UTF-8 | en_US.UTF-8 |            |           | 
 postgres       | postgres | UTF8     | libc            | en_US.UTF-8 | en_US.UTF-8 |            |           | 
 template0      | postgres | UTF8     | libc            | en_US.UTF-8 | en_US.UTF-8 |            |           | =c/postgres          +
                |          |          |                 |             |             |            |           | postgres=CTc/postgres
 template1      | postgres | UTF8     | libc            | en_US.UTF-8 | en_US.UTF-8 |            |           | =c/postgres          +
                |          |          |                 |             |             |            |           | postgres=CTc/postgres
(6 rows)
```

#### Kết nối với cơ sở dữ liệu
- Cú pháp:
```bash
\c <cơ sở dữ liệu bạn muốn kết nối
```
- Ví dụ:
```bash
postgres=# \c n3347_22 
You are now connected to database "n3347_22" as user "postgres".
n3347_22=# 
```

#### Xem tất cả các người dùng

```\du```

```sql
n3347_22=# \du
 chu       | Superuser, Create role, Create DB
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS
```

# 3 Thao tác với schema  
#### Xem các schema đã tạo:

```bash
\dn
```

```sql
n3347_22=# \dn
 n3247_22_schema_lab1 | postgres
 public               | pg_database_owner
```

#### Tạo Schema
```sql
CREATE SCHEMA <tên_lược_đồ>;
```
**ví dụ**

```sql
create schema n3247_22_schema_lab1;
```

#### Đổi tên schema
```sql
ALTER SCHEMA tên_schema_cũ RENAME TO tên_schema_mới;
```

#### Xóa schema
```sql
DROP SCHEMA tên_schema;
```
### Phân quyền cho schema (Grant permission Schema)

**Bạn có thể cấp các quyền truy cập sau cho schema:**

- USAGE: Cho phép người dùng truy cập vào schema, nhưng không thể tạo đối tượng mới trong schema.
- CREATE: Cho phép người dùng tạo đối tượng mới (như bảng, chỉ mục) trong schema.
- Cú pháp:
```sql
GRANT quyền_truy_cập ON SCHEMA tên_schema TO tên_người_dùng;
```
- Cho phép người dùng chu có quyền truy cập (usage) vào schema n3247_22_schema_lab1:
```sql
n3347_22=# grant usage on schema n3247_22_schema_lab1 to chu;
GRANT
```
- Cho phép người dùng chu có quyền tạo đối tượng (create) trong schema n3247_22_schema_lab1:

```sql
n3347_22=# grant create on schema n3247_22_schema_lab1 to chu;
GRANT
```
- ấp cả quyền truy cập và tạo đối tượng cho người dùng chu
```sql
n3347_22=# grant usage, create on schema n3247_22_schema_lab1 to chu;
GRANT
```

### Phân quyền cho các đối tượng trong schema

**Bạn cũng có thể cấp quyền truy cập vào các đối tượng bên trong schema, như bảng hoặc hàm:**

- SELECT: Cho phép người dùng đọc dữ liệu từ bảng.
- INSERT: Cho phép người dùng thêm dữ liệu vào bảng.
- UPDATE: Cho phép người dùng cập nhật dữ liệu trong bảng.
- DELETE: Cho phép người dùng xóa dữ liệu từ bảng.
- ALL PRIVILEGES: Cấp tất cả các quyền cho đối tượng
- Cú pháp:
```sql
GRANT quyền_truy_cập ON đối_tượng (bảng/hàm) TO tên_người_dùng;
```
- Ví dụ:
```sql
n3347_22=# grant select on n3247_22_schema_lab1.my_table to chu;
GRANT
```
### Xóa quyền trên schema
- Cú pháp:
```sql
REVOKE quyền_truy_cập ON SCHEMA tên_schema FROM tên_người_dùng;
```
- Ví dụ:
```sql
n3347_22=# revoke usage on schema n3247_22_schema_lab1 from chu;
REVOKE
```
###  Xóa quyền trên các đối tượng trong schema (bảng, hàm)
- Cú pháp
```sql
REVOKE quyền_truy_cập ON đối_tượng (bảng/hàm) FROM tên_người_dùng;
```
- Ví dụ:
```sql
n3347_22=# revoke select on n3247_22_schema_lab1.my_table from chu;
REVOKE
```
###  Xóa quyền trên tất cả các đối tượng hiện tại và tương lai trong schema
- Nếu bạn đã cấp quyền cho tất cả các đối tượng bên trong schema, và muốn xóa chúng, bạn có thể sử dụng lệnh như sau:
```sql
REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA tên_schema FROM tên_người_dùng;
```
- Ví dụ:
```sql
n3347_22=# revoke all privileges on all tables in schema n3247_22_schema_lab1 from chu;
REVOKE
```

# 4 Thao tác với bảng

