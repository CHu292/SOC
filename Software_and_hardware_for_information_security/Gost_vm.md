# Mục 1: Phạm vi áp dụng

- Tiêu chuẩn này đưa ra các yêu cầu về bảo vệ thông tin được xử lý khi sử dụng công nghệ ảo hóa.
- Trong tiêu chuẩn này, chỉ xem xét các mối đe dọa an ninh và các biện pháp bảo vệ thông tin được xử lý bằng công nghệ ảo hóa. Các biện pháp bảo vệ thông tin nêu trong tiêu chuẩn này chỉ áp dụng khi xử lý thông tin bằng công nghệ ảo hóa. Ngoài các biện pháp bảo vệ thông tin đã nêu, để đảm bảo mức độ an ninh thông tin cần thiết trong các hệ thống thông tin được xây dựng bằng công nghệ ảo hóa, cần áp dụng thêm các biện pháp bảo vệ thông tin thường dùng cho bất kỳ hệ thống tự động hóa nào trong môi trường bảo mật.
- Tiêu chuẩn này được áp dụng cùng với các tiêu chuẩn khác quy định đặc điểm sản phẩm, quy tắc thực hiện và đặc điểm của các quy trình thiết kế, sản xuất, xây dựng, lắp đặt, hiệu chuẩn, vận hành, lưu trữ, vận chuyển, bán và tiêu hủy, thực hiện công việc hoặc cung cấp dịch vụ trong lĩnh vực b; ảo vệ thông tin.

# Mục 2: Tham chiếu tiêu chuẩn

- Trong tiêu chuẩn này, các tham chiếu tiêu chuẩn sau được sử dụng:
  - ГОСТ 34.003 Công nghệ thông tin. Tập hợp các tiêu chuẩn cho hệ thống tự động hóa. Hệ thống tự động hóa. Thuật ngữ và định nghĩa.
  - ГОСТ R 50922 Bảo vệ thông tin. Các thuật ngữ và định nghĩa cơ bản.
  - ГОСТ R 53114 Bảo vệ thông tin. Đảm bảo an ninh thông tin trong tổ chức. Các thuật ngữ và định nghĩa cơ bản.
  - ГОСТ R ISO/IEC 27000 Công nghệ thông tin. Phương pháp và công cụ bảo mật. Hệ thống quản lý an ninh thông tin. Tổng quan và thuật ngữ.
- Lưu ý: Khi sử dụng tiêu chuẩn này, nên kiểm tra hiệu lực của các tiêu chuẩn tham chiếu trong hệ thống thông tin công cộng — trên trang web chính thức của Cơ quan Liên bang về Quy định Kỹ thuật và Đo lường hoặc trong chỉ mục thông tin hàng năm "Tiêu chuẩn Quốc gia", được công bố tính đến ngày 1 tháng 1 của năm hiện tại, và trong chỉ mục thông tin hàng tháng "Tiêu chuẩn Quốc gia". Nếu tiêu chuẩn tham chiếu được thay thế, thì nên sử dụng phiên bản mới nhất của tiêu chuẩn đó với các thay đổi được cập nhật. Nếu tiêu chuẩn tham chiếu được thay thế hoặc hủy bỏ mà không có thay thế, thì nên áp dụng phần liên quan mà không ảnh hưởng đến tham chiếu đó.

# Mục 3: Thuật ngữ và định nghĩa

Trong tiêu chuẩn này, các thuật ngữ theo ГОСТ R ISO/IEC 27000, ГОСТ 34.003, ГОСТ R 50922, ГОСТ R 53114 được áp dụng, cũng như các thuật ngữ sau đây với các định nghĩa tương ứng:
  
## 3.1 Ảo hóa: 
Nhóm các công nghệ dựa trên việc chuyển đổi định dạng hoặc thông số của các yêu cầu phần mềm hoặc mạng đối với tài nguyên máy tính nhằm đảm bảo quá trình xử lý thông tin độc lập với nền tảng phần mềm hoặc phần cứng của hệ thống thông tin.

## 3.2 Ảo hóa phần mềm (ảo hóa chương trình): 
Công nghệ tạo ra môi trường phần mềm cách ly (container) với một tập hợp các thành phần cụ thể của hệ điều hành mô phỏng, cung cấp khả năng hoạt động cho các chương trình riêng lẻ.

## 3.3 Ảo hóa phần cứng, ảo hóa hệ thống máy tính: 
Công nghệ tạo ra môi trường phần mềm cách ly với tập hợp các thành phần cụ thể của phần cứng và vi chương trình mô phỏng, cung cấp khả năng hoạt động cho các hệ điều hành riêng lẻ.

## 3.4 Máy ảo (VM): 

Hệ thống máy tính ảo bao gồm các thiết bị ảo xử lý, lưu trữ và truyền dữ liệu, và có thể chứa phần mềm và dữ liệu người dùng.
Lưu ý:
  - Máy ảo là dạng đơn giản nhất của hệ thống máy tính ảo.
  - Một số máy ảo, khi được kết hợp để giải quyết các nhiệm vụ nhất định, cũng cấu thành một hệ thống máy tính ảo.
  - Máy ảo che giấu sự thực hiện thực sự của các quy trình và đối tượng bên trong nó khỏi các quy trình bên ngoài máy ảo và ngược lại.

## 3.5 Hệ điều hành khách: 
Hệ điều hành được cài đặt trong máy ảo.

