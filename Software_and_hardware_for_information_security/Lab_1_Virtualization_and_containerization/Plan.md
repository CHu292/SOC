# Khái niệm
- Ảo hóa là việc tạo ra một môi trường điện toán trong đó các máy ảo khác nhau có thể chạy trên cùng một tài nguyên vật lý, hoàn toàn tách biệt với nhau. Nói cách khác, đây là khả năng tạo ra phần mềm tương tự của các đối tượng vật lý khác nhau, chẳng hạn như máy tính, bộ lưu trữ dữ liệu, mạng, máy chủ và ứng dụng. Một ví dụ về điều này là việc sử dụng nhiều hệ điều hành trên một thiết bị, với tất cả các hệ điều hành và quy trình tính toán của chúng tách biệt với nhau.
- Containerization là một phương pháp trong đó mã chương trình được đóng gói thành một tệp thực thi duy nhất cùng với các thư viện và phần phụ thuộc để đảm bảo mã chương trình chạy chính xác. Những tập tin như vậy được gọi là container. Các container có thể được triển khai trong các môi trường khác nhau và được quản lý ở đó. Nếu mã được phát triển trong một môi trường điện toán cụ thể (ví dụ: khi được chuyển sang máy chủ mới), các lỗi liên quan đến sự tinh tế trong cấu hình thường xảy ra. Với việc container hóa, những vấn đề như vậy sẽ ít hơn nhiều. Xét cho cùng, vùng chứa không phụ thuộc vào cài đặt của hệ điều hành chính và có thể chạy trên bất kỳ nền tảng nào hoặc trên đám mây.
# Thực hiện

## 1. Lựa chọn công nghệ ảo hóa/containerization
Trong bài thực hành này, chúng tôi đã chọn công nghệ ảo hóa. Phần mềm ảo hóa được chọn là Oracle VM VirtualBox. Hệ điều hành khách được chọn là Windows 7.

## 2. Nghiên cứu các cơ chế bảo vệ của công nghệ đã chọn
- Khi đánh giá việc tuân thủ các yêu cầu pháp luật, chúng tôi đã dựa trên các khía cạnh bảo mật thông tin, được phân loại theo các đối tượng bảo vệ và mô tả trong Điều 6 của tiêu chuẩn GOST R 56938-2016 "Bảo vệ thông tin khi sử dụng công nghệ ảo hóa" 

# Mục 6: Các đặc điểm bảo vệ thông tin khi sử dụng công nghệ ảo hóa

- Việc bảo vệ thông tin được xử lý trong hệ thống thông tin (IS) được xây dựng bằng cách sử dụng công nghệ ảo hóa được đảm bảo thông qua việc tuân thủ các yêu cầu về các biện pháp bảo vệ thông tin (ZIS). Hệ thống thông tin điển hình này được trình bày trong Phụ lục B. Nhìn chung, các biện pháp bảo vệ tương tự như các biện pháp được áp dụng trong IS không sử dụng công nghệ ảo hóa. Tuy nhiên, dưới đây là các biện pháp bảo vệ thông tin đặc thù cần áp dụng khi sử dụng công nghệ ảo hóa.
- Các biện pháp bảo vệ thông tin được chia thành các nhóm khác nhau tùy thuộc vào đối tượng bảo vệ.
- Vì tính bảo mật của thông tin được xác định bởi các yêu cầu bảo vệ, mức độ và chiều sâu của nó thay đổi tùy theo lớp bảo mật của IS, bao gồm cả khi sử dụng công nghệ ảo hóa. Trong tiêu chuẩn này, đối với mỗi đối tượng bảo vệ, một tập hợp các biện pháp bảo vệ thông tin tương ứng với lớp bảo mật cao nhất khỏi truy cập trái phép (NSD) được cung cấp.
- Các biện pháp bảo vệ thông tin cần được lựa chọn dựa trên các mối đe dọa an ninh, đặc điểm sử dụng của các đối tượng bảo vệ, và các quy định pháp luật hiện hành trong lĩnh vực bảo vệ thông tin. Dữ liệu tổng hợp về các mối đe dọa và các biện pháp bảo vệ thông tin được xử lý bằng công nghệ ảo hóa được nêu trong Phụ lục V.

## 6.1 Bảo vệ các phương tiện tạo và quản lý hạ tầng ảo
**Các biện pháp bảo vệ phương tiện tạo và quản lý hạ tầng ảo bao gồm:**

**Các biện pháp bảo vệ phương tiện tạo và quản lý hạ tầng ảo bao gồm:**
- Thay đổi tự động các tuyến truyền gói tin mạng giữa các thành phần của hạ tầng ảo bên trong hypervisor;
- Chặn truy cập vào các đối tượng của hạ tầng ảo đối với những người dùng không qua được quá trình xác thực;
- Phát hiện, phân tích và chặn các kênh truyền thông tin ẩn trong hạ tầng ảo để vượt qua các biện pháp bảo vệ thông tin hoặc trong các giao thức mạng được phép;
- Bảo vệ chống truy cập trái phép (НСД) đối với thông tin xác thực mà người dùng trong hạ tầng ảo nhập vào;
- Bảo vệ chống truy cập trái phép vào thông tin xác thực của người dùng được lưu trữ trong các thành phần của hạ tầng ảo;
- Xác định và xác thực người dùng khi họ truy cập cục bộ hoặc từ xa đến các đối tượng trong hạ tầng ảo;
- Xác định và xác thực người dùng khi họ cố gắng truy cập vào bảng điều khiển quản lý các thông số phần cứng;
- Kiểm soát việc nhập (xuất) thông tin vào (ra) hạ tầng ảo;
- Kiểm soát việc nhập (xuất) thông tin vào (ra) hệ thống thông tin (ИС);
- Kiểm soát truy cập của người dùng vào không gian địa chỉ cách ly trong bộ nhớ của hypervisor;
- Kiểm soát truy cập của người dùng vào không gian địa chỉ cách ly trong bộ nhớ của hệ điều hành máy chủ;
- Kiểm soát truy cập của người dùng vào các phương tiện cấu hình phần cứng ảo;
- Kiểm soát truy cập của người dùng vào các phương tiện cấu hình của hypervisor và máy ảo (VM);
- Kiểm soát truy cập của người dùng vào các phương tiện cấu hình của hệ điều hành máy chủ và/hoặc hệ điều hành khách;
- Kiểm soát quá trình khởi động hypervisor và máy ảo dựa trên các tiêu chí bảo mật được đặt ra (chế độ khởi động, loại phương tiện lưu trữ, v.v.);
- Kiểm soát quá trình khởi động hệ điều hành máy chủ và/hoặc hệ điều hành khách dựa trên các tiêu chí bảo mật được đặt ra;
- Kiểm soát việc truyền các thông báo thông tin nội bộ trong các mạng ảo của hệ điều hành máy chủ theo các đặc tính như thành phần, dung lượng, v.v.;
- Kiểm soát hoạt động của các thành phần dự phòng quan trọng của phần cứng hệ thống thông tin (ИС);
- Kiểm soát hoạt động của các thành phần dự phòng quan trọng của hạ tầng ảo;
- Kiểm soát tính toàn vẹn của các thành phần quan trọng cho hoạt động của hypervisor và máy ảo;
- Kiểm soát tính toàn vẹn của các thành phần quan trọng cho hoạt động của hệ điều hành máy chủ và hệ điều hành khách;
- Kiểm soát tính toàn vẹn của phần mềm nhúng trong phần cứng hệ thống thông tin;
- Giám sát việc sử dụng năng lực phần cứng vật lý và ảo;
- Đảm bảo khả năng kế thừa các quyền truy cập được thiết lập ở cấp quản lý cho người dùng đến các đối tượng truy cập ở cấp ảo hóa và phần cứng;
- Đảm bảo sự cô lập của các luồng dữ liệu khác nhau, được truyền và xử lý bởi các thành phần của hạ tầng ảo của hệ điều hành máy chủ;
- Đảm bảo tính xác thực của các kết nối mạng (phiên tương tác) trong hạ tầng ảo, bao gồm bảo vệ chống lại việc giả mạo thiết bị mạng và dịch vụ;
- Vô hiệu hóa các giao thức mạng không sử dụng bởi các thành phần của hạ tầng ảo của hệ điều hành máy chủ;
- Ngăn chặn sự chậm trễ hoặc gián đoạn của các quy trình có ưu tiên cao trong hạ tầng ảo bởi các quy trình có ưu tiên thấp;
- Ngăn chặn sự chậm trễ hoặc gián đoạn của các quy trình máy ảo có ưu tiên cao bởi các quy trình máy ảo có ưu tiên thấp;
- Áp dụng quyền truy cập cá nhân đến các đối tượng cho một hoặc nhiều thành phần của hạ tầng ảo;
- Kiểm tra sự tồn tại của phần mềm độc hại trong các khu vực khởi động của các thiết bị lưu trữ thông tin kết nối với hệ thống thông tin;
- Kiểm tra sự tồn tại của phần mềm độc hại trong phần mềm nhúng của phần cứng vật lý và ảo;
- Kiểm tra sự tồn tại của phần mềm độc hại trong các tệp cấu hình của hypervisor và/hoặc máy ảo;
- Kiểm tra sự tồn tại của phần mềm độc hại trong các tệp cấu hình của hệ điều hành máy chủ và hệ điều hành khách;
- Kiểm tra sự tồn tại của phần mềm độc hại trong các tệp hình ảnh của phần mềm ảo hóa và máy ảo, cũng như các tệp hình ảnh được sử dụng để vận hành hệ thống tệp ảo;
- Kiểm tra bộ nhớ tạm thời và hệ thống tệp của hypervisor và/hoặc máy ảo để tìm phần mềm độc hại;
- Kiểm tra bộ nhớ tạm thời và hệ thống tệp của hệ điều hành máy chủ và/hoặc hệ điều hành khách để tìm phần mềm độc hại;
- Đặt các cảm biến của hệ thống phát hiện (ngăn chặn) xâm nhập trong phần cứng ảo;
- Đặt các cảm biến của hệ thống phát hiện (ngăn chặn) xâm nhập trong hypervisor và/hoặc máy ảo;
- Đặt các cảm biến của hệ thống phát hiện (ngăn chặn) xâm nhập trong hệ điều hành máy chủ và/hoặc hệ điều hành khách;
- Ghi nhật ký và theo dõi việc khởi động (kết thúc) các thành phần của hạ tầng ảo;
- Ghi nhật ký việc truy cập của người dùng vào hypervisor và/hoặc máy ảo;
- Ghi nhật ký việc truy cập của người dùng vào hệ điều hành máy chủ và/hoặc hệ điều hành khách;
- Ghi nhật ký việc khởi động (kết thúc) hypervisor và/hoặc máy ảo, các chương trình và quy trình trong hypervisor và/hoặc máy ảo;
- Ghi nhật ký việc khởi động (kết thúc) hệ điều hành máy chủ và/hoặc hệ điều hành khách, các chương trình và quy trình trong hệ điều hành máy chủ và/hoặc hệ điều hành khách;
- Ghi nhật ký và theo dõi các thay đổi trong phần mềm và phần cứng của hệ thống thông tin trong quá trình hoạt động và/hoặc trong thời gian hệ thống bị tắt phần cứng;
- Ghi nhật ký các thay đổi về quy tắc truy cập vào phần cứng ảo;
- Ghi nhật ký các thay đổi về thành phần và cấu hình của phần cứng ảo;
- Ghi nhật ký các thay đổi về thành phần và cấu hình của máy ảo;
- Ghi nhật ký các thay đổi về phần mềm và phần cứng ảo trong hypervisor và/hoặc máy ảo;
- Ghi nhật ký các thay đổi về phần mềm và phần cứng ảo trong hệ điều hành máy chủ và/hoặc hệ điều hành khách;
- Ghi nhật ký các thay đổi về quy tắc truy cập vào thông tin hạn chế, được lưu trữ và xử lý trong hypervisor và/hoặc máy ảo;
- Ghi nhật ký các thay đổi về quy tắc truy cập vào thông tin hạn chế, được lưu trữ và xử lý trong hệ điều hành máy chủ và/hoặc hệ điều hành khách;
- Dự phòng băng thông mạng để đảm bảo tương tác ổn định giữa các thành phần của hạ tầng ảo trong hypervisor;
- Sao lưu thông tin cần bảo vệ trong hypervisor và/hoặc máy ảo, được lưu trữ trên các thiết bị lưu trữ vật lý và/hoặc ảo;
- Sao lưu thông tin cần bảo vệ trong hệ điều hành máy chủ và/hoặc hệ điều hành khách, được lưu trữ trên các thiết bị lưu trữ vật lý và/hoặc ảo;
- Sao lưu không gian đĩa vật lý và/hoặc ảo, được sử dụng để lưu trữ nhật ký sự kiện của hypervisor và/hoặc máy ảo;
- Phát hiện kịp thời sự cố của các thành phần hạ tầng ảo;
- Tạo (mô phỏng) các thành phần giả của hạ tầng ảo để phát hiện, ghi lại và phân tích các hành động của kẻ xâm nhập trong quá trình thực hiện các mối đe dọa bảo mật;
- Xóa thông tin còn sót lại sau khi xóa dữ liệu được xử lý trong hạ tầng ảo chứa thông tin hạn chế;
- Xóa thông tin còn sót lại sau khi xóa dữ liệu chứa thông tin hạn chế trong hypervisor và/hoặc máy ảo;
- Xóa thông tin còn sót lại sau khi xóa dữ liệu chứa thông tin hạn chế trong hệ điều hành máy chủ và/hoặc hệ điều hành khách;
- Xóa thông tin còn sót lại sau khi xóa các tệp chứa cấu hình phần mềm ảo hóa và phần cứng ảo;
- Quản lý quyền truy cập vào phần cứng của hệ thống thông tin, kiểm soát việc kết nối (ngắt kết nối) các thiết bị lưu trữ;
- Quản lý việc khởi động (truy cập) các thành phần phần mềm, bao gồm xác định các thành phần được khởi động, thiết lập tham số khởi động và kiểm soát việc khởi động thành phần phần mềm;
- Quản lý việc cài đặt (cài đặt) các thành phần phần mềm trong hạ tầng ảo, bao gồm xác định các thành phần cần cài đặt, thiết lập tham số cài đặt và kiểm soát việc cài đặt các thành phần phần mềm;
- Chỉ cài đặt phần mềm và/hoặc các thành phần được phép sử dụng trong hạ tầng ảo;
- Lọc lưu lượng mạng giữa các thành phần hạ tầng ảo và các mạng bên ngoài của hệ điều hành máy chủ, bao gồm cả các mạng công cộng;
- Lọc lưu lượng mạng từ/đến mỗi hệ điều hành khách.

