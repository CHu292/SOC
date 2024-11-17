# 1.3 Các bước thực hiện công việc và các tùy chọn bài tập 

## Bước 1. Hình thành thông điệp

Sử dụng họ và tên viết tắt của sinh viên thực hiện bài tập làm thông điệp ban đầu để truyền tải. Để biểu diễn thông điệp này dưới dạng số, hãy sử dụng mã hệ thập lục phân theo bảng mã (xem Bảng 1.2).

Ghi lại thông điệp ban đầu bằng mã thập lục phân và mã nhị phân. Xác định độ dài của thông điệp.

Dưới đây là nội dung của **Bảng 1.2** từ tài liệu "Задачи_сети.pdf" đã được dịch sang tiếng Việt:

---

### Bảng 1.2

| Ký hiệu | Mã  | Ký hiệu | Mã  | Ký hiệu | Mã  | Ký hiệu | Mã  | Ký hiệu | Mã  |
|---------|-----|---------|-----|---------|-----|---------|-----|---------|-----|
| А       | C0  | Р       | D0  | а       | E0  | р       | F0  | khoảng trắng | 20  |
| Б       | C1  | С       | D1  | б       | E1  | с       | F1  | ,       | 2C  |
| В       | C2  | Т       | D2  | в       | E2  | т       | F2  | .       | 2E  |
| Г       | C3  | У       | D3  | г       | E3  | у       | F3  | 0       | 30  |
| Д       | C4  | Ф       | D4  | д       | E4  | ф       | F4  | 1       | 31  |
| Е       | C5  | Х       | D5  | е       | E5  | х       | F5  | 2       | 32  |
| Ж       | C6  | Ц       | D6  | ж       | E6  | ц       | F6  | 3       | 33  |
| З       | C7  | Ч       | D7  | з       | E7  | ч       | F7  | 4       | 34  |
| И       | C8  | Ш       | D8  | и       | E8  | ш       | F8  | 5       | 35  |
| Й       | C9  | Щ       | D9  | й       | E9  | щ       | F9  | 6       | 36  |
| К       | CA  | Ъ       | DA  | к       | EA  | ъ       | FA  | 7       | 37  |
| Л       | CB  | Ы       | DB  | л       | EB  | ы       | FB  | 8       | 38  |
| М       | CC  | Ь       | DC  | м       | EC  | ь       | FC  | 9       | 39  |
| Н       | CD  | Э       | DD  | н       | ED  | э       | FD  |         |     |
| О       | CE  | Ю       | DE  | о       | EE  | ю       | FE  |         |     |
| П       | CF  | Я       | DF  | п       | EF  | я       | FF  |         |     |

---

Bảng này hiển thị các mã thập lục phân cho từng ký tự chữ cái trong bảng chữ cái Cyrillic, cùng với một số ký hiệu đặc biệt và số.

Thông điệp ban đầu: `Чу В.Д.`

Mã thập lục phân (hexadecimal code): `D7 F3 20 C2 2E C4 2E`

Code để chuyển từ hex sang bin:

```python
def hex_to_bin(hex_code):
    # Xóa khoảng trắng khỏi chuỗi hexadecimal
    hex_code = hex_code.replace(" ", "")
    
    # Chuyển mã hexadecimal sang số nhị phân
    bin_code = bin(int(hex_code, 16))[2:]
    
    # Đảm bảo độ dài nhị phân bằng 4 lần số chữ số của mã hexadecimal
    return bin_code.zfill(len(hex_code) * 4)

# Ví dụ sử dụng
hex_code = input("Nhập mã hexadecimal: ")
bin_code = hex_to_bin(hex_code)
print(f"Mã nhị phân tương ứng: {bin_code}")
```
Mã nhị phân: `11010111111100110010000011000010001011101100010000101110`

Độ dài thông điệp: 7 byte (56 bit)

**Băng thông của kênh truyền là $C = 1$ Gbit/s**.

Bốn byte đầu tiên của chuỗi nhị phân là: `11010111 11110011 00100000 11000010`.

## Bước 2. Mã hóa vật lý thông điệp ban đầu

Thực hiện mã hóa vật lý cho thông điệp ban đầu bằng mã Manchester và thêm hai phương pháp mã hóa khác (để đạt điểm "đạt"), ba phương pháp (để đạt điểm "khá") hoặc bốn phương pháp (để đạt điểm "giỏi") mà được xem là phù hợp nhất.


