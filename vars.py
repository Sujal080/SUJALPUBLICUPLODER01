#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", ""))
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER = int(environ.get("OWNER", "8118667253"))  # Optional: still used maybe for logs or admin
CREDIT = "✿𝐒𝐔𝐉𝐀𝐋✿"

# 🟢 PUBLIC ACCESS: sabko allow kiya gaya hai
AUTH_USERS = []  # Empty list: koi restriction nahi rahegi

# ➕ MongoDB config (Render env se aayega)
MONGO_URI = environ.get("MONGO_URI", "")
DB_NAME = environ.get("DB_NAME", "Telegrambot")
COLLECTION_NAME = environ.get("COLLECTION_NAME", "Telegrambot")

#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
