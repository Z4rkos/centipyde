import argparse
import json
import sys


def get_args():
    args = parse_args()

    # Everything here will be passed to the right classes/functions.
    # Just have to do the self.foo shizzle.
    main_arg_list = ["workers"]
    wordlist_arg_list = ["wordlist", "chunk_size"]
    request_handler_arg_list = [
        "url", "fail_string", "status_codes", "username", "password", "headers", "cookies"]

    req_args = {}
    wordlist_args = {}
    main_args = {}
    for arg in vars(args):
        opt = getattr(args, arg)
        if opt != None:
            if arg in main_arg_list:
                main_args[arg] = opt

            elif arg in wordlist_arg_list:
                wordlist_args[arg] = opt

            elif arg in request_handler_arg_list:
                req_args[arg] = opt

            elif arg == "request_handler":
                handler = opt

    return main_args, wordlist_args, req_args, handler


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-u",
        "--url",
        help="Target URL.",
        type=str,
        required=True
    )
    parser.add_argument(
        "-r",
        "--request_handler",
        help="What type of request_handler to use (username, password, directory)",
        required=True
    )
    parser.add_argument(
        "-w",
        "--wordlist",
        type=str,
        help="Path to wordlist.",
        required=True
    )
    parser.add_argument(
        "--password",
        help="Password used when enumerating usernames (default = password)",
        default="password"
    )
    parser.add_argument(
        "--cookies",
        help="Cooooookies. Expects dictionary as input.",
        default={},
        type=json.loads
    )
    parser.add_argument(
        "--headers",
        help="Heaaaaaders. Expects dictionary as input.",
        default={},
        type=json.loads
    )
    parser.add_argument(
        "--workers",
        help="Amount of workers to use.",
        default=30,
        type=int)

    parser.add_argument(
        "--chunk_size",
        help="Size of chunk the wordlist should be split into (default = 100000). If len(wordlist) * 2 < chunk size it will not be split.",
        default=100000,
        type=int
    )

    try:
        # Conditionally required argumets.
        parser.add_argument(
            "-f",
            "--fail_string",
            help="Fail message used when using username or password handeler.",
            default="",
            required=sys.argv[(sys.argv.index("-r") + 1)] != "directory"
        )
        parser.add_argument(
            "-s",
            "--status_codes",
            help="Allowed status codes for directory enumeration.",
            default=[i for i in range(200, 399)],
            type=int,
            nargs='+',
        )
        parser.add_argument(
            "--username",
            help="username to use when enumerating passwords (default = username)",
            default="username",
            required=sys.argv[(sys.argv.index("-r") + 1)] == "password"
        )
    except:
        parser.print_help()
        sys.exit()

    args = parser.parse_args()
    return args
