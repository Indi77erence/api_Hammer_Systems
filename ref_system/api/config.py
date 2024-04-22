from dotenv import load_dotenv
import os

load_dotenv()
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
TWILIO_TOKEN = os.environ.get('TWILIO_TOKEN')
TWILIO_SID = os.environ.get('TWILIO_SID')
NUMBER = os.environ.get('NUMBER')
