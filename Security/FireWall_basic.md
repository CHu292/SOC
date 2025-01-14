# Mục lục

1. [Tường lửa là gì?](#tường-lửa-là-gì)
2. [Tường lửa gồm có bao nhiêu loại?](#tường-lửa-gồm-có-bao-nhiêu-loại)
   - [Tường lửa Personal](#tường-lửa-personal)
   - [Network Firewalls](#network-firewalls)
3. [Cách thức hoạt động của tường lửa như thế nào?](#cách-thức-hoạt-động-của-tường-lửa-như-thế-nào)
4. [Nhiệm vụ của tường lửa (Firewall) là gì?](#nhiệm-vụ-của-tường-lửa-firewall-là-gì)
5. [Ưu và nhược điểm của tường lửa](#ưu-và-nhược-điểm-của-tường-lửa)
   - [Ưu điểm của tường lửa](#ưu-điểm-của-tường-lửa)
   - [Nhược điểm của tường lửa](#nhược-điểm-của-tường-lửa)
6. [Những tùy chọn khi triển khai Firewall mà bạn nên biết](#những-tùy-chọn-khi-triển-khai-firewall-mà-bạn-nên-biết)
   - [Stateful firewall (Tường lửa có trạng thái)](#stateful-firewall-tường-lửa-có-trạng-thái)
   - [Next-generation firewalls – NGFW (Tường lửa thế hệ tiếp theo)](#next-generation-firewalls-ngfw-tường-lửa-thế-hệ-tiếp-theo)
   - [Proxy-based firewall (Tường lửa dựa trên proxy)](#proxy-based-firewall-tường-lửa-dựa-trên-proxy)
   - [Web application firewall – WAF (Tường lửa ứng dụng web)](#web-application-firewall-waf-tường-lửa-ứng-dụng-web)
   - [Tường lửa phần cứng](#tường-lửa-phần-cứng)
   - [Tường lửa phần mềm](#tường-lửa-phần-mềm)
   - [Kiểm tra trạng thái tường lửa](#kiểm-tra-trạng-thái-tường-lửa)
   - [Tường lửa phát hiện và diệt virus](#tường-lửa-phát-hiện-và-diệt-virus)
   - [Kiểm tra tầng ổ bảo mật SSL](#kiểm-tra-tầng-ổ-bảo-mật-ssl)
   - [Intrusion Prevention Systems – IPS (Hệ thống phòng chống xâm nhập)](#intrusion-prevention-systems-ips-hệ-thống-phòng-chống-xâm-nhập)
   - [Theo dõi lưu lượng gửi đi (DPI)](#theo-dõi-lưu-lượng-gửi-đi-dpi)
7. [Những lỗ hổng của tường lửa](#những-lỗ-hổng-của-tường-lửa)
   - [Tấn công nội bộ](#tấn-công-nội-bộ)
   - [Tấn công từ chối dịch vụ phân tán (DDos)](#tấn-công-từ-chối-dịch-vụ-phân-tán-ddos)
   - [Các phần mềm độc hại](#các-phần-mềm-độc-hại)
   - [Cấu hình tường lửa kém, thiếu cập nhật](#cấu-hình-tường-lửa-kém-thiếu-cập-nhật)

---

# Nội dung

<h1 id="tường-lửa-là-gì">Phần 1: Tường lửa là gì?</h1>

<h1 id="tường-lửa-gồm-có-bao-nhiêu-loại">Phần 2: Tường lửa gồm có bao nhiêu loại?</h1>
<h2 id="tường-lửa-personal">2.1. Tường lửa Personal</h2>
<h2 id="network-firewalls">2.2. Network Firewalls</h2>

<h1 id="cách-thức-hoạt-động-của-tường-lửa-như-thế-nào">Phần 3: Cách thức hoạt động của tường lửa như thế nào?</h1>

<h1 id="nhiệm-vụ-của-tường-lửa-firewall-là-gì">Phần 4: Nhiệm vụ của tường lửa (Firewall) là gì?</h1>

<h1 id="ưu-và-nhược-điểm-của-tường-lửa">Phần 5: Ưu và nhược điểm của tường lửa</h1>
<h2 id="ưu-điểm-của-tường-lửa">5.1. Ưu điểm của tường lửa</h2>
<h2 id="nhược-điểm-của-tường-lửa">5.2. Nhược điểm của tường lửa</h2>

<h1 id="những-tùy-chọn-khi-triển-khai-firewall-mà-bạn-nên-biết">Phần 6: Những tùy chọn khi triển khai Firewall mà bạn nên biết</h1>
<h2 id="stateful-firewall-tường-lửa-có-trạng-thái">6.1. Stateful firewall (Tường lửa có trạng thái)</h2>
<h2 id="next-generation-firewalls-ngfw-tường-lửa-thế-hệ-tiếp-theo">6.2. Next-generation firewalls – NGFW (Tường lửa thế hệ tiếp theo)</h2>
<h2 id="proxy-based-firewall-tường-lửa-dựa-trên-proxy">6.3. Proxy-based firewall (Tường lửa dựa trên proxy)</h2>
<h2 id="web-application-firewall-waf-tường-lửa-ứng-dụng-web">6.4. Web application firewall – WAF (Tường lửa ứng dụng web)</h2>
<h2 id="tường-lửa-phần-cứng">6.5. Tường lửa phần cứng</h2>
<h2 id="tường-lửa-phần-mềm">6.6. Tường lửa phần mềm</h2>
<h2 id="kiểm-tra-trạng-thái-tường-lửa">6.7. Kiểm tra trạng thái tường lửa</h2>
<h2 id="tường-lửa-phát-hiện-và-diệt-virus">6.8. Tường lửa phát hiện và diệt virus</h2>
<h2 id="kiểm-tra-tầng-ổ-bảo-mật-ssl">6.9. Kiểm tra tầng ổ bảo mật SSL</h2>
<h2 id="intrusion-prevention-systems-ips-hệ-thống-phòng-chống-xâm-nhập">6.10. Intrusion Prevention Systems – IPS (Hệ thống phòng chống xâm nhập)</h2>
<h2 id="theo-dõi-lưu-lượng-gửi-đi-dpi">6.11. Theo dõi lưu lượng gửi đi (DPI)</h2>

<h1 id="những-lỗ-hổng-của-tường-lửa">Phần 7: Những lỗ hổng của tường lửa</h1>
<h2 id="tấn-công-nội-bộ">7.1. Tấn công nội bộ</h2>
<h2 id="tấn-công-từ-chối-dịch-vụ-phân-tán-ddos">7.2. Tấn công từ chối dịch vụ phân tán (DDos)</h2>
<h2 id="các-phần-mềm-độc-hại">7.3. Các phần mềm độc hại</h2>
<h2 id="cấu-hình-tường-lửa-kém-thiếu-cập-nhật">7.4. Cấu hình tường lửa kém, thiếu cập nhật</h2>
