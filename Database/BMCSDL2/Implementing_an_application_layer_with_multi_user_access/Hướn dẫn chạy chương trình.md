# 1. Thiết lập môi trường
## 1.1 Tạo và kích hoạt môi trường ảo (khuyến nghị):

```bash
sudo apt install python3.10-venv
````

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate    # Trên MacOS/Linux
venv\Scripts\activate       # Trên Windows
```

## 1.2 Cài đặt các thư viện cần thiết: Dựa vào tệp requirements.txt, cài đặt tất cả các thư viện bằng lệnh:

```bash
pip install -r requirements.txt
```

