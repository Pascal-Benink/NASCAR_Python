import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

class SQLClient:

    def __init__(self):
        self.db = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST", "mysql"),
            user=os.getenv("MYSQL_USER", "mysql"),
            password=os.getenv("MYSQL_PASSWORD", "mysql"),
            database=os.getenv("MYSQL_DATABASE", "api"),
            port=int(os.getenv("MYSQL_PORT", "3306")),
            connection_timeout=int(os.getenv("MYSQL_CONNECTION_TIMEOUT", "180")),
        )
        print("Connected")
        self.cursor = self.db.cursor(
            buffered=True,
            dictionary=True
        )

    def update(self, query: str, params: tuple):
        self.cursor.execute(query, params)
        self.db.commit()

    def fetch_all(self, query: str, params=None) -> dict:
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def query_fix(self, query: str, params=None) -> dict:
        self.cursor.execute(query, params)
        self.db.commit()


    def insert(self, keys: tuple, values: tuple, table: str):
        key_str = ", ".join(keys)
        val_str = ", ".join(["%s"] * len(keys))
        q = f"INSERT INTO {table} ({key_str}) VALUES ({val_str})"
        self.cursor.execute(q, values)  # Use the `values` tuple here
        self.db.commit()
