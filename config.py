# config.py

from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
LABEL_NAME = 'ARTICOLI INTERESSANTI'
DATABASE_NAME = 'articoli.db'
