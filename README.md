
# IPBlocker

**Developer**: Abderrahim Chadli

IPBlocker is a Python-based application designed to manage and restrict access based on IP addresses. It provides functionalities for user authentication and IP blocking to enhance security.

## Features

- **User Authentication**: Secure user registration and login system.
- **IP Blocking**: Restrict access based on specified IP addresses.

## Project Structure

The repository is organized as follows:

- `auth_app/`: Contains modules related to user authentication.
- `project/`: Core project configurations and settings.
- `static/`: Stores static files like images, CSS, and JavaScript.
- `manage.py`: Django's command-line utility for administrative tasks.
- `db.sqlite3`: SQLite database file.
- `outline.md`: Project outline and notes.

## Installation

To set up the project locally:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/abderrahimchadli/ipblocker.git
   cd ipblocker
   ```

2. **Set up a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

   Access the application at `http://127.0.0.1:8000/`.

## Usage

- **User Registration**: Navigate to the registration page to create a new account.
- **IP Management**: Configure IP blocking settings through the admin interface or designated management pages.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your proposed changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

Abderrahim Chadli
