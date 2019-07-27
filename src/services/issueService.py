from repositories.issueRepository import IssueRepository
from lib.messageHandlers import postToTrello
from config import trello

class IssueService:
	def __init__(self, environment: str, issueRepository: IssueRepository):
		self.environment = environment
		self.issueRepo = issueRepository
		self.issueTypes = ['FEATURE', 'BUG']

	def createNewIssue(self, issue: dict):
		self.issueRepo.createNewIssue(issue)
		if trello and self.environment != 'Development':
			title = f"{self.issueTypes[issue['type']]}: {self.environment}: {issue['title']}"
			message = {issue['message']}
			response = postToTrello(title, message)