## 3.6 Ảnh máy ảo: 
Tệp (hoặc tệp tin) chứa thông tin về cấu hình, cài đặt và trạng thái của máy ảo, cũng như các chương trình và dữ liệu được lưu trữ bên trong.

## 3.7 Ảo hóa hệ thống lưu trữ dữ liệu: 
Công nghệ xây dựng không gian lưu trữ dữ liệu cách ly với giao diện quản lý thống nhất dựa trên các thiết bị lưu trữ máy móc, cung cấp khả năng truy cập thông tin cần thiết thông qua việc truyền tải qua các kênh dữ liệu.

## 3.8 Ảo hóa mạng máy tính (ảo hóa kênh truyền dữ liệu): 
Công nghệ kết hợp các tài nguyên mạng phần cứng và phần mềm và các chức năng mạng trong một đối tượng được quản lý bằng phần mềm để thực hiện sự tương tác logic của chúng thông qua các tài nguyên và chức năng mạng ảo bổ sung.

## 3.9 Mạng máy tính ảo (kênh truyền dữ liệu ảo): 
Mạng máy tính chứa một hoặc nhiều tài nguyên mạng ảo và/hoặc chức năng mạng.

## 3.10 Hỗ trợ phần cứng cho ảo hóa: 
Công nghệ được triển khai trong các bộ xử lý (chipset) của máy tính dưới dạng các lệnh (các chỉ thị), được sử dụng để cải thiện đặc tính kỹ thuật của hệ thống thông tin được xây dựng bằng cách sử dụng công nghệ ảo hóa và/hoặc tăng cường bảo mật cho các đối tượng bảo vệ trong các hệ thống này.

## 3.11 Hypervisor (hệ thống máy tính): 
Phần mềm tạo ra môi trường hoạt động cho các phần mềm khác (bao gồm cả các hypervisor khác) bằng cách mô phỏng phần cứng của hệ thống máy tính, quản lý các tài nguyên này và các hệ điều hành khách hoạt động trong môi trường này.

Lưu ý:

Có hai loại hypervisor: loại I và loại II.

## 3.12 Hệ điều hành chủ: 
Hệ điều hành trong đó hypervisor hoạt động.

## 3.13 Hypervisor loại I: 
Hypervisor được cài đặt trực tiếp trên phần cứng như phần mềm hệ thống.

## 3.14 Hypervisor loại II: 
Hypervisor được cài đặt trong môi trường của hệ điều hành chủ như phần mềm ứng dụng.

## 3.15 Hypervisor của hệ thống lưu trữ dữ liệu: 
- Phần mềm được cài đặt trực tiếp trên phần cứng như phần mềm hệ thống hoặc trong môi trường của hệ điều hành chủ như phần mềm ứng dụng, thực hiện các chức năng trung gian giữa không gian địa chỉ logic và vật lý để cung cấp mức quản lý cao cho các tài nguyên lưu trữ dữ liệu.
- Lưu ý: Để đạt được mức quản lý cao nhất của toàn bộ tài nguyên tính toán, hypervisor của hệ thống lưu trữ dữ liệu được sử dụng cùng với hypervisor loại I hoặc loại II. Trong trường hợp này, hypervisor của hệ thống lưu trữ dữ liệu thay đổi cách xử lý các yêu cầu đầu vào/đầu ra của các hypervisor loại I hoặc II để tăng hiệu suất, hiệu quả sử dụng và quản lý tài nguyên lưu trữ dữ liệu.

## 3.16 Hạ tầng ảo: 
- Cấu trúc liên kết phân cấp của các nhóm thiết bị ảo xử lý, lưu trữ và/hoặc truyền dữ liệu, cũng như các nhóm phần cứng và/hoặc phần mềm cần thiết cho hoạt động của chúng.
- Lưu ý:
  - Nhóm các thiết bị phần cứng và/hoặc các chương trình đang chạy (các quy trình, luồng) được sử dụng để thực hiện các chức năng của các thiết bị ảo xử lý, lưu trữ và/hoặc truyền dữ liệu tạo thành biên giới của hạ tầng ảo.
  - Trong hạ tầng ảo, có ít nhất ba cấp độ phân cấp:
    - Cấp độ thứ nhất (cấp độ thấp nhất) là phần cứng của hạ tầng ảo — các thiết bị phần cứng được sử dụng để thực hiện công nghệ ảo hóa, bao gồm hỗ trợ phần cứng cho ảo hóa.
    - Cấp độ thứ hai là hypervisor và các đối tượng do nó tạo ra (máy ảo, máy chủ ảo, bộ xử lý ảo, đĩa ảo, bộ nhớ ảo, thiết bị mạng ảo chủ động và thụ động, các phương tiện bảo vệ thông tin ảo, v.v.).
    - Cấp độ thứ ba (cấp độ quản lý) là phương tiện quản lý tập trung hypervisor trong phạm vi một hạ tầng ảo — bảng điều khiển quản lý hạ tầng ảo.

## 3.17 Thành phần của hạ tầng ảo: 
- Một phần của hạ tầng ảo được phân loại theo một tiêu chí hoặc tập hợp các tiêu chí và được xem xét như một tổng thể.

