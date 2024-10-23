import pg8000
from config import Config

def get_db_connection():
    conn = pg8000.connect(
        host=Config.DB_CONFIG['host'],
        user=Config.DB_CONFIG['user'],
        password=Config.DB_CONFIG['password'],
        database=Config.DB_CONFIG['database'],
        port=Config.DB_CONFIG.get('port', 5432)
    )
    return conn
