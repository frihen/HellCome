from log import LogUtils as log
import os
from dotenv import load_dotenv

import mysql.connector

load_dotenv()

host = os.getenv("HOST_DB")
port = os.getenv("PORT_DB")
user = os.getenv("USER_DB")
password = os.getenv("PASS_DB")


class Connect:
    def __init__(self):
        self.db = None
        self.cursor = None

    def connect(self):
        try:
            self.db = mysql.connector.connect(
                host=host,
                port=int(port),
                user=user,
                password=password,
            )
            return self.db
        except mysql.connector.Error as err:
            log(f"Error connection mysql: {err}")

    def execute_sql(self, query):
        db = self.connect()
        cur = db.cursor()
        cur.execute(query)
        count = cur.fetchone()[0]
        log(f"{query} - {count}")
        return f"{query} - {count}"