**Ký hiệu:**
- tần số cơ bản $$f_0$$;
- giới hạn tần số trên trong thông điệp truyền $$f_upper$$;
- giới hạn tần số dưới trong thông điệp truyền $$f_lower$$;
- giá trị trung bình của tần số trong phổ của tín hiệu truyền $$f_{avg}$$;
- băng thông cần thiết để truyền thông điệp này chất lượng $$S$$;


- **$$f_0$$**: Fundamental frequency
- **$$f_upper$$**: Upper frequency limit
- **$$f_lower$$**: Lower frequency limit
- **$$f_{avg}$$**: Average frequency in spectrum
- **$$S$$**: Required bandwidth for quality transmission


### Trong mã hóa NRZ:

Trong mã hóa NRZ, mỗi bit được biểu diễn bởi một mức điện áp cố định trong suốt khoảng thời gian bit mà không quay về mức 0 giữa các bit. Điều này dẫn đến tần số cơ bản của tín hiệu NRZ bằng một nửa tốc độ bit (bit rate).

- **Tần số cơ bản $$f_0$$** được tính bằng công thức:
  
$$
  f_0 = \frac{C}{2}= \frac{1 \text{ Gbps}}{2} = 0.5 \text{ GHz}
$$

-  **giới hạn tần số trên** $$f_{\text{upper}}$$ có thể được ước tính bằng công thức:

$$
f_{\text{upper}} = 7 \times f_0
$$

Điều này dựa trên việc mở rộng phổ tần số của tín hiệu trong các hệ thống thực tế, đặc biệt là khi cần đảm bảo chất lượng truyền dẫn cho các loại tín hiệu mã hóa như **NRZ (Non-Return-to-Zero)**. Công thức này cho phép bao quát các thành phần tần số cao hơn của tín hiệu, nhằm giảm thiểu sự suy giảm chất lượng do các yếu tố như nhiễu và suy hao trong môi trường truyền.

   $$
   f_{\text{upper}} = 7 \times 0.5 \text{ GHz} = 3.5 \text{ GHz}
   $$

- **Giới hạn tần số dưới**:  chuỗi bit liên tiếp dài nhất chỉ gồm toàn 0 hoặc toàn 1

$$
f_{lower} = \frac{1}{n \cdot t} = \frac{1}{2 \cdot n \cdot T} = \frac{C}{2 \cdot n} 
$$

Trong đó:
- **n**: Chuỗi bit liên tiếp dài nhất.

Với ví dụ trên ta nhận ra có 7 bit 1 liên tiếp:

$$
f_{upper} = \frac{f_0}{7} = \frac{500}{7} \approx 71.429 \text{ MHz} 
$$

- **Tần số trung bình**: Chúng ta sẽ phân tích các chuỗi liên tiếp khác nhau trong tín hiệu, đại diện cho mức đóng góp tần số từ các chuỗi đó. Những thành phần này tính đến sự xuất hiện của các chuỗi liên tiếp khác nhau, từ đó tính toán ảnh hưởng của chúng đến tần số trung bình của toàn bộ tín hiệu.


$$
f_{\text{avg}} = \frac{1}{32} \left( 6 f_0 + \frac{10}{2} f_0 + \frac{4}{4} f_0 + \frac{5}{5} f_0 + \frac{7}{7} f_0 \right) = \frac{14}{32} f_0 = 218.75 \text{ MHz}
$$

Để hiểu cách công thức này hoạt động, chúng ta sẽ phân tích từng thành phần.

 Các Thành Phần Của Công Thức
- **Tần số cơ bản ($$f_0$$)**: Đây là tần số cơ bản của tín hiệu, phụ thuộc vào băng thông của kênh. Với băng thông $$1 \text{ Gbit/s}$$, tần số cơ bản của tín hiệu NRZ là $$f_0 = 500 \text{ MHz}$$.
  
