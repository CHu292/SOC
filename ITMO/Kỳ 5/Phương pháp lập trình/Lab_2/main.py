import os
import time
import hashlib
import threading
import sys

# Tên tệp chứa thông tin người dùng
USER_FILE = "user_data.txt"
LIMIT_FILE = "limit_data.txt"
MAX_STARTS = 5
TIME_LIMIT = 180  # 3 phút (tính theo giây)

def hash_string(s):
    """Hàm băm chuỗi để lưu trữ băm thay vì thông tin gốc."""
    return hashlib.sha256(s.encode()).hexdigest()

def check_user_exists(full_name):
    """Kiểm tra xem người dùng có tồn tại trong tệp không."""
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as file:
            for line in file:
                if hash_string(full_name) == line.strip():
                    return True
    return False

def add_user(full_name):
    """Thêm người dùng mới vào tệp."""
    with open(USER_FILE, "a") as file:
        file.write(hash_string(full_name) + "\n")

def check_limits():
    """Kiểm tra giới hạn sử dụng: số lần khởi động hoặc thời gian."""
    if not os.path.exists(LIMIT_FILE):
        with open(LIMIT_FILE, "w") as file:
            file.write(f"starts:0\ntime:0\n")

    with open(LIMIT_FILE, "r") as file:
        data = file.readlines()
        starts = int(data[0].split(":")[1].strip())
        used_time = int(data[1].split(":")[1].strip())

    # Kiểm tra giới hạn khởi động
    if starts >= MAX_STARTS:
        print("Bạn đã đạt đến giới hạn khởi động. Vui lòng mua phiên bản đầy đủ hoặc gỡ cài đặt chương trình.")
        return False

    # Kiểm tra giới hạn thời gian
    if used_time >= TIME_LIMIT:
        print("Bạn đã đạt đến giới hạn thời gian sử dụng. Vui lòng mua phiên bản đầy đủ hoặc gỡ cài đặt chương trình.")
        return False

    return True

def update_limits(start_time, end_time):
    """Cập nhật số lần khởi động và thời gian sử dụng."""
    with open(LIMIT_FILE, "r") as file:
        data = file.readlines()
        starts = int(data[0].split(":")[1].strip()) + 1
        used_time = int(data[1].split(":")[1].strip()) + (end_time - start_time)

    with open(LIMIT_FILE, "w") as file:
        file.write(f"starts:{starts}\ntime:{used_time}\n")
    return starts, used_time

def countdown_timer(remaining_time, program_running):
    """Đếm ngược thời gian."""
    while remaining_time > 0 and program_running.is_set():
        time.sleep(1)
        remaining_time -= 1
    if remaining_time <= 0 and program_running.is_set():
        print("\nThời gian sử dụng đã kết thúc. Nhập 1 để xem tất cả thông báo.")
        program_running.clear()

def uninstall_program():
    """Hàm gỡ cài đặt chương trình."""
    try:
        if os.path.exists(USER_FILE):
            os.remove(USER_FILE)
        if os.path.exists(LIMIT_FILE):
            os.remove(LIMIT_FILE)
        # Nếu chương trình được đóng gói dưới dạng .exe, việc gỡ bỏ tệp có thể phức tạp hơn
        print("Chương trình đã được gỡ cài đặt thành công.")
        sys.exit()
    except Exception as e:
        print(f"Lỗi khi gỡ cài đặt: {e}")

def main():
    # Kiểm tra giới hạn trước khi cho phép sử dụng chương trình
    if not check_limits():
        user_choice = input("Nhập 'uninstall' để gỡ cài đặt chương trình hoặc nhấn Enter để thoát: ").strip().lower()
        if user_choice == 'uninstall':
            uninstall_program()
        return

    # Nhập họ tên đầy đủ
    full_name = input("Vui lòng nhập họ tên đầy đủ của bạn: ").strip()

    # Kiểm tra xem họ tên đầy đủ đã tồn tại hay chưa
    if check_user_exists(full_name):
        print("Họ tên của bạn đã tồn tại trong hệ thống.")
    else:
        add_user(full_name)
        print("Thông tin của bạn đã được lưu thành công.")

    # Bắt đầu tính thời gian sử dụng chương trình
    start_time = time.time()

    # Tạo cờ để kiểm tra trạng thái chương trình
    program_running = threading.Event()
    program_running.set()

    # Tạo và chạy bộ đếm thời gian
    remaining_time = TIME_LIMIT
    timer_thread = threading.Thread(target=countdown_timer, args=(remaining_time, program_running))
    timer_thread.start()

    try:
        while program_running.is_set():
            user_input = input("Nhập 'show' để xem số lần sử dụng và thời gian còn lại hoặc 'exit' để thoát: ").strip().lower()
            if user_input == "show":
                # Đọc giới hạn hiện tại
                with open(LIMIT_FILE, "r") as file:
                    data = file.readlines()
                    starts = int(data[0].split(":")[1].strip())
                    used_time = int(data[1].split(":")[1].strip()) + (time.time() - start_time)
                remaining_starts = MAX_STARTS - starts
                remaining_time_overall = TIME_LIMIT - used_time
                if remaining_time_overall > 0:
                    remaining_minutes = remaining_time_overall // 60
                    remaining_seconds = remaining_time_overall % 60
                    print(f"Bạn còn {remaining_starts} lần khởi động và còn {int(remaining_minutes)} phút {int(remaining_seconds)} giây.")
                else:
                    print("Bạn đã sử dụng hết thời gian.")
                program_running.clear()
            elif user_input == "exit":
                program_running.clear()
            else:
                print("Lệnh không hợp lệ. Vui lòng thử lại.")
    except KeyboardInterrupt:
        print("\nChương trình đã bị dừng bởi người dùng.")
        program_running.clear()

    # Đợi bộ đếm thời gian kết thúc
    timer_thread.join()

    # Cập nhật giới hạn sử dụng
    end_time = time.time()
    starts, used_time = update_limits(start_time, end_time - start_time)

    # Tính toán thời gian còn lại
    remaining_starts = MAX_STARTS - starts
    remaining_time_overall = TIME_LIMIT - used_time

    if remaining_time_overall > 0:
        remaining_minutes = remaining_time_overall // 60
        remaining_seconds = remaining_time_overall % 60
        print(f"Bạn còn {remaining_starts} lần khởi động và {int(remaining_minutes)} phút {int(remaining_seconds)} giây còn lại.")
    else:
        print("Bạn đã sử dụng hết thời gian. Vui lòng mua phiên bản đầy đủ hoặc gỡ cài đặt chương trình.")

    print("Cảm ơn bạn đã sử dụng chương trình.")

    # Kiểm tra xem đã đạt giới hạn chưa sau khi cập nhật
    if starts >= MAX_STARTS or used_time >= TIME_LIMIT:
        user_choice = input("Nhập 'uninstall' để gỡ cài đặt chương trình hoặc nhấn Enter để thoát: ").strip().lower()
        if user_choice == 'uninstall':
            uninstall_program()

if __name__ == "__main__":
    main()
    input("Nhấn Enter để đóng chương trình.")
