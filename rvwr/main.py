from argparse import ArgumentParser, Namespace

from rvwr.models.pull_request import PRLink, PullRequest
from rvwr.git_services.github import GitHubService


def parse_args() -> Namespace:
    parser = ArgumentParser(
        description="Customizable LLM-based PR Reviewer that understands your repo"
    )
    parser.add_argument("pr_link", type=str, help="Link to the PR")
    return parser.parse_args()


def main():
    args = parse_args()

    pr_link = PRLink(args.pr_link)
    pr_link.validate()
    pull_request = PullRequest.from_link(pr_link)

    # fetch diffs for PR
    service = GitHubService()
    diffs = service.get_diffs(pull_request)
    print(diffs)

    # for every diff, get a comment from LLM

    # comment
    ...


if __name__ == "__main__":
    main()