- **Phân tích chuỗi nhị phân và chuỗi không đổi**:
 
  - Trong công thức này, chúng ta chia tổng của các giá trị bằng tổng độ dài của chuỗi bit ($$32$$). Điều này là để tính ra giá trị trung bình của tần số trong toàn bộ chuỗi.
  

  - Mỗi thành phần của công thức đều biểu diễn sự đóng góp của tần số từ một nhóm chuỗi nhất định trong tín hiệu.
  - Ví dụ, **$$6 f_0$$** đại diện cho tần số từ nhóm có 1 bit không thay đổi.
  - **$$\frac{10}{2} f_0$$** đại diện cho đóng góp tần số từ nhóm chuỗi có 2 bit liên tiếp ko đổi
  - Tương tự, **$$\frac{4}{4} f_0$$**, **$$\frac{5}{5} f_0$$**, và **$$\frac{7}{7} f_0$$** cũng biểu thị sự đóng góp từ các nhóm chuỗi với tỉ lệ khác nhau.

### Trong mã hóa RZ:

$$ f_0 = C = 1 \text{ GHz} $$
$$ f_{upper} = 7 \times f_0 = 3500 \text{ MHz} $$

Tính giới hạn tần số dưới

Để tính **giới hạn tần số dưới** $$ f_{\text{lower}} $$ cho chuỗi bit bạn cung cấp, chúng ta cần xác định độ dài chuỗi bit 0 dài nhất và áp dụng công thức:

$$ f_{\text{lower}} = \frac{f_0}{n_{\text{max}}} $$

 Các bước tính toán:

Bước 1: Xác định chuỗi bit 0 dài nhất

$$ 11010111111100110010000011000010 $$

- Đếm các chuỗi bit 0 liên tiếp:
  - $$1$$: giữa bit thứ 2 và 3.
  - $$2$$: giữa bit thứ 7 và 9.
  - $$4$$: giữa bit thứ 19 và 23.
  - $$2$$: giữa bit thứ 25 và 26.
  - $$3$$: giữa bit thứ 28 và 30.

=> Chuỗi bit 0 dài nhất $$n_{\text{max}} = 4$$.

 Bước 2: Áp dụng công thức
Giả sử tần số cơ bản $$f_0 = 1 \, \text{GHz}$$, khi đó:

$$f_{\text{lower}} = \frac{f_0}{n_{\text{max}}} = \frac{1 \, \text{GHz}}{4} = 250 \, \text{MHz}.$$


 1. **Hiểu bản chất của mã hóa RZ:**
   - Trong mã hóa RZ, mỗi bit (0 hoặc 1) được biểu diễn bằng một tín hiệu ngắn hơn chu kỳ đầy đủ, tức là tín hiệu trở về mức "0" trước khi chu kỳ bit kết thúc.
   - Với bit $$1$$, tín hiệu thường có mức dương (+V) trong nửa đầu chu kỳ và trở về 0 trong nửa sau.
   - Với bit $$0$$, tín hiệu không tạo mức điện áp (luôn là 0 trong suốt chu kỳ).

 2. **Xác định tần số chuyển đổi tín hiệu:**
   - **Số lần chuyển đổi** (từ mức 0 sang +V hoặc -V, hoặc ngược lại) trong một chuỗi là cơ sở để tính tần số trung bình.
   - Trong mã hóa RZ, mỗi bit $$1$$ luôn tạo ra ít nhất **2 chuyển đổi** (0 → +V và +V → 0).
   - Với bit $$0$$, không có chuyển đổi nào.

3. **Công thức tính tần số trung bình:**
   Tần số trung bình $$f_{avg}$$ được tính bằng:
   $$f_{avg} = \frac{\text{Tổng số chuyển đổi tín hiệu}}{\text{Tổng thời gian}}$$
   hoặc
   $$f_{avg} = \frac{\text{Số chuyển đổi trên một chu kỳ bit} \times \text{Số bit '1'}}{\text{Tổng số bit}} \times f_{bit}$$
   - $$f_{bit}$$: Tần số của luồng bit (tốc độ bit).
   - Số chuyển đổi trên mỗi chu kỳ bit RZ = 2 (cho mỗi $$1$$).