# Mục 4: Đối tượng bảo vệ
- Thuật ngữ "ảo hóa" đề cập đến nhiều công nghệ thông tin nhằm giảm chi phí triển khai mạng máy tính của tổ chức, nâng cao khả năng chịu lỗi của các giải pháp máy chủ, và đạt được các lợi ích khác. Ảo hóa bao gồm việc mô phỏng phần mềm và/hoặc phần cứng mà trong môi trường (hoặc dựa trên đó) các chương trình khác nhau hoạt động.
- Việc ảo hóa được thực hiện đối với:
   - Phần mềm;
   - Hệ thống tính toán;
   - Hệ thống lưu trữ dữ liệu;
   - Mạng tính toán;
   - Bộ nhớ;
   - Dữ liệu.
- Khi sử dụng công nghệ ảo hóa, các đối tượng truy cập (ảo và ảo hóa) được tạo ra, cần được bảo vệ giống như các đối tượng khác trong hệ thống thông tin, bao gồm các thiết bị phần cứng của hệ thống thông tin được sử dụng để triển khai công nghệ ảo hóa. Các đối tượng bảo vệ chính khi sử dụng công nghệ ảo hóa bao gồm:
  - Các phương tiện tạo và quản lý hạ tầng ảo (hypervisor loại I, hypervisor loại II, hypervisor của hệ thống lưu trữ dữ liệu, bảng điều khiển quản lý hạ tầng ảo, v.v.);
  - Hệ thống tính toán ảo (VM, máy chủ ảo, v.v.);
  - Hệ thống lưu trữ dữ liệu ảo;
  - Kênh truyền dữ liệu ảo;
  - Các thiết bị ảo riêng lẻ xử lý, lưu trữ và truyền dữ liệu (bộ xử lý ảo, đĩa ảo, bộ nhớ ảo, thiết bị mạng ảo chủ động và thụ động, v.v.);
  - Các phương tiện bảo vệ thông tin ảo (ZIS) và các phương tiện ZIS được thiết kế để sử dụng trong môi trường ảo hóa;
  - Biên giới của hạ tầng ảo (các bộ xử lý trung tâm và lõi của chúng, không gian địa chỉ bộ nhớ, giao diện mạng, cổng kết nối thiết bị ngoại vi, v.v.).

# Mục 5: Các mối đe dọa an ninh liên quan đến việc sử dụng công nghệ ảo hóa

Việc sử dụng công nghệ ảo hóa tạo điều kiện cho sự xuất hiện của các mối đe dọa an ninh không đặc trưng cho các hệ thống thông tin được xây dựng mà không sử dụng công nghệ ảo hóa. Danh sách tổng quát các mối đe dọa có thể phát sinh thêm khi sử dụng công nghệ ảo hóa bao gồm các mối đe dọa được mô tả sau đây.

## 5.1 Mối đe dọa tấn công vào thiết bị mạng vật lý và/hoặc ảo (chủ động và/hoặc thụ động) từ mạng vật lý và/hoặc ảo
Những mối đe dọa này phát sinh do các hạn chế về tính năng (tồn tại các lỗ hổng) của thiết bị mạng vật lý và/hoặc ảo chủ động và/hoặc thụ động trong hạ tầng ảo. Việc thực hiện các mối đe dọa này bị ảnh hưởng trực tiếp bởi sự tồn tại của các lỗ hổng trong phần mềm và/hoặc vi chương trình của thiết bị, việc sử dụng địa chỉ mạng cố định, và các tham số cài đặt khác, cũng như khả năng thay đổi thuật toán hoạt động của phần mềm thiết bị mạng bởi phần mềm độc hại.

## 5.2 Mối đe dọa tấn công vào các kênh truyền dữ liệu ảo
Những mối đe dọa này liên quan đến các lỗ hổng của công nghệ ảo hóa mạng, được sử dụng để xây dựng các kênh truyền dữ liệu ảo. Việc sử dụng không chính xác công nghệ ảo hóa mạng có thể tạo điều kiện cho việc chiếm đoạt trái phép lưu lượng của các nút mạng mà không thể truy cập bằng các công nghệ mạng khác.

## 5.3 Mối đe dọa tấn công vào hypervisor từ máy ảo và/hoặc mạng vật lý

Những mối đe dọa này liên quan đến các lỗ hổng của hypervisor, cũng như các lỗ hổng trong phần mềm và hạn chế về tính năng của phần cứng được sử dụng để đảm bảo hoạt động của hypervisor. Việc thực hiện các mối đe dọa này có thể dẫn đến sự mất khả năng hoạt động của toàn bộ (nếu chỉ có một hypervisor) hoặc một phần (nếu có nhiều hypervisor tương tác với nhau) hạ tầng ảo.

## 5.4 Mối đe dọa tấn công vào các thiết bị ảo cần bảo vệ từ mạng vật lý và/hoặc ảo
Những mối đe dọa này phát sinh do sự tồn tại của các giao diện phần mềm mạng của hypervisor, được thiết kế để quản lý từ xa thành phần và cấu hình của các thiết bị ảo được tạo ra (hoặc đang được tạo) bởi hypervisor, cho phép kẻ tấn công có thể truy cập trái phép từ xa vào các thiết bị này thông qua các công nghệ mạng từ mạng vật lý và/hoặc ảo. Thiệt hại tiềm tàng có thể liên quan đến tính khả dụng của các thiết bị ảo đó.

## 5.5 Mối đe dọa tấn công vào các máy ảo cần bảo vệ từ mạng vật lý và/hoặc ảo
Những mối đe dọa này phát sinh do sự tồn tại của địa chỉ mạng của các máy ảo được tạo ra và khả năng giao tiếp mạng của chúng với các đối tượng khác thông qua các công nghệ mạng tiêu chuẩn và công nghệ ảo hóa mạng.

