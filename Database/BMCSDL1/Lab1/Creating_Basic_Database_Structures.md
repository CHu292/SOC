# Tạo các thành phần cơ bản của cơ sở dữ liệu

## 1. Kết nối dữ liệu bằng máy khách psql

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

## 2. Tạo cơ sở dữ liệu:
**Cú pháp**

```bash
CREATE DATABASE <tên_cơ_sở_dữ_liệu>;
```

```bash
postgres=# create database n3347_22;
CREATE DATABASE
```

**Kiểm tra**

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
