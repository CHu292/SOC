# 3 Lớp vật lý của mô hình OSI
Lớp vật lý (Physical) là lớp thấp nhất trong mô hình OSI. Nó thực hiện việc truyền một luồng bit nhận được từ lớp liên kết (Data Link) thông qua môi trường vật lý dưới dạng tín hiệu điện, quang học hoặc vô tuyến. Lớp vật lý chịu trách nhiệm thiết lập, duy trì và hủy kích hoạt kênh giữa các hệ thống đầu cuối, xác định các kênh, thông báo về việc xảy ra lỗi và lỗi, đồng thời, nếu cần, lắng nghe các kênh để xác định hoạt động trong đó. Liên minh Viễn thông Quốc tế (International Telecommunication Union - ITU) đã áp dụng một số tiêu chuẩn lớp vật lý. Các tiêu chuẩn lớp vật lý do Liên minh Công nghiệp Điện tử (Electronics Industries Alliance- EIA) và Hiệp hội Công nghiệp Viễn thông (Telecommunications Industry Association, - TIA) phát triển được biết đến và sử dụng rộng rãi. Thông số kỹ thuật của lớp vật lý mô tả chi tiết các giao diện cơ, quang, điện, chức năng với môi trường truyền dẫn: điện áp, tần số, bước sóng, đầu nối, số lượng và chức năng của các tiếp điểm, sơ đồ mã hóa tín hiệu, v.v. Lớp vật lý cũng xem xét các vấn đề liên quan đến cấu trúc liên kết vật lý của mạng.


## 3.1 Khái niệm về đường truyền và kênh liên lạc

Đường truyền thông được sử dụng để truyền tín hiệu giữa các hệ thống tương tác trong mạng máy tính.

Theo nghĩa hẹp, thuật ngữ liên kết truyền tải hoặc **đường truyền** (transmission link, link) dùng để chỉ môi trường vật lý mà qua đó tín hiệu được truyền giữa hai hệ thống đầu cuối. Tín hiệu được tạo ra bằng các phương tiện kỹ thuật đặc biệt (máy phát, bộ khuếch đại, bộ ghép kênh, v.v.) liên quan đến thiết bị mạng.

**Môi trường truyền dẫn (transmission medium)** hoặc môi trường vật lý là một chất liệu mà qua đó tín hiệu được truyền đi.

Mạng máy tính sử dụng hai loại phương tiện truyền dẫn: cáp và không dây.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_1_Types_of_transmission_media.png" alt="Hình 3.1 - Các loại phương tiện truyền dẫn" width="1000">
</p>
<p align="center"><b>Hình 3.1 - Các loại phương tiện truyền dẫn"</b></p>

Cơ sở của phương tiện truyền dẫn không dây là bầu khí quyển của trái đất hoặc không gian bên ngoài mà sóng điện từ lan truyền qua đó. Phương tiện truyền dẫn cáp sử dụng nhiều loại cáp: cáp đồng trục, cáp quang, cáp xoắn đôi. Việc truyền dữ liệu tới chúng được thực hiện bằng tín hiệu điện (dòng điện) hoặc tín hiệu quang (ánh sáng).

Theo nghĩa rộng, thuật ngữ “đường truyền - communication line” trong lĩnh vực mạng máy tính dùng để chỉ một kênh liên lạc.

**Kênh liên lạc (channel, data link)** là một tập hợp gồm một hoặc nhiều phương tiện truyền dẫn vật lý và thiết bị tạo kênh (mạng) cung cấp khả năng truyền dữ liệu giữa các hệ thống tương tác dưới dạng tín hiệu tương ứng với loại phương tiện vật lý.

Trong bối cảnh này, thuật ngữ "đường truyền" và "kênh liên lạc" là đồng nghĩa.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_2_Communication_channel.png" alt="Hình 3.2 - Kênh liên lạc" width="1000">
</p>
<p align="center"><b>Hình 3.2 - Kênh liên lạc</b></p>

Có các kênh **vật lý (physical link)** và **kênh logic (logical link)**. Kênh liên lạc vật lý là phương tiện truyền tín hiệu giữa các hệ thống tương tác. Tùy thuộc vào loại tín hiệu truyền và môi trường vật lý được sử dụng để phân phối, các kênh vật lý được chia thành điện (cặp xoắn, cáp đồng trục), quang (cáp quang) và không dây (kênh vô tuyến, kênh hồng ngoại, v.v.).

Các kênh logic được thiết lập giữa các giao thức của bất kỳ lớp nào trong mô hình OSI của các hệ thống tương tác và xác định đường dẫn dữ liệu được truyền từ nguồn đến máy thu thông qua một hoặc một chuỗi các kênh vật lý.

Khi đặt một số kênh logic trong một kênh vật lý, tài nguyên của kênh vật lý được phân phối giữa các kênh logic bằng phương pháp ghép kênh.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_3_Physical_and_logical_communication_channels.png" alt="Hình 3.3 - Các kênh truyền thông vật lý và logic" width="1000">
</p>
<p align="center"><b>Hình 3.3 - Các kênh truyền thông vật lý và logic</b></p>


Các kênh truyền liên lạc (đường truyền) có thể được phân loại dựa trên các đặc điểm sau:

- theo loại môi trường vật lý;
- theo kiểu trình bày thông tin được truyền đi;
- theo hướng truyền dữ liệu;
- theo thời gian tồn tại;
- bằng phương thức kết nối;
- về mặt băng thông.

Tùy thuộc vào loại trình bày thông tin được truyền, các kênh được chia thành kênh analog (liên tục), dành cho việc truyền tín hiệu liên tục và **rời rạc**, được sử dụng để truyền tín hiệu rời rạc (kỹ thuật số).

Tùy thuộc vào hướng truyền dữ liệu, các kênh được phân biệt:

- đơn giản (**simplex**), là chế độ truyền tín hiệu đơn giản và hiệu quả, được sử dụng trong các ứng dụng yêu cầu giao tiếp một chiều.
- bán song công (**half-duplex**),  là chế độ truyền tín hiệu hiệu quả, được sử dụng trong các ứng dụng yêu cầu giao tiếp hai chiều nhưng không đồng thời.
- song công (**full duplex**), là chế độ truyền tín hiệu hiệu suất cao, được sử dụng trong các ứng dụng yêu cầu giao tiếp hai chiều đồng thời.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_4_Simplex.png" alt="Hình 3.4 - Simplex" width="700">
</p>
<p align="center"><b>"Hình 3.4 - Simplex</b></p>


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_5_half_duplex.png" alt="Hình 3.5 - Half Duplex" width="700">
</p>
<p align="center"><b>"Hình 3.5 - Half Duplex</b></p>

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_6_Full_Duplex.png" alt="Hình 3.6 - Full Duplex" width="700">
</p>
<p align="center"><b>"Hình 3.6 - Full Duplex</b></p>


