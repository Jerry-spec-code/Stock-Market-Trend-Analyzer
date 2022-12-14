import os 
from dotenv import load_dotenv
load_dotenv()

pythonEnv = os.environ.get('PYTHON_ENV')
host = os.environ.get('DB_HOST')
database = os.environ.get('DB_DATABASE')
user = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')
