import pytest

from rvwr.models.repository import GitHost, Repository, UrlType


@pytest.mark.parametrize(
    "url,type_",
    [
        ("git@github.com:username/reponame.git", UrlType.SSH),
        ("https://github.com/username/reponame", UrlType.HTTPS),
        ("https://github.com/username/reponame.git", UrlType.HTTPS),
    ],
)
def test_from_url(url: str, type_: UrlType):
    repo = Repository.from_url(url)
    assert repo.url.value == url
    assert repo.url.type == type_
    assert repo.host == GitHost.GITHUB


@pytest.mark.parametrize(
    "url,expected",
    [
        ("git@github.com:username/reponame.git", "username"),
        ("https://github.com/username/reponame", "username"),
        ("https://github.com/username/reponame.git", "username"),
    ],
)
def test_username(url: str, expected: str):
    repo = Repository.from_url(url)
    assert repo.username == expected

@pytest.mark.parametrize(
    "url,expected",
    [
        ("git@github.com:username/reponame.git", "reponame"),
        ("https://github.com/username/reponame", "reponame"),
        ("https://github.com/username/reponame.git", "reponame"),
    ],
)
def test_name(url: str, expected: str):
    repo = Repository.from_url(url)
    assert repo.name == expected
