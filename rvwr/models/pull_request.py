from dataclasses import dataclass

from rvwr.models.repository import Repository


@dataclass
class PullRequest:
    number: int
    repository: Repository
