

# 2.1 Built in Functions - Hàm tích hợp sẵn

Có rất nhiều hàm có sẵn như: print(), len(), type(), int(), float(), str(), input(), list(), dict(), min(), max(), sum(), sorted(), open(), file(), help(),  dir()

[Để xem rõ chức năng từng hàm có thể tham khảo tại:](https://docs.python.org/3.9/library/functions.html)

![Built-in Functions](./img/2.1.png)

- Một số hàm phổ biến:

```python
chu@chu-Latitude-5510:~$ python3
Python 3.10.12 (main, Jul 29 2024, 16:56:48) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print('Hello, World!') # it prints the text value Hello, World!
Hello, World!
>>> len('Hello, World!') # it counts the number of characters including space
13
>>> type('Hello, World!') # it checks the data type
<class 'str'>
>>> str(5) # it converts number to string
'5'
>>> int('5') # it converts to number
5
>>> float(10) # it converts integer to decimal
10.0
>>> input('Enter your name:') # it takes user input
Enter your name:Chumiran
'Chumiran'
>>> exit() # để thoát ra
```

- Chúng ta hãy thực hành nhiều hơn bằng cách sử dụng các hàm tích hợp khác nhau

```python
chu@chu-Latitude-5510:~$ python3
Python 3.10.12 (main, Jul 29 2024, 16:56:48) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> help('keywords') # prints all python reserved words

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

>>> help(str) # give information about string

>>> dir(str) # give information about string
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', 
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', 
'__mod__', '__mul__', '__ne__', '__new__', '__reduce__', 
'__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', 
'__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 
'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 
'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 
'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 
'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
  'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 
  'title', 'translate', 'upper', 'zfill']
```

- Như bạn có thể thấy từ terminal ở trên, Python có các từ dành riêng. Chúng ta không sử dụng các từ dành riêng để khai báo biến hoặc hàm

```python
chu@chu-Latitude-5510:~$ python3
Python 3.10.12 (main, Jul 29 2024, 16:56:48) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> min(20, 30, 40, 50) # give the minimum value
20
>>> max(20, 30, 40, 50) # give the maximum value
50
>>> min([20, 30, 40, 50]) # it takes list as an argument and return min
20
>>> max([20, 30, 40, 50]) # it takes list as an argument and return max
50
>>> sum([20, 30, 40, 50]) # it takes only list as an argument and return the sum
140
>>> exit()
```
---

# 2.2 Variable - Biến

- Biến lưu trữ dữ liệu trong bộ nhớ máy tính. Biến Mnemonic được khuyến khích sử dụng trong nhiều ngôn ngữ lập trình. Biến Mnemonic là tên biến có thể dễ nhớ và liên kết. Biến tham chiếu đến địa chỉ bộ nhớ trong đó dữ liệu được lưu trữ. Không được phép sử dụng số ở đầu, ký tự đặc biệt, dấu gạch nối khi đặt tên biến. Biến có thể có tên ngắn (như x, y, z), nhưng nên sử dụng tên mô tả hơn (tên, họ, tuổi, quốc gia).
- Quy tắc tên biến Python
  - Tên biến phải bắt đầu bằng một chữ cái hoặc ký tự gạch dưới
  - Tên biến không được bắt đầu bằng một số
  - Tên biến chỉ có thể chứa các ký tự chữ và số và dấu gạch dưới (A-z, 0-9 và _)
  - Tên biến phân biệt chữ hoa chữ thường (firstname, Firstname, FirstName và FIRSTNAME) là các biến khác nhau)
 
- Dưới đây là một số ví dụ về biến

```python
firstname
lastname
age
country
city
first_name
last_name
capital_city
_if # if we want to use reserved word as a variable
year_2021
year2021
current_year_2021
birth_year
num1
num2
```

- Dưới đây là một số ví dụ về biến không hợp lệ

```python
first-name
first@name
first$name
num-1
1num
```