4. **Tính toán với chuỗi đã cho:**
   Chuỗi: **11010111111100110010000011000010**

   - Đếm số bit $$1$$: Có **16 bit 1**.
   - Mỗi bit $$1$$ có **2 chuyển đổi** → Tổng số chuyển đổi = $$16 \times 2 = 32$$.
   - Tổng số bit = $$32$$.
   - Tần số bit $$f_{bit}$$: Được cho trước hoặc phụ thuộc vào hệ thống.

   **Tần số trung bình (theo số lần chuyển đổi):**
   $$f_{avg} = \frac{32}{32} \times f_{bit} = 1 \times f_{bit}$$

  $$f_{bit} = t = 2T = \frac{f_0}{2}$$
   => $$f_{avg} = \frac{1000}{2} = 500 \, \text{MHz}$$

 6. **Kết luận:**
   Tần số trung bình của tín hiệu trong mã hóa RZ sẽ luôn cao hơn hoặc bằng tần số bit, phụ thuộc vào tỷ lệ bit $$1$$ trong chuỗi. 

### Trong mã hóa PAM-5 (Pulse Amplitude Modulation - 5 level) - Mã năm mức PAM-5

$$ f_0 = \frac{c}{4} = 240 \, \text{МГц} $$

$$ f_{\text{avg}} = 7 \cdot f_0 = 1750 \, \text{МГц} $$


- ** Giới hạn tần số dưới: tìm đoạn tín hiệu dài nhất mà tín hiệu không thay đổi mức giá trị**.
**1. Tại sao phải tìm chu kỳ dài nhất?**
- Tần số dưới $f_{\text{lower}}$ được xác định bởi chu kỳ dài nhất $T_{\text{lower}}$ của tín hiệu.
- Chu kỳ dài nhất là **khoảng thời gian lâu nhất mà tín hiệu giữ nguyên giá trị trước khi thay đổi**.
- Mức tín hiệu cụ thể ($-2, +1, +2, \dots$) không quan trọng — điều cần thiết là **tìm đoạn tín hiệu dài nhất giữ nguyên mức bất kỳ**.

**2. Phân tích tín hiệu một cách chính xác**
Chuỗi tín hiệu sau khi ánh xạ là:

$$
\{+1, -1, -1, +1, +1, +1, -2, +1, -2, +2, -2, -2, +1, -2, +2\}.
$$

**Quan sát chu kỳ dài nhất:**
1. **Mức $+1$:**
   - Đoạn $+1, +1, +1$ có độ dài 3 ký hiệu liên tiếp.
   - Đây là chu kỳ dài nhất tín hiệu giữ mức $+1$.

2. **Các mức khác:**
   - $-1$: Đoạn $-1, -1$ chỉ kéo dài 2 ký hiệu.
   - $-2$: Đoạn $-2, -2$ chỉ kéo dài 2 ký hiệu.
   - $+2$: Không có đoạn nào kéo dài quá 1 ký hiệu.

**Chu kỳ dài nhất:**
- Chu kỳ dài nhất $T_{\text{lower}}$ là **3 ký hiệu**, xảy ra khi tín hiệu giữ mức $+1$.

**3. Tính toán tần số dưới $f_{\text{lower}}$**
**Thời gian mỗi ký hiệu:**
- Một ký hiệu kéo dài:

$$
T = \frac{1}{f_0} = \frac{1}{250 \, \text{MHz}} = 4 \, \text{t}.
$$

**Chu kỳ dài nhất:**
ta thấy chuỗi 3 ký hiệu là 6 bit
Để hoàn thành chu kỳ thì sẽ là 12 bit 
- Thời gian chu kỳ dài nhất là:
  
$$
T_{\text{lower}} = 12 \text{t}.
$$

**Tần số dưới:**
- Tần số dưới được tính bằng:
  
$$
f_{\text{lower}} = \frac{1}{T_{\text{lower}}}.
$$

- Thay $T_{\text{lower}} = 12 \, \text{ns}$:

$$
f_{\text{lower}} = \frac{1}{12 \cdot 10^{-9}} = 83.33 \, \text{MHz}.
$$



---
Cảm ơn bạn đã giải thích rõ hơn về ý nghĩa của \(n\) và \(m\). Giờ tôi sẽ làm rõ và tính lại chính xác:

- **\(n\):** Tổng số lần chuyển trạng thái xảy ra với **tần số \(f_0\)**, nghĩa là chuyển đổi rõ ràng giữa trạng thái cao-thấp (High-Low) hoặc thấp-cao (Low-High) trên từng bit.
- **\(m\):** Tổng số lần chuyển trạng thái xảy ra với **tần số \(f_0/2\)**, nghĩa là duy trì tín hiệu (không thay đổi trạng thái trong mã Manchester).