## 6.2 Bảo vệ hệ thống tính toán ảo

**Các biện pháp bảo vệ hệ thống tính toán ảo bao gồm:**

- Chặn truy cập vào các đối tượng của hạ tầng ảo đối với những người dùng không qua được quá trình xác thực;
- Bảo vệ chống truy cập trái phép (НСД) vào thông tin xác thực do người dùng trong hạ tầng ảo nhập vào;
- Bảo vệ chống truy cập trái phép vào thông tin xác thực của người dùng được lưu trữ trong các thành phần của hạ tầng ảo;
- Xác định và xác thực người dùng khi họ truy cập cục bộ hoặc từ xa đến các đối tượng trong hạ tầng ảo;
- Kiểm soát truy cập của người dùng vào không gian địa chỉ cách ly trong bộ nhớ của hypervisor;
- Kiểm soát truy cập của người dùng vào không gian địa chỉ cách ly trong bộ nhớ của hệ điều hành máy chủ;
- Kiểm soát truy cập của người dùng vào các phương tiện cấu hình của hypervisor và máy ảo (VM);
- Kiểm soát truy cập của người dùng vào các phương tiện cấu hình của hệ điều hành máy chủ và/hoặc hệ điều hành khách;
- Kiểm soát truy cập của người dùng vào các tệp hình ảnh của phần mềm ảo hóa và máy ảo, cũng như các tệp hình ảnh được sử dụng để vận hành hệ thống tệp ảo;
- Kiểm soát quá trình khởi động hypervisor và máy ảo dựa trên các tiêu chí bảo mật được đặt ra (chế độ khởi động, loại phương tiện lưu trữ, v.v.);
- Kiểm soát quá trình khởi động hệ điều hành máy chủ và/hoặc hệ điều hành khách dựa trên các tiêu chí bảo mật được đặt ra;
- Kiểm soát tính toàn vẹn của các thành phần quan trọng cho hoạt động của hypervisor và máy ảo;
- Kiểm soát tính toàn vẹn của các thành phần quan trọng cho hoạt động của hệ điều hành máy chủ và hệ điều hành khách;
- Kiểm soát tính toàn vẹn của các tệp chứa cấu hình phần mềm ảo hóa và máy ảo;
- Kiểm soát tính toàn vẹn của các tệp hình ảnh của phần mềm ảo hóa và máy ảo, cũng như các tệp hình ảnh được sử dụng để vận hành hệ thống tệp ảo;
- Ngăn chặn sự chậm trễ hoặc gián đoạn của các quy trình máy ảo có ưu tiên cao bởi các quy trình máy ảo có ưu tiên thấp;
- Kiểm tra sự tồn tại của phần mềm độc hại trong phần mềm nhúng của phần cứng vật lý và ảo;
- Kiểm tra sự tồn tại của phần mềm độc hại trong các tệp cấu hình của hypervisor và/hoặc máy ảo;
- Kiểm tra sự tồn tại của phần mềm độc hại trong các tệp cấu hình của hệ điều hành máy chủ và hệ điều hành khách;
- Kiểm tra sự tồn tại của phần mềm độc hại trong các tệp hình ảnh của phần mềm ảo hóa và máy ảo, cũng như các tệp hình ảnh được sử dụng để vận hành hệ thống tệp ảo;
- Kiểm tra bộ nhớ tạm thời và hệ thống tệp của hypervisor và/hoặc máy ảo để tìm phần mềm độc hại;
- Kiểm tra bộ nhớ tạm thời và hệ thống tệp của hệ điều hành máy chủ và/hoặc hệ điều hành khách để tìm phần mềm độc hại;
- Đặt các cảm biến của hệ thống phát hiện (ngăn chặn) xâm nhập trong phần cứng ảo;
- Đặt các cảm biến của hệ thống phát hiện (ngăn chặn) xâm nhập trong hypervisor và/hoặc máy ảo;
- Đặt các cảm biến của hệ thống phát hiện (ngăn chặn) xâm nhập trong hệ điều hành máy chủ và/hoặc hệ điều hành khách;
- Ghi nhật ký việc truy cập của người dùng vào hypervisor và/hoặc máy ảo;
- Ghi nhật ký việc truy cập của người dùng vào hệ điều hành máy chủ và/hoặc hệ điều hành khách;
- Ghi nhật ký việc khởi động (kết thúc) hypervisor và/hoặc máy ảo, các chương trình và quy trình trong hypervisor và/hoặc máy ảo;
- Ghi nhật ký việc khởi động (kết thúc) hệ điều hành máy chủ và/hoặc hệ điều hành khách, các chương trình và quy trình trong hệ điều hành máy chủ và/hoặc hệ điều hành khách;
- Ghi nhật ký các thay đổi về quyền truy cập vào các tệp hình ảnh của phần mềm ảo hóa và máy ảo, cũng như các tệp hình ảnh được sử dụng để vận hành hệ thống tệp ảo;
- Ghi nhật ký các thay đổi về quy tắc truy cập vào phần cứng ảo;
- Ghi nhật ký các thay đổi về thành phần và cấu hình của máy ảo;
- Ghi nhật ký các thay đổi về phần mềm và phần cứng ảo trong hypervisor và/hoặc máy ảo;
- Ghi nhật ký các thay đổi về phần mềm và phần cứng ảo trong hệ điều hành máy chủ và/hoặc hệ điều hành khách;
- Ghi nhật ký các thay đổi về quy tắc truy cập vào thông tin hạn chế, được lưu trữ và xử lý trong hypervisor và/hoặc máy ảo;
- Ghi nhật ký các thay đổi về quy tắc truy cập vào thông tin hạn chế, được lưu trữ và xử lý trong hệ điều hành máy chủ và/hoặc hệ điều hành khách;
- Sao lưu thông tin cần bảo vệ trong hypervisor và/hoặc máy ảo, được lưu trữ trên các thiết bị lưu trữ vật lý và/hoặc ảo;
- Sao lưu thông tin cần bảo vệ trong hệ điều hành máy chủ và/hoặc hệ điều hành khách, được lưu trữ trên các thiết bị lưu trữ vật lý và/hoặc ảo;
- Sao lưu các tệp hình ảnh của phần mềm ảo hóa và máy ảo, cũng như các tệp hình ảnh được sử dụng để vận hành hệ thống tệp ảo;
- Sao lưu không gian đĩa vật lý và/hoặc ảo, được sử dụng để lưu trữ nhật ký sự kiện của hypervisor và/hoặc máy ảo;
- Tạo (mô phỏng) các thành phần giả của hạ tầng ảo để phát hiện, ghi lại và phân tích các hành động của kẻ xâm nhập trong quá trình thực hiện các mối đe dọa bảo mật;
- Xóa thông tin còn sót lại sau khi xóa dữ liệu chứa thông tin hạn chế trong hypervisor và/hoặc máy ảo;
- Xóa thông tin còn sót lại sau khi xóa dữ liệu chứa thông tin hạn chế trong hệ điều hành máy chủ và/hoặc hệ điều hành khách;
- Xóa thông tin còn sót lại sau khi xóa các tệp hình ảnh của máy ảo, nơi đã xử lý thông tin hạn chế;
- Cài đặt (cài đặt) chỉ phần mềm và/hoặc các thành phần được phép sử dụng trong hạ tầng ảo;
- Lọc lưu lượng mạng từ/đến mỗi hệ điều hành khách;
- Mã hóa các tệp hình ảnh của phần mềm ảo hóa và máy ảo, cũng như các tệp hình ảnh được sử dụng để vận hành hệ thống tệp ảo, chứa thông tin hạn chế.


