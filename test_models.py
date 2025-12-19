#!/usr/bin/env python3
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    
    print("Fetching available models...")
    try:
        models = genai.list_models()
        print("\nAvailable models:")
        for model in models:
            print(f"  - {model.name}")
            if hasattr(model, 'supported_generation_methods'):
                print(f"    Methods: {model.supported_generation_methods}")
    except Exception as e:
        print(f"Error: {e}")
else:
    print("GEMINI_API_KEY not found in .env")
