# 🔑 Google Gemini API Key Setup Instructions

## ⚠️ IMPORTANT: Set Up Your API Key Before Using AI Recommendations

The AI Recommendation feature requires a valid Google Gemini API key. Follow these steps to get and configure your API key:

---

## 📋 Step-by-Step Guide

### Step 1: Get Your Google Gemini API Key

1. **Visit the Google AI Studio**:
   - Go to: **https://aistudio.google.com/app/apikey**
   - Or: **https://makersuite.google.com/app/apikey**

2. **Sign In**:
   - Sign in with your Google account
   - If you don't have one, create a free Google account

3. **Create API Key**:
   - Click the **"Create API Key"** button
   - Or click **"Get API Key"** if available
   - Choose **"Create API key in new project"** (recommended)

4. **Copy Your API Key**:
   - Your API key will be displayed (looks like: `AIzaSyD...`)
   - Click the copy button to copy it
   - **IMPORTANT**: Save it securely - you'll need it!

---

### Step 2: Configure the API Key in Your Project

#### Method 1: Using .env File (Recommended) ✅

1. **Open the `.env` file** in your project folder:
   ```
   /Users/ameen/Documents/AI-Powered-Travel-Recommendation-System-using-ML-and-Gen-AI-Techniques/.env
   ```

2. **Edit the file**:
   - Find this line:
     ```
     GEMINI_API_KEY=YOUR_API_KEY_HERE
     ```
   
   - Replace `YOUR_API_KEY_HERE` with your actual API key:
     ```
     GEMINI_API_KEY=AIzaSyDaGZr3VwqINY1n-kHQPJ8TvJ7oiBULm3s
     ```

3. **Save the file**

4. **Restart the application**:
   - Stop the Flask server (Ctrl+C)
   - Run: `python app.py`

---

#### Method 2: Using Environment Variable

**On macOS/Linux:**
```bash
export GEMINI_API_KEY="your_api_key_here"
python app.py
```

**On Windows (Command Prompt):**
```cmd
set GEMINI_API_KEY=your_api_key_here
python app.py
```

**On Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY="your_api_key_here"
python app.py
```

---

### Step 3: Verify the Configuration

1. **Restart the Flask Application**:
   ```bash
   python app.py
   ```

2. **Check the Console Output**:
   - ✅ If successful, you'll see: `"✅ Google Gemini API configured successfully!"`
   - ⚠️ If there's an issue, you'll see warning messages with instructions

3. **Test the AI Recommendation**:
   - Login to your account
   - Navigate to **AI Recommendation** page
   - Fill out the form
   - Click **"Generate AI Recommendations"**
   - You should see personalized recommendations!

---

## 🔒 Security Best Practices

### DO ✅:
- Keep your API key in the `.env` file
- Add `.env` to `.gitignore` to avoid committing it
- Use environment variables for production
- Regenerate your key if accidentally exposed
- Keep your API key private

### DON'T ❌:
- Share your API key publicly
- Commit `.env` file to GitHub/Git
- Hardcode API key in source code
- Use the same key for multiple projects (optional)

---

## 🚨 Troubleshooting

### Problem 1: "API key not valid" Error

**Solution**:
1. Double-check your API key in the `.env` file
2. Ensure there are no extra spaces or quotes
3. Make sure you copied the complete key
4. Try regenerating a new API key from Google AI Studio

### Problem 2: "GEMINI_API_KEY not found" Warning

**Solution**:
1. Verify the `.env` file exists in the project root
2. Check the file name is exactly `.env` (not `env.txt` or `.env.txt`)
3. Ensure the key name is exactly `GEMINI_API_KEY`
4. Restart the application after editing `.env`

### Problem 3: No Recommendations Generated

**Solution**:
1. Check your internet connection
2. Verify the API key is valid
3. Check the API quota/limits in Google Cloud Console
4. Look for error messages in the browser

### Problem 4: ".env file not found"

**Solution**:
1. The file was created at: `AI-Powered-Travel-Recommendation-System-using-ML-and-Gen-AI-Techniques/.env`
2. If missing, create it manually with the content:
   ```
   GEMINI_API_KEY=YOUR_API_KEY_HERE
   ```
3. Replace `YOUR_API_KEY_HERE` with your actual key

---

## 💡 Quick Setup Example

```bash
# 1. Navigate to project folder
cd /Users/ameen/Documents/AI-Powered-Travel-Recommendation-System-using-ML-and-Gen-AI-Techniques

# 2. Edit .env file
nano .env
# or
open .env

# 3. Add your API key
GEMINI_API_KEY=AIzaSyD_your_actual_key_here

# 4. Save and close the file

# 5. Restart the app
python app.py
```

---

## 📊 API Key Format

Your API key should look like this:
```
AIzaSyDaGZr3VwqINY1n-kHQPJ8TvJ7oiBULm3s
```

**Characteristics**:
- Starts with `AIza`
- Contains letters, numbers, and some special characters
- About 39 characters long
- Case-sensitive

---

## 🆓 Free Tier Information

**Google Gemini AI Free Tier Includes**:
- 60 requests per minute
- 1,500 requests per day
- 1 million tokens per month

**Note**: These limits are sufficient for testing and development!

---

## 🔗 Helpful Links

1. **Get API Key**: https://aistudio.google.com/app/apikey
2. **Google AI Documentation**: https://ai.google.dev/docs
3. **Gemini API Guide**: https://ai.google.dev/tutorials/python_quickstart
4. **Manage API Keys**: https://console.cloud.google.com/apis/credentials

---

## ✅ Checklist

Before using AI Recommendations, ensure:

- [ ] You have a Google account
- [ ] You've created a Gemini API key
- [ ] The API key is copied correctly
- [ ] The `.env` file exists in project root
- [ ] The API key is pasted in `.env` file
- [ ] No extra spaces or quotes around the key
- [ ] The Flask app has been restarted
- [ ] You see the success message in console
- [ ] You can access the AI Recommendation page while logged in

---

## 📞 Still Having Issues?

If you're still experiencing problems:

1. **Check the Console**: Look for error messages when starting the app
2. **Verify .env Location**: The file must be in the project root
3. **Test API Key**: Try creating a new API key
4. **Check Quota**: Verify you haven't exceeded API limits
5. **Review Logs**: Check Flask console for detailed error messages

---

## 🎯 Final Notes

- The `.env` file is already created in your project folder
- You just need to replace `YOUR_API_KEY_HERE` with your actual key
- The application will show clear error messages if the key is missing or invalid
- API keys are free for reasonable usage (see free tier limits above)

**Once configured, you'll have access to powerful AI-generated travel recommendations! 🌍✈️**

---

**Last Updated**: December 19, 2025  
**Status**: Ready for Configuration
