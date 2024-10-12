#!/bin/bash

# Tạo thư mục để lưu trữ dữ liệu
INSTALL_DIR="$HOME/.simple_program"
if [ ! -d "$INSTALL_DIR" ]; then
    mkdir "$INSTALL_DIR"
    echo "Thông tin chương trình sẽ được lưu trong $INSTALL_DIR"
else
    echo "Chương trình đã được cài đặt trước đó."
fi

# Tạo tệp lưu thông tin giới hạn (thời gian và số lần khởi chạy)
echo "start_limit=5" > "$INSTALL_DIR/limits.txt"
echo "start_count=0" >> "$INSTALL_DIR/limits.txt"
echo "install_time=$(date +%s)" >> "$INSTALL_DIR/limits.txt"
echo "time_limit=180" >> "$INSTALL_DIR/limits.txt"  # Thời gian tính bằng giây

# Đăng ký chương trình
ln -s "$PWD/simple_program.py" /usr/local/bin/simple_program
echo "Chương trình đã được cài đặt thành công. Chạy: 'simple_program'"
