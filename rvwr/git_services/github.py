from github import Github

from rvwr.models.diff import Diff
from rvwr.models.pull_request import PullRequest

from .base import GitService


class GitHubService(GitService):
    def __init__(self):
        self.github = Github()

    def get_diff(self, pr: PullRequest) -> Diff:
        repo = self.github.get_repo(pr.repository.full_name)
        pull = repo.get_pull(pr.number)
        full_diff = "\n".join([f.patch for f in pull.get_files()])
        return Diff.from_str(full_diff)
