from flask import Blueprint, request

from repositories.siteRepository import SiteRepository
from services.siteService import SiteService
from lib.response import makeJsonResponse
from config import database

siteService = SiteService(SiteRepository(database))

siteRoutes = Blueprint('sites', __name__)

@siteRoutes.route('/<int:itemId>/', methods=['GET'])
def sitesById(itemId):
	if request.method == 'GET':
		sites = siteService.getSitesById(itemId)
		return makeJsonResponse(sites)
