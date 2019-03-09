import sqlite3

class PhraseRepository:
	def __init__(self, dbConnection: str):
		self.dbConnection = dbConnection

	def getPhrases(self):
		conn = sqlite3.connect(self.dbConnection)
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM phrase')
		conn.commit()
		phraseTuples = cursor.fetchall()
		phraseList = []
		for phraseTuple in phraseTuples:
			phraseList.append(phraseTuple[0])
		return phraseList
