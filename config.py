 import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

SALESEEN_API_KEY = os.getenv("SALESEEN_API_KEY")
SALESEEN_API_URL = os.getenv("SALESEEN_API_URL")

CHANNEL_1 = os.getenv("CHANNEL_1")
CHANNEL_2 = os.getenv("CHANNEL_2")