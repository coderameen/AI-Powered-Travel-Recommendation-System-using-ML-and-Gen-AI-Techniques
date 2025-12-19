#!/usr/bin/env python3
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    
    print("Testing gemini-2.5-flash model with a sample travel prompt...")
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        test_prompt = "Give me 2 short travel destination recommendations."
        response = model.generate_content(test_prompt)
        print("\n✅ SUCCESS! Model works perfectly.\n")
        print("Response preview:")
        print(response.text[:200] + "...")
    except Exception as e:
        print(f"❌ Error: {e}")
else:
    print("GEMINI_API_KEY not found in .env")