### Quy trình tính:
1. Phân tích chuỗi Manchester để đếm:
   - **\(n\)**: Các chuyển đổi trạng thái thực tế.
   - **\(m\)**: Các duy trì tín hiệu.
2. Áp dụng công thức:
   \[
   f_{avg} = \frac{n \cdot f_0 + m \cdot \frac{f_0}{2}}{64}
   \]

Tôi sẽ tính toán chính xác.

Kết quả chính xác sau khi tính lại:

1. **Số lần chuyển trạng thái với \( f_0 \) (\( n \))**: \( 18 \).  
   - Đây là các lần chuyển đổi trạng thái rõ ràng (High-Low hoặc Low-High).

2. **Số lần chuyển trạng thái với \( \frac{f_0}{2} \) (\( m \))**: \( 14 \).  
   - Đây là các lần tín hiệu duy trì trạng thái (High-High hoặc Low-Low).

3. **Tần số trung bình (\( f_{avg} \))**:
   \[
   f_{avg} = \frac{18 \cdot f_0 + 14 \cdot \frac{f_0}{2}}{64} = 390.625 \, \text{MHz}.
   \]

---

### **Kết luận**:
Tần số trung bình \( f_{avg} \) của tín hiệu Manchester là **390.625 MHz**.

--- 











Để tính tần số cơ bản $$ f_0 $$ từ chuỗi bit được mã hóa theo phương pháp MLT-3 (Multi-Level Transmit-3), cần thực hiện các bước sau:

1. **Hiểu nguyên lý của mã hóa MLT-3:**
   - Mã hóa MLT-3 sử dụng ba mức điện áp $$-1, 0, +1$$ để biểu diễn dữ liệu nhị phân. Chuyển đổi mức điện áp chỉ xảy ra khi có một bit `1`, và nó xoay vòng theo trình tự $$0 \rightarrow +1 \rightarrow 0 \rightarrow -1 \rightarrow 0$$. Nếu bit là `0`, mức điện áp sẽ giữ nguyên.

2. **Tính chu kỳ tín hiệu cơ bản:**
   - Chu kỳ tín hiệu cơ bản được xác định bởi chu kỳ lặp lại ngắn nhất trong chuỗi điện áp đã mã hóa.

3. **Tính tần số cơ bản:**
   - Tần số cơ bản $$ f_0 = \frac{1}{T} $$, trong đó $$ T $$ là chu kỳ tín hiệu cơ bản.

### Dữ liệu trong bài:
- Tốc độ đường truyền $$ C = 1 \, \text{GHz} $$, tức là mỗi bit được truyền trong $$ T_b = \frac{1}{C} = 1 \, \text{ns} $$.
- Dựa trên mã hóa MLT-3, ta cần phân tích chu kỳ tín hiệu để tính $$ f_0 $$.

Tôi sẽ phân tích chu kỳ ngắn nhất từ hình ảnh mã hóa này. Một chút thời gian để tính toán.

Phân tích tín hiệu MLT-3 từ chuỗi bit đã cho và hình ảnh mã hóa, ta có:

1. **Chu kỳ tín hiệu cơ bản (MLT-3):**
   - Trong MLT-3, chuyển đổi mức điện áp chỉ xảy ra với bit `1`, và chu kỳ cơ bản là chuỗi ngắn nhất mà tín hiệu điện áp quay lại trạng thái ban đầu (theo trình tự $$-1, 0, +1, 0, -1$$).

2. **Chuỗi mã hóa:**
   - Chuỗi bit: $$11010111111100110010000011000010$$.
   - Từ mã hóa trong hình, chu kỳ ngắn nhất trong mã MLT-3 xảy ra khi một chuỗi `101` được mã hóa, do đó chu kỳ tín hiệu cơ bản kéo dài $$T = 4 \, T_b$$ (vì mỗi chuyển đổi xảy ra sau một bit `1`).

3. **Tần số cơ bản $$f_0$$:**
   - Tốc độ đường truyền $$C = 1 \, \text{GHz} \Rightarrow T_b = 1 \, \text{ns}$$.
   - Chu kỳ tín hiệu cơ bản $$T = 4 \, T_b = 4 \, \text{ns}$$.
   - Tần số cơ bản $$f_0 = \frac{1}{T} = \frac{1}{4 \, \text{ns}} = 250 \, \text{MHz}$$.

