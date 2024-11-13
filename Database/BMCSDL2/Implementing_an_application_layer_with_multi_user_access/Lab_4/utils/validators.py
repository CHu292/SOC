import re

def is_valid_email(email):
    """
    Kiểm tra xem email có hợp lệ hay không.
    """
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email) is not None

def is_valid_phone_number(phone):
    """
    Kiểm tra xem số điện thoại có hợp lệ hay không.
    """
    phone_regex = r'^\+?1?\d{9,15}$'
    return re.match(phone_regex, phone) is not None

def validate_customer_data(data):
    """
    Kiểm tra dữ liệu của khách hàng trước khi thêm vào cơ sở dữ liệu.
    """
    errors = []
    if 'name' not in data or not data['name']:
        errors.append("Name is required")
    if 'email' in data and not is_valid_email(data['email']):
        errors.append("Invalid email format")
    if 'phone_number' in data and not is_valid_phone_number(data['phone_number']):
        errors.append("Invalid phone number format")
    return errors
