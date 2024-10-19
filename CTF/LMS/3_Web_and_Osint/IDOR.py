import requests

# URL cơ bản
base_url = "https://d971719e-b86d-4cea-b332-1fbc5fa2adf6-idor-webapp.web.lms.itmo.xyz/user/"

# Phạm vi ID bạn muốn kiểm tra
start_id = 1
end_id = 50  # Bạn có thể thay đổi giới hạn ID theo nhu cầu

for user_id in range(start_id, end_id + 1):
    # Tạo URL với ID hiện tại
    url = f"{base_url}{user_id}"
    
    try:
        # Gửi yêu cầu GET
        response = requests.get(url)
        
        # Kiểm tra mã trạng thái phản hồi
        if response.status_code == 200:
            print(f"User ID: {user_id}")
            print(response.text)  # In ra nội dung phản hồi
            print("-" * 50)  # Dấu phân cách giữa các phản hồi
        else:
            print(f"User ID: {user_id} - Không tìm thấy (Mã trạng thái: {response.status_code})")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi truy cập {url}: {e}")

