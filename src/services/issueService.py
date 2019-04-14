from repositories.issueRepository import IssueRepository

class IssueService:
	def __init__(self, issueRepository: IssueRepository):
		self.issueRepo = issueRepository

	def createNewIssue(self, issue: dict):
		self.issueRepo.createNewIssue(issue)
