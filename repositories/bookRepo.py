import sqlite3
from sqlite3 import Error

class BookRepo:
    def __init__(self, dbConnection: str):
        self.db = sqlite3.connect(dbConnection).cursor()
