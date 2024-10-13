import math

def gcd(a, b):
    """Hàm tính UCLN của hai số a và b sử dụng thuật toán Euclid."""
    print(f"Tính GCD giữa {a} và {b}...")
    while b != 0:
        print(f"{a} mod {b} = {a % b}")
        a, b = b, a % b
    print(f"GCD là {a}")
    return a

def parse_expression(exp):
    """Hàm phân tích và tính giá trị của biểu thức."""
    try:
        result = eval(exp)
        print(f"Biểu thức '{exp}' cho kết quả: {result}")
        return result
    except Exception as e:
        print(f"Lỗi khi phân tích biểu thức '{exp}': {e}")
        return None

def main():
    # Nhập vào một chuỗi biểu thức từ người dùng
    numbers = input("Nhập các biểu thức (cách nhau bởi dấu phẩy, ví dụ: 2^3, 3*2, 4.5 + 1): ")
    
    # Chia tách các biểu thức và chuyển đổi thành danh sách số
    num_list = []
    for num in numbers.split(','):
        value = parse_expression(num.strip())
        if value is not None:
            num_list.append(value)
    
    # Khởi tạo UCLN với số đầu tiên
    current_gcd = num_list[0]
    
    # Tính UCLN cho tất cả các số
    for num in num_list[1:]:
        current_gcd = gcd(int(current_gcd), int(num))  # Chuyển đổi về số nguyên trước khi tính UCLN
    
    print(f"UCLN của các biểu thức {numbers} là: {current_gcd}")

if __name__ == "__main__":
    main()
