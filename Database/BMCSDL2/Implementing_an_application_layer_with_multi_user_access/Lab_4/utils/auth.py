from flask import request, jsonify
from functools import wraps

def require_role(required_role):
    """
    Decorator yêu cầu vai trò cụ thể cho một endpoint.
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user_role = request.headers.get('Role')  # Lấy vai trò từ header yêu cầu
            
            if user_role != required_role:
                return jsonify({'message': 'Permission denied'}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator
