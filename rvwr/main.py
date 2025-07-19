from argparse import ArgumentParser, Namespace

from rvwr.git_services.github import GitHubService
from rvwr.models.pull_request import PullRequest
from rvwr.models.repository import GitHost, Repository


def parse_args() -> Namespace:
    parser = ArgumentParser(
        description="Customizable LLM-based PR Reviewer that understands your repo"
    )
    parser.add_argument("--repo", type=str, help="Link to the repo")
    parser.add_argument("--pr", type=int, help="PR number")
    return parser.parse_args()


def main():
    args = parse_args()

    repo = Repository.from_url(args.repo)
    pr = PullRequest(repository=repo, number=args.pr)

    match repo.host:
        # only github for now
        case GitHost.GITHUB:
            service = GitHubService()

    # fetch diffs for PR
    diff = service.get_diff(pr)
    print(diff)

    # for every diff, get a comment from LLM

    # comment
    ...


if __name__ == "__main__":
    main()
