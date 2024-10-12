# 4. Mô hình thực thể-liên kết: Các khái niệm

## 4.1 Mô hình thực thể-liên kết là gì

- Mô hình thực thể-liên kết (Entity-Relationship, viết tắt ER) là một mô hình dữ liệu mức quan niệm nhằm mô tả các đối tượng trong thế giới thực và quan hệ giữa chúng 
- Thực thể là một đối tượng trong thế giới thực, có sự tồn tại độc lập: 
  - Thực thể cụ thể: có thể cảm nhận bằng giác quan, ví dụ xe đạp, bàn, ghế 
  - Thực thể trừu tượng: có thể nhận biết bằng nhận thức

## 4.2  Thuộc tính của thực thể

- Mỗi một thực thể có các thuộc tính, đó là các đặc trưng cụ thể mô tả thực thể đó; chẳng hạn màu sơn của xe ô tô, số nhân viên một công ty là các thuộc tính 
- Phân loại các thuộc tính: 
  - Thuộc tính đơn là thuộc tính không thể phân chia ra được thành các thành phần nhỏ hơn 
  - Thuộc tính phức hợp là thuộc tính có thể phân chia được thành các thành phần nhỏ hơn, biểu diễn các thuộc tính cơ bản hơn với các ý nghĩa độc lập 
  - Những thuộc tính có giá trị duy nhất cho một thực thể cụ thể gọi là các thuộc tính đơn trị 
  - Một thuộc tính có thể có một tập giá trị cho cùng một thực thể: thuộc tính đa trị
  - Ví dụ:
      - Một thực thể là công ty, công ty này có thuộc tính là địa chỉ. Vậy thuộc tính địa chỉ là thuộc tính đa trị, vì một công ty có thể có nhiều chi nhánh, có nhiều địa chỉ khác nhau. 
      - Tiếp theo là thuộc tính tên công ty là thuộc tính đơn trị, vì công ty chỉ có thể có một tên duy nhất.
  - Thuộc tính có giá trị có thể tính được thông qua giá trị của các thuộc tính khác gọi là thuộc tính suy diễn được 
  - ví dụ: Đối với thực thể người, thuộc tính tuổi có thể suy ra từ thuộc tính ngày tháng năm sinh. 
  - Trong một số trường hợp, một số thuộc tính của một thực thể cụ thể không xác định được giá trị. Trong trường hợp như vậy, ta phải tạo ra một giá trị đặc biệt gọi là giá trị null. Các thuộc tính nói trên là thuộc tính có thể nhận giá trị null
  - ví dụ: thuộc tính số điện thoại của thực thể nhân viên sẽ không có giá trị đối với các nhân viên không có số điện thoại.
    
## 4.3 Thuộc tín của kiểu thực thể: Định nghĩa hình thức
