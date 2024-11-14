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


#### Bước 3. Phân tích phổ tần số

Xác định giới hạn tần số trên và dưới trong phổ của tín hiệu đã truyền, giá trị trung bình của tần số, và băng thông cần thiết để truyền thông điệp này một cách chất lượng.

#### Bước 4. Mã hóa logic thông điệp

Thực hiện mã hóa logic cho thông điệp ban đầu bằng một hoặc hai phương pháp đã chọn. Mô tả chi tiết quá trình mã hóa và các đặc điểm chính của mỗi phương pháp.

#### Bước 5. So sánh các phương pháp mã hóa

So sánh các phương pháp mã hóa đã sử dụng ở các bước trước và đưa ra nhận xét về ưu điểm và nhược điểm của từng phương pháp. Trình bày kết quả so sánh dưới dạng bảng tóm tắt.

---

Phần dịch này cung cấp chi tiết các bước để sinh viên thực hiện bài tập liên quan đến mã hóa và truyền tín hiệu, với các tiêu chuẩn đánh giá từ điểm "đạt" đến "giỏi" dựa trên số lượng và sự phù hợp của các phương pháp mã hóa được áp dụng
