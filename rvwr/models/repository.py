from __future__ import annotations

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

    @classmethod
    def from_str(cls, value: str):
        """
        Valid link examples:
            - git@github.com:username/reponame.git
            - https://github.com/username/reponame
            - https://github.com/username/reponame.git

        Raises ValueError if not a valid PR link.
        """
        if re.match(r"git@github.com:.+/.+\.git", value):
            return cls(value=value, type=UrlType.SSH)
        if re.match(r"https://github.com/.+/.+", value):
            return cls(value=value, type=UrlType.HTTPS)
        raise ValueError("Invalid repo URL")


class GitHost(StrEnum):
    GITHUB = "GITHUB"


@dataclass
class Repository:
    url: RepoUrl
    host: GitHost

    @classmethod
    def from_url(cls, url: str) -> Repository:
        return cls(RepoUrl.from_str(url), host=GitHost.GITHUB)

    @property
    def username(self) -> str:
        match = re.search(r"[:/]([^/]+)/[^/]+(?:\.git)?$", self.url.value)
        if not match:
            raise ValueError()
        return match.group(1)

    @property
    def full_name(self) -> str:
        return f"{self.username}/{self.name}"

    @property
    def name(self) -> str:
        return self.url.value.split("/")[-1].removesuffix(".git")