## 6.3 Bảo vệ hệ thống lưu trữ dữ liệu ảo

**Các biện pháp bảo vệ hệ thống lưu trữ dữ liệu ảo bao gồm:**

- Khôi phục tự động khả năng hoạt động của hệ thống lưu trữ dữ liệu kết nối với hạ tầng ảo trong trường hợp một hoặc nhiều thành phần của nó bị hỏng;
- Chặn truy cập vào các đối tượng của hạ tầng ảo đối với những người dùng không qua được quá trình xác thực;
- Bảo vệ chống truy cập trái phép (НСД) vào thông tin xác thực do người dùng trong hạ tầng ảo nhập vào;
- Bảo vệ chống truy cập trái phép vào thông tin xác thực của người dùng được lưu trữ trong các thành phần của hạ tầng ảo;
- Xác định và xác thực người dùng khi họ truy cập cục bộ hoặc từ xa đến các đối tượng trong hạ tầng ảo;
- Kiểm soát việc nhập (xuất) thông tin vào (ra) các hệ thống lưu trữ dữ liệu trong hạ tầng ảo;
- Kiểm soát truy cập của người dùng vào các phương tiện cấu hình của hệ thống lưu trữ dữ liệu trong hạ tầng ảo;
- Kiểm soát truy cập của người dùng vào các tệp hình ảnh của phần mềm ảo hóa và máy ảo, cũng như các tệp hình ảnh được sử dụng để vận hành hệ thống tệp ảo;
- Kiểm soát hoạt động (mức độ hao mòn) của các thiết bị lưu trữ thông tin kết nối với hạ tầng ảo, chuyển sang chế độ dự phòng khi cần thiết;
- Kiểm soát tính toàn vẹn của dữ liệu lưu trữ trên các thiết bị lưu trữ thông tin kết nối với hạ tầng ảo;
- Kiểm soát tính toàn vẹn của các tệp hình ảnh của phần mềm ảo hóa và máy ảo, cũng như các tệp hình ảnh được sử dụng để vận hành hệ thống tệp ảo;
- Đảm bảo các kênh (đường truyền) bảo mật cho việc truyền dữ liệu vào/ra hệ thống lưu trữ dữ liệu trong hạ tầng ảo;
- Đảm bảo tính xác thực của các kết nối mạng (phiên tương tác) trong hạ tầng ảo, bao gồm bảo vệ chống lại việc giả mạo thiết bị mạng và dịch vụ;
- Kiểm tra sự tồn tại của phần mềm độc hại trong môi trường hoạt động của hypervisor của hệ thống lưu trữ dữ liệu;
- Kiểm tra sự tồn tại của phần mềm độc hại trong các tệp hình ảnh của phần mềm ảo hóa và máy ảo, cũng như các tệp hình ảnh được sử dụng để vận hành hệ thống tệp ảo;
- Phân chia dữ liệu dựa trên mức độ bảo mật của thông tin đang được xử lý giữa các thành phần của hệ thống lưu trữ dữ liệu, các thiết bị lưu trữ thông tin riêng lẻ trong hạ tầng ảo, các ổ đĩa logic hoặc giữa các thư mục tệp;
- Đặt hệ thống lưu trữ dữ liệu trong một phân đoạn bảo mật của hệ thống thông tin;
- Ghi nhật ký các thay đổi về quyền truy cập vào thông tin lưu trữ trong hệ thống lưu trữ dữ liệu trong hạ tầng ảo;
- Ghi nhật ký các thay đổi về quyền truy cập vào các tệp hình ảnh của phần mềm ảo hóa và máy ảo, cũng như các tệp hình ảnh được sử dụng để vận hành hệ thống tệp ảo;
- Ghi nhật ký các thay đổi về quy tắc truy cập vào phần cứng ảo và vật lý của hệ thống lưu trữ dữ liệu;
- Ghi nhật ký các thay đổi về thành phần và cấu hình của phần cứng ảo và vật lý của hệ thống lưu trữ dữ liệu;
- Sao lưu các tệp hình ảnh của phần mềm ảo hóa và máy ảo, cũng như các tệp hình ảnh được sử dụng để vận hành hệ thống tệp ảo;
- Tạo (mô phỏng) các thành phần giả của hạ tầng ảo để phát hiện, ghi lại và phân tích các hành động của kẻ xâm nhập trong quá trình thực hiện các mối đe dọa bảo mật;
- Quản lý quyền truy cập vào phần cứng của hệ thống lưu trữ dữ liệu, kiểm soát việc kết nối (ngắt kết nối) các thiết bị lưu trữ thông tin với/đến hạ tầng ảo;
- Mã hóa các tệp hình ảnh của phần mềm ảo hóa và máy ảo, cũng như các tệp hình ảnh được sử dụng để vận hành hệ thống tệp ảo, chứa thông tin hạn chế.


