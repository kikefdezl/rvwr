from github import Github

from rvwr.models.diff import Diff
from rvwr.models.pull_request import PullRequest

from .base import GitService


class GitHubService(GitService):
    def __init__(self):
        self.github = Github()

    def get_diffs(self, pr: PullRequest) -> list[Diff]:
        repo = self.github.get_repo(pr.link.value)
        print(repo)
