import sqlite3
import sys
from sqlite3 import Error

class ItemRepository:
    def __init__(self, dbConnection: str, table="item"):
        self.dbConnection = dbConnection
        self.table = table
    
    def getListOfItems(self):
        conn = sqlite3.connect(self.dbConnection)
        cursor = conn.cursor()
        cursor.execute('SELECT rowid, * FROM ? ORDER BY title', self.table)
        listOfItemTuples = cursor.fetchall()