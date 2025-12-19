# 🔐 Authentication System Documentation

## Overview
This Travel Recommendation System now includes a complete user authentication system with signup and login functionality, storing user credentials securely in a SQLite3 database.

## ✨ Features Implemented

### 1. **User Authentication**
- ✅ User Registration (Signup)
- ✅ User Login
- ✅ User Logout
- ✅ Session Management
- ✅ Password Hashing (using werkzeug.security)
- ✅ Protected Routes (Login Required)

### 2. **Database**
- SQLite3 database (`users.db`)
- User table with fields:
  - `id` (Primary Key, Auto-increment)
  - `username` (Unique, Not Null)
  - `password` (Hashed, Not Null)
  - `created_at` (Timestamp)

### 3. **Beautiful UI with Navigation Bar**
- Modern gradient design
- Responsive navigation bar with Font Awesome icons
- Smooth animations and transitions
- Bootstrap 5 framework
- Mobile-friendly responsive design
- Professional color scheme (Purple gradient theme)

## 🎨 UI Components

### Navigation Bar Features:
- **Brand Logo**: Travel Recommender with plane icon
- **Home Link**: Navigate to homepage
- **Recommendations Link**: Access recommendations (protected)
- **User Display**: Shows logged-in username
- **Login/Signup Buttons**: For guest users
- **Logout Button**: For authenticated users

### Pages Styling:
1. **Home Page**: 
   - Video background with overlay
   - Centered welcome card
   - Call-to-action buttons

2. **Login Page**:
   - Modern card design with gradient header
   - Icon-based input fields
   - Smooth animations
   - Link to signup page

3. **Signup Page**:
   - Similar styling to login page
   - Password confirmation field
   - Client-side validation
   - Link to login page

4. **Recommendation Page**:
   - Enhanced form with icons
   - Beautiful table design for results
   - Gradient buttons and badges

## 🔒 Security Features

1. **Password Hashing**: Uses `pbkdf2:sha256` algorithm
2. **Session Management**: Flask sessions with secret key
3. **Login Required Decorator**: Protects sensitive routes
4. **SQL Injection Prevention**: Parameterized queries
5. **Password Confirmation**: Ensures passwords match during signup

## 📁 File Structure

```
├── app.py                          # Main Flask application with authentication
├── users.db                        # SQLite3 database (auto-created)
├── templates/
│   ├── index.html                  # Home page with navbar
│   ├── login.html                  # Login form
│   ├── signup.html                 # Signup form
│   └── recommendation.html         # Recommendations page with navbar
└── AUTHENTICATION_README.md        # This file
```

## 🚀 How to Use

### 1. Start the Application
```bash
python app.py
```

### 2. Access the Application
Open your browser and navigate to: `http://127.0.0.1:5000`

### 3. Create an Account
1. Click on "Sign Up" button
2. Enter username (minimum 3 characters)
3. Enter password (minimum 6 characters)
4. Confirm password
5. Click "Sign Up"

### 4. Login
1. Click on "Login" button
2. Enter your username and password
3. Click "Login"

### 5. Access Recommendations
- Once logged in, you can access the "Recommendations" page
- The system will remember your session
- You can logout anytime using the "Logout" button

## 🔑 Key Functions in app.py

### Database Functions
```python
init_db()                    # Initialize database and create users table
```

### Route Protection
```python
@login_required             # Decorator to protect routes
```

### Routes
- `/` - Home page
- `/login` - Login page (GET/POST)
- `/signup` - Signup page (GET/POST)
- `/logout` - Logout and clear session
- `/recommendation` - Recommendations page (Protected)
- `/recommend` - Process recommendations (Protected)

## 🎨 Design Elements

### Color Scheme
- Primary: `#667eea` (Purple Blue)
- Secondary: `#764ba2` (Dark Purple)
- Gradient: `linear-gradient(135deg, #667eea 0%, #764ba2 100%)`

### Icons (Font Awesome)
- `fa-plane` - Travel/Brand icon
- `fa-home` - Home
- `fa-compass` - Recommendations
- `fa-user` - User profile
- `fa-sign-in-alt` - Login
- `fa-sign-out-alt` - Logout
- `fa-user-plus` - Signup
- `fa-lock` - Password field
- And many more...

### Animations
- Fade-in effects
- Hover transitions
- Scale transformations
- Smooth color transitions

## ⚡ Flash Messages

The system uses Flask's flash messaging for user feedback:
- ✅ Success messages (green)
- ⚠️ Warning messages (yellow)
- ❌ Error messages (red)
- ℹ️ Info messages (blue)

## 🔐 Session Management

- User ID stored in session after login
- Username displayed in navbar when logged in
- Session cleared on logout
- Protected routes redirect to login if not authenticated

## 📝 Database Schema

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🛡️ Password Requirements

- Minimum 6 characters for password
- Password confirmation required during signup
- Passwords are hashed before storage
- Never stored in plain text

## 🌟 User Experience Features

1. **Smooth Navigation**: Responsive navbar with active page highlighting
2. **Visual Feedback**: Flash messages for all user actions
3. **Form Validation**: Client and server-side validation
4. **Professional Design**: Modern UI with gradients and shadows
5. **Mobile Responsive**: Works on all device sizes
6. **Accessibility**: Clear labels and ARIA support

## 🔧 Technical Stack

- **Backend**: Flask (Python)
- **Database**: SQLite3
- **Security**: Werkzeug Security (Password Hashing)
- **Frontend**: HTML5, CSS3, JavaScript
- **Framework**: Bootstrap 5
- **Icons**: Font Awesome 6
- **Session**: Flask Sessions

## 📱 Responsive Design

The application is fully responsive and works on:
- Desktop computers
- Tablets
- Mobile phones
- All modern browsers

## 🎯 Next Steps (Optional Enhancements)

1. Add "Remember Me" functionality
2. Implement password reset feature
3. Add email verification
4. User profile page
5. Password strength indicator
6. Two-factor authentication
7. Social login (Google, Facebook)
8. User activity logging

## 🐛 Troubleshooting

### Database Issues
If you encounter database issues, delete `users.db` and restart the application. The database will be recreated automatically.

### Port Already in Use
If port 5000 is already in use, modify the last line in `app.py`:
```python
app.run(debug=True, port=5001)
```

### Static Files Not Loading
Ensure you're accessing the application through `http://127.0.0.1:5000` and not `localhost:5000`

## 📄 License
This authentication system is part of the AI-Powered Travel Recommendation System.

## 👨‍💻 Developer Notes

- All passwords are hashed using `pbkdf2:sha256`
- Session secret key should be changed in production
- Database is created automatically on first run
- Flash messages are categorized for styling
- Routes use decorators for protection
- SQL injection is prevented through parameterized queries

---

**Created**: December 19, 2025
**Version**: 1.0
**Status**: ✅ Fully Functional
