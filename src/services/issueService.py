from repositories.issueRepository import IssueRepository
from lib.messageHandlers import postToTrello

class IssueService:
	def __init__(self, environment: str, issueRepository: IssueRepository):
		self.environment = environment
		self.issueRepo = issueRepository
		self.issueTypes = ['FEATURE', 'BUG']

	def createNewIssue(self, issue: dict):
		self.issueRepo.createNewIssue(issue)
		title = f"{self.issueTypes[issue['type']]}: {self.environment}: {issue['title']}"
		message = {issue['message']}
		response = postToTrello(title, message)
