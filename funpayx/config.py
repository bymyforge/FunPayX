import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')
PASSWORD = os.environ.get('PASSWORD')
GKEY = os.environ.get('GKEY')
GSEAL = os.environ.get('GSEAL')
FUNPAY_PROXY = os.environ.get('FUNPAY_PROXY')
TELEGRAM_PROXY = os.environ.get('TELEGRAM_PROXY')