from flask import Blueprint, request

from services.issueService import IssueService
from repositories.issueRepository import IssueRepository
from config import database

issueService = IssueService(IssueRepository(database))

issueRoutes = Blueprint("issues", __name__)

@issueRoutes.route('/', methods=['POST'])
def issues():
	if request.method == 'POST':
		jsonreq = request.get_json(force=True)
		issueService.createNewIssue(jsonreq)