## 5.6 Mối đe dọa tấn công vào các máy ảo cần bảo vệ từ mạng vật lý và/hoặc ảo khác
Các mối đe dọa này tương tự như mối đe dọa ở mục 5.5 nhưng liên quan đến khả năng giao tiếp giữa các máy ảo khác nhau, có thể dẫn đến việc xâm phạm an ninh của các máy ảo này từ các mạng khác.

## 5.7 Mối đe dọa tấn công vào hệ thống lưu trữ dữ liệu từ mạng vật lý và/hoặc ảo
Các mối đe dọa này liên quan đến các lỗ hổng trong các công nghệ phân phối thông tin trên các thiết bị lưu trữ dữ liệu ảo khác nhau và/hoặc các đĩa ảo, cũng như các lỗ hổng của công nghệ không gian đĩa ảo duy nhất. Những lỗ hổng này liên quan đến độ phức tạp của các thuật toán đảm bảo sự nhất quán trong việc phân phối thông tin trong một không gian đĩa ảo duy nhất, cũng như sự tương tác với các kênh truyền dữ liệu ảo và vật lý để đảm bảo hoạt động trong cùng một không gian đĩa.

## 5.8 Mối đe dọa sự thoát khỏi phạm vi của máy ảo
Những mối đe dọa này liên quan đến các lỗ hổng trong phần mềm của hypervisor, thực hiện chức năng tạo ra môi trường phần mềm cách ly cho các chương trình hoạt động bên trong. Trong trường hợp một phần mềm độc hại khởi động một hypervisor riêng, hoạt động ở mức tương tác logic thấp hơn hypervisor bị tấn công, hypervisor bị tấn công, cũng như các phương tiện bảo vệ được cài đặt trong nó, không thể thực hiện các chức năng bảo mật đối với các chương trình hoạt động trong hypervisor riêng này.

## 5.9 Mối đe dọa truy cập trái phép vào dữ liệu ngoài không gian địa chỉ được dự trữ, bao gồm cả không gian được phân bổ cho phần cứng ảo
Những mối đe dọa này liên quan đến các lỗ hổng của phần mềm hypervisor, vốn đảm bảo tính cách ly của không gian địa chỉ được sử dụng để lưu trữ mã phần mềm, không chỉ thông tin được bảo vệ và các chương trình xử lý nó mà còn cả mã phần mềm thực hiện phần cứng ảo (các thiết bị xử lý, lưu trữ và truyền dữ liệu ảo). Trong trường hợp chương trình độc hại trong máy ảo thực hiện truy cập trái phép vào dữ liệu nằm ngoài không gian địa chỉ dự trữ dành cho dữ liệu người dùng, chương trình độc hại này có thể làm hỏng tính toàn vẹn của mã phần mềm của chính nó và/hoặc các máy ảo khác đang hoạt động dưới sự kiểm soát của cùng một hypervisor, cũng như thay đổi các tham số cài đặt của hypervisor đó.

## 5.10 Mối đe dọa vi phạm cách ly dữ liệu người dùng bên trong máy ảo
Những mối đe dọa này liên quan đến các lỗ hổng của phần mềm hypervisor, đảm bảo tính cách ly của không gian địa chỉ được sử dụng để lưu trữ dữ liệu người dùng từ chương trình độc hại hoạt động ngoài máy ảo. Việc thực hiện mối đe dọa này có thể dẫn đến vi phạm tính an toàn của dữ liệu người dùng trong các chương trình đang hoạt động bên trong máy ảo.

## 5.11 Mối đe dọa vi phạm quy trình xác thực các đối tượng tương tác thông tin ảo
Mối đe dọa này liên quan đến việc tồn tại nhiều giao thức khác nhau cho việc xác định và xác thực các đối tượng ảo, ảo hóa và vật lý tương tác với nhau trong quá trình truyền dữ liệu, cả bên trong một cấp độ của hạ tầng ảo và giữa các cấp độ của nó. Khả năng thực hiện mối đe dọa này phụ thuộc trực tiếp vào chất lượng thực hiện của chính các giao thức và cơ chế tương tác của chúng.

## 5.12 Mối đe dọa chiếm quyền kiểm soát hypervisor
Mối đe dọa chiếm quyền kiểm soát hypervisor liên quan đến sự tồn tại của các giao diện phần mềm quản lý hypervisor và khả năng truy cập trái phép vào các giao diện này. Thiệt hại tiềm tàng có thể liên quan đến việc vi phạm an ninh của các tài nguyên thông tin, chương trình và tính toán, được quản lý và dự trữ bởi hypervisor.

## 5.13 Mối đe dọa chiếm quyền kiểm soát môi trường ảo hóa
Mối đe dọa chiếm quyền kiểm soát môi trường ảo hóa liên quan đến việc các giao diện phần mềm của bảng điều khiển quản lý hạ tầng ảo, cũng như các hypervisor được quản lý bởi nó, có khả năng tương tác với các chương trình khác, và do đó, có thể bị truy cập trái phép. Thiệt hại tiềm tàng có thể liên quan đến việc vi phạm an ninh của các tài nguyên thông tin, chương trình và tính toán trong hạ tầng ảo.

