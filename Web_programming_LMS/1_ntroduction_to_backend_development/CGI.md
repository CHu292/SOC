# CGI (Common Gateway Interface)
## CGI là gì ?
Common Gateway Interface hoặc CGI là một chuẩn cho các chương trình gateway để giao tiếp thông tin với các server như là HTTP server
Web browsing
Để hiểu hơn về khái niệm của CGI, ta hãy xem chuyện gì xảy ra khi click vào một hyper link trong trình duyệt ở một trang web hoặc một URL.
Trình duyệt sẽ kết nối với HTTP web server và yêu cầu URL, filename...
Web server sẽ phân tích cú pháp URL và tìm kiếm filename. Nếu nó tìm thấy file đó sau đó gửi chúng quay ngược lại cho trình duyệt, nếu không thì chúng sẽ gửi một thông báo lỗi mô tả request đến file bị sai
Trình duyệt nhận phản hồi từ web serrver và hiển thị file nhận được hoặc nhận một thông báo lỗi
Tuy nhiên, có thể cài đặt máy chủ HTTP để bất cứ khi nào một tệp trong thư mục chỉ định được request không được gửi trở lại, thay vào đó nó được thực hiện như một chương trình và bất kì output nào của chương trình đó được gửi lại để trình duyệt hiển thị. Chức năng này được gọi là Common Gateway Interface hay CGI và chương trình đó được gọi là CGI scripts. Các chương trình này có thể là Python Script, Perl script, C or C++.