## 6.4 Bảo vệ các kênh truyền dữ liệu ảo

**Các biện pháp bảo vệ kênh truyền dữ liệu ảo bao gồm:**

- Khôi phục tự động khả năng hoạt động của hệ thống lưu trữ dữ liệu kết nối với hạ tầng ảo trong trường hợp một hoặc nhiều thành phần của nó bị hỏng;
- Thay đổi tự động các tuyến truyền gói tin mạng giữa các thành phần của hạ tầng ảo bên trong hypervisor;
- Chặn truy cập vào các đối tượng của hạ tầng ảo đối với những người dùng không qua được quá trình xác thực;
- Phát hiện, phân tích và chặn các kênh truyền thông tin ẩn trong hạ tầng ảo để vượt qua các biện pháp bảo vệ thông tin hoặc trong các giao thức mạng được phép;
- Bảo vệ chống truy cập trái phép (НСД) vào thông tin xác thực mà người dùng trong hạ tầng ảo nhập vào;
- Bảo vệ chống truy cập trái phép vào thông tin xác thực của người dùng được lưu trữ trong các thành phần của hạ tầng ảo;
- Xác định và xác thực người dùng khi họ truy cập cục bộ hoặc từ xa đến các đối tượng trong hạ tầng ảo;
- Kiểm soát việc truyền các thông báo thông tin nội bộ trong các mạng ảo của hệ điều hành máy chủ theo các đặc tính như thành phần, dung lượng, v.v.;
- Giám sát việc sử dụng năng lực phần cứng vật lý và ảo;
- Đảm bảo sự cô lập của các luồng dữ liệu khác nhau, được truyền và xử lý bởi các thành phần của hạ tầng ảo của hệ điều hành máy chủ;
- Đảm bảo tính xác thực của các kết nối mạng (phiên tương tác) trong hạ tầng ảo, bao gồm bảo vệ chống lại việc giả mạo thiết bị mạng và dịch vụ;
- Vô hiệu hóa các giao thức mạng không sử dụng bởi các thành phần của hạ tầng ảo của hệ điều hành máy chủ;
- Truyền tải và kiểm soát tính toàn vẹn của các thuộc tính bảo mật (thẻ bảo mật) liên quan đến thông tin hạn chế được xử lý trong hạ tầng ảo khi trao đổi thông tin với các hệ thống thông tin khác;
- Dự phòng băng thông mạng để đảm bảo tương tác ổn định giữa các thành phần của hạ tầng ảo trong hypervisor;
- Tạo (mô phỏng) các thành phần giả của hạ tầng ảo để phát hiện, ghi lại và phân tích các hành động của kẻ xâm nhập trong quá trình thực hiện các mối đe dọa bảo mật;
- Lọc lưu lượng mạng giữa các thành phần của hạ tầng ảo và các mạng bên ngoài của hệ điều hành máy chủ, bao gồm cả các mạng công cộng;
- Lọc lưu lượng mạng từ/đến mỗi hệ điều hành khách;
- Mã hóa thông tin hạn chế được truyền qua các kênh giao tiếp ảo và vật lý của hypervisor;
- Mã hóa thông tin hạn chế được truyền qua các kênh giao tiếp ảo và vật lý của hệ điều hành máy chủ.


