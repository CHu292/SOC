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
