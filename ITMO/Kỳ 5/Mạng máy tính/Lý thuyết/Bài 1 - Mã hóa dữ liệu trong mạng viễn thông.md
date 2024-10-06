# 1. Mã hóa kỹ thuật số

Mã hóa kỹ thuật số của dữ liệu rời rạc được thực hiện bằng cách sử dụng mã xung hoặc mã điện thế. Để biểu diễn các số 0 và số 1 nhị phân, các mã thế sử dụng các giá trị tiềm năng tín hiệu khác nhau và mã xung sử dụng các xung có cực tính hoặc mức giảm tiềm năng khác nhau.

Chất lượng truyền dữ liệu, cụ thể là: độ tin cậy và độ chính xác của việc phân phối, khả năng phát hiện và sửa lỗi xảy ra cũng như chi phí thực hiện, phụ thuộc đáng kể vào phương pháp mã hóa kỹ thuật số đã chọn, do đó, quyết định phần lớn thông lượng của dữ liệu phương tiện truyền dẫn.

Về vấn đề này, để đảm bảo chất lượng truyền dữ liệu, một số yêu cầu được đặt ra đối với các phương thức mã hóa kỹ thuật số:

- Giảm phổ tín hiệu ở cùng tốc độ bit;
- Hỗ trợ đồng bộ hóa giữa máy phát và máy thu tín hiệu do sự hiện diện của các tín hiệu được truyền đi trên cơ sở thực hiện tự đồng bộ hóa;
- Sự vắng mặt của thành phần không đổi trong tín hiệu, làm dịch chuyển phổ tín hiệu sang vùng tần số thấp;
- Khả năng phát hiện lỗi và sửa chúng;
- Chi phí thực hiện phương pháp mã hóa thấp, tùy thuộc vào số lượng mức tín hiệu.

Việc giảm thiểu phổ của tín hiệu thu được sẽ đảm bảo rằng, đối với băng thông kênh liên lạc nhất định, lượng dữ liệu lớn hơn có thể được truyền đi trên một đơn vị thời gian. Điều này có thể được thực hiện, ví dụ, thông qua việc sử dụng ghép kênh tần số bằng cách tổ chức một số kênh logic trong cùng một đường truyền, cho phép tăng tốc độ truyền dữ liệu.

Ngoài ra, trong phổ tín hiệu không được có thành phần trực tiếp, tức là không được có dòng điện một chiều giữa máy phát và máy thu. Điều này là do việc sử dụng các mạch biến áp trong đường dây truyền thông điện để cách ly điện, ngăn cản dòng điện một chiều đi qua. Phổ của tín hiệu thu được phụ thuộc vào:

- Phương pháp mã hóa và điều chế;
- Tốc độ điều chế, ảnh hưởng đến tốc độ truyền dữ liệu;
- Thành phần của dữ liệu được truyền đi.

Để đồng bộ hóa máy phát và máy thu tín hiệu nhằm xác định thời điểm máy thu đọc giá trị của khoảng bit tiếp theo, các phương pháp mã hóa tự đồng bộ đặc biệt được sử dụng. Trong các phương pháp này, việc đồng bộ hóa máy thu với máy phát được thực hiện trên cơ sở dấu hiệu, tức là bất kỳ sự thay đổi đột ngột nào trong tín hiệu, được gọi là biên tín hiệu.

Yêu cầu không có thành phần không đổi trong tín hiệu là do nhu cầu duy trì sự đồng bộ giữa máy thu và máy phát. Ngoài ra, điều mong muốn là tần số thấp hơn của tín hiệu truyền đi khác với 0. Điều này giúp giảm phổ tín hiệu và cũng không cản trở dòng điện một chiều đi qua đường dây truyền thông điện khi có mạch cách ly điện máy biến áp.

Một yêu cầu mong muốn nhưng không bắt buộc đối với các phương pháp mã hóa kỹ thuật số là khả năng phát hiện lỗi và lý tưởng nhất là sửa chúng. Điều này giúp tiết kiệm thời gian vì lỗi được phát hiện ở lớp vật lý. Trong trường hợp này, khung bị lỗi sẽ bị loại bỏ trước khi hoàn tất quá trình nhận vào bộ đệm.

Chi phí thực hiện phương pháp mã hóa kỹ thuật số liên quan đến số lượng mức tín hiệu và càng nhiều mức tín hiệu thì thiết bị thu và phát càng mạnh và do đó, đắt hơn.

Các yêu cầu đối với các phương pháp mã hóa kỹ thuật số là trái ngược nhau. Hơn nữa, mỗi phương pháp mã hóa kỹ thuật số, so với các phương pháp khác, đều có những ưu điểm và nhược điểm riêng, sẽ được thảo luận dưới đây.
# 2. Phương pháp mã hóa vật lý
## 2.1 NRZ - Non Return to Zero

Phương pháp mã hóa nhị phân đơn giản và rõ ràng nhất là phương pháp mã hóa tiềm năng không quay về mức 0 – NRZ (Non Return to Zero), trong đó bit "1" tương ứng với mức điện thế cao, còn bit "0" tương ứng với mức điện thế thấp
<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/ITMO/K%E1%BB%B3%205/M%E1%BA%A1ng%20m%C3%A1y%20t%C3%ADnh/image/1/NRZ.png" alt="Alt text" width="300">
  <figcaption>Non Return to Zero</figcaption>
</p>
- Ví dụ: Trong chuỗi "1010", mã NRZ sẽ giữ mức điện áp cao cho "1", chuyển xuống thấp cho "0", rồi lại chuyển lên cao cho "1", và cuối cùng xuống thấp cho "0".


Để xác định giới hạn tần số trên, cần tìm thành phần tần số cao nhất trong phổ của thông điệp được truyền. Trong mã NRZ, thành phần tần số cao nhất xuất hiện khi truyền các giá trị 0 và 1 luân phiên, trong đó chu kỳ của sóng sin (tín hiệu điều hòa) được sử dụng để truyền tín hiệu hình chữ nhật 0 và 1 sẽ bằng gấp đôi độ dài của khoảng thời gian bit $$T$$:

$$
T = 2T_b
$$

Trong đó $$T_b$$ được xác định là giá trị nghịch đảo của tốc độ truyền dữ liệu (băng thông kênh):

$$
T_b = \frac{1}{C}
$$

Từ đó, giới hạn tần số trên sẽ bằng:

$$
f_{\text{top}} = \frac{C}{2}
$$

Với băng thông kênh truyền $$C$$, tần số điều hòa cơ bản sẽ bằng:

$$
f_0 = \frac{C}{2}
$$

Trong trường hợp mã hóa bất kỳ thông điệp nào bằng phương pháp NRZ, tần số lớn nhất (giới hạn trên) sẽ đạt được khi truyền các giá trị 0 và 1 luân phiên, còn tần số nhỏ nhất (giới hạn dưới) sẽ đạt được khi truyền các chuỗi dài (vô hạn) các giá trị 0 hoặc 1, làm cho tần số giới hạn dưới gần bằng 0:

$$
f_{\text{lower}} \approx 0
$$

Do đó, trong trường hợp lý tưởng, độ rộng phổ sẽ bằng:

$$
\Delta f = f_{\text{top}} - f_{\text{lower}} = \frac{C}{2}
$$

Mặt khác, khi truyền thông điệp cụ thể, tần số giới hạn dưới luôn lớn hơn 0 và phụ thuộc vào độ dài tối đa của chuỗi các giá trị 0 hoặc 1. Trong thông điệp được mã hóa theo phương pháp NRZ, như minh họa trên hình 1.1a, thành phần tần số thấp được tạo ra khi truyền 4 số 1 liên tiếp và 4 số 0 liên tiếp. Chu kỳ của tín hiệu hình sin khi truyền những chuỗi này sẽ bằng 8 khoảng thời gian bit, và giới hạn tần số dưới sẽ bằng:

$$
f_{\text{lower}} = \frac{C}{8}
$$

Do đó, độ rộng phổ khi truyền thông điệp này bằng mã NRZ sẽ bằng:

$$
\Delta f = f_{\text{top}} - f_{\text{lower}} = \frac{C}{2} - \frac{C}{8} = \frac{3C}{8}
$$

Lưu ý rằng các giá trị tần số giới hạn dưới và phổ thu được chỉ đúng cho thông điệp cụ thể này. Khi truyền các thông điệp khác, các giá trị này sẽ khác nhau.

Vì vậy, có thể khẳng định rằng khi mã hóa theo phương pháp NRZ, độ rộng phổ của tín hiệu sẽ nằm trong khoảng:

$$
f_{\text{lower}} \leq f_{\text{signal}} \leq f_{\text{lower}}
$$

Giá trị trung bình của tần số thông điệp được truyền sẽ nằm trong khoảng:

$$
f_{\text{average}} = \frac{f_{\text{lower}} + f_{\text{top}}}{2}
$$

Nó cho biết những tần số nào (cao hay thấp) chiếm ưu thế trong phổ của tín hiệu được truyền.

Để tính giá trị trung bình của tần số thông điệp được truyền, cần xác định tần số tương ứng cho từng khoảng thời gian bit, cộng chúng lại và chia cho tổng số khoảng thời gian bit. Trong trường hợp của chúng ta, tần số điều hòa cơ bản $$f_0$$ tương ứng với 7 khoảng thời gian bit, 4 khoảng thời gian bit tương ứng với tần số thấp hơn gấp đôi so với tần số điều hòa cơ bản, tức là:

$$
f_{\text{lower}} = \frac{f_0}{2}
$$

và 8 khoảng thời gian bit tương ứng với tần số:

$$
f_{\text{lower}} = \frac{f_0}{4}
$$

Khi đó, tần số trung bình của thông điệp này sẽ bằng:

$$
f_{\text{average}} = \frac{1}{19} \left( 7f_0 + 4 \cdot \frac{f_0}{2} + 8 \cdot \frac{f_0}{4} \right) = 0.58 f_0 \approx 0.58 C
$$

Vì vậy, phổ của tín hiệu không có sự khác biệt lớn giữa tần số thấp và tần số cao:

$$
f_{\text{lower}} < \frac{f_{\text{average}}}{2}
$$

Để truyền tín hiệu nhị phân qua kênh truyền thực và để nhận dạng chúng với số lỗi tối thiểu, lý tưởng nhất là tín hiệu ở phía phát cần được định dạng gần giống dạng sóng hình chữ nhật. Tuy nhiên, phổ của các tín hiệu như vậy quá rộng. Trong khi đó, để nhận dạng tín hiệu chất lượng ở phía nhận khi truyền các giá trị luân phiên 0 và 1, chỉ cần tín hiệu chứa 4 điều hòa đầu tiên (vì các điều hòa có tần số cao hơn ít ảnh hưởng đến tín hiệu tổng) với các tần số:

$$
f_{\text{top}} = 7f_0
$$

Do đó, băng thông cần thiết để truyền thông điệp này bằng mã NRZ sẽ bằng:

$$
\Delta f = 6C/4
$$

Ưu điểm của mã NRZ là:

- Đơn giản và chi phí thấp do chỉ có hai mức điện thế.
- Phổ tín hiệu hẹp hơn so với các phương pháp mã hóa khác: $$\Delta f = 0.5C$$, trong đó $$C$$ là tốc độ truyền dữ liệu [bit/s].

Tuy nhiên, mã NRZ không được sử dụng trong các mạng máy tính do các nhược điểm sau:

- Thiếu đồng bộ hóa, điều này có thể dẫn đến mất đồng bộ giữa đồng hồ của bộ nhận và bộ phát khi truyền chuỗi dài các giá trị 0 hoặc 1.
- Không thể sử dụng trong các kênh truyền điện có các mạch cách ly bằng điện giữa bộ phát và bộ nhận.

Tuy nhiên, các biến thể của mã NRZ được sử dụng, trong đó thành phần cố định được loại bỏ bằng các phương pháp mã hóa logic, cụ thể là mã hóa dư thừa.