## 6.5 Bảo vệ các thiết bị ảo riêng lẻ xử lý, lưu trữ và truyền dữ liệu

**Các biện pháp bảo vệ các thiết bị ảo riêng lẻ xử lý, lưu trữ và truyền dữ liệu bao gồm:**

- Chặn truy cập vào các đối tượng của hạ tầng ảo đối với những người dùng không qua được quá trình xác thực;
- Bảo vệ chống truy cập trái phép (НСД) vào thông tin xác thực mà người dùng trong hạ tầng ảo nhập vào;
- Bảo vệ chống truy cập trái phép vào thông tin xác thực của người dùng được lưu trữ trong các thành phần của hạ tầng ảo;
- Xác định và xác thực người dùng khi họ truy cập cục bộ hoặc từ xa đến các đối tượng trong hạ tầng ảo;
- Kiểm soát truy cập của người dùng vào các phương tiện cấu hình phần cứng ảo;
- Kiểm soát truy cập của người dùng vào các tệp hình ảnh của phần mềm ảo hóa và máy ảo, cũng như các tệp hình ảnh được sử dụng để vận hành hệ thống tệp ảo;
- Kiểm soát hoạt động của các thành phần dự phòng quan trọng của hạ tầng ảo;
- Kiểm soát tính toàn vẹn của các tệp chứa cấu hình phần mềm ảo hóa và máy ảo;
- Giám sát việc sử dụng năng lực phần cứng vật lý và ảo;
- Đảm bảo khả năng kế thừa các quyền truy cập được thiết lập ở cấp quản lý cho người dùng đến các đối tượng truy cập ở cấp ảo hóa và phần cứng;
- Đảm bảo tính xác thực của các kết nối mạng (phiên tương tác) trong hạ tầng ảo, bao gồm bảo vệ chống lại việc giả mạo thiết bị mạng và dịch vụ;
- Vô hiệu hóa các giao thức mạng không sử dụng bởi các thành phần của hạ tầng ảo của hệ điều hành máy chủ;
- Áp dụng quyền truy cập cá nhân cho người dùng vào các đối tượng của một hoặc nhiều thành phần của hạ tầng ảo;
- Kiểm tra sự tồn tại của phần mềm độc hại trong phần mềm nhúng của phần cứng vật lý và ảo;
- Phân chia các tài nguyên vật lý giữa các thành phần của hạ tầng ảo dựa trên mức độ bảo mật của thông tin đang được xử lý;
- Đặt các cảm biến và/hoặc bộ phát hiện (ngăn chặn) xâm nhập trong phần cứng ảo;
- Ghi nhật ký và theo dõi việc khởi động (kết thúc) hoạt động của các thành phần của hạ tầng ảo;
- Ghi nhật ký và theo dõi các thay đổi trong phần mềm và phần cứng của hệ thống thông tin trong quá trình hoạt động và/hoặc trong thời gian hệ thống bị tắt phần cứng;
- Ghi nhật ký các thay đổi về quy tắc truy cập vào phần cứng ảo;
- Ghi nhật ký các thay đổi về thành phần và cấu hình của phần cứng ảo;
- Ghi nhật ký các thay đổi về phần mềm và phần cứng ảo trong hypervisor và/hoặc máy ảo;
- Ghi nhật ký các thay đổi về phần mềm và phần cứng ảo trong hệ điều hành máy chủ và/hoặc hệ điều hành khách;
- Sao lưu thông tin cần bảo vệ được lưu trữ trên các thiết bị lưu trữ vật lý và ảo;
- Phát hiện kịp thời sự cố của các thành phần hạ tầng ảo;
- Tạo (mô phỏng) các thành phần giả của hạ tầng ảo để phát hiện, ghi lại và phân tích các hành động của kẻ xâm nhập trong quá trình thực hiện các mối đe dọa bảo mật;
- Xóa thông tin còn sót lại sau khi xóa các tệp chứa cấu hình phần mềm ảo hóa và phần cứng ảo;
- Quản lý quyền truy cập vào phần cứng của hệ thống thông tin, kiểm soát việc kết nối (ngắt kết nối) các thiết bị lưu trữ thông tin với/đến hạ tầng ảo.