Các kênh cũng có thể được phân loại theo thời gian sẵn có của người đăng ký. Các kênh giữa các hệ thống đầu cuối có sẵn để truyền dữ liệu dài hạn nhờ kết nối cố định với các đặc tính cụ thể được gọi là **kênh chuyên dụng (dedicated)** hoặc **kênh không chuyển mạch (non-switched)**. Các kênh liên lạc chỉ có thể truyền dữ liệu sau khi thiết lập kết nối giữa các hệ thống tương tác được gọi là **kênh chuyển mạch (switched)** hoặc **kênh tạm thời (temporary)**. Kênh này chỉ tồn tại trong suốt phiên kết nối, tức là chỉ trong thời gian cần thiết để truyền dữ liệu.

Theo phương thức kết nối, các kênh được chia thành: “điểm-điểm” **(point-to-point)**, “điểm-đa điểm” **(point-to-multipoint)**, “đa điểm” **(multipoint)**. Liên kết point-to-point chỉ kết nối hai nút hoặc hai hệ thống truyền thông. Liên kết point-to-multipoint kết nối một hệ thống trung tâm node (nút) với một nhóm các hệ thống node (nút) khác. Liên kết multipoint cho phép một nhóm nút hoặc hệ thống kết nối với nhau.

Một đặc tính quan trọng của kênh liên lạc là **băng thông (bandwidth)** của nó. Tùy thuộc vào băng thông (sự khác biệt giữa tần số cắt của băng thông) và phương thức truyền tín hiệu, các kênh được chia thành kênh **băng thông cơ sở (baseband channel)** và kênh **băng thông rộng (broadband channel)**.

Kênh băng thông cơ sở được đặc trưng bởi sự đơn giản và chi phí triển khai thấp và do đó được sử dụng rộng rãi trong các mạng cục bộ (từ “BASE” trong tên của các thông số kỹ thuật của lớp vật lý Ethernet (ví dụ: 10BASE-T, 100BASE-FX, 1000BASE-SX ) biểu thị việc truyền băng cơ sở). Tín hiệu qua kênh băng thông cơ sở được truyền trong tần số cở bản, tức là không điều chế sóng mang, với toàn bộ băng thông chỉ được sử dụng để truyền một tín hiệu.

Không giống như kênh băng thông cơ sở, toàn bộ băng thông của kênh băng rộng được phân chia giữa một số kênh logic bằng kỹ thuật ghép kênh, cho phép tín hiệu được truyền đồng thời và độc lập giữa nhiều cặp hệ thống liên lạc. Các công nghệ truy cập băng thông rộng (ví dụ: xDSL, PowerLine (PLC), 3G (UMTS), 4G (LTE)) được sử dụng để tổ chức kết nối với một loạt dịch vụ do các nhà khai thác viễn thông cung cấp.


## 3.2 Tín Hiệu

Việc truyền dữ liệu qua các kênh liên lạc được thực hiện bằng cách sử dụng biểu diễn vật lý của chúng - tín hiệu điện (dòng điện), quang (ánh sáng) hoặc điện từ.

Nếu chúng ta coi tín hiệu là hàm của thời gian thì nó có thể là:

- analog (liên tục) - giá trị của nó thay đổi liên tục theo thời gian;
- kỹ thuật số (rời rạc) - có số lượng giá trị hữu hạn, thường nhỏ.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_7_Analog_signal.png" alt="Hình 3.7 - Analog Signal" width="700">
</p>
<p align="center"><b>"Hình 3.7 - Analog Signal</b></p>

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_8_Digital_signal.png" alt="Hình 3.8 - Digital Signal" width="700">
</p>
<p align="center"><b>"Hình 3.8 - Digital Signal</b></p>

Loại tín hiệu đơn giản nhất là tín hiệu tuần hoàn **(periodic signal)**. Dạng đơn giản nhất của tín hiệu tuần hoàn là tín hiệu điều hòa **(harmonic signal)**.

**Tín hiệu tuần hoàn** là một loại ảnh hưởng khi hình dạng tín hiệu được lặp lại sau một khoảng thời gian T nhất định, được gọi là một khoảng thời gian.

**Tín hiệu điều hòa** là một dao động điều hòa lan truyền trong không gian theo thời gian, mang theo thông tin hoặc một số loại dữ liệu.

**Dao động điều hòa** là dao động trong đó một đại lượng vật lý (hoặc bất kỳ đại lượng nào khác) thay đổi theo thời gian theo định luật hình sin hoặc cosin.

Nói chung, tín hiệu điều hòa có thể được xác định bởi ba tham số: biên độ cực đại A, pha φ và tần số ƒ. Biên độ cực đại là giá trị hoặc cường độ tối đa của tín hiệu theo thời gian; nó thường được đo bằng vôn. Tần số là số dao động xảy ra trong một đơn vị thời gian. Đơn vị của tần số là Hz. Pha là thước đo sự dịch chuyển thời gian tương đối trong một khoảng thời gian tín hiệu cụ thể. Pha được đo bằng radian hoặc độ.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_9_Harmonic_signal.png" alt="Hình 3.9 - Tín hiệu điều hòa" width="700">
</p>
<p align="center"><b>"Hình 3.9 - Tín hiệu điều hòa</b></p>

Tín hiệu analog cơ bản là sóng hình sin. Nói chung, các dao động điều hòa thay đổi theo định luật hình sin có thể được biểu diễn dưới dạng sau:

$$ 
y(t) = A \sin(\omega t + \varphi_0) = A \sin(2 \pi f t + \varphi_0), (3.1)
$$

Trong đó:
- $$A$$ là biên độ tín hiệu;
- $$\omega$$ là tần số góc: $$\omega = 2 \pi f$$;
- $$f$$ là tần số, được tính bằng $$f = \frac{1}{T}$$, nghịch đảo của chu kỳ $$T$$;
- $$\varphi_0$$ là pha ban đầu của tín hiệu điều hòa;
- $$t$$ là thời gian.

Giả sử rằng tín hiệu thực được truyền qua kênh liên lạc là tín hiệu tuần hoàn. Trong trường hợp này, nó có thể được biểu diễn dưới dạng chuỗi Fourier,tức là phân tích thành các thành phần hình sin:

$$
x(t) = C_0 + \sum_{i=1}^{\infty} \left( A_i \cos(i \omega_1 t) + B_i \sin(i \omega_1 t) \right) = C_0 + \sum_{i=1}^{\infty} C_i \cos(i \omega_1 t - \varphi_i), (3.2)
$$

Trong đó:
- $$i$$ — số thứ tự của điều hòa;  
- $$C_i = \sqrt{A_i^2 + B_i^2}$$ — biên độ,  
- $$\varphi_i$$ — pha ban đầu của điều hòa thứ $$i$$;  
- $$\omega_1 = 2 \pi f = \frac{2 \pi}{T}$$ — tần số cơ bản;  
- $$t$$ — thời gian.

Nhà khoa học người Pháp J.B. Fourier đã chứng minh rằng bất kỳ sự thay đổi thời gian nào của một hàm số nào đó đều có thể được tính gần đúng như một tổng hữu hạn hoặc vô hạn của một chuỗi dao động điều hòa có biên độ, tần số và pha ban đầu khác nhau.

Nói cách khác, bất kỳ tín hiệu tuần hoàn nào (analog hoặc digital signal) được mô tả bằng hàm phức tạp của thời gian đều có thể được biểu diễn dưới dạng tổng vô hạn hoặc hữu hạn của các hình sin có tần số là bội số của tần số cơ bản $$\omega_1$$ và với biên độ và pha ban đầu được chọn đúng. Các thuật ngữ riêng lẻ được gọi là sóng điều hòa. Dao động của tần số cơ bản $$\omega_1$$ được gọi là sóng điều hòa đầu tiên hay sóng điều hòa cơ bản của tín hiệu; sóng điều hòa bậc hai gọi là dao động có tần số $$2\omega_1$$; sóng điều hòa thứ ba là dao động có tần số $$3\omega_1$$, v.v.

Thành phần hằng số $$C_0$$ đơn giản là giá trị trung bình của hàm x(t) và thường không có trong thực tế.

Từ tập hợp các sóng điều hòa tạo nên tín hiệu, biên độ và phổ pha được tách biệt và phân biệt. Phổ biên độ là tập hợp các giá trị $$C_1$$. Về mặt đồ họa, phổ được biểu diễn theo tọa độ $$C_i$$ và $$\omega$$, như trong Hình 3.10. Độ dài của các đoạn thẳng đứng biểu thị biên độ của các sóng điều hòa tương ứng; những đoạn này được gọi là vạch quang phổ. Biên độ và phổ pha xác định duy nhất tín hiệu. Tuy nhiên, đối với nhiều bài toán thực tế, chỉ cần giới hạn ở phổ biên độ là đủ, để cho ngắn gọn gọi là phổ.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_10_Signal_spectrum.png" alt="Hình 3.10 - Phổ" width="700">
</p>
<p align="center"><b>"Hình 3.10 - Sự hình thành tín hiệu từ tổng của 4 sóng điều hòa đầu tiên và sơ đồ biên độ phổ của tín hiệu tuần hoàn</b></p>

Trong trường hợp tổng quát, tổng công thức (3.2) biểu thị một chuỗi vô hạn. Nhưng thực tế không có tín hiệu nào trong tự nhiên có phổ vô hạn. Phần năng lượng chiếm ưu thế của tín hiệu thực tập trung ở một vùng (dải) tần số giới hạn và bản thân tín hiệu đó được biểu diễn dưới dạng tổng hữu hạn của các dao động điều hòa, bởi vì biên độ của các sóng điều hòa, bắt đầu từ một số n nhất định, nhỏ đến mức có thể bỏ qua. Vì vậy, trong thực tế, tín hiệu được biểu diễn bằng các hàm có phổ giới hạn. Khoảng trên thang tần số chứa phổ giới hạn được gọi là **độ rộng phổ**.

Khi truyền tín hiệu qua kênh liên lạc, hình dạng của nó bị biến dạng do sự biến dạng không đồng đều của các sóng điều hòa ở các tần số khác nhau. Điều này xảy ra do các thông số vật lý của kênh liên lạc khác với các thông số lý tưởng.Tín hiệu bị ảnh hưởng bởi các yếu tố như suy giảm, tiếng ồn và nhiễu. Tuy nhiên, yếu tố chính ảnh hưởng đến hình dạng tín hiệu là băng thông của kênh truyền thông. Để truyền tín hiệu mà không bị biến dạng đáng kể, kênh liên lạc phải có băng thông không nhỏ hơn độ rộng phổ của tín hiệu được truyền.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_11_The_influence_of_physical_parameters_of_the_transmission_medium_on_the_signal.png" alt="Hình 3.11 - Ảnh hưởng của các thông số vật lý của môi trường truyền dẫn đến tín hiệu" width="700">
</p>
<p align="center"><b>"Hình 3.11 - Ảnh hưởng của các thông số vật lý của môi trường truyền dẫn đến tín hiệu</b></p>


## 3.3 Đặc điểm chính của kênh liên lạc

Các đặc điểm chính của kênh liên lạc (đường truyền), ảnh hưởng đáng kể đến chất lượng truyền tín hiệu, bao gồm:

- băng thông (bandwidth);
- suy giảm (attenuation);
- khả năng chống ồn (noise immunity);
- thông lượng (noise immunity);
- độ tin cậy của việc truyền dữ liệu (data transmission reliability).

### 3.3.1 Băng thông - Bandwidth

**Băng thông** là dải tần trong đó đáp ứng tần số biên độ (amplitude-frequency response - AFC) của kênh liên lạc (đường truyền) đủ đồng nhất để đảm bảo truyền tín hiệu mà không bị biến dạng đáng kể về hình dạng của nó.

Băng thông F được định nghĩa là sự chênh lệch giữa tần số trên $$f_{upper}$$ và tần số dưới $$f_{lower}$$ của phần đáp ứng tần số mà tại đó công suất tín hiệu giảm không quá 2 lần so với giá trị cực đại: $$F=f_P{upper}-f_{lower}$$ (xấp xỉ tương ứng với −3 dB).

Băng thông được đo bằng (Hz).

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_12_Bandwidth_of_the_communication_channel.png" alt="Hình 3.12  Băng thông kênh liên lạc" width="700">
</p>
<p align="center"><b>"Hình 3.12 -  Băng thông kênh liên lạc</b></p>

Băng thông ảnh hưởng rất lớn đến tốc độ truyền dữ liệu tối đa có thể qua kênh truyền thông và phụ thuộc vào loại môi trường truyền dẫn cũng như sự hiện diện của các bộ lọc tần số trong kênh.

