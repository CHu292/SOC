# Ping là gì ?

- Ping (viết tắt của Packet Internet Grouper ). là lệnh cơ bản để kiểm tra xem thiết bị của bạn có truy cập đến địa chỉ cần kiểm tra và mất bao lâu để yêu cầu nhận được phản hồi. Đồng thời khi sử dụng lệnh ping với tên miền, tương đương với việc sẽ kiểm tra được địa chỉ IP thực của trang web đó.  Ping còn được sử dụng để kiểm tra xem thời gian phản hồi từ thiết bị của bạn đến các nhà cung cấp dịch vụ Internet lớn như:
  - FPT: ```ping 210.245.31.130```
  - Viettel: ```ping 203.113.131.1```
  - VNN: ```ping 203.162.4.190```

Ví dụ:

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Terminology/igmae/Ping/ping.png" alt="Ping" width="1000">
</p>

```64 bytes from lt-in-f102.1e100.net (108.177.14.102): icmp_seq=1 ttl=109 time=6.17 ms```

- Phản hồi từ IP 108.177.14.102, gói tin dung lượng 64 bytes, thời gian phản hồi là 6.17 mili giây
- Vậy thế nào là thời gian phản hồi tốt khi kiểm tra lệnh ping :
  - <30 ms - ping tuyệt vời ; hầu như không có độ trễ, rất tốt để xử lý các yêu cầu cần phản hồi nhanh như chơi game online (phản hồi theo thời gian thực).
  - 30 đến 50 ms - ping trung bình; phản hồi trang web vẫn rất nhanh.
  - 50 đến 100 ms - thời gian ping hơi chậm;  web bắt đầu phản hồi chậm khi  truy cập.
  - 100 ms đến 500 ms - ping chậm; ảnh hưởng rõ ràng hơn đến trình duyệt web, load web rất lâu.
  - > 500 ms - ping nửa giây trở lên sẽ thêm độ trễ đáng chú ý cho tất cả các yêu cầu; thường xảy ra khi nguồn và đích ở các khu vực khác nhau trên thế giới.