## 6.6 Bảo vệ các phương tiện bảo vệ thông tin ảo và các phương tiện bảo vệ thông tin được thiết kế để sử dụng trong môi trường ảo hóa

**Các biện pháp bảo vệ các phương tiện bảo vệ thông tin ảo và các phương tiện bảo vệ thông tin được thiết kế để sử dụng trong môi trường ảo hóa bao gồm:**

- Tự động khôi phục tất cả các chức năng của các phương tiện bảo vệ thông tin trong hệ thống thông tin;
- Bảo vệ khỏi truy cập trái phép vào thông tin xác thực được nhập bởi các đối tượng truy cập trong hạ tầng ảo;
- Bảo vệ khỏi truy cập trái phép vào thông tin xác thực được lưu trữ trong các thành phần của hạ tầng ảo;
- Nhận dạng và xác thực các đối tượng truy cập khi họ truy cập cục bộ hoặc từ xa vào các đối tượng của hạ tầng ảo;
- Đảm bảo kênh truyền tin cậy giữa các thành phần bảo vệ thông tin trong hạ tầng ảo;
- Mã hóa thông tin hạn chế được truyền qua các kênh vật lý và ảo.

# Theo Quyết định của FSTEC Nga số 17, các hệ thống ảo hóa phải đáp ứng các yêu cầu bảo vệ thông tin (Bảng 1).

