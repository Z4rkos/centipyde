from dataclasses import dataclass, field, asdict, fields
import argparse
import sys
import json


@dataclass
class Arguments:
    url: str
    wordlist_path: str
    request_handeler: str = ""
    wordlist_path: str = ""
    fail_string: str = ""

    workers: int = 30
    headers: dict = field(default_factory=dict)
    cookies: dict = field(default_factory=dict)
    status_codes: list = field(default_factory=list)


class WebStuff:

    def __init__(self, args: dict):

        for key, value in args.items():
            setattr(self, key, value)

        for key, value in self.__dict__.items():
            if value is not None:
                print(f"{key}: {value}")


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        ("-u", "url"), help="Target URL.", type=str, required=True)
    parser.add_argument(
        "-r", "--request_handeler", help="What type of request_handeler to use (username, password, directory)", required=True)
    parser.add_argument(
        "--username", help="Username used when bute forcing password.", type=str, required=sys.argv[(sys.argv.index("-r") + 1)] == "username")
    parser.add_argument(
        "--password", help="Password used when enumerating usernames (default = password)")
    parser.add_argument(
        "-f", "--fail_string", help="Fail message used when using username or password handeler.", required=sys.argv[(sys.argv.index("-r") + 1)] != "directory")
    parser.add_argument(
        "-s", "--status_codes", help="Allowed status codes for directory enumeration.", type=int, nargs='+', required=sys.argv[(sys.argv.index("-r") + 1)] == "directory")
    parser.add_argument(
        "--cookies", help="Cooooookies. Expects dictionary as input.", type=json.loads)
    parser.add_argument(
        "--headers", help="Heaaaaaders. Expects dictionary as input.", type=json.loads)

    parser.add_argument(
        "--workers", help="Amount of workers to use (default = 30)", type=int)
    parser.add_argument(
        "--chunk_size", help="Size of chunk the wordlist should be split into (default = 100000). If len(wordlist) * 2 < chunk size it will not be split.", type=int)
    parser.add_argument(
        "-w", "--wordlist", type=str, help="Path to wordlist.", required=True)

    args = parser.parse_args()

    return args


main()
