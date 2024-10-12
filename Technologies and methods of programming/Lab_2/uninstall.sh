#!/bin/bash

# Xóa các tệp chương trình
INSTALL_DIR="$HOME/.simple_program"
if [ -d "$INSTALL_DIR" ]; then
    rm -rf "$INSTALL_DIR"
    echo "Dữ liệu chương trình đã bị xóa."
fi

# Xóa liên kết tượng trưng của chương trình
if [ -L "/usr/local/bin/simple_program" ]; then
    rm /usr/local/bin/simple_program
    echo "Chương trình đã bị xóa khỏi hệ thống."
else
    echo "Chương trình chưa được đăng ký."
fi
