from repositories.phraseRepository import PhraseRepository

class PhraseService:
	def __init__(self, phraseRepository: PhraseRepository):
		self.phraseRepo = phraseRepository

	def getListOfPhrases(self):
		return self.phraseRepo.getPhrases()