### Kết quả:
Tần số cơ bản $$f_0 = 250 \, \text{MHz}$$.



Để giải thích tại sao chu kỳ tín hiệu cơ bản \( T \) lại bằng \( 4T_b \) trong mã hóa MLT-3, chúng ta cần hiểu cách mã hóa và nguyên tắc hoạt động của MLT-3:

---

### **1. Nguyên tắc mã hóa MLT-3**
- Mã hóa MLT-3 sử dụng ba mức điện áp: \(-1, 0, +1\).
- Chỉ khi gặp một bit `1`, tín hiệu mới **thay đổi mức điện áp**, và nó thay đổi theo chu kỳ tuần hoàn sau:
  \[
  0 \rightarrow +1 \rightarrow 0 \rightarrow -1 \rightarrow 0 \rightarrow +1 \dots
  \]
- Khi gặp một bit `0`, tín hiệu **không thay đổi mức** mà giữ nguyên trạng thái hiện tại.

---

### **2. Phân tích chu kỳ tín hiệu cơ bản \( T \)**
- Chu kỳ cơ bản là khoảng thời gian ngắn nhất để tín hiệu MLT-3 quay lại trạng thái ban đầu, tức là hoàn thành một vòng \( 0 \rightarrow +1 \rightarrow 0 \rightarrow -1 \rightarrow 0 \).
- Để tín hiệu hoàn thành một chu kỳ đầy đủ, cần 4 lần chuyển mức điện áp:
  - Chuyển từ \( 0 \rightarrow +1 \).
  - Chuyển từ \( +1 \rightarrow 0 \).
  - Chuyển từ \( 0 \rightarrow -1 \).
  - Chuyển từ \( -1 \rightarrow 0 \).

- **Mỗi lần chuyển mức** xảy ra khi gặp **một bit `1`**. Trong trường hợp lý tưởng, một chu kỳ đầy đủ cần xuất hiện 4 bit `1` liên tiếp (không bị gián đoạn bởi bit `0`).

- Với tốc độ truyền \( C = 1 \, \text{GHz} \), thời gian truyền cho mỗi bit là:
  \[
  T_b = \frac{1}{C} = 1 \, \text{ns}.
  \]
  Do đó, một chu kỳ tín hiệu cơ bản \( T \) sẽ kéo dài \( T = 4T_b \).

---

### **3. Minh họa từ chuỗi bit**
Xét chuỗi bit \( 11010111111100110010000011000010 \):
- Khi phân tích hình ảnh mã hóa MLT-3 từ chuỗi bit này, ta nhận thấy mỗi chu kỳ tín hiệu đầy đủ yêu cầu tối thiểu 4 bit `1` (liên tục hoặc xen kẽ bởi bit `0`), tương ứng với 4 lần thay đổi mức điện áp.
- Mỗi lần thay đổi mức điện áp xảy ra sau một khoảng \( T_b = 1 \, \text{ns} \).
- Như vậy, chu kỳ ngắn nhất (tín hiệu quay lại trạng thái ban đầu) là \( T = 4T_b = 4 \, \text{ns} \).

---

### **Kết luận**
Chu kỳ tín hiệu cơ bản \( T \) của mã hóa MLT-3 là \( 4T_b \) vì một chu kỳ tín hiệu hoàn chỉnh cần 4 lần thay đổi mức điện áp, tương ứng với 4 bit `1`. 

### **Tính giới hạn tần số dưới \( f_{\text{lower}} \):**

Giới hạn tần số dưới \( f_{\text{lower}} \) được xác định bởi tín hiệu có chu kỳ dài nhất trong chuỗi mã hóa. Với mã hóa **MLT-3**, tín hiệu có chu kỳ dài nhất xảy ra khi có một chuỗi các bit `0` liên tục, vì khi gặp bit `0`, tín hiệu không thay đổi trạng thái.

---

#### **1. Công thức tính tần số dưới:**

Tần số dưới được tính như sau:

\[
f_{\text{lower}} = \frac{1}{T_{\text{max}}}
\]

Trong đó:
- \( T_{\text{max}} \) là chu kỳ dài nhất, tương ứng với khoảng thời gian giữa hai lần tín hiệu thay đổi mức điện áp.

---

#### **2. Xác định \( T_{\text{max}} \):**
Từ chuỗi bit:
\[
11010111111100110010000011000010
\]

