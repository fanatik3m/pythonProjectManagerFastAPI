import os

from dotenv import load_dotenv

load_dotenv()

DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_PORT = os.environ.get('DB_PORT')
DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')

TEST_DB_USER = os.environ.get('TEST_DB_USER')
TEST_DB_PASS = os.environ.get('TEST_DB_PASS')
TEST_DB_PORT = os.environ.get('TEST_DB_PORT')
TEST_DB_HOST = os.environ.get('TEST_DB_HOST')
TEST_DB_NAME = os.environ.get('TEST_DB_NAME')

SECRET = os.environ.get('SECRET')