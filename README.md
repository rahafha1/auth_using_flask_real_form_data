# 🛡️ User Authentication System using Flask with HTML Frontend

This project is a complete user authentication system built with **Flask** and **HTML** frontend, including registration, login with JWT tokens, protected routes, and profile management. The frontend includes login and signup forms that communicate with the backend to handle user authentication.

# 🚀 Features

- **User Registration** with password hashing (secured using Werkzeug)
- **User Login** with JWT Token (expires in 1 hour)
- **Protected Routes** to access user profile data after login
- **HTML Forms** for registration and login
- **JWT Authentication** to secure user sessions without traditional session cookies
- **User Profile** route protected by JWT authentication
- **Email welcome message** (simulated via console output for simplicity)
- **Simple and responsive UI** using HTML, CSS, and JavaScript
- **Clean Project Structure** using Flask Blueprints
- **SQLite Database** for storing user credentials and profiles
- **CORS enabled** for cross-origin frontend requests

---

# ⚙️ Tech Stack

- **Backend**:
  - Flask
  - Flask-JWT-Extended (for JWT token management)
  - Flask-SQLAlchemy (for database management)
  - SQLite (for database storage)
  - Flask-CORS (for handling cross-origin requests)
  - Werkzeug (for secure password hashing)

- **Frontend**:
  - HTML (forms for registration and login)
  - CSS (for styling the pages)
  - JavaScript (for frontend logic, JWT handling, and form submission)

- **Development Tools**:
  - Postman (for testing APIs)

---

# 📂 Project Structure

project/
│
├── app.py # Main Flask application file
├── config.py # Configuration settings
├── models.py # Database models (User)
├── requirements.txt # Project dependencies
│
├── routes/ # Folder containing Flask route definitions
│ ├── init.py
│ ├── auth_routes.py # Routes for user authentication (register, login)
│ └── protected_routes.py # Protected routes that require JWT (profile)
│
├── templates/ # Folder for HTML templates
│ ├── login.html # Login page HTML
│ ├── register.html # Registration page HTML
│ └── profile.html # User profile page (protected)
│
├── static/ # Folder for static assets (CSS, JavaScript)
│ ├── style.css # Styles for the frontend
│ └── script.js # JavaScript for handling form actions and JWT
└── .env # Environment file for secret keys and credentials


---

# 🧪 API Endpoints

## 🔐 Authentication Routes

### `POST /auth/register`
Register a new user.

##### **Request Body (JSON)**:
  json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "password": "securepassword"
  }
##### Responses:

201 Created: User successfully created
409 Conflict: Email already in use
400 Bad Request: Missing or invalid fields
POST /auth/login
Login with email and password to receive a JWT token.

##### Request Body (JSON):
{
  "email": "john@example.com",
  "password": "securepassword"
}

##### Responses:

200 OK: Returns JWT token on successful login
401 Unauthorized: Invalid credentials

## 🔐 Protected Routes:
GET /api/profile
Returns the user's profile data. Requires JWT token in the Authorization header.

##### Headers:
Authorization: Bearer <your_jwt_token>
##### Response:
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "created_at": "2024-05-01T12:34:56"
}

#  Setup & Run :
1- Clone the repository:
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2-Create a virtual environment and install dependencies:
python -m venv venv
mac use:source venv/bin/activate 
On Windows, use: .\venv\Scripts\activate then 
pip install -r requirements.txt
3-Create a .env file (optional): SECRET_KEY=your_secret_key
4-Create the database: python :
from app import db
db.create_all()
exit()
5- Run the app:
python app.py , then The application will run on http://localhost:5000.



# Frontend Usage:
##### Registration: Navigate to the registration page, fill out the form, and submit the details to register a new user.
##### Login: Once registered, use the login form to authenticate and receive a JWT token.
##### Profile: After successful login, you'll be redirected to the profile page, where your user details will be shown.
##### Logout: You can clear the token and log out from the application by removing the token stored in your browser’s localStorage.


# Requirements:
To generate requirements.txt with all dependencies:
pip freeze > requirements.txt
or pip install -r requirements.txt 




