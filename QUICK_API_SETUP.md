# 🚀 QUICK FIX: Set Up Your Google Gemini API Key

## ⚡ 3-Minute Setup

### Step 1️⃣: Get Your API Key (2 minutes)

1. **Open this link**: https://aistudio.google.com/app/apikey
2. **Sign in** with your Google account
3. **Click** "Create API Key" button
4. **Copy** the generated key (starts with `AIza...`)

---

### Step 2️⃣: Update .env File (30 seconds)

**The `.env` file is already created in your project!**

📁 Location: `AI-Powered-Travel-Recommendation-System-using-ML-and-Gen-AI-Techniques/.env`

**Open the file and change this:**

```bash
# BEFORE (current):
GEMINI_API_KEY=YOUR_API_KEY_HERE

# AFTER (with your key):
GEMINI_API_KEY=AIzaSyDaGZr3VwqINY1n-YOUR-ACTUAL-KEY-HERE
```

**Save the file!** 💾

---

### Step 3️⃣: Restart the App (30 seconds)

```bash
# Stop the current app (press Ctrl+C in terminal)
# Then restart:
python app.py
```

**Look for this message**: ✅ `Google Gemini API configured successfully!`

---

## ✅ That's It!

Now you can use the **AI Recommendation** feature! 🤖

---

## 🎯 Visual Guide

```
┌─────────────────────────────────────────────────┐
│  1. Visit: aistudio.google.com/app/apikey       │
│  2. Click: "Create API Key"                     │
│  3. Copy: AIzaSyD... (your key)                 │
└─────────────────────────────────────────────────┘
                      ⬇️
┌─────────────────────────────────────────────────┐
│  Open: .env file in project folder              │
│  Replace: YOUR_API_KEY_HERE                     │
│  With: Your copied API key                      │
│  Save: The file                                 │
└─────────────────────────────────────────────────┘
                      ⬇️
┌─────────────────────────────────────────────────┐
│  Stop: Current Flask app (Ctrl+C)               │
│  Run: python app.py                             │
│  Check: ✅ Success message                       │
└─────────────────────────────────────────────────┘
                      ⬇️
┌─────────────────────────────────────────────────┐
│  🎉 Ready to use AI Recommendations!            │
└─────────────────────────────────────────────────┘
```

---

## 📝 Example .env File Content

```bash
# Google Gemini API Key
# Get your API key from: https://aistudio.google.com/app/apikey

GEMINI_API_KEY=AIzaSyDaGZr3VwqINY1n-kHQPJ8TvJ7oiBULm3s
```

---

## 🔍 Troubleshooting

### Error: "API key not valid"
**Fix**: Double-check you copied the FULL key with no spaces

### Error: "GEMINI_API_KEY not found"
**Fix**: Make sure the `.env` file is in the project ROOT folder

### No .env file?
**Create it**: A file named `.env` (with the dot) in the project folder with:
```
GEMINI_API_KEY=your_key_here
```

---

## 💰 Is It Free?

**YES!** Google Gemini offers a generous free tier:
- 60 requests per minute
- 1,500 requests per day
- Perfect for development and testing!

---

## 🎓 Need More Help?

Check the detailed guide: `GEMINI_API_SETUP.md`

---

**That's all! Simple, right?** 😊
