from flask import Blueprint, request

from services.phraseService import PhraseService
from repositories.phraseRepository import PhraseRepository
from lib.response import makeJsonResponse
from initialize import socketio
from config import database

phraseService = PhraseService(PhraseRepository(database))

phraseRoutes = Blueprint("phrases", __name__)

@phraseRoutes.route('/', methods=['GET', 'POST', 'DELETE'])
def phrases():
	if request.method == 'GET':
		phraseList = phraseService.getListOfPhrases()
		return makeJsonResponse(phraseList)
	elif request.method == 'POST':
		jsonreq = request.get_json(force=True)
		phrase = jsonreq['data']
		phraseService.createPhrase(phrase)
		socketio.emit('new_phrase', phrase, broadcast=True)
		return makeJsonResponse({"success": True})
	elif request.method == 'DELETE':
		jsonreq = request.get_json(force=True)
		phrase = jsonreq['data']
		phraseService.removePhrase(phrase)
		socketio.emit('delete_phrase', phrase, broadcast=True)
		return makeJsonResponse({"success": True})
