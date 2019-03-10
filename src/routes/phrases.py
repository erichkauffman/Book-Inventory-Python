from flask import Blueprint, request

from services.phraseService import PhraseService
from repositories.phraseRepository import PhraseRepository
from lib.response import makeJsonResponse
from config import database

phraseService = PhraseService(PhraseRepository(database))

phraseRoutes = Blueprint("phrases", __name__)

@phraseRoutes.route('/', methods=['GET'])
def phrases():
	if request.method == 'GET':
		phraseList = phraseService.getListOfPhrases()
		return makeJsonResponse(phraseList)

@phraseRoutes.route('/<string:phrase>/', methods=['POST', 'DELETE'])
def setPhrase(phrase):
	if request.method == 'POST':
		phraseService.createPhrase(phrase)
		return makeJsonResponse({"success": True})
	if request.method == 'DELETE':
		phraseService.removePhrase(phrase)
		return makeJsonResponse({"success": True})
