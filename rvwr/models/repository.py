import re
from dataclasses import dataclass
from enum import StrEnum


class UrlType(StrEnum):
    HTTPS = "HTTPS"
    SSH = "SSH"


@dataclass
class RepoUrl:
    value: str
    type: UrlType

    def validate(self):
        """
        Raises ValueError if not a valid PR link.

        Valid link examples:
            - git@github.com:username/reponame.git
            - https://github.com/username/reponame
            - https://github.com/username/reponame.git
        """
        if re.match(r"git@github.com:.+/.+\.git", self.value):
            return
        if re.match(r"https://github.com/.+/.+", self.value):
            return
        if re.match(r"https://github.com/.+/.+.git", self.value):
            return
        raise ValueError("Invalid repo URL")


@dataclass
class Repository:
    url: RepoUrl