## 5.14 Mối đe dọa tăng không kiểm soát số lượng máy ảo
Những mối đe dọa này liên quan đến sự hạn chế về dung lượng không gian đĩa được phân bổ cho hạ tầng ảo và những lỗ hổng trong việc kiểm soát quá trình tạo máy ảo, dẫn đến việc có thể tạo ra một số lượng lớn máy ảo một cách vô tình hoặc trái phép. Việc thực hiện mối đe dọa này có thể dẫn đến việc hạn chế hoặc vi phạm tính khả dụng của các tài nguyên ảo cho người dùng cuối của các dịch vụ đám mây.

## 5.15 Mối đe dọa tăng không kiểm soát số lượng tài nguyên tính toán được dự trữ
Những mối đe dọa này liên quan đến các lỗ hổng trong phần mềm quản lý hạ tầng ảo, phần mềm này có nhiệm vụ phân bổ tài nguyên máy tính (tài nguyên tính toán và bộ nhớ). Việc thực hiện mối đe dọa này có thể xảy ra do truy cập trái phép vào phần mềm này hoặc do lỗi trong mã của nó.

## 5.16 Mối đe dọa vi phạm công nghệ xử lý thông tin bằng cách thực hiện các thay đổi trái phép vào hình ảnh máy ảo
- Những mối đe dọa này liên quan đến việc thiếu cơ chế bảo vệ trong phần mềm ảo hóa để ngăn chặn truy cập trái phép vào các hình ảnh máy ảo. Việc thực hiện mối đe dọa này có thể dẫn đến việc vi phạm tính bí mật của thông tin được bảo vệ, tính toàn vẹn của các chương trình được cài đặt trên máy ảo, cũng như tính khả dụng của tài nguyên máy ảo.
- Ngoài ra, việc cài đặt phần mềm độc hại vào các hình ảnh máy ảo, được sử dụng làm mẫu (hình ảnh tiêu chuẩn), có thể được sử dụng để tạo ra mạng botnet trong quá trình chuẩn bị cho các cuộc tấn công từ chối dịch vụ. Trong trường hợp này, an ninh của thông tin được xử lý trong các máy ảo khác, các phân đoạn của hạ tầng ảo hoặc các hệ thống thông tin bên ngoài có thể bị xâm phạm.

## 5.17 Mối đe dọa truy cập trái phép vào thông tin được bảo vệ trong không gian ảo
Do việc sử dụng nhiều công nghệ ảo hóa khác nhau để xử lý thông tin (phân phối dữ liệu giữa các đĩa logic và ảo, phân phối giữa các thiết bị lưu trữ vật lý và ảo, phân bổ không gian đĩa dưới dạng các đĩa riêng lẻ, v.v.), hầu hết các tệp tin đều được lưu trữ dưới dạng các đoạn riêng biệt. Do đó, trong hầu hết các trường hợp, việc đọc tuần tự dữ liệu từ một thiết bị lưu trữ riêng lẻ không cho phép vi phạm tính bí mật của thông tin được bảo vệ. Tuy nhiên, việc sử dụng phần mềm và công nghệ thông tin để xử lý thông tin phân tán có thể khôi phục tính toàn vẹn của các tệp dữ liệu, do đó, vi phạm tính bí mật của chúng.

## 5.18 Mối đe dọa lỗi cập nhật hypervisor
- Những mối đe dọa này liên quan đến việc phụ thuộc của mỗi thiết bị ảo và mỗi đối tượng truy cập ảo hóa vào tính khả dụng của hypervisor. Việc cập nhật hypervisor không chính xác có thể dẫn đến việc vô hiệu hóa các cơ chế bảo vệ, làm giảm tính bảo mật của thông tin được bảo vệ, tính toàn vẹn của các chương trình, và tính khả dụng của các tài nguyên máy ảo.
- Lưu ý - Lỗi cập nhật Hypervisor là:
  - lỗi trong quá trình cập nhật;
  - các bản cập nhật trong đó các lỗi mới được đưa vào mã bộ ảo hóa;
  - các bản cập nhật trong đó mã chương trình được đưa vào bộ ảo hóa gây ra sự không tương thích hypervisor với môi trường hoạt động của nó;
  - các sự cố bảo mật thông tin khác xảy ra trong quá trình cập nhật bộ ảo hóa.
# Mục 6: Các đặc điểm bảo vệ thông tin khi sử dụng công nghệ ảo hóa
- Việc bảo vệ thông tin được xử lý trong hệ thống thông tin (IS) được xây dựng bằng cách sử dụng công nghệ ảo hóa được đảm bảo thông qua việc tuân thủ các yêu cầu về các biện pháp bảo vệ thông tin (ZIS). Hệ thống thông tin điển hình này được trình bày trong Phụ lục B. Nhìn chung, các biện pháp bảo vệ tương tự như các biện pháp được áp dụng trong IS không sử dụng công nghệ ảo hóa. Tuy nhiên, dưới đây là các biện pháp bảo vệ thông tin đặc thù cần áp dụng khi sử dụng công nghệ ảo hóa.
- Các biện pháp bảo vệ thông tin được chia thành các nhóm khác nhau tùy thuộc vào đối tượng bảo vệ.
- Vì tính bảo mật của thông tin được xác định bởi các yêu cầu bảo vệ, mức độ và chiều sâu của nó thay đổi tùy theo lớp bảo mật của IS, bao gồm cả khi sử dụng công nghệ ảo hóa. Trong tiêu chuẩn này, đối với mỗi đối tượng bảo vệ, một tập hợp các biện pháp bảo vệ thông tin tương ứng với lớp bảo mật cao nhất khỏi truy cập trái phép (NSD) được cung cấp.
- Các biện pháp bảo vệ thông tin cần được lựa chọn dựa trên các mối đe dọa an ninh, đặc điểm sử dụng của các đối tượng bảo vệ, và các quy định pháp luật hiện hành trong lĩnh vực bảo vệ thông tin. Dữ liệu tổng hợp về các mối đe dọa và các biện pháp bảo vệ thông tin được xử lý bằng công nghệ ảo hóa được nêu trong Phụ lục V.