- Chúng ta sẽ sử dụng kiểu đặt tên biến Python chuẩn đã được nhiều nhà phát triển Python áp dụng. Các nhà phát triển Python sử dụng quy ước đặt tên biến snake case (snake_case). Chúng ta sử dụng ký tự gạch dưới sau mỗi từ cho một biến chứa nhiều hơn một từ (ví dụ: first_name, last_name, engine_rotation_speed). Ví dụ bên dưới là một ví dụ về cách đặt tên biến chuẩn, dấu gạch dưới là bắt buộc khi tên biến có nhiều hơn một từ.
- Khi chúng ta gán một kiểu dữ liệu nhất định cho một biến, thì đó được gọi là khai báo biến. Ví dụ trong ví dụ bên dưới, tên của tôi được gán cho một biến first_name. Dấu bằng là toán tử gán. Gán có nghĩa là lưu trữ dữ liệu trong biến. Dấu bằng trong Python không phải là dấu bằng như trong Toán học.
- Ví dụ:

```python
# Variables in Python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }
```

- hạn. Đối số là một giá trị mà chúng ta có thể được truyền hoặc đặt bên trong dấu ngoặc đơn của hàm, xem ví dụ bên dưới.
- Ví dụ:

```python
print('Hello, World!') # Văn bản "Hello, World!" là một đối số
print('Hello',',', 'World','!') # Nó có thể nhận nhiều đối số, ở đây có bốn đối số được truyền vào
print(len('Hello, World!')) # Nó chỉ nhận một đối số
```

- Ví dụ in ra và tìm độ dài của các biến

```python
chu@chu-Latitude-5510:$ cat variable_2.py 
# Variables in Python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

chu@chu-Latitude-5510:$ python3 variable_2.py 
First name: Asabeneh
First name length: 8
Last name:  Yetayeh
Last name length:  7
Country:  Finland
City:  Helsinki
Age:  250
Married:  True
Skills:  ['HTML', 'CSS', 'JS', 'React', 'Python']
```

- Khai báo nhiều biến trong một dòng

```python
chu@chu-Latitude-5510:$ cat multiple_variable.py 
first_name, last_name, country, age, is_married = 'Mirann', 'Chu', 'Vietnam', 22, False
print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name:', last_name)
print('Country:', country)
print('Age:', age)
print('Married:', is_married)

chu@chu-Latitude-5510:$ python3 multiple_variable.py 
Mirann Chu Vietnam 22 False
First name: Mirann
Last name: Chu
Country: Vietnam
Age: 22
Married: False
```

- Nhận thông tin đầu vào của người dùng bằng hàm có sẵn input(). Chúng ta hãy gán dữ liệu chúng ta nhận được từ người dùng vào các biến first_name và age.

```python3

chu@chu-Latitude-5510:$ cat the_input_function.py 
first_name = input('What is your name: ')
age = input('How old are you: ')

print('First name: ', first_name)
print('Age: ', age)

chu@chu-Latitude-5510:$ python3 the_input_function.py 
What is your name: Chumirann
How old are you: 22
First name:  Chumirann
Age:  22
```

# 2.3 Data Types - Kiểu dữ liệu

- Có một số loại dữ liệu trong Python. Để xác định loại dữ liệu, chúng tôi sử dụng hàm có sẵn type().
- Kiểm tra kiểu dữ liệu: Để kiểm tra kiểu dữ liệu của dữ liệu/biến nhất định, chúng tôi sử dụng type()
- Ví dụ:

```python
chu@chu-Latitude-5510:$ cat check_data_type.py 
# Different python data types
# Let's declare  variables with various  data types

first_name = 'Chu'		# str
last_name = 'Mirann'		# str
country = 'Vietnam'		# str
city = 'Dalat'			# str
age = 22			# int

# printing out types

print(type('Chu'))		# str
print(type(first_name))		# str
print(type(10))			# int
print(type(3.14))		# float
print(type(2 + 3j))		# complex
print(type(False))		# bool
print(type([1, 2, 3]))		# list
print(type({'name': 'Chu', 'age':22, 'is_married': False}))	# dict
print(type((1,2)))		# tuple
print(type(zip([1,2],[3,4])))	# set

chu@chu-Latitude-5510:$ python3 check_data_type.py 
<class 'str'>
<class 'str'>
<class 'int'>
<class 'float'>
<class 'complex'>
<class 'bool'>
<class 'list'>
<class 'dict'>
<class 'tuple'>
<class 'zip'>
```

**Ép kiểu (Casting):** Chuyển đổi một kiểu dữ liệu sang một kiểu dữ liệu khác. Chúng ta sử dụng các hàm như `int()`, `float()`, `str()`, `list()`, `set()` để thực hiện việc này. 

- Khi thực hiện các phép toán số học, các chuỗi chứa số cần được chuyển đổi trước thành kiểu `int` hoặc `float`, nếu không sẽ gây ra lỗi.  
- Nếu chúng ta nối (concatenate) một số với một chuỗi, số đó cần được chuyển đổi sang chuỗi trước.  

Chúng ta sẽ tìm hiểu thêm về phép nối chuỗi trong phần **Chuỗi (String)**.

- Ví dụ:

```python
# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
num_float = float(num_str)
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']
```
---

# 2.4 Bài tập

---

## 2.4.1 Bài tập 1

1. Khai báo một biến tên là first_name và gán giá trị cho nó.
2. Khai báo một biến tên là last_name và gán giá trị cho nó.
3. Khai báo một biến tên là full_name và gán giá trị cho nó.
4. Khai báo một biến tên là country và gán giá trị cho nó.
5. Khai báo một biến tên là city và gán giá trị cho nó.
6. Khai báo một biến tên là age và gán giá trị cho nó.
7. Khai báo một biến tên là year và gán giá trị cho nó.
8. Khai báo một biến tên là is_married và gán giá trị cho nó.
9. Khai báo một biến tên là is_true và gán giá trị cho nó.
10. Khai báo một biến tên là is_light_on và gán giá trị cho nó.
11. Khai báo nhiều biến trên một dòng.

```python
first_name = 'Mirann'
last_name = 'Chu'
full_name = 'Chumirann'
country = 'Vietnam'
city = 'Dalat'
age = 22
year = 2024
is_married = False
is_true = True
is_light_on = True

first_name_2, last_name_2, full_name_2, country_2, city_2, age_2, year_2 = 'Mirann', 'Chu', 'Chumirann', 'Vietnam', 'Dalat', 22, 2024
```

## 2.4.2 Bài tập 2

1. Kiểm tra kiểu dữ liệu của tất cả các biến bằng cách sử dụng hàm tích hợp `type()`.  
2. Sử dụng hàm tích hợp `len()` để tìm độ dài của tên (first name) của bạn.  
3. So sánh độ dài giữa tên (first name) và họ (last name) của bạn.  
4. Khai báo giá trị 5 là `num_one` và 4 là `num_two`.  
5. Cộng `num_one` và `num_two` rồi gán giá trị vào biến `total`.  
6. Trừ `num_two` khỏi `num_one` rồi gán giá trị vào biến `diff`.  
7. Nhân `num_two` với `num_one` rồi gán giá trị vào biến `product`.  
8. Chia `num_one` cho `num_two` rồi gán giá trị vào biến `division`.  
9. Sử dụng phép chia dư (modulus) để tìm phần dư khi `num_two` chia cho `num_one`, sau đó gán giá trị vào biến `remainder`.  
10. Tính lũy thừa của `num_one` mũ `num_two` và gán giá trị vào biến `exp`.  
11. Tìm kết quả của phép chia lấy phần nguyên (floor division) giữa `num_one` và `num_two`, sau đó gán giá trị vào biến `floor_division`.  
12. Bán kính của hình tròn là 30 mét.  
    - Tính diện tích của hình tròn và gán giá trị vào biến `area_of_circle`.  
    - Tính chu vi của hình tròn và gán giá trị vào biến `circum_of_circle`.  
    - Nhập bán kính từ người dùng và tính diện tích.  
13. Sử dụng hàm `input()` tích hợp để nhập tên, họ, quốc gia và tuổi từ người dùng, sau đó gán giá trị vào các biến tương ứng.  
14. Chạy lệnh `help('keywords')` trong Python shell hoặc trong tệp của bạn để kiểm tra các từ khóa dành riêng trong Python.  

```python
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print('lenght of first name: ', len(first_name))

if len(first_name) > len(last_name):
	print('lenght of first name longer than last name')
else:
	print('lenght of last name longer than frist name')

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one*num_two
divison = num_one/num_two
remainder = num_one%num_two
exp = num_one**num_two
floor_division = num_one//num_two

radius = 30
area_of_circle = 3.14 * 30 * 30
print('Area of a circle: ', area_of_circle)
circum_of_circle = 2 * 3.14 * 30
print('circumference of a circle: ', circum_of_circle)

first_name_3 = input()
last_name_3  = input()
country_3 = input()
age_3 = input()
```
