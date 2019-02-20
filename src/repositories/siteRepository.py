import sqlite3

class SiteRepository:
	def __init__(self, dbConnection: str):
		self.dbConnection = dbConnection
