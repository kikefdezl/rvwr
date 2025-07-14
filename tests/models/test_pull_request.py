import pytest
from rvwr.models.pull_request import PRLink


@pytest.mark.parametrize(
    "pr_link",
    [
        "git@github.com:username/reponame.git/pull/42",
        "https://github.com/username/reponame/pull/42",
    ],
)
def test_validate_pr_link_passes(pr_link: str):
    PRLink(pr_link).validate()


@pytest.mark.parametrize(
    "pr_link",
    [
        "invalid",
        "git@github.com:username/namewithnodotgit/pull/42",
        "git@github.com:username/missingpullnumber/pull/",
    ],
)
def test_validate_pr_link_fails(pr_link: str):
    with pytest.raises(ValueError):
        PRLink(pr_link).validate()
