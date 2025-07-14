from abc import ABC, abstractmethod

from rvwr.models.diff import Diff
from rvwr.models.pull_request import PullRequest


class GitService(ABC):
    @abstractmethod
    def get_diffs(self, pr: PullRequest) -> list[Diff]: ...
