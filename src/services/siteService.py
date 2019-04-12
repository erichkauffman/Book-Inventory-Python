from data.Site import Site
from repositories.siteRepository import SiteRepository

class SiteService:
	def __init__(self, siteRepository: SiteRepository):
		self.siteRepo = siteRepository

	def getSitesById(self, itemId: int):
		return self.siteRepo.getSitesById(itemId)

	def getSiteValuesById(self, itemId: int):
		return self.siteRepo.getSiteValuesById(itemId)

	def setSite(self, site: Site):
		self.siteRepo.setSite(site)

	def editSite(self, siteList: Site):
		self.siteRepo.editSite(siteList)