## 6.1 Bảo vệ các phương tiện tạo và quản lý hạ tầng ảo
**Các biện pháp bảo vệ phương tiện tạo và quản lý hạ tầng ảo bao gồm:**

- Thay đổi tự động tuyến đường truyền gói tin mạng giữa các thành phần của hạ tầng ảo bên trong hypervisor;
- Chặn quyền truy cập vào các đối tượng của hạ tầng ảo đối với các đối tượng truy cập không qua quy trình xác thực;
- Phát hiện, phân tích và chặn các kênh truyền thông ẩn bên trong hạ tầng ảo, vượt qua các biện pháp bảo vệ thông tin được triển khai hoặc bên trong các giao thức mạng được phép;
- Bảo vệ khỏi truy cập trái phép vào thông tin xác thực được nhập bởi các đối tượng truy cập trong hạ tầng ảo;
- Bảo vệ khỏi truy cập trái phép vào thông tin xác thực của các đối tượng truy cập được lưu trữ trong các thành phần của hạ tầng ảo;
- Nhận dạng và xác thực các đối tượng truy cập khi họ truy cập cục bộ hoặc từ xa vào các đối tượng của hạ tầng ảo;
- Kiểm soát việc nhập (xuất) thông tin vào (ra khỏi) hạ tầng ảo;
- Kiểm soát truy cập của các đối tượng truy cập vào không gian địa chỉ cách ly trong bộ nhớ của hypervisor;
- Kiểm soát truy cập của các đối tượng truy cập vào không gian địa chỉ cách ly trong bộ nhớ của hệ điều hành chủ;
- Kiểm soát truy cập của các đối tượng truy cập vào các công cụ cấu hình của phần cứng ảo;
- Kiểm soát truy cập của các đối tượng truy cập vào các công cụ cấu hình của hypervisor và máy ảo;
- Kiểm soát việc khởi động hypervisor và máy ảo dựa trên các tiêu chí bảo mật của đối tượng bảo vệ (chế độ khởi động, loại phương tiện sử dụng, v.v.);
- Kiểm soát tính toàn vẹn của các thành phần quan trọng cho hoạt động của hypervisor và máy ảo;
- Đảm bảo khả năng kế thừa các quyền truy cập đã được thiết lập ở cấp độ quản lý đối với các đối tượng truy cập ở cấp độ ảo hóa và thiết bị;
- Đảm bảo tính xác thực của các kết nối mạng (phiên tương tác) bên trong hạ tầng ảo, bao gồm việc bảo vệ khỏi việc thay thế các thiết bị và dịch vụ mạng;
- Đặt các cảm biến và/hoặc thiết bị phát hiện (ngăn chặn) xâm nhập trong phần cứng ảo;
- Đăng ký và theo dõi quá trình khởi động (hoặc tắt) của các thành phần trong hạ tầng ảo;
- Sao lưu thông tin được bảo vệ trong hypervisor và/hoặc máy ảo, được lưu trữ trên các phương tiện vật lý và/hoặc ảo;
- Sao lưu không gian đĩa vật lý và/hoặc ảo được sử dụng để lưu trữ nhật ký sự kiện của hypervisor và/hoặc máy ảo;
- Phát hiện kịp thời các lỗi của các thành phần trong hạ tầng ảo;
- Tạo các thành phần giả trong hạ tầng ảo nhằm phát hiện, ghi lại và phân tích hành động của những kẻ vi phạm trong quá trình thực hiện các mối đe dọa an ninh;
- Xóa dữ liệu dư thừa sau khi xóa dữ liệu trong hạ tầng ảo, bao gồm cả thông tin hạn chế.

## 6.2 Bảo vệ hệ thống tính toán ảo

**Các biện pháp bảo vệ hệ thống tính toán ảo bao gồm:**

