from repositories.locationRepository import LocationRepository

class LocationService:
	def __init__(self, locationRepository: LocationRepository):
		self.locationRepo = locationRepository

	def getListOfLocations(self):
		return self.locationRepo.getLocations()

	def createLocation(self, location: str):
		self.locationRepo.setLocation(location)
