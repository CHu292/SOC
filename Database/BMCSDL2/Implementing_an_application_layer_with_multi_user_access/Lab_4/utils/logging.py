import logging
from datetime import datetime

# Cấu hình logging
logging.basicConfig(filename='app.log', level=logging.INFO, 
                    format='%(asctime)s %(levelname)s %(message)s')

def log_event(action, user_id=None, details=None):
    """
    Ghi lại một sự kiện vào hệ thống log.
    """
    log_message = f"Action: {action}, User ID: {user_id}, Details: {details}"
    logging.info(log_message)
