import os
import hashlib
import fnmatch
import stat
import subprocess

TEMPLATE_FILE = 'template.tbl'

# Функция для чтения файла template.tbl
def read_template_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    hashed_password = lines[0].strip()  # Первая строка содержит хешированный пароль
    forbidden_files = [line.strip() for line in lines[1:]]  # Список запрещённых файлов
    return hashed_password, forbidden_files

# Функция для хэширования пароля
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Функция проверки пароля пользователя
def check_password(hashed_password, input_password):
    return hashed_password == hash_password(input_password)

# Функция проверки, является ли файл запрещённым
def is_forbidden_file(filename, forbidden_files):
    for pattern in forbidden_files:
        if fnmatch.fnmatch(filename, pattern):
            return True
    return False

# Функция для защиты файла (запрет на чтение, запись, удаление, перемещение)
def protect_file(filepath):
    # Установка прав без чтения, записи и выполнения для всех пользователей
    os.chmod(filepath, 0)
    # Используем chattr для предотвращения удаления и перемещения файла (immutable)
    subprocess.run(['sudo', 'chattr', '+i', filepath])
    print(f"Файл защищён: {filepath}")

# Функция для снятия защиты с файла (разрешение чтения, записи, удаления, перемещения)
def unprotect_file(filepath):
    # Снять атрибут immutable (разрешить удаление файла)
    subprocess.run(['sudo', 'chattr', '-i', filepath])
    # Восстановить права на чтение, запись и выполнение для владельца
    os.chmod(filepath, stat.S_IRWXU)
    print(f"Доступ к файлу восстановлен: {filepath}")

# Функция для защиты или снятия защиты файлов в текущем каталоге
def protect_files(directory, forbidden_files, enable=True):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if is_forbidden_file(file, forbidden_files):
                filepath = os.path.join(root, file)
                if enable:
                    protect_file(filepath)
                else:
                    unprotect_file(filepath)

# Функция для включения/выключения режима защиты
def toggle_protection(template_file, enable=True):
    hashed_password, forbidden_files = read_template_file(template_file)
    
    input_password = input("Введите пароль для включения/выключения защиты: ")
    
    if check_password(hashed_password, input_password):
        if enable:
            print("Пароль правильный! Начинаем защищать файлы.")
        else:
            print("Пароль правильный! Снимаем защиту с файлов.")
        current_directory = os.getcwd()  # Текущая директория
        protect_files(current_directory, forbidden_files, enable)
    else:
        print("Неправильный пароль! Не могу включить/выключить защиту.")

# Запуск программы
if __name__ == "__main__":
    choice = input("Введите 'on' для включения защиты или 'off' для отключения защиты: ").strip().lower()
    if choice == 'on':
        toggle_protection(TEMPLATE_FILE, enable=True)
    elif choice == 'off':
        toggle_protection(TEMPLATE_FILE, enable=False)
    else:
        print("Неверный выбор.")