Các tín hiệu bao gồm một tập hợp lớn các sóng điều hòa, nhưng máy thu chỉ có thể nhận được những sóng điều hòa có tần số nằm trong băng thông của kênh. Băng thông của kênh càng rộng, tốc độ truyền dữ liệu có thể càng cao và các sóng hài tần số cao của tín hiệu càng có thể truyền được. Nếu các sóng hài có biên độ đóng góp chính vào tín hiệu kết quả rơi vào băng thông của kênh, hình dạng tín hiệu sẽ thay đổi không đáng kể và tín hiệu sẽ được nhận diện đúng bởi máy thu.

Ngược lại, hình dạng tín hiệu sẽ bị méo đáng kể, dẫn đến giảm tốc độ truyền thông qua kênh do gặp vấn đề trong việc nhận diện tín hiệu, gây ra lỗi liên lạc và yêu cầu truyền lại.



<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_13_The_influence_of_bandwidth_on_the_signal.png" alt="Hình 3.13 Ảnh hưởng của băng thông đến tín hiệu" width="700">
</p>
<p align="center"><b>"Hình 3.13 Ảnh hưởng của băng thông đến tín hiệu</b></p>

### 3.3.2 Suy giảm

Khi truyền tín hiệu qua kênh liên lạc, tín hiệu sẽ bị suy giảm dần, điều này do các đặc tính vật lý và kỹ thuật của môi trường truyền dẫn và các thiết bị mạng được sử dụng. Để tín hiệu có thể được nhận diện chính xác tại điểm tiếp nhận, mức suy giảm này không được vượt quá một giá trị ngưỡng nhất định.

Suy giảm (attenuation) là độ lớn cho thấy mức độ giảm của công suất (biên độ) tín hiệu tại đầu ra của kênh truyền so với công suất (biên độ) tín hiệu tại đầu vào. Hệ số suy giảm $$d$$ được đo bằng decibel (dB) trên một đơn vị chiều dài và được tính theo công thức sau:

$$
d \, [\text{dB}] = 10 \log \frac{P_{\text{out}}}{P_{\text{in}}} (3.3)
$$


trong đó $$P_{\text{out}}$$ là công suất tín hiệu đầu ra (out signal); $$P_{\text{in}}$$ là công suất tín hiệu đầu vào (P_in signal).

Suy giảm đặc trưng cho cả tín hiệu analog và tín hiệu số (digital). Mức độ suy giảm tăng lên khi tần số của tín hiệu tăng: tần số càng cao thì tín hiệu càng dễ bị suy giảm. Vì lý do này, các thiết bị thu của các thiết bị tốc độ cao sẽ gặp khó khăn đáng kể hơn trong việc nhận diện tín hiệu gốc.

Suy giảm tín hiệu ảnh hưởng đến khoảng cách mà tín hiệu có thể đi qua giữa hai điểm mà không cần khuếch đại hoặc phục hồi. Suy giảm là một trong những thông số quan trọng được xác định cho các loại cáp (cặp xoắn, cáp quang, cáp đồng trục). Cáp có độ suy giảm càng thấp thì chất lượng càng cao. Do đó, khi thiết kế các kênh truyền dẫn có dây, cần xem xét các đặc tính của cáp và sử dụng các loại cáp có độ suy giảm thấp nhất để đạt được chiều dài kênh tối đa.

### 3.3.3 Khả năng chống nhiễu

Trong kênh liên lạc thực tế, có tồn tại nhiễu, do các đặc tính của môi trường truyền dẫn, thiết bị tạo kênh, và tác động của các trường điện từ từ các thiết bị điện tử khác nhau. Do ảnh hưởng của các nhiễu này, các lỗi xuất hiện trong kênh truyền.

Một trong những chỉ số quan trọng nhất của kênh liên lạc là khả năng chống nhiễu của nó, được hiểu là khả năng của kênh trong việc chống lại tác động của nhiễu. Khả năng chống nhiễu dựa trên khả năng phân biệt tín hiệu với nhiễu với độ tin cậy nhất định. Vì vậy, khi xây dựng kênh liên lạc, cần phải xem xét các nhiễu có thể xảy ra và tối đa hóa sự khác biệt giữa chúng và tín hiệu.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_14_The_influence_of_interference_on_the_communication_channel.png" alt="Hình 3.14 Ảnh hưởng của nhiễu lên kênh truyền thông" width="700">
</p>
<p align="center"><b>"Hình 3.14 Ảnh hưởng của nhiễu lên kênh truyền thông</b></p>


Tùy thuộc vào nguồn gốc phát sinh và đặc tính tác động của chúng, nhiễu được chia thành nhiễu bên trong, nhiễu bên ngoài và nhiễu tương hỗ. 

**Nhiễu bên trong**, hay còn gọi là nhiễu nội tại, phát sinh từ các nguồn bên trong kênh này và xuất hiện ngay sau khi thiết bị liên lạc được bật lên. Chúng chủ yếu bao gồm nhiễu nhiệt, nhiễu chập, nhiễu tiếp xúc và nhiễu xung, và hầu như không thể loại bỏ được.

**Nhiễu bên ngoài** được chia thành nhiễu công nghiệp, nhiễu vô tuyến, nhiễu khí quyển và nhiễu vũ trụ. 
-  Nhiễu công nghiệp (giao thoa điện từ, hay còn gọi là EMI - Electro Magnetic Interference) được tạo ra do tác động của các trường điện từ từ các thiết bị điện khác nhau đến kênh liên lạc: đèn huỳnh quang, thiết bị gia dụng, máy tính, hệ thống vô tuyến, đường dây điện, thiết bị điện của các xí nghiệp công nghiệp, thiết bị y tế, mạng tiếp xúc của các phương tiện giao thông điện (như tàu điện, xe buýt điện v.v.), quảng cáo đèn neon và nhiều thiết bị tương tự. 
- Nhiễu vô tuyến (nhiễu tần số vô tuyến, RFI - Radio Frequency Interference) phát sinh từ bức xạ của các đài phát thanh với các mục đích khác nhau, có phổ tần vì một lý do nào đó trùng lên phổ tín hiệu hữu ích của kênh liên lạc.
- Nhiễu khí quyển bao gồm các nhiễu do hiện tượng khí quyển khác nhau gây ra: bão từ, cực quang, sấm sét, v.v. - Nhiễu vũ trụ bao gồm các nhiễu điện từ được tạo ra từ bức xạ của Mặt Trời, các ngôi sao nhìn thấy và không nhìn thấy, các tinh vân trong các dải tần số tương ứng.


