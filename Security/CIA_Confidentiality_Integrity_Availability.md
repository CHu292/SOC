# Tam Giác Bảo Mật CIA

### Mục lục

1. [3 yếu tố bảo mật “tính bảo mật”, “tính toàn vẹn” và “tính sẵn sàng” là gì?](#3-yếu-tố-bảo-mật-tính-bảo-mật-tính-toàn-vẹn-và-tính-sẵn-sàng-là-gì)
2. [Tính bảo mật: Confidentiality là gì?](#tính-bảo-mật-confidentiality-là-gì)
   - [Tài sản thông tin cần được bảo mật](#tài-sản-thông-tin-cần-được-bảo-mật)
     - [Thông tin cá nhân](#thông-tin-cá-nhân)
     - [Bí mật kinh doanh](#bí-mật-kinh-doanh)
     - [Thông tin hợp đồng](#thông-tin-hợp-đồng)
     - [Thông tin tài chính](#thông-tin-tài-chính)
     - [Thông tin pháp lý và luật định](#thông-tin-pháp-lý-và-luật-định)
     - [Thông tin bảo mật](#thông-tin-bảo-mật)
   - [Các biện pháp cụ thể](#các-biện-pháp-cụ-thể)
     - [Kiểm soát truy cập](#kiểm-soát-truy-cập)
     - [Mã hóa](#mã-hóa)
     - [Phân loại dữ liệu](#phân-loại-dữ-liệu)
     - [Giáo dục và đào tạo về an toàn thông tin](#giáo-dục-và-đào-tạo-về-an-toàn-thông-tin)
     - [An ninh vật lý](#an-ninh-vật-lý)
     - [Thiết lập chính sách và quy trình an toàn thông tin](#thiết-lập-chính-sách-và-quy-trình-an-toàn-thông-tin)
     - [Kiểm tra và đánh giá bảo mật](#kiểm-tra-và-đánh-giá-bảo-mật)
3. [Tính toàn vẹn: Integrity là gì?](#tính-toàn-vẹn-integrity-là-gì)
   - [Tài sản thông tin cần duy trì tính toàn vẹn](#tài-sản-thông-tin-cần-duy-trì-tính-toàn-vẹn)
     - [Thông tin tài chính](#thông-tin-tài-chính-1)
     - [Thông tin khách hàng](#thông-tin-khách-hàng)
     - [Thông tin nhân viên](#thông-tin-nhân-viên)
     - [Thông tin sản phẩm và dịch vụ](#thông-tin-sản-phẩm-và-dịch-vụ)
     - [Thông tin liên quan đến pháp luật và quy định](#thông-tin-liên-quan-đến-pháp-luật-và-quy-định)
     - [Tài sản trí tuệ](#tài-sản-trí-tuệ)
     - [Thông tin kế toán và tài chính](#thông-tin-kế-toán-và-tài-chính)
   - [Các biện pháp cụ thể](#các-biện-pháp-cụ-thể-1)
     - [Kiểm soát truy cập](#kiểm-soát-truy-cập-1)
     - [Sao lưu dữ liệu](#sao-lưu-dữ-liệu)
     - [Tổng kiểm và hàm băm](#tổng-kiểm-và-hàm-băm)
     - [Xác minh nhập và chỉnh sửa dữ liệu](#xác-minh-nhập-và-chỉnh-sửa-dữ-liệu)
4. [Tính sẵn sàng: Availability là gì?](#tính-sẵn-sàng-availability-là-gì)
   - [Tài sản thông tin cần duy trì tính sẵn sàng](#tài-sản-thông-tin-cần-duy-trì-tính-sẵn-sàng)
     - [Cơ sở dữ liệu khách hàng](#cơ-sở-dữ-liệu-khách-hàng)
     - [Thông tin tài chính](#thông-tin-tài-chính-2)
     - [Tài liệu nội bộ](#tài-liệu-nội-bộ)
     - [Hệ thống và ứng dụng](#hệ-thống-và-ứng-dụng)
     - [Email](#email)
   - [Các biện pháp cụ thể](#các-biện-pháp-cụ-thể-2)
     - [Dự phòng](#dự-phòng)
     - [Sao lưu](#sao-lưu)
     - [Bảo trì](#bảo-trì)
     - [Giám sát](#giám-sát)
5. [Cách phân loại mức độ của CIA (Confidentiality, Integrity, Availability)](#cách-phân-loại-mức-độ-của-cia-confidentiality-integrity-availability)
6. [Cách áp dụng CIA vào hoạt động kinh doanh](#cách-áp-dụng-cia-vào-hoạt-động-kinh-doanh)
   - [Tính bảo mật (Confidentiality)](#tính-bảo-mật-confidentiality)
   - [Tính toàn vẹn (Integrity)](#tính-toàn-vẹn-integrity)
   - [Tính sẵn sàng (Availability)](#tính-sẵn-sàng-availability)
7. [Sự cân bằng quan trọng giữa tính bảo mật, tính toàn vẹn và tính sẵn sàng](#sự-cân-bằng-quan-trọng-giữa-tính-bảo-mật-tính-toàn-vẹn-và-tính-sẵn-sàng)
8. [Bốn tính chất mới trong khái niệm an ninh thông tin](#bốn-tính-chất-mới-trong-khái-niệm-an-ninh-thông-tin)
   - [Tính xác thực (Authenticity)](#tính-xác-thực-authenticity)
   - [Tính đáng tin cậy (Reliability)](#tính-đáng-tin-cậy-reliability)
   - [Tính trách nhiệm (Accountability)](#tính-trách-nhiệm-accountability)
   - [Tính không thể chối bỏ (Non-repudiation)](#tính-không-thể-chối-bỏ-non-repudiation)


### Nội dung

<h1 id="3-yếu-tố-bảo-mật-tính-bảo-mật-tính-toàn-vẹn-và-tính-sẵn-sàng-là-gì">Phần 1: 3 yếu tố bảo mật “tính bảo mật”, “tính toàn vẹn” và “tính sẵn sàng” là gì?</h1>

SMS (ISO 27001) yêu cầu xây dựng một hệ thống có thể duy trì 3 yếu tố “tính bảo mật”, “tính toàn vẹn” và “tính sẵn sàng”. Đây là 3 yếu tố ngăn chặn việc làm sai lệch, thất thoát, mất mát, hư hỏng các thông tin quan trọng và xử lý thông tin một cách an toàn.

Ba yếu tố bảo mật, toàn vẹn và sẵn sàng thường được gọi bằng từ viết tắt tiếng Anh là “CIA”.

- “Tính bảo mật”: confidentiality
- “Tính toàn vẹn”: integrity
- “Tính sẵn sàng”: availability

<h1 id="tính-bảo-mật-confidentiality-là-gì">Phần 2: Tính bảo mật: Confidentiality là gì?</h1>

Tính bảo mật tức là, đảm bảo thông tin chỉ được phép truy cập bởi những đối tượng được cấp phép, hay nói cách khác, là việc đảm bảo thông tin được bảo vệ sao cho không bị tiết lộ cho những đối tượng không được cấp phép.

Tính bí mật của thông tin có thể đạt được bằng cách sử dụng các biện pháp như xác thực, giới hạn truy cập và mã hóa.

Nếu tính bảo mật của thông tin được đảm bảo, thì có thể ngăn chặn sự xâm nhập từ bên ngoài và giảm thiểu khả năng rò rỉ, mất mát, thất thoát hoặc hư hỏng thông tin.

<h2 id="tài-sản-thông-tin-cần-được-bảo-mật">2.1 Tài sản thông tin cần được bảo mật</h2>


### Thông tin cá nhân
Thông tin cá nhân của khách hàng và nhân viên, bao gồm địa chỉ, số điện thoại, địa chỉ email và thông tin nhận dạng cá nhân khác, phải được bảo vệ dưới góc độ quyền riêng tư.

### Bí mật kinh doanh
Thông tin liên quan đến bí mật thương mại cần được bảo vệ, bao gồm:
- Nghiên cứu và phát triển
- Thông tin kỹ thuật
- Chiến lược kinh doanh
- Thông tin về sản phẩm và dịch vụ mới

### Thông tin hợp đồng
Các thông tin liên quan đến hợp đồng cần được bảo mật, bao gồm:
- Hợp đồng với đối tác kinh doanh và công ty đối tác
- Thông tin dự án trong quá trình đàm phán kinh doanh

### Thông tin tài chính
Thông tin liên quan đến tình hình tài chính của một tổ chức cần được giữ bí mật, bao gồm:
- Dữ liệu kế toán
- Ngân sách và dự toán
- Kế hoạch tài trợ

### Thông tin pháp lý và luật định
Thông tin cần bảo vệ bao gồm các yêu cầu pháp lý và luật định, chẳng hạn như:
- Tài liệu pháp lý
- Thông tin kiện tụng
- Báo cáo kiểm toán

### Thông tin bảo mật
Tính bảo mật rất quan trọng đối với các thông tin sau:
- Sơ đồ cấu hình mạng
- Thông tin lỗ hổng hệ thống
- Mật khẩu
