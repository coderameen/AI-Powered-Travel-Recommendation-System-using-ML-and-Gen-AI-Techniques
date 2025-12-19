from flask import Flask, render_template, request, redirect, url_for, session, flash
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import numpy as np
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import google.generativeai as genai
import os
import markdown
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# app
app = Flask(__name__)
app.secret_key = 'your_secret_key_here_change_in_production'  # Change this in production

# Configure Google Gemini API
# Get API key from environment variable
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Check if API key is set
if not GEMINI_API_KEY or GEMINI_API_KEY == 'YOUR_API_KEY_HERE':
    print("=" * 70)
    print("⚠️  WARNING: GEMINI_API_KEY not found or not set!")
    print("=" * 70)
    print("Please follow these steps to set up your API key:")
    print("1. Visit: https://aistudio.google.com/app/apikey")
    print("2. Sign in with your Google account")
    print("3. Click 'Create API Key' or 'Get API Key'")
    print("4. Copy the generated API key")
    print("5. Open the .env file in your project folder")
    print("6. Replace 'YOUR_API_KEY_HERE' with your actual API key")
    print("7. Save the file and restart the application")
    print("=" * 70)
else:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        print("✅ Google Gemini API configured successfully!")
    except Exception as e:
        print(f"❌ Error configuring Gemini API: {e}")

# Database initialization
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Initialize database on startup
init_db()

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login to access this page.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Load datasets and models
features = ['Name_x', 'State', 'Type', 'BestTimeToVisit', 'Preferences', 'Gender', 'NumberOfAdults', 'NumberOfChildren']
model = pickle.load(open('model.pkl','rb'))
label_encoders = pickle.load(open('label_encoders.pkl','rb'))

destinations_df = pd.read_csv("Expanded_Destinations.csv")
userhistory_df = pd.read_csv("Final_Updated_Expanded_UserHistory.csv")
df = pd.read_csv("final_df.csv")


# Collaborative Filtering Function
# Create a user-item matrix based on user history
user_item_matrix = userhistory_df.pivot(index='UserID', columns='DestinationID', values='ExperienceRating')

# Fill missing values with 0 (indicating no rating/experience)
user_item_matrix.fillna(0, inplace=True)

# Compute cosine similarity between users
user_similarity = cosine_similarity(user_item_matrix)


# Function to recommend destinations based on user similarity
def collaborative_recommend(user_id, user_similarity, user_item_matrix, destinations_df):
    """
    Recommends destinations based on collaborative filtering.

    Args:
    - user_id: ID of the user for whom recommendations are to be made.
    - user_similarity: Cosine similarity matrix for users.
    - user_item_matrix: User-item interaction matrix (e.g., ratings or preferences).
    - destinations_df: DataFrame containing destination details.

    Returns:
    - DataFrame with recommended destinations and their details.
    """
    # Find similar users
    similar_users = user_similarity[user_id - 1]

    # Get the top 5 most similar users
    similar_users_idx = np.argsort(similar_users)[::-1][1:6]

    # Get the destinations liked by similar users
    similar_user_ratings = user_item_matrix.iloc[similar_users_idx].mean(axis=0)

    # Recommend the top 5 destinations
    recommended_destinations_ids = similar_user_ratings.sort_values(ascending=False).head(5).index

    # Filter the destinations DataFrame to include detailed information
    recommendations = destinations_df[destinations_df['DestinationID'].isin(recommended_destinations_ids)][[
        'DestinationID', 'Name', 'State', 'Type', 'Popularity', 'BestTimeToVisit'
    ]]

    return recommendations

# Prediction system
def recommend_destinations(user_input, model, label_encoders, features, data):
    # Encode user input
    encoded_input = {}
    for feature in features:
        if feature in label_encoders:
            encoded_input[feature] = label_encoders[feature].transform([user_input[feature]])[0]
        else:
            encoded_input[feature] = user_input[feature]

    # Convert to DataFrame
    input_df = pd.DataFrame([encoded_input])

    # Predict popularity
    predicted_popularity = model.predict(input_df)[0]

    return predicted_popularity


# Route for the Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Route for Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        conn.close()
        
        if user and check_password_hash(user[2], password):
            session['user_id'] = user[0]
            session['username'] = user[1]
            flash('Login successful!', 'success')
            return redirect(url_for('recommendation'))
        else:
            flash('Invalid username or password!', 'danger')
    
    return render_template('login.html')

