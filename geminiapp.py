import os

import requests
import psycopg2
from dotenv import load_dotenv

load_dotenv()

URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=YOUR_API_KEY"

res = requests.post(
    URL,
    headers={"Content-Type": "application/json"},
    
    json={"prompt": "Hello, my name is"})
