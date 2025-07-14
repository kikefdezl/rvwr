from __future__ import annotations

from dataclasses import dataclass
from rvwr.models.repo import RepositoryId



@dataclass
class PullRequest:
    repository_id: RepositoryId
    id: int

    @classmethod
    def from_link(cls, pr_link: PRLink) -> PullRequest:
        return cls(pr_link)
