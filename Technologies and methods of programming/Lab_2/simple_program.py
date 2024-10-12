import os
import time

# Đường dẫn đến tệp dữ liệu
INSTALL_DIR = os.path.expanduser("~/.simple_program")
LIMITS_FILE = os.path.join(INSTALL_DIR, "limits.txt")
USER_FILE = os.path.join(INSTALL_DIR, "users.txt")

# Hàm đọc giới hạn
def read_limits():
    limits = {}
    with open(LIMITS_FILE, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            limits[key] = int(value)
    return limits

# Hàm ghi giới hạn
def write_limits(limits):
    with open(LIMITS_FILE, 'w') as file:
        for key, value in limits.items():
            file.write(f"{key}={value}\n")

# Kiểm tra giới hạn thời gian và số lần khởi chạy
def check_limits():
    limits = read_limits()
    current_time = time.time()
    elapsed_time = current_time - limits['install_time']
    if elapsed_time > limits['time_limit']:
        print("Thời gian sử dụng chương trình đã hết. Vui lòng mua phiên bản đầy đủ.")
        exit()

    if limits['start_count'] >= limits['start_limit']:
        print("Đã đạt giới hạn số lần khởi chạy chương trình. Vui lòng mua phiên bản đầy đủ.")
        exit()

    limits['start_count'] += 1
    write_limits(limits)

# Hàm kiểm tra sự tồn tại của người dùng
def check_user(name):
    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as file:
            users = file.readlines()
            if name + '\n' in users:
                print(f"Tên {name} đã có trong cơ sở dữ liệu.")
            else:
                with open(USER_FILE, 'a') as file:
                    file.write(name + '\n')
                print(f"Tên {name} đã được thêm vào cơ sở dữ liệu.")
    else:
        with open(USER_FILE, 'w') as file:
            file.write(name + '\n')
        print(f"Tên {name} đã được thêm vào cơ sở dữ liệu.")

# Hàm chính
def main():
    check_limits()

    # Nhập tên của người dùng
    name = input("Nhập họ và tên của bạn: ")
    check_user(name)

    print("Chương trình đã kết thúc.")

if __name__ == "__main__":
    main()
