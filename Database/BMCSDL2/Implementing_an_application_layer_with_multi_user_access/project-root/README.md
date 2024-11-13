# Flask Web Application with PostgreSQL Integration

## Setup
1. Clone the repository
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up PostgreSQL database and update `config.py` with credentials.
5. Run the application:
   ```bash
   flask run
   ```

## Features
- User login/logout system
- Basic dashboard with product list and add product functionality
- Role-based access control (read-only for some roles)
- Logging system for monitoring actions
