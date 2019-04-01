from repositories.savedDataRepository import SavedDataRepository

class SavedDataService:
	def __init__(self, savedDataRepository: SavedDataRepository):
		self.savedDataRepo = savedDataRepository

	def getListOfData(self, dataType: str):
		return self.savedDataRepo.getData(dataType)

	def createData(self, dataType: str, data: str):
		self.savedDataRepo.setData(dataType, data)

	def removeData(self, dataType: str, data: str):
		self.savedDataRepo.deleteData(dataType, data)
