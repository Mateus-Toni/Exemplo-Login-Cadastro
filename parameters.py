import os
from dotenv import load_dotenv

load_dotenv()

NAME = os.environ.get('DB_USER_NAME')
PASSWORD  = os.environ.get('DB_PASSWORD')
HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')