- Phân tích chuỗi bit, chuỗi `0` dài nhất là **chuỗi 6 bit `0` liên tiếp**:
  \[
  000000
  \]

- Trong trường hợp này, tín hiệu không thay đổi trong \( T_{\text{max}} = 6T_b \), vì mỗi bit kéo dài \( T_b = 1 \, \text{ns} \). Do đó:
  \[
  T_{\text{max}} = 12 \, \text{ns}.
  \]

---

#### **3. Tính \( f_{\text{lower}} \):**
\[
f_{\text{lower}} = \frac{1}{T_{\text{max}}}  = \frac{f_0}{3} \, \text{MHz}.
\]

---

### **Làm thế nào để tính số lần xuất hiện các thành phần \( f_0 \), \( \frac{f_0}{2} \), \( \frac{f_0}{3} \), ...?**

Khi sử dụng mã hóa MLT-3, việc xác định số lần xuất hiện các thành phần \( f_0, \frac{f_0}{2}, \dots \) phụ thuộc vào cách **chuỗi bit `1` liên tục** gây ra các chuyển đổi mức điện áp. Các bước sau đây sẽ giúp bạn hiểu và tính toán số lần xuất hiện:

---

### **1. Nguyên lý mã hóa MLT-3**
- Trong mã hóa MLT-3:
  - **\( f_0 \):** Bit `1` đầu tiên trong một cụm làm tín hiệu thay đổi **mức lớn nhất** (ví dụ, từ \( 0 \rightarrow +1 \) hoặc \( +1 \rightarrow 0 \)).
  - **\( \frac{f_0}{2} \):** Bit `1` thứ hai trong cụm làm tín hiệu thay đổi **ít hơn** (ví dụ, tín hiệu quay lại trạng thái trung gian hoặc giữ trạng thái thấp hơn).
  - **\( \frac{f_0}{3} \), \( \frac{f_0}{4} \), ...:** Các bit `1` tiếp theo tiếp tục gây ra thay đổi nhỏ hơn nữa, tương ứng với tần số giảm.

---

### **2. Cách tính số lần xuất hiện từng thành phần**
#### **Bước 1: Xác định các cụm `1` trong chuỗi bit**
- Một **cụm `1`** là một nhóm bit `1` liên tiếp trong chuỗi bit. Ví dụ:
  - Chuỗi \( 110101111 \): Các cụm `1` là \( 11 \), \( 1 \), \( 1111 \).
  - Chuỗi \( 111 \): Là một cụm duy nhất.

#### **Bước 2: Phân loại các thành phần trong mỗi cụm**
- Mỗi cụm `1` đóng góp các thành phần:
  - Bit đầu tiên trong cụm luôn góp \( f_0 \).
  - Bit thứ hai góp \( \frac{f_0}{2} \).
  - Bit thứ ba góp \( \frac{f_0}{3} \).
  - Bit thứ tư góp \( \frac{f_0}{4} \), ...
  
Ví dụ: Với cụm \( 111 \):
- Bit đầu: \( f_0 \),
- Bit thứ hai: \( \frac{f_0}{2} \),
- Bit thứ ba: \( \frac{f_0}{3} \).

#### **Bước 3: Tính tổng các thành phần từ toàn bộ chuỗi**
- Xét toàn bộ chuỗi và đếm số lần xuất hiện của \( f_0, \frac{f_0}{2}, \frac{f_0}{3}, \dots \) từ tất cả các cụm.

---

### **3. Ví dụ chi tiết**
Chuỗi bit: \( 11010111111100110010000011000010 \).

#### **Phân tích từng cụm:**
1. **Cụm 1: \( 11 \):**
   - Bit đầu: \( f_0 \),
   - Bit thứ hai: \( \frac{f_0}{2} \).

2. **Cụm 2: \( 1 \):**
   - Bit đầu: \( f_0 \).

3. **Cụm 3: \( 111111 \):**
   - Bit đầu: \( f_0 \),
   - Bit thứ hai: \( \frac{f_0}{2} \),
   - Bit thứ ba: \( \frac{f_0}{3} \),
   - Bit thứ tư: \( \frac{f_0}{4} \),
   - Bit thứ năm: \( \frac{f_0}{5} \),
   - Bit thứ sáu: \( \frac{f_0}{6} \).