**Nhiễu tương hỗ** (hay nhiễu xuyên âm, crosstalk) xảy ra khi truyền thông tin qua các kênh liền kề - tín hiệu truyền qua một kênh liên lạc gây ra hiệu ứng không mong muốn ở kênh khác (xuất hiện nhiễu tín hiệu).

Các kênh liên lạc không dây là những kênh ít được bảo vệ nhất khỏi ảnh hưởng của nhiễu. Chúng chịu tác động của cả nhiễu bên ngoài và nhiễu xuyên âm. Trong các mạng không dây gia đình, nhiễu bên ngoài phát sinh từ các thiết bị như lò vi sóng, máy tính, điện thoại di động, v.v. Còn nhiễu xuyên âm liên quan đến nhiễu từ các thiết bị không dây khác hoạt động trên cùng tần số. Điều này đặc biệt phổ biến ở các tòa nhà chung cư, nơi các mạng gia đình chủ yếu được xây dựng bằng công nghệ không dây.


Trong số các kênh cáp, kênh sử dụng cáp điện dễ bị ảnh hưởng bởi nhiễu nhất. Để chống lại nhiễu, các nhà sản xuất cáp điện áp dụng các biện pháp như che chắn (shielding) và xoắn cặp dây dẫn. Che chắn được sử dụng để bảo vệ khỏi nhiễu điện từ và nhiễu vô tuyến. Lớp che chắn là một lớp lưới kim loại hoặc lá kim loại bao quanh từng dây hoặc nhóm dây trong cáp, đóng vai trò như một rào cản ngăn chặn các tín hiệu tương tác.

Bản thân cáp điện cũng là nguồn phát bức xạ điện từ, có thể gây ra nhiễu xuyên âm. Trong các loại cáp xoắn đôi, nhiễu này được biết đến với tên gọi nhiễu xuyên âm đầu gần (NEXT - Near End Cross Talk) và nhiễu xuyên âm đầu xa (FEXT - Far End Cross Talk), phát sinh từ sự ảnh hưởng lẫn nhau của các trường điện từ của tín hiệu được truyền qua các cặp dây dẫn khác nhau. Để giảm thiểu các trường điện từ này, cặp dây dẫn trong cáp xoắn đôi được xoắn lại với nhau.


Các kênh quang học là loại được bảo vệ tốt nhất khỏi nhiễu. Cáp quang không bị ảnh hưởng bởi nhiễu điện từ (EMI), nhiễu tần số vô tuyến (RFI), sét và các xung điện áp cao. Ngoài ra, cáp quang cũng không tạo ra bất kỳ nhiễu điện từ hay nhiễu tần số vô tuyến nào.

Để nhiễu không làm giảm đáng kể chất lượng truyền dẫn, cần phải hạn chế ảnh hưởng của nó. Các phương pháp chống nhiễu nhằm đảm bảo mức độ tín hiệu tại nơi nhận sao cho đáp ứng được chất lượng tín hiệu yêu cầu.

Một trong những thông số quan trọng của kênh truyền dẫn, cho phép đánh giá tác động gây nhiễu của nhiễu lên tín hiệu, là tỷ lệ tín hiệu trên nhiễu (SNR, Signal-to-Noise Ratio). Tỷ lệ này được xác định là tỷ số giữa công suất của tín hiệu $$P_s$$ và công suất của nhiễu (nhiễu) $$P_n$$. Để thuận tiện, biểu thức này thường được biểu diễn bằng decibel (dB).


$$
\text{SNR} \, [\text{dB}] = 10 \cdot \log \left( \frac{P_s}{P_n} \right) (3.4)
$$


trong đó $$P_s$$ là công suất tín hiệu (signal power); $$P_n$$ là công suất nhiễu -noise power (nhiễu loạn).

Khi tỷ lệ tín hiệu trên nhiễu càng lớn, nhiễu càng ít ảnh hưởng đến tín hiệu hữu ích khi nó được truyền qua kênh liên lạc và giúp máy thu nhận diện tín hiệu tốt hơn.

Để tăng khả năng chống nhiễu của kênh truyền, các phương pháp sau đây được áp dụng:

- Tăng tỷ lệ tín hiệu trên nhiễu;
- Mở rộng phổ tín hiệu;
- Tăng độ dư thừa thông tin;
- Sử dụng mã chống nhiễu;
- Lọc tín hiệu hữu ích.

### 3.3.4 Thông lượng  
Thông lượng (throughput) của kênh truyền là tốc độ truyền thông tin tối đa có thể qua kênh, được xác định bởi các giới hạn của nó. Thông lượng được đo bằng bit trên giây (bit/s hoặc bps — bits per second) và các đơn vị dẫn xuất khác.  

Mối quan hệ giữa thông lượng tối đa và băng thông của kênh truyền đã được Claude Shannon xác định:

$$
C = F \log_2 \left(1 + \frac{P_s}{P_n}\right),
$$


Trong đó $$C$$ là thông lượng tối đa của kênh (bit/s); $$F$$ là băng thông của kênh (Hz); $$P_s$$ là công suất tín hiệu và $$P_n$$ là công suất nhiễu.  

Như có thể thấy từ công thức, thông lượng tối đa của kênh có thể được tăng lên bằng cách mở rộng băng thông $$F$$ hoặc giảm công suất nhiễu trên đường truyền.  

Thuật ngữ "thông lượng" có thể mang ý nghĩa lý thuyết và thực tiễn. Thông thường, nó được sử dụng theo nghĩa thực tế và là thước đo lượng dữ liệu hữu ích được truyền qua một kênh truyền nhất định trong một khoảng thời gian xác định, dưới những điều kiện nhất định. Thông lượng lý thuyết bị giới hạn bởi băng thông hoặc tốc độ truyền dữ liệu của công nghệ cụ thể. Ví dụ, trong đặc tả của Gigabit Ethernet, tốc độ được xác định là 1 Gbit/s. Đối với mạng Gigabit Ethernet, giá trị này sẽ là giới hạn trên của thông lượng. Tuy nhiên, thông lượng thực tế của mạng luôn nhỏ hơn thông lượng lý thuyết, vì nó phụ thuộc vào các tham số của thiết bị kênh truyền, cách tổ chức truyền dữ liệu, số lượng nút được kết nối với kênh truyền. Ngoài ra, thông lượng cũng bị giảm do chi phí quản lý liên quan đến việc truyền các gói tin điều khiển cần thiết cho hoạt động của các giao thức mạng.

Hãy xem các ví dụ liên quan đến công thức Shannon.

**Ví dụ 1.** Phổ của kênh chiếm dải từ 5 MHz đến 15 MHz. Tỷ lệ tín hiệu/nhiễu (SRN) là 24,1 dB. Xác định thông lượng của kênh truyền.

