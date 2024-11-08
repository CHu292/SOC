# 1. Tính chất đơn giản nhất của các phép tính số học trên tập số nguyên

##  Tính chất của phép cộng và phép nhân trên tập hợp số nguyên

### 1. tính giao hoán của phép cộng

$$
\forall a, b \quad a + b = b + a
$$

### 2. tính kết hợp của phép nhân

$$
\forall a, b, c \quad (a + b) + c = a + (b + c)
$$

### 3. sự tồn tại của một phần tử trung tính cộng (không)

$$
\exists 0 \quad \forall a \quad 0 + a = a + 0 = a
$$

### 4. sự tồn tại của một phần tử đối lập (một phần tử nghịch đảo của phép cộng)

$$
\forall a \quad \exists (-a) \quad a + (-a) = (-a) + a = 0
$$

### 5. tính giao hoán của phép nhân

$$
\forall a, b \quad a \cdot b = b \cdot a
$$

### 6. tính kết hợp của phép nhân

$$
\forall a, b, c \quad (a \cdot b) \cdot c = a \cdot (b \cdot c)
$$

### 7. sự tồn tại của một phần tử (đơn vị) trung tính nhân

$$
\exists 1 \quad \forall a \quad 1 \cdot a = a \cdot 1 = a
$$

### 8. Tính phân phối của phép nhân đối với phép cộng

$$
\forall a, b, c \quad a \cdot (b + c) = a \cdot b + a \cdot c
$$

Và

$$
\forall a, b, c \quad (b + c) \cdot a = b \cdot a + c \cdot a
$$

Việc thỏa mãn tất cả các tính chất này chứng tỏ rằng ( Z, +, * ) là một vành giao hoán có đẳng thức.

### 9 

$$
\forall a \quad a \cdot 0 = 0 \cdot a = 0
$$

Chứng minh:


$$
a = a \cdot 1 = a \cdot (1 + 0) = a \cdot 1 + a \cdot 0 = a + a \cdot 0 \quad \Rightarrow \quad -a + a = -a + (a + a \cdot 0) \quad \Longleftrightarrow
$$

$$
0 = (-a + a) + a \cdot 0 \quad \Longleftrightarrow \quad 0 = 0 + a \cdot 0 \quad \Longleftrightarrow \quad 0 = a \cdot 0 \quad \Longleftrightarrow \quad 0 = 0 \cdot a
$$


### 10

$$
\forall a \quad (-1) \cdot a = a \cdot (-1) = -a
$$

Chứng minh:


$$
0 = 0 \cdot a = (1 + (-1)) \cdot a = 1 \cdot a + (-1) \cdot a = a + (-1) \cdot a \quad \Rightarrow \quad -a + 0 = -a + (a + (-1) \cdot a) \quad \Longleftrightarrow
$$

$$
-a = (-a + a) + (-1) \cdot a \quad \Longleftrightarrow \quad -a = 0 + (-1) \cdot a \quad \Longleftrightarrow \quad -a = (-1) \cdot a
$$


### 11

$$
\forall a \quad -(-a) = a
$$

### 12

$$
(-1) \cdot (-1) = 1
$$

Chứng minh

$$
a \cdot ((-1) \cdot (-1)) = (a \cdot (-1)) \cdot (-1) = (-a) \cdot (-1) = -(-a) = a
$$

Khi thay \( a = 1 \), ta có:

$$
1 = 1 \cdot ((-1) \cdot (-1)) = (-1) \cdot (-1)
$$

### 13

$$
\forall a, b \quad (-a) \cdot (-b) = a \cdot b
$$

Chứng minh:

$$
(-a)(-b) = (a \cdot (-1))((-1) \cdot b) = (a \cdot ((-1) \cdot (-1)))) \cdot b = (a \cdot 1) \cdot b = a \cdot b
$$

### 14

$$
\forall a, b \quad a \cdot (-b) = (-a) \cdot b = -(a \cdot b)
$$

Chứng minh:

$$
a \cdot b + a \cdot (-b) = a \cdot (b + (-b)) = a \cdot 0 = 0
$$

$$
-(a \cdot b) + (a \cdot b + a \cdot (-b)) = -(a \cdot b) + 0 \quad \Longleftrightarrow
$$