# Route for Signup Page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('signup'))
        
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        
        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', 
                         (username, hashed_password))
            conn.commit()
            conn.close()
            flash('Account created successfully! Please login.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username already exists!', 'danger')
    
    return render_template('signup.html')

# Route for Logout
@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

# Route for Travel Recommendation Page
@app.route('/recommendation')
@login_required
def recommendation():
    return render_template('recommendation.html')

# Route for AI Recommendation Page
@app.route('/ai-recommendation', methods=['GET', 'POST'])
@login_required
def ai_recommendation():
    if request.method == 'POST':
        # Get form data
        user_interest = request.form.get('user_interest')
        climate = request.form.getlist('climate')
        place_type = request.form.getlist('place_type')
        travel_group = request.form.get('travel_group')
        transport = request.form.get('transport')
        budget_min = request.form.get('budget_min')
        budget_max = request.form.get('budget_max')
        
        # Create a prompt for Gemini AI
        prompt = f"""
You are an expert travel advisor. Based on the following user preferences, provide detailed travel recommendations:

User Interests: {user_interest}
Preferred Climate: {', '.join(climate) if climate else 'Any'}
Type of Places: {', '.join(place_type) if place_type else 'Any'}
Traveling With: {travel_group}
Preferred Transport: {transport}
Budget Range: ₹{budget_min} - ₹{budget_max}

Please provide recommendations in the following format:

### 🇮🇳 Best Places to Visit in India
List 3-5 places with brief descriptions and why they match the preferences.

### 🌍 Best Places to Visit in the World
List 3-5 international destinations with brief descriptions.

### 📅 When to Visit
Recommend the best time to visit based on climate preferences and risk factors (weather, crowds, etc.)

### 🛡️ Safety Information
Provide safety tips and considerations for the recommended destinations.

### 🏨 Accommodation Suggestions
Suggest types of accommodations within the budget range (hotels, hostels, homestays, etc.)

### 💡 Additional Tips
Any extra advice for making the trip memorable.

Make your recommendations detailed, practical, and personalized based on the user's preferences.
"""
        
        try:
            # Check if API key is configured
            if not GEMINI_API_KEY or GEMINI_API_KEY == 'YOUR_API_KEY_HERE':
                flash('Google Gemini API key is not configured. Please check the .env file.', 'danger')
                return render_template('ai_recommendation.html')
            
            # Generate content using Gemini AI
            model = genai.GenerativeModel('gemini-2.5-latest')
            response = model.generate_content(prompt)
            
            # Convert markdown to HTML
            recommendation_html = markdown.markdown(response.text)
            
            return render_template('ai_recommendation.html', recommendation=recommendation_html)
        
        except Exception as e:
            error_message = str(e)
            if 'API_KEY_INVALID' in error_message or '400' in error_message:
                flash('Invalid API Key! Please update your GEMINI_API_KEY in the .env file. Visit https://aistudio.google.com/app/apikey to get a valid key.', 'danger')
            else:
                flash(f'Error generating recommendations: {error_message}', 'danger')
            return render_template('ai_recommendation.html')
    
    return render_template('ai_recommendation.html')

# Route for the recommendation
@app.route("/recommend", methods=['GET', 'POST'])
@login_required
def recommend():
    if request.method == "POST":
        user_id = request.form['user_id']
        user_id = int(user_id)
        # Capture form data
        user_input = {
            'Name_x': request.form['name'],
            'Type': request.form['type'],
            'State': request.form['state'],
            'BestTimeToVisit': request.form['best_time'],
            'Preferences': request.form['preferences'],
            'Gender': request.form['gender'],
            'NumberOfAdults': request.form['adults'],
            'NumberOfChildren': request.form['children'],
        }

        # Collaborative filtering function
        recommended_destinations = collaborative_recommend(user_id, user_similarity,
                                                           user_item_matrix, destinations_df)

        # Prediction function for popularity (if applicable)
        predicted_popularity = recommend_destinations(user_input, model, label_encoders, features, df)

        # Render the recommendation page with recommendations
        return render_template('recommendation.html', recommended_destinations=recommended_destinations,
                               predicted_popularity=predicted_popularity)
    return render_template('recommendation.html')


if __name__ == '__main__':
    # Run the app in debug mode
    app.run(debug=True)