1. Xác định băng thông của kênh (Hz). $$F = 15 \, \text{MHz} - 5 \, \text{MHz} = 10 \, \text{MHz} = 10 \times 10^6 \, \text{Hz}$$.

2. Thực hiện chuyển đổi tỷ lệ tín hiệu/nhiễu từ decibel sang đơn vị thông thường. $$24,1 = 10 \lg(x) \Rightarrow x = 10^{\frac{24,1}{10}} \approx 257$$.

3. Sử dụng công thức Shannon để xác định thông lượng của kênh truyền.

$$
C = 10 \times 10^6 \times \log_2 \left(1 + 257\right) \approx 10 \times 10^6 \times 8,011 \approx 80,11 \, \text{Mbit/s}.
$$

Công thức và tính toán trên cho thấy cách xác định thông lượng kênh dựa trên băng thông và tỷ lệ tín hiệu/nhiễu.



**Ví dụ 2.** Phổ của kênh chiếm dải từ 2401 MHz đến 2423 MHz. Công suất tín hiệu là 150 mW, công suất nhiễu là 10 mW. Xác định thông lượng của kênh truyền.

1. Xác định băng thông của kênh (Hz). $$F = 2423 \, \text{MHz} - 2401 \, \text{MHz} = 22 \, \text{MHz} = 22 \times 10^6 \, \text{Hz}$$.

2. Sử dụng công thức Shannon để xác định thông lượng của kênh truyền.
 
$$
C = 22 \times 10^6 \times \log_2 \left(1 + \frac{150}{10}\right) = 22 \times 10^6 \times 4 = 88 \, \text{Mbit/s}.
$$

Bài toán trên minh họa cách tính thông lượng kênh dựa trên băng thông và tỷ lệ công suất tín hiệu/nhiễu.

**Ví dụ 3.** Độ rộng băng thông của kênh truyền là 100 MHz. Công suất tín hiệu - 20 dBm, công suất nhiễu - 3 dBm. Xác định khả năng truyền tải của kênh liên lạc.

1. Xác định tỷ lệ tín hiệu/nhiễu và thực hiện chuyển đổi giữa decibel và tỷ lệ. $$20 - 3 = 10 \cdot \lg(x) \Rightarrow x = 50$$.

   Cách thứ hai để tính tỷ lệ tín hiệu/nhiễu là chuyển đổi công suất tín hiệu từ dBm sang mW. Có thể sử dụng bảng hoặc tự tính như sau: 20 dBm = 100 mW, 3 dBm = 2.0 mW. Do đó, SRN = $$\frac{100}{2} = 50$$.

2. Theo công thức của Shannon, xác định khả năng truyền tải của kênh liên lạc. 

$$
C = 100 \times 10^6 \times \log_2(1 + 50) \approx 100 \times 10^6 \times 5.672 = 567,2 \, \text{Mbit/s}.
$$

Cần hiểu rõ sự khác biệt giữa tốc độ truyền dữ liệu và tốc độ ký hiệu. **Tốc độ truyền dữ liệu** (information rate, data rate) là tốc độ truyền các bit, đo bằng bit/s và các đơn vị phát sinh khác. \)

**Tốc độ ký hiệu** (symbol rate) hay **tốc độ điều chế** là tốc độ thay đổi các ký hiệu, đo bằng baud hoặc ký hiệu mỗi giây. Mỗi ký hiệu đại diện cho một hoặc nhiều bit thông tin tùy thuộc vào phương pháp mã hóa được chọn.


### 3.3.5 Độ tin cậy của truyền dữ liệu

Chất lượng thông tin được truyền qua kênh liên lạc thường được đánh giá dựa trên độ tin cậy của truyền dữ liệu, tức là mức độ tương ứng giữa thông tin nhận được và thông tin đã truyền. **Độ tin cậy của truyền dữ liệu** được đặc trưng bởi xác suất lỗi trong quá trình nhận mỗi bit dữ liệu truyền, tức là tần suất xuất hiện của các bit bị lỗi. Đôi khi chỉ số này còn được gọi là **tỷ lệ lỗi bit** (Bit Error Rate, BER).

BER được xác định bằng tỷ lệ giữa số bit nhận bị lỗi với tổng số bit đã truyền.

Thông thường, các lỗi xuất hiện chủ yếu do nhiễu và tiếng ồn trong kênh. Đối với các kênh truyền mà không có phương tiện bảo vệ bổ sung, giá trị BER nằm trong khoảng từ $$10^{-4}$$ đến $$10^{-6}$$, còn trong các kênh quang học, BER có thể đạt đến $$10^{-9}$$. Giá trị độ tin cậy của truyền dữ liệu, ví dụ như $$10^{-4}$$, cho biết trung bình cứ 10.000 bit thì có một bit bị sai lệch.

Có thể tăng độ tin cậy của dữ liệu truyền bằng cách nâng cao khả năng chống nhiễu của kênh liên lạc.


## 3.4 Các phương pháp sử dụng chung môi trường truyền tải của kênh liên lạc

Trong thực tế, thường phải thực hiện việc truyền các luồng dữ liệu từ nhiều người dùng qua môi trường truyền tải chung (shared medium), vì việc lắp đặt một kênh liên lạc riêng cho mọi hệ thống tương tác quá đắt đỏ, phức tạp hoặc không khả thi. Thông thường, điều này liên quan đến các hạn chế như mạng điện thoại đã có sẵn, các kênh truyền tải đã được thiết lập, tài nguyên tần số vô tuyến bị phân bổ, hoặc khó khăn trong việc xây dựng các kênh truyền tải mới do cấu trúc đô thị.

Để có thể truyền tải nhiều tín hiệu từ các người dùng khác nhau đồng thời qua cùng một cáp hoặc kênh không dây, người ta sử dụng các phương pháp **ghép kênh** (multiplexing).

**Ghép kênh** (multiplexing) là công nghệ truyền tải dữ liệu của nhiều kênh với thuông lượng thấp hơn qua một kênh có thông lượng cao hơn.

Nhiệm vụ của ghép kênh là phân bổ cho mỗi kênh một khoảng thời gian, tần số và/hoặc mã với sự can thiệp tối thiểu và tận dụng tối đa các đặc điểm của môi trường truyền tải chung.

Kết quả của ghép kênh là trong một kênh vật lý tạo ra một nhóm các kênh logic. Khi đó, **thông lượng** của kênh vật lý được chia sẻ giữa các kênh logic và cần đủ để đảm bảo tốc độ truyền dữ liệu cần thiết cho các kênh logic.

