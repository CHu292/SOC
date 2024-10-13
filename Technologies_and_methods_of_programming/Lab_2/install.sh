#!/bin/bash

# Thư mục cài đặt là thư mục hiện tại nơi tập lệnh được chạy
INSTALL_DIR="$PWD"
INSTALL_FLAG="$INSTALL_DIR/installed.flag"

# Kiểm tra xem chương trình đã được cài đặt chưa
if [ -f "$INSTALL_FLAG" ]; then
    echo "Chương trình đã được cài đặt trước đó. Vui lòng gỡ cài đặt trước khi cài đặt lại."
    exit 1
fi

# Tạo tệp cờ để chỉ định rằng chương trình đã được cài đặt
touch "$INSTALL_FLAG"

# Tạo tệp cần thiết nếu không tồn tại
if [ ! -f "$INSTALL_DIR/user_data.txt" ]; then
    touch "$INSTALL_DIR/user_data.txt"
    echo "Tệp user_data.txt đã được tạo."
else
    echo "Tệp user_data.txt đã tồn tại."
fi

if [ ! -f "$INSTALL_DIR/limit_data.txt" ]; then
    echo "starts:0" > "$INSTALL_DIR/limit_data.txt"
    echo "time:0" >> "$INSTALL_DIR/limit_data.txt"
    echo "Tệp limit_data.txt đã được tạo."
else
    echo "Tệp limit_data.txt đã tồn tại."
fi

# Hướng dẫn sử dụng
echo "Chương trình đã được cài đặt trong thư mục hiện tại. Để chạy chương trình, sử dụng: './simple_program.py'."

