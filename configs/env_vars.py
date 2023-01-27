import os
from dotenv import load_dotenv

load_dotenv()  # loads .env variables

TELEGRAM_BOT_API_TOKEN = os.environ.get('TELEGRAM_BOT_API_TOKEN')  # retrieves token from .env
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
