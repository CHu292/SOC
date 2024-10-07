# 1. Xây dựng chương trình bảo vệ file
```
import os
import hashlib
import fnmatch
import stat
import subprocess

TEMPLATE_FILE = 'template.tbl'

# Hàm để đọc file template.tbl
def read_template_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    hashed_password = lines[0].strip()  # Dòng đầu tiên chứa mật khẩu đã được băm
    forbidden_files = [line.strip() for line in lines[1:]]  # Danh sách các tệp bị cấm
    return hashed_password, forbidden_files

# Hàm để băm mật khẩu
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Hàm kiểm tra mật khẩu người dùng
def check_password(hashed_password, input_password):
    return hashed_password == hash_password(input_password)

# Hàm kiểm tra xem tệp có bị cấm hay không
def is_forbidden_file(filename, forbidden_files):
    for pattern in forbidden_files:
        if fnmatch.fnmatch(filename, pattern):
            return True
    return False

# Hàm bảo vệ tệp (cấm đọc, ghi, xóa, di chuyển)
def protect_file(filepath):
    # Đặt quyền không đọc, ghi và thực thi cho tất cả người dùng
    os.chmod(filepath, 0)
    # Sử dụng chattr để ngăn chặn xóa và di chuyển tệp (immutable)
    subprocess.run(['sudo', 'chattr', '+i', filepath])
    print(f"Tệp đã được bảo vệ: {filepath}")

# Hàm gỡ bảo vệ tệp (cho phép đọc, ghi, xóa, di chuyển)
def unprotect_file(filepath):
    # Gỡ thuộc tính immutable (cho phép xóa tệp)
    subprocess.run(['sudo', 'chattr', '-i', filepath])
    # Khôi phục quyền đọc, ghi và thực thi cho chủ sở hữu
    os.chmod(filepath, stat.S_IRWXU)
    print(f"Quyền truy cập tệp đã được khôi phục: {filepath}")

# Hàm bảo vệ hoặc gỡ bảo vệ các tệp trong thư mục hiện tại
def protect_files(directory, forbidden_files, enable=True):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if is_forbidden_file(file, forbidden_files):
                filepath = os.path.join(root, file)
                if enable:
                    protect_file(filepath)
                else:
                    unprotect_file(filepath)

# Hàm bật/tắt chế độ bảo vệ
def toggle_protection(template_file, enable=True):
    hashed_password, forbidden_files = read_template_file(template_file)
    
    input_password = input("Nhập mật khẩu để bật/tắt bảo vệ: ")
    
    if check_password(hashed_password, input_password):
        if enable:
            print("Mật khẩu đúng! Bắt đầu bảo vệ các tệp.")
        else:
            print("Mật khẩu đúng! Đang gỡ bảo vệ các tệp.")
        current_directory = os.getcwd()  # Thư mục hiện tại
        protect_files(current_directory, forbidden_files, enable)
    else:
        print("Mật khẩu sai! Không thể bật/tắt chế độ bảo vệ.")

# Chạy chương trình
if __name__ == "__main__":
    choice = input("Nhập 'on' để bật bảo vệ hoặc 'off' để tắt bảo vệ: ").strip().lower()
    if choice == 'on':
        toggle_protection(TEMPLATE_FILE, enable=True)
    elif choice == 'off':
        toggle_protection(TEMPLATE_FILE, enable=False)
    else:
        print("Lựa chọn không hợp lệ.")
```

## 1.1 Xử lý tệp tin (File Handling)

1.1 Open Files
Trước khi làm việc với bất cứ file nào, bạn phải mở file đó. Để mở một file, Python cung cấp hàm `open()`. Nó trả về một đối tượng file mà được sử dụng với các hàm khác. Với file đã mở, bạn có thể thực hiện các hoạt động như đọc, ghi mới, ghi thêm … trên file đó.
- Cú pháp:
`file object = open(file_name [, access_mode][, buffering])`
Trong đó:
- **filename**: Đối số file_name là một giá trị chuỗi chứa tên của các file mà bạn muốn truy cập.
- **access_mode**: Các access_mode xác định các chế độ của file được mở ra như read, write, append,... Đây là thông số tùy chọn và chế độ truy cập file mặc định là read (r).
- **buffering**: Nếu buffer được thiết lập là 0, nghĩa là sẽ không có trình đệm nào diễn ra. Nếu xác định là 1, thì trình đệm dòng được thực hiện trong khi truy cập một File. Nếu là số nguyên lớn hơn 1, thì hoạt động đệm được thực hiện với kích cỡ bộ đệm đã cho. Nếu là số âm, thì kích cỡ bộ đệm sẽ là mặc định.
