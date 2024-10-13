#!/usr/bin/env python3
import os
import time
import hashlib
import threading
import sys

# Thư mục cài đặt hiện tại
INSTALL_DIR = os.getcwd()
USER_FILE = os.path.join(INSTALL_DIR, "user_data.txt")
LIMIT_FILE = os.path.join(INSTALL_DIR, "limit_data.txt")
INSTALL_FLAG = os.path.join(INSTALL_DIR, "installed.flag")
MAX_STARTS = 5
TIME_LIMIT = 30  # Giới hạn thời gian sử dụng (giây)

def hash_string(s):
    """Hàm băm chuỗi để lưu trữ thông tin dưới dạng mã băm."""
    return hashlib.sha256(s.encode()).hexdigest()

def check_user_exists(full_name):
    """Kiểm tra xem tên người dùng đã tồn tại trong tệp chưa."""
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as file:
            for line in file:
                if hash_string(full_name) in line:
                    return True
    return False

def add_user(full_name):
    """Thêm người dùng mới vào tệp."""
    with open(USER_FILE, "a") as file:
        file.write(hash_string(full_name) + "\n")

def check_limits():
    """Kiểm tra giới hạn về số lần sử dụng hoặc thời gian."""
    if not os.path.exists(LIMIT_FILE):
        with open(LIMIT_FILE, "w") as file:
            file.write(f"starts:0\ntime:0\n")

    with open(LIMIT_FILE, "r") as file:
        data = file.readlines()
        starts = int(data[0].split(":")[1].strip())
        used_time = int(data[1].split(":")[1].strip())

    if starts >= MAX_STARTS:
        return False, "Hết lượt sử dụng. Vui lòng mua phiên bản đầy đủ hoặc gỡ cài đặt chương trình."

    if used_time >= TIME_LIMIT:
        return False, "Hết thời gian sử dụng. Vui lòng mua phiên bản đầy đủ hoặc gỡ cài đặt chương trình."

    return True, ""

def update_limits(start_time):
    """Cập nhật số lần chạy và thời gian đã sử dụng."""
    with open(LIMIT_FILE, "r") as file:
        data = file.readlines()
        starts = int(data[0].split(":")[1].strip()) + 1
        used_time = int(data[1].split(":")[1].strip()) + int(time.time() - start_time)

    with open(LIMIT_FILE, "w") as file:
        file.write(f"starts:{starts}\ntime:{used_time}\n")

    return starts, used_time

def countdown_timer(remaining_time, program_running):
    """Đếm ngược thời gian sử dụng."""
    while remaining_time > 0 and program_running.is_set():
        time.sleep(1)
        remaining_time -= 1

    if remaining_time <= 0:
        program_running.clear()

def check_installation():
    """Kiểm tra xem chương trình đã được cài đặt chưa."""
    if not os.path.exists(INSTALL_FLAG):
        print("Chương trình chưa được cài đặt. Vui lòng cài đặt chương trình trước khi chạy.")
        sys.exit(1)

def main():
    # Kiểm tra xem chương trình đã được cài đặt chưa
    check_installation()

    # Kiểm tra giới hạn trước khi cho phép sử dụng chương trình
    allowed, message = check_limits()
    if not allowed:
        print(message)
        sys.exit(1)

    start_time = time.time()

    # Tạo cờ kiểm soát trạng thái chương trình
    program_running = threading.Event()
    program_running.set()

    # Tạo và khởi chạy bộ đếm thời gian
    remaining_time = TIME_LIMIT
    timer_thread = threading.Thread(target=countdown_timer, args=(remaining_time, program_running))
    timer_thread.start()

    try:
        # Nhập tên và họ đầy đủ
        full_name = input("Vui lòng nhập họ và tên của bạn: ")
        if not program_running.is_set():
            print("\nHết thời gian sử dụng.")
            sys.exit(1)  # Thoát chương trình khi hết thời gian

        # Kiểm tra xem người dùng có tồn tại không
        if check_user_exists(full_name):
            print("Tên của bạn đã tồn tại trong hệ thống.")
        else:
            add_user(full_name)
            print("Thông tin của bạn đã được lưu thành công.")

        # Người dùng nhập 'show' để xem thông tin hoặc nhấn Enter để thoát
        action = input("Nhập 'show' để xem số lần sử dụng và thời gian còn lại, hoặc nhấn Enter để thoát: ")
        if action == "show":
            # Cập nhật và hiển thị thông tin số lần sử dụng và thời gian còn lại
            starts, used_time = update_limits(start_time)
            remaining_starts = MAX_STARTS - starts
            remaining_time_overall = TIME_LIMIT - used_time

            remaining_minutes = remaining_time_overall // 60
            remaining_seconds = remaining_time_overall % 60
            print(f"Số lần sử dụng còn lại: {remaining_starts}. Thời gian còn lại: {remaining_minutes} phút {remaining_seconds} giây.")
        
        # Sau khi hiển thị thông tin, thoát chương trình luôn
        program_running.clear()

    except KeyboardInterrupt:
        print("\nChương trình bị dừng bởi người dùng.")
        program_running.clear()

    # Chờ bộ đếm thời gian kết thúc
    timer_thread.join()

    # Nếu hết thời gian hoặc số lần sử dụng
    starts, used_time = update_limits(start_time)
    if used_time >= TIME_LIMIT or starts >= MAX_STARTS:
        print("Bạn đã hết thời gian hoặc số lần sử dụng. Vui lòng mua phiên bản đầy đủ hoặc gỡ cài đặt chương trình.")
        sys.exit(1)

if __name__ == "__main__":
    main()