$$
(- (a \cdot b) + a \cdot b) + a \cdot (-b) = -(a \cdot b) \quad \Longleftrightarrow \quad 0 + a \cdot (-b) = -(a \cdot b) \quad \Longleftrightarrow \quad -(a \cdot b) = a \cdot (-b)
$$

Vậy, theo những gì đã chứng minh, ta có:

$$
(-a) \cdot b = b \cdot (-a) = -(b \cdot a) = -(a \cdot b)
$$

### 15. 

$$
\forall a, b, c \quad a \cdot (b - c) = a \cdot b - a \cdot c \quad \text{và} \quad \forall a, b, c \quad (b - c) \cdot a = b \cdot a - c \cdot a
$$

**Định lý phân phối phép nhân đối với phép trừ**

**Chứng minh:**

Nhớ lại rằng \( b - c = b + (-c) \) theo định nghĩa phép trừ. Vậy ta có:

$$
a \cdot (b - c) = a \cdot (b + (-c)) = a \cdot b + a \cdot (-c) = a \cdot b + (-(a \cdot c)) = a \cdot b - (a \cdot c)
$$

Tương tự, ta có:

$$
(b - c) \cdot a = (b + (-c)) \cdot a = b \cdot a + (-c) \cdot a = b \cdot a + (-(c \cdot a)) = b \cdot a - (c \cdot a)
$$

---
## Định lý về tính chia trong vành các số nguyên

$$
\text{Định nghĩa 1.1: Người ta nói rằng số } a \text{ chia hết cho số } b \text{ (hoặc là bội của số } b\text{), nếu tồn tại một số duy nhất } c \text{ sao cho } a = b \cdot c.
$$
Vậy ta có:
$$
a \mid b \iff \exists! c \quad a = b \cdot c.
$$

$$
\text{Định nghĩa 1.1'. Nếu tồn tại một số duy nhất } c \text{ sao cho } a = b \cdot c, \text{ thì người ta cũng nói rằng số } b \text{ chia số } a \text{ và ký hiệu là } b \mid a.
$$

$$
\text{Định nghĩa 1.2: Chia số } a \text{ cho số } b \text{ (không có dư), nghĩa là biểu diễn số } a \text{ dưới dạng } a = b \cdot c.
$$


Tự nhiên, chúng ta có thể đặt câu hỏi: Liệu có đúng là bất kỳ số nào cũng có thể chia cho bất kỳ số nào khác không? Không khó để nhận ra rằng câu trả lời cho câu hỏi này là phủ định.

Tự nhiên, chúng ta có thể đặt câu hỏi: Liệu có đúng là bất kỳ số nào cũng có thể chia cho bất kỳ số nào khác không? Không khó để nhận ra rằng câu trả lời cho câu hỏi này là phủ định.

Hãy thử chia số 3 cho số 2. Vì tích của hai số dương luôn là một số dương, nên kết quả của phép chia cũng phải là một số dương. Phép cộng với một số dương làm tăng tổng. Từ đó, ta có thể thấy rằng việc nhân một số dương với một số dương lớn hơn sẽ cho kết quả lớn hơn. Cụ thể, nếu $c > b$, tức là tồn tại $x > 0$ sao cho $c = b + x$, thì khi $a > 0$, ta có:

$$
a \cdot c = a \cdot (b + x) = a \cdot b + a \cdot x > a \cdot b.
$$

Lưu ý rằng:

$$
2 \cdot 1 = 2 < 3, \quad 2 \cdot 2 = 4 > 3,
$$

và khi $b > 2$, theo chứng minh, ta có:

$$
2 \cdot b > 2 \cdot 2 = 4 > 3.
$$

Vậy, ta đã chứng minh rằng không tồn tại một số nguyên $c$ sao cho $3 = c \cdot 2$, do đó phép chia 3 cho 2 là không thể thực hiện được.

**Định lý 1.1.** Không có số nào chia hết cho 0.

**Chứng minh:** Giả sử có một số $a \neq 0$ sao cho $a$ chia hết cho 0. Điều này có nghĩa là tồn tại một số $c$ sao cho:

$$
a = 0 \cdot c = 0,
$$

nhưng $a \neq 0$, điều này tạo ra một mâu thuẫn.

Bây giờ, thử chia 0 cho 0. Điều này có nghĩa là tồn tại một số $c$ sao cho:

$$
0 = 0 \cdot c = 0.
$$

Điều này đúng với mọi giá trị của $c$, tức là kết quả của phép chia 0 cho 0 có thể là bất kỳ số nào, do đó không có tính duy nhất (phép chia không phải là một phép toán xác định). Vì vậy, không thể chia 0 cho 0. $\boxed{\text{Chứng minh hoàn tất.}}$

**Hệ quả 1.1.** Khi $b = 0$ theo Định lý 1.1, phép chia cho $b$ là không thể, còn khi $b \neq 0$, để chứng minh tính chia hết của $a$ cho $b$, chỉ cần chứng minh (ví dụ, chỉ ra rõ ràng) sự tồn tại của một số $c$ sao cho:

$$
a = b \cdot c,
$$

tức là tính duy nhất không cần phải chứng minh.

---

## Tính chất chia hết

**Tính chất 1.1.**
a) $\forall a \neq 0 \, a \, a$

