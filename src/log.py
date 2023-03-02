import os
from datetime import datetime


class LogUtils:
    def __init__(self, message):
        self.message = message
        self.log()

    @staticmethod
    def logs_dir():
        if not os.path.exists("../logs"):
            os.mkdir("../logs")

    def log(self):
        self.logs_dir()
        with open("../logs/log.log", "a") as f:
            f.write(f"{datetime.utcnow()} - {self.message}\n")
            f.close()
