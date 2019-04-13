from data.Site import Site
from repositories.siteRepository import SiteRepository

class SiteService:
	def __init__(self, siteRepository: SiteRepository):
		self.siteRepo = siteRepository

	def getSiteValuesById(self, itemId: int):
		return self.siteRepo.getSiteValuesById(itemId)

	def setSites(self, site: Site):
		self.siteRepo.setSites(site)

	def editSites(self, siteList: Site):
		self.siteRepo.editSites(siteList)