Ghép kênh được thực hiện bằng chương trình hoặc thiết bị gọi là **bộ ghép kênh** (multiplexer, MUX). Bộ ghép kênh kết nối nhóm các kênh tốc độ thấp với một kênh vật lý tốc độ cao.

Quá trình ngược lại của ghép kênh được gọi là **tách kênh** (demultiplexing), và thiết bị hoặc chương trình thực hiện quá trình này gọi là **bộ tách kênh** (demultiplexer, DEMUX). Bộ tách kênh phân phối dữ liệu nhận được từ kênh vật lý chung đến nhóm các kênh đầu ra.

Trong các mạng máy tính, các loại ghép kênh chủ yếu bao gồm:

- ghép kênh theo thời gian (TDM);
- ghép kênh theo tần số (FDM);
- ghép kênh theo bước sóng (WDM);
- ghép kênh với phân chia theo mã (CDM).


### 3.4.1 Ghép kênh theo phân chia thời gian

**Ghép kênh theo phân chia thời gian** (*Time Division Multiplexing, TDM*) hay ghép kênh tạm thời là quá trình chia sẻ băng thông của kênh giữa các hệ thống tương tác trong một khoảng thời gian ngắn. Nói cách khác, tất cả các người gửi sử dụng cùng một dải tần số của kênh chung tại các thời điểm khác nhau. Công nghệ TDM thường được sử dụng trong các kênh truyền dẫn kỹ thuật số.

Mỗi kênh đầu vào được cấp một khoảng thời gian, gọi là *thời gian khe* hoặc *khe thời gian* - Time slot, để truyền tải dữ liệu. Thời gian khe có thể là khoảng thời gian cần thiết để truyền một bit, byte, khung, hoặc gói tin.

Có hai loại ghép kênh theo phân chia thời gian: *đồng bộ* và *không đồng bộ*.

Trong chế độ đồng bộ (*Synchronous Time Division Multiplexing*), thời gian hoạt động của kênh được chia thành các chu kỳ lặp lại, bao gồm các khung TDM. Mỗi khung TDM bắt đầu bằng một chuỗi đồng bộ hóa và được chia thành các khe thời gian có độ dài bằng nhau, mỗi khe dành riêng cho một kênh logic. Các khe thời gian được phân bổ cho tất cả các kênh đầu vào được kết nối với bộ ghép kênh, được đánh số và sắp xếp trong khung TDM theo thứ tự cố định.

Các kênh đầu vào lần lượt truyền các khối dữ liệu có kích thước bằng nhau trong mỗi khe thời gian của mỗi chu kỳ. Hình 3.15 minh họa chế độ ghép kênh theo phân chia thời gian đồng bộ, đảm bảo truyền tải dữ liệu giữa bốn cặp thiết bị. Khối dữ liệu từ cổng 1 của bộ ghép kênh sẽ được truyền trong khe thời gian 1 cho kết nối A1–A2. Khối dữ liệu từ cổng 2 sẽ được truyền trong khe thời gian 2 cho kết nối B1–B2. Khối dữ liệu từ cổng 3 sẽ được truyền trong khe thời gian 3 cho kết nối C1–C2. Cuối cùng, khối dữ liệu từ cổng 4 sẽ được truyền trong khe thời gian 4 cho kết nối D1–D2.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_15_Synchronous_Time_Division_Multiplexing.png" alt=Hình 3.15 Ghép kênh phân chia thời gian đồng bộ" width="700">
</p>
<p align="center"><b>"Hình 3.15 Ghép kênh phân chia thời gian đồng bộ</b></p>


Việc sử dụng phương pháp này có thể dẫn đến tình trạng trong cùng một chu kỳ, một hệ thống không có dữ liệu để truyền, trong khi hệ thống khác lại không đủ thời gian được phân bổ. Khi một thiết bị không có dữ liệu để truyền, khe thời gian được phân cho nó sẽ vẫn trống và không thể được sử dụng bởi thiết bị khác.

Để bộ giải ghép kênh ở đầu kia của kênh truyền có thể đọc chính xác các khối dữ liệu và phân phối chúng vào các kênh đầu ra tương ứng, thứ tự của các khe thời gian trong khung TDM phải được tuân thủ nghiêm ngặt. Mỗi kênh đầu vào trong TDM đồng bộ được nhận dạng bởi vị trí thời gian của nó trong khung, tức là bằng số thứ tự của khe thời gian. Vị trí này được sử dụng làm thông tin địa chỉ.

Để bên nhận có thể xác định điểm bắt đầu của khe thời gian tiếp theo trong khung TDM, cần phải có sự đồng bộ hóa. Đồng bộ hóa có thể thực hiện bằng nhiều cách. Ví dụ, một trong những cách là truyền một chuỗi đồng bộ hóa ở đầu khung TDM, giúp phân biệt giữa các khung với nhau. Việc mất đồng bộ dẫn đến việc bên nhận không thể phân phối chính xác luồng dữ liệu đến các kênh, vì vị trí tương đối của các khe thời gian thay đổi, và do đó thông tin địa chỉ bị mất.


TDM đồng bộ được sử dụng trong các mạng chuyển mạch kênh. Hai kiến trúc cơ bản dựa trên TDM đồng bộ là hệ thống phân cấp số không đồng bộ (*PDH*, *Plesiochronous Digital Hierarchy*), được sử dụng để truyền tín hiệu số của nhiều cuộc gọi điện thoại qua các kênh T1 (1,544 Mbps) và E1 (2 Mbps), và các hệ thống truyền dẫn số *SDH/SONET*, cung cấp khả năng truyền tín hiệu số qua cả dây đồng và cáp quang. Các giao diện *BRI* (*Basic Rate Interface*) và *PRI* (*Primary Rate Interface*) của mạng *ISDN* (*Integrated Services Digital Network*) cũng được sử dụng để vận chuyển dữ liệu dựa trên TDM đồng bộ.

Thông lượng của kênh chung trong TDM đồng bộ được xác định bằng tổng thông lượng của tất cả các kênh đầu vào cộng thêm một số chi phí quản lý. Một trong những nhược điểm chính của chế độ đồng bộ là sự ràng buộc giữa các kênh đầu vào và các khe thời gian. Nếu một thiết bị không có dữ liệu để truyền, thiết bị khác không thể truyền dữ liệu trong khe thời gian đó. Điều này dẫn đến việc sử dụng băng thông không hiệu quả và làm giảm thông lượng của kênh truyền.