- Chặn quyền truy cập vào các đối tượng của hạ tầng ảo đối với các đối tượng truy cập không qua quy trình xác thực;
- Bảo vệ khỏi truy cập trái phép vào thông tin xác thực được nhập bởi các đối tượng truy cập trong hạ tầng ảo;
- Bảo vệ khỏi truy cập trái phép vào thông tin xác thực của các đối tượng truy cập được lưu trữ trong các thành phần của hạ tầng ảo;
- Nhận dạng và xác thực các đối tượng truy cập khi họ truy cập cục bộ hoặc từ xa vào các đối tượng của hạ tầng ảo;
- Kiểm soát truy cập của các đối tượng truy cập vào không gian địa chỉ cách ly trong bộ nhớ của hypervisor;
- Kiểm soát truy cập của các đối tượng truy cập vào không gian địa chỉ cách ly trong bộ nhớ của hệ điều hành chủ;
- Kiểm soát truy cập của các đối tượng truy cập vào các công cụ cấu hình của hypervisor và máy ảo;
- Kiểm soát truy cập của các đối tượng truy cập vào các công cụ cấu hình của hệ điều hành chủ và/hoặc hệ điều hành khách;
- Kiểm soát truy cập vào các tệp ảnh ảo của phần mềm ảo hóa và máy ảo, cũng như các tệp ảnh được sử dụng cho hoạt động của hệ thống tệp ảo;
- Kiểm soát việc khởi động hypervisor và máy ảo dựa trên các tiêu chí bảo mật của đối tượng bảo vệ (chế độ khởi động, loại phương tiện sử dụng, v.v.);
- Kiểm soát tính toàn vẹn của các thành phần quan trọng cho hoạt động của hypervisor và máy ảo;
- Kiểm soát tính toàn vẹn của các thành phần quan trọng cho hoạt động của hệ điều hành chủ và hệ điều hành khách;
- Kiểm soát tính toàn vẹn của các tệp chứa cài đặt phần mềm ảo hóa và máy ảo;
- Ngăn chặn sự chậm trễ hoặc gián đoạn trong việc thực hiện các quy trình của máy ảo có mức ưu tiên cao từ các quy trình của máy ảo có mức ưu tiên thấp;
- Kiểm tra sự hiện diện của phần mềm độc hại trong vi chương trình của phần cứng vật lý và ảo;
- Kiểm tra sự hiện diện của phần mềm độc hại trong các tệp cấu hình của hypervisor và/hoặc máy ảo;
- Kiểm tra sự hiện diện của phần mềm độc hại trong các tệp ảnh của phần mềm ảo hóa và máy ảo, cũng như các tệp ảnh được sử dụng cho hoạt động của hệ thống tệp ảo;
- Kiểm tra bộ nhớ và hệ thống tệp của hypervisor và/hoặc máy ảo để phát hiện phần mềm độc hại;
- Kiểm tra bộ nhớ và hệ thống tệp của hệ điều hành chủ và/hoặc hệ điều hành khách để phát hiện phần mềm độc hại;
- Đặt các cảm biến và/hoặc thiết bị phát hiện (ngăn chặn) xâm nhập trong phần cứng ảo;
- Đăng ký việc đăng nhập/thoát ra của các đối tượng truy cập trong hypervisor và/hoặc máy ảo;
- Đăng ký việc khởi động (hoặc tắt) hypervisor và/hoặc máy ảo, các chương trình và quy trình trong hypervisor và/hoặc máy ảo;
- Đăng ký các thay đổi về quyền truy cập vào các tệp ảnh của phần mềm ảo hóa và máy ảo, cũng như các tệp ảnh được sử dụng cho hoạt động của hệ thống tệp ảo;
- Đăng ký các thay đổi về quyền truy cập vào phần cứng ảo;
- Đăng ký các thay đổi về cấu trúc và cấu hình của phần mềm và phần cứng ảo trong hypervisor và/hoặc máy ảo;
- Đăng ký các thay đổi về cấu trúc và cấu hình của phần mềm và phần cứng ảo trong hệ điều hành chủ và/hoặc hệ điều hành khách;
- Sao lưu thông tin được bảo vệ trong hypervisor và/hoặc máy ảo, được lưu trữ trên các phương tiện vật lý và/hoặc ảo;
- Sao lưu các tệp ảnh của phần mềm ảo hóa và máy ảo, cũng như các tệp ảnh được sử dụng cho hoạt động của hệ thống tệp ảo;
- Tạo các thành phần giả trong hạ tầng ảo nhằm phát hiện, ghi lại và phân tích hành động của những kẻ vi phạm trong quá trình thực hiện các mối đe dọa an ninh;
- Xóa dữ liệu dư thừa sau khi xóa thông tin được bảo vệ trong hypervisor và/hoặc máy ảo;
- Mã hóa các tệp ảnh của phần mềm ảo hóa và máy ảo, cũng như các tệp ảnh được sử dụng cho hoạt động của hệ thống tệp ảo, chứa thông tin hạn chế.

## 6.3 Bảo vệ hệ thống lưu trữ dữ liệu ảo

**Các biện pháp bảo vệ hệ thống lưu trữ dữ liệu ảo bao gồm:**

- Tự động khôi phục khả năng hoạt động của hệ thống lưu trữ dữ liệu được kết nối với hạ tầng ảo trong trường hợp một hoặc nhiều thành phần của nó bị hỏng;
- Chặn quyền truy cập vào các đối tượng của hạ tầng ảo đối với các đối tượng truy cập không qua quy trình xác thực;
- Bảo vệ khỏi truy cập trái phép vào thông tin xác thực được nhập bởi các đối tượng truy cập trong hạ tầng ảo;
- Nhận dạng và xác thực các đối tượng truy cập khi họ truy cập cục bộ hoặc từ xa vào các đối tượng của hạ tầng ảo;
- Kiểm soát việc nhập (xuất) thông tin vào (ra khỏi) hệ thống lưu trữ dữ liệu, được kết nối với hạ tầng ảo;
- Kiểm soát tính toàn vẹn của các dữ liệu được lưu trữ trên các phương tiện thông tin máy móc được kết nối với hạ tầng ảo;
- Đảm bảo kênh, tuyến đường truyền tin cậy trong/ra khỏi hệ thống lưu trữ dữ liệu được kết nối với hạ tầng ảo;
- Kiểm tra sự hiện diện của phần mềm độc hại trong môi trường hệ điều hành của hypervisor hệ thống lưu trữ dữ liệu;
- Phân chia dữ liệu dựa trên mức độ bảo mật của thông tin được xử lý giữa các thành phần của hệ thống lưu trữ dữ liệu, giữa các phương tiện lưu trữ thông tin riêng lẻ;
- Đăng ký các thay đổi về quyền truy cập vào thông tin được lưu trữ trong hệ thống lưu trữ dữ liệu;
- Mã hóa các tệp ảnh của phần mềm ảo hóa và máy ảo, cũng như các tệp ảnh được sử dụng cho hoạt động của hệ thống tệp ảo, chứa thông tin hạn chế.