b) $\forall a \neq 0 \, a \, (-a)$

c) $\forall a \, a \, 1$

d) $\forall a \, a \, (-1)$

**Chứng minh:**

a) $a = a \cdot 1$.

b) $a = (-a) \cdot (-1)$.

c) $a = 1 \cdot a$.

d) $a = (-1) \cdot (-a)$.



**Tính chất 1.2.** Nếu trong số các số $a_1, a_2, ..., a_n$ có ít nhất một số chia hết cho $d$, thì tích $a_1 \cdot a_2 \cdot ... \cdot a_n$ cũng chia hết cho $d$.

**Chứng minh:** 

Giả sử $a_i \, d$, tức là $a_i = b \cdot d$. Do tính giao hoán và kết hợp của phép nhân, ta có thể đưa $d$ ra ngoài tích. Vì vậy, ta có:

$$
a_1 \cdot a_2 \cdot ... \cdot a_n = d \cdot (b_1 \cdot b_2 \cdot ... \cdot b_n),
$$

và rõ ràng rằng tích này chia hết cho $d$.


**Tính chất 1.3.** (Tính chuyển tiếp của quan hệ chia hết)

Nếu $a \, b$ và $b \, c$, thì $a \, c$.

**Chứng minh:**

$ a \, b \iff \exists d_1 \, a = b \cdot d_1 $.

$ b \, c \iff \exists d_2 \, b = c \cdot d_2 $.

Từ đó ta có:

$$
a = b \cdot d_1 = (c \cdot d_2) \cdot d_1 = c \cdot (d_2 \cdot d_1),
$$

do đó $a \, c$.

**Tính chất 1.4.**

Nếu $a \, c$ và $b \, d$, thì $(a \cdot b) \, (c \cdot d)$.

**Chứng minh:**

$ a \, c \iff \exists x \, a = c \cdot x $, 

$ b \, d \iff \exists y \, b = d \cdot y $.

Từ đó ta có:

$$
a \cdot b = (c \cdot x)(d \cdot y) = c \cdot ((x \cdot d) \cdot y) = c \cdot ((d \cdot x) \cdot y) = (c \cdot d) \cdot (x \cdot y),
$$

do đó $(a \cdot b) \, (c \cdot d)$.



**Tính chất 1.5.** Nếu $a = b + c$ và trong phương trình này cả hai số $b$ và $c$ đều chia hết cho $d$, thì số $a$ cũng chia hết cho $d$.

**Chứng minh:**

Nếu $a \, d$ và $b \, d$, thì tồn tại các số $k_1$ và $k_2$ sao cho:

$$
a = d \cdot k_1 \quad \text{và} \quad b = d \cdot k_2.
$$

Thay vào phương trình ban đầu, ta có:

$$
d \cdot k_1 = d \cdot k_2 + c \quad \Rightarrow \quad d \cdot k_1 - d \cdot k_2 = c \quad \Rightarrow \quad d \cdot (k_1 - k_2) = c \quad \Rightarrow \quad c \, d.
$$

Trường hợp $a \, d$ và $c \, d$ được giải quyết tương tự.

Nếu $b \, d$ và $c \, d$, thì tồn tại các số $k_1$ và $k_2$ sao cho:

$$
b = d \cdot k_1 \quad \text{và} \quad c = d \cdot k_2.
$$

Thay vào phương trình ban đầu, ta có:

$$
a = d \cdot k_1 + d \cdot k_2 \quad \Rightarrow \quad a = d \cdot (k_1 + k_2) \quad \Rightarrow \quad a \, d.
$$