[Xem tài liệu gốc ở đây](https://fstec.ru/dokumenty/vse-dokumenty/prikazy/prikaz-fstek-rossii-ot-11-fevralya-2013-g-n-17)

[Xem file pdf]()

**Bảng 1 – Yêu cầu của FSTEC**

| Mã số | Yêu cầu                                                           |
|-------|------------------------------------------------------------------|
| ZSV.1 | Xác thực và định danh người dùng và đối tượng truy cập trong hạ tầng ảo |
| ZSV.2 | Quản lý quyền truy cập của người dùng vào đối tượng trong hạ tầng ảo |
| ZSV.3 | Đăng ký các sự kiện bảo mật trong hạ tầng ảo                    |
| ZSV.4 | Quản lý luồng thông tin giữa các thành phần trong hạ tầng ảo     |
| ZSV.5 | Tải tin cậy máy chủ ảo hóa và các máy ảo                         |
| ZSV.6 | Quản lý di chuyển máy ảo và dữ liệu                               |
| ZSV.7 | Kiểm soát tính toàn vẹn của hạ tầng ảo và cấu hình của nó        |
| ZSV.8 | Sao lưu dữ liệu và dự phòng các thành phần trong hạ tầng ảo      |
| ZSV.9 | Quản lý bảo vệ chống virus trong hạ tầng ảo                      |
| ZSV.10| Phân đoạn hạ tầng ảo để xử lý dữ liệu cá nhân                    |

**Bảng 2 – Các biện pháp bảo vệ trong VirtualBox**

| Mã số | Có áp dụng trong VirtualBox không? |
|-------|-------------------------------------|
| ZSV.1 | Có                                  |
| ZSV.2 | Có                                  |
| ZSV.3 | Có                                  |
| ZSV.4 | Có                                  |
| ZSV.5 | Có                                  |
| ZSV.6 | Có                                  |
| ZSV.7 | Có                                  |
| ZSV.8 | Có                                  |
| ZSV.9 | Không                               |
| ZSV.10| Có                                  |


## Tài liệu tham khảo
