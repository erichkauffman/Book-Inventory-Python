import sqlite3

class IssueRepository:
	def __init__(self, dbConnection: str):
		self.dbConnection = dbConnection

	def createNewIssue(self, issue: dict):
		conn = sqlite3.connect(self.dbConnection)
		conn.execute('''INSERT INTO issue
						(type, title, message, dateReceived)
						VALUES(?,?,?,?,date('now'))''')
		conn.commit()
