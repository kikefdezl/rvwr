from __future__ import annotations

from dataclasses import dataclass
from rvwr.models.repository import Repository



@dataclass
class PullRequest:
    number: int
    repository: Repository

    @classmethod
    def from_link(cls, pr_link: PRLink) -> PullRequest:
        return cls(pr_link)
