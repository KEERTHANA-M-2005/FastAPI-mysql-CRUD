from sqlalchemy import create_engine, text
from utils.config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME

DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

def get_connection():
    return engine.connect()