4. **Cụm 4: \( 11 \):**
   - Bit đầu: \( f_0 \),
   - Bit thứ hai: \( \frac{f_0}{2} \).

5. **Cụm 5: \( 1 \):**
   - Bit đầu: \( f_0 \).

6. **Cụm 6: \( 1 \):**
   - Bit đầu: \( f_0 \).

#### **Tính số lần xuất hiện tổng cộng:**
- \( f_0 \): Xuất hiện từ tất cả các bit đầu tiên trong mỗi cụm:
  - \( 1 + 1 + 1 + 1 + 1 + 1 = 6 \) lần.

- \( \frac{f_0}{2} \): Xuất hiện từ các bit thứ hai trong cụm:
  - \( 1 + 1 + 1 = 3 \) lần.

- \( \frac{f_0}{3} \): Xuất hiện từ bit thứ ba trong cụm \( 111111 \):
  - \( 1 \) lần.

- \( \frac{f_0}{4} \): Xuất hiện từ bit thứ tư trong cụm \( 111111 \):
  - \( 1 \) lần.

- \( \frac{f_0}{5} \): Xuất hiện từ bit thứ năm trong cụm \( 111111 \):
  - \( 1 \) lần.

- \( \frac{f_0}{6} \): Xuất hiện từ bit thứ sáu trong cụm \( 111111 \):
  - \( 1 \) lần.

---

### **4. Tính \( f_{\text{avg}} \):**
Tổng hợp các thành phần:
\[
f_{\text{avg}} = \frac{6 \cdot f_0 + 3 \cdot \frac{f_0}{2} + 1 \cdot \frac{f_0}{3} + 1 \cdot \frac{f_0}{4} + 1 \cdot \frac{f_0}{5} + 1 \cdot \frac{f_0}{6}}{32}.
\]

Thay \( f_0 = 250 \, \text{MHz} \):
1. \( 6 \cdot f_0 = 6 \cdot 250 = 1500 \, \text{MHz} \),
2. \( 3 \cdot \frac{f_0}{2} = 3 \cdot 125 = 375 \, \text{MHz} \),
3. \( 1 \cdot \frac{f_0}{3} = 1 \cdot 83.33 = 83.33 \, \text{MHz} \),
4. \( 1 \cdot \frac{f_0}{4} = 1 \cdot 62.5 = 62.5 \, \text{MHz} \),
5. \( 1 \cdot \frac{f_0}{5} = 1 \cdot 50 = 50 \, \text{MHz} \),
6. \( 1 \cdot \frac{f_0}{6} = 1 \cdot 41.67 = 41.67 \, \text{MHz} \).

Tổng đóng góp:
\[
\text{Tổng} = 1500 + 375 + 83.33 + 62.5 + 50 + 41.67 = 2112.5 \, \text{MHz}.
\]

Chia cho \( N_{\text{total}} = 32 \):
\[
f_{\text{avg}} = \frac{2112.5}{32} = 66.02 \, \text{MHz}.
\]

---

### **Kết luận:**
Tần số trung bình \( f_{\text{avg}} \) là:
\[
f_{\text{avg}} = 66.02 \, \text{MHz}.
\]






#### Bước 3. Phân tích phổ tần số

Xác định giới hạn tần số trên và dưới trong phổ của tín hiệu đã truyền, giá trị trung bình của tần số, và băng thông cần thiết để truyền thông điệp này một cách chất lượng.

#### Bước 4. Mã hóa logic thông điệp

Thực hiện mã hóa logic cho thông điệp ban đầu bằng một hoặc hai phương pháp đã chọn. Mô tả chi tiết quá trình mã hóa và các đặc điểm chính của mỗi phương pháp.

#### Bước 5. So sánh các phương pháp mã hóa

So sánh các phương pháp mã hóa đã sử dụng ở các bước trước và đưa ra nhận xét về ưu điểm và nhược điểm của từng phương pháp. Trình bày kết quả so sánh dưới dạng bảng tóm tắt.

---

Phần dịch này cung cấp chi tiết các bước để sinh viên thực hiện bài tập liên quan đến mã hóa và truyền tín hiệu, với các tiêu chuẩn đánh giá từ điểm "đạt" đến "giỏi" dựa trên số lượng và sự phù hợp của các phương pháp mã hóa được áp dụng
