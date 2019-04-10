from repositories.siteRepository import SiteRepository

class SiteService:
	def __init__(self, siteRepository: SiteRepository):
		self.siteRepo = siteRepository

	def getSitesById(self, itemId: int):
		return self.siteRepo.getSitesById(itemId)