Một ưu điểm của TDM đồng bộ là tính minh bạch đối với các giao thức tầng trên, vì nó được thực hiện ở tầng vật lý của mô hình OSI. Trong các khe thời gian, có thể truyền nhiều loại lưu lượng khác nhau: dữ liệu, thoại, video. Vì các hệ thống tương tác nhận được khe thời gian với cùng một số thứ tự trong mỗi chu kỳ, các khối dữ liệu được truyền đi sẽ xuất hiện ở bên nhận trong khoảng thời gian bằng nhau và đến với cùng độ trễ. Do đó, không cần sử dụng bộ đệm, vì luồng dữ liệu được truyền và nhận với cùng một tốc độ.

### 3.4.2 Ghép kênh phân chia theo tần số

Trong ghép kênh tần số hoặc ghép kênh phân chia theo tần số (Frequency Division Multiplexing - FDM), băng thông rộng của kênh vật lý $$F$$ được chia thành $$n$$ dải tần số hẹp $$f \ll F$$, trong mỗi dải tần này tạo ra một kênh logic. Kích thước của các dải tần số $$f$$ có thể khác nhau. Mỗi hệ thống tương tác được chỉ định một dải tần riêng (kênh logic). Các bộ phát có thể gửi tín hiệu đồng thời. Tín hiệu truyền qua các kênh logic khác nhau được đặt trên các tần số sóng mang khác nhau và do đó trong miền tần số không nên chồng chéo nhau. Để loại bỏ ảnh hưởng lẫn nhau của các tín hiệu truyền qua các kênh logic khác nhau, các dải bảo vệ được hình thành giữa chúng, đóng vai trò là biên giới giữa các kênh.

Tuy nhiên, mặc dù có các dải bảo vệ, các thành phần phổ của tín hiệu vẫn có thể vượt quá giới hạn của kênh logic và gây nhiễu cho kênh logic lân cận.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_17_Frequency_Division_Multiplexing.png" alt="Hình 3.17 Ghép kênh phân chia theo tần số" width="900">
</p>
<p align="center"><b>Hình 3.17 Ghép kênh phân chia theo tần số</b></p>


Ưu điểm của ghép kênh tần số là cho phép truyền đồng thời các tín hiệu bởi nhiều hệ thống tương tác. Tuy nhiên, vì mỗi hệ thống được chỉ định một kênh riêng biệt theo cách tĩnh, điều này dẫn đến việc sử dụng không hiệu quả băng thông của kênh truyền chung. Tại một thời điểm, một hệ thống có thể không có dữ liệu để truyền và kênh sẽ để trống, trong khi các hệ thống khác có thể thiếu tài nguyên từ các kênh logic được phân bổ cho chúng. Ngoài ra, sự tồn tại của các dải bảo vệ giữa các kênh logic làm giảm băng thông có sẵn để truyền.

Ghép kênh phân chia theo tần số là một phương pháp ghép kênh được sử dụng rộng rãi trong phát thanh và truyền hình cũng như trong truyền thông di động. Nó cũng được sử dụng trong các mạng dựa trên công nghệ xDSL.

Tuy nhiên, trong ghép kênh tần số, có thể chia băng thông thành các kênh mà không cần sử dụng dải bảo vệ. 

Trong ghép kênh phân chia theo tần số trực giao (Orthogonal Frequency Division Multiplexing - OFDM), toàn bộ băng thông của kênh vật lý được chia thành nhiều tần số con (subcarriers) hoặc các kênh con. Các tần số con này có thể lên đến hàng chục, thậm chí hàng nghìn. Mỗi bộ phát được chỉ định để truyền trên một số tần số con nhất định, được chọn từ nhiều tần số con theo một quy luật xác định. Các tần số con này là trực giao với nhau, nghĩa là việc truyền thông tin trên mỗi tần số con không ảnh hưởng đến các tần số con lân cận. Như được thể hiện trong Hình 3.18, các trung tâm của tần số con được đặt sao cho mức năng lượng tối đa của một tần số con trùng với mức năng lượng tối thiểu của các tần số con khác, mặc dù tín hiệu của chúng chồng chéo nhau trong phổ tần số. Cách sắp xếp này cho phép sử dụng băng thông có sẵn một cách hiệu quả hơn.

Truyền dẫn được thực hiện đồng thời trên tất cả các tần số con. Luồng dữ liệu tốc độ cao ở đầu phát được chia thành $$n$$ luồng tốc độ thấp (với $$n$$ là số lượng tần số con được chỉ định cho bộ phát đó), mỗi luồng trong số đó được điều chế trên một tần số con riêng biệt. Phân bổ các tần số con có thể thay đổi động trong quá trình hoạt động.

Để truyền một tín hiệu phức tạp, bao gồm nhiều tần số con, phép biến đổi Fourier ngược nhanh (IFFT) được sử dụng. Bộ phát sẽ lấy các tín hiệu điều chế từ mỗi kênh con, cộng chúng lại để tạo thành một tín hiệu tổng hợp. Tín hiệu OFDM tổng hợp có thể được xem như một tập hợp các tín hiệu hẹp băng được điều chế chậm, thay vì một tín hiệu rộng băng được điều chế nhanh. Khi nhận tín hiệu, phép biến đổi Fourier nhanh (FFT) sẽ được thực hiện. Tất cả các tần số con được tách ra đồng thời và các thông số mang thông tin của từng tần số con (biên độ và/hoặc pha) được xác định.

Ngoài việc sử dụng băng thông hiệu quả, OFDM còn giúp giảm các hiệu ứng tiêu cực nổi tiếng của hiện tượng đa đường và nhiễu liên ký tự. Tín hiệu OFDM kết hợp nhiều kênh con hẹp băng, mỗi kênh có thể truyền ở tốc độ thấp. Do đó, hệ thống chỉ gặp phải nhiễu liên ký tự ở mức tối thiểu, điều mà các hệ thống tốc độ cao dễ bị ảnh hưởng.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_18_Orthogonal_Frequency_Division_Multiplexing.png" alt="Hình 3.18 Ghép kênh phân chia theo tần số trực giao" width="700">
</p>
<p align="center"><b>Hình 3.18 Ghép kênh phân chia theo tần số trực giao</b></p>



OFDM không phải là một công nghệ mới. Phần lớn các nghiên cứu cơ bản mô tả hoạt động của nó xuất hiện vào những năm 1960. Nó được sử dụng rộng rãi trong mạng không dây chuẩn 802.11, mạng truyền hình cáp, mạng dựa trên dây điện, mạng dựa trên công nghệ xDSL và mạng truyền dữ liệu di động thế hệ thứ 4 (LTE).