## 6.4 Bảo vệ các kênh truyền dữ liệu ảo

**Các biện pháp bảo vệ kênh truyền dữ liệu ảo bao gồm:**

- Tự động khôi phục khả năng hoạt động của hệ thống lưu trữ dữ liệu được kết nối với hạ tầng ảo trong trường hợp một hoặc nhiều thành phần của nó bị hỏng;
- Thay đổi tự động tuyến đường truyền gói tin mạng giữa các thành phần của hạ tầng ảo bên trong hypervisor;
- Chặn quyền truy cập vào các đối tượng của hạ tầng ảo đối với các đối tượng truy cập không qua quy trình xác thực;
- Phát hiện, phân tích và chặn các kênh truyền thông ẩn bên trong hạ tầng ảo, vượt qua các biện pháp bảo vệ thông tin;
- Bảo vệ khỏi truy cập trái phép vào thông tin xác thực của các đối tượng truy cập trong hạ tầng ảo;
- Kiểm soát việc truyền các thông điệp thông tin dịch vụ, được truyền trong các mạng ảo của hệ điều hành chủ, theo các đặc điểm: thành phần, khối lượng, v.v.;
- Đảm bảo tính cách ly của các luồng dữ liệu khác nhau, được truyền và xử lý bởi các thành phần của hạ tầng ảo của hệ điều hành chủ;
- Mã hóa thông tin hạn chế được truyền qua các kênh truyền dữ liệu ảo và vật lý của hypervisor.

## 6.5 Bảo vệ các thiết bị ảo riêng lẻ xử lý, lưu trữ và truyền dữ liệu

**Các biện pháp bảo vệ các thiết bị ảo riêng lẻ xử lý, lưu trữ và truyền dữ liệu bao gồm:**

- Chặn quyền truy cập vào các đối tượng của hạ tầng ảo đối với các đối tượng truy cập không qua quy trình xác thực;
- Bảo vệ khỏi truy cập trái phép vào thông tin xác thực được nhập bởi các đối tượng truy cập trong hạ tầng ảo;
- Bảo vệ khỏi truy cập trái phép vào thông tin xác thực của các đối tượng truy cập được lưu trữ trong các thành phần của hạ tầng ảo;
- Nhận dạng và xác thực các đối tượng truy cập khi họ truy cập cục bộ hoặc từ xa vào các đối tượng của hạ tầng ảo;
- Kiểm soát truy cập của các đối tượng truy cập vào các công cụ cấu hình của phần cứng ảo;
- Kiểm soát truy cập vào các tệp ảnh của phần mềm ảo hóa và máy ảo, cũng như các tệp ảnh được sử dụng cho hoạt động của hệ thống tệp ảo;
- Kiểm soát tính toàn vẹn của các tệp chứa cài đặt phần mềm ảo hóa và máy ảo;
- Đảm bảo quyền truy cập được kế thừa từ cấp độ quản lý xuống cấp độ ảo hóa và phần cứng;
- Đảm bảo tính xác thực của các kết nối mạng (phiên tương tác) trong hạ tầng ảo, bao gồm việc bảo vệ khỏi sự thay thế các thiết bị và dịch vụ mạng;
- Tắt các giao thức mạng không sử dụng của các thành phần trong hạ tầng ảo thuộc hệ điều hành chủ;
- Cung cấp các quyền truy cập cá nhân vào các đối tượng truy cập cho một hoặc nhiều thành phần của hạ tầng ảo;
- Kiểm tra sự hiện diện của phần mềm độc hại trong bộ nhớ và các tệp cấu hình của hypervisor và/hoặc máy ảo;
- Sao lưu dữ liệu quan trọng của hệ thống ảo hóa và máy ảo.

## 6.6 Bảo vệ các phương tiện bảo vệ thông tin ảo và các phương tiện bảo vệ thông tin được thiết kế để sử dụng trong môi trường ảo hóa

**Các biện pháp bảo vệ các phương tiện bảo vệ thông tin ảo và các phương tiện bảo vệ thông tin được thiết kế để sử dụng trong môi trường ảo hóa bao gồm:**

- Tự động khôi phục tất cả các chức năng của các phương tiện bảo vệ thông tin trong hệ thống thông tin;
- Bảo vệ khỏi truy cập trái phép vào thông tin xác thực được nhập bởi các đối tượng truy cập trong hạ tầng ảo;
- Bảo vệ khỏi truy cập trái phép vào thông tin xác thực được lưu trữ trong các thành phần của hạ tầng ảo;
- Nhận dạng và xác thực các đối tượng truy cập khi họ truy cập cục bộ hoặc từ xa vào các đối tượng của hạ tầng ảo;
- Đảm bảo kênh truyền tin cậy giữa các thành phần bảo vệ thông tin trong hạ tầng ảo;
- Mã hóa thông tin hạn chế được truyền qua các kênh vật lý và ảo.
