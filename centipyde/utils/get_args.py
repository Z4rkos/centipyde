import argparse
import ast
from re import subn
from typing import Tuple

from ..request_handlers.request_handler_factory import REQUEST_HANDLERS


# Several returns are returned as a tuple.
def get_args() -> Tuple[str, dict, dict, dict]:
    """
    Puts the args in the right dicts so they end up in the right place.
    """
    args = parse_args()

    executor_arg_list = ["workers"]
    wordlist_arg_list = ["wordlist"]
    request_handler_arg_list = [
        "url",
        "fail_string",
        "status_codes",
        "data",
        "headers",
        "cookies",
        "test"
    ]

    mode = ""
    request_handler_args = {}
    wordlist_loader_args = {}
    executor_args = {}
    for arg in vars(args):
        opt = getattr(args, arg)
        if opt is not None:

            if arg == "mode":
                mode = opt

            elif arg in executor_arg_list:
                executor_args[arg] = opt

            elif arg in wordlist_arg_list:
                wordlist_loader_args[arg] = opt

            elif arg in request_handler_arg_list:
                request_handler_args[arg] = opt

    # this needs to be reworked
    if mode == "dir":
        try:
            request_handler_args["status_codes"]
        except KeyError:
            request_handler_args["status_codes"] = [404]
            
    return mode, executor_args, wordlist_loader_args, request_handler_args


def parse_args() -> argparse.Namespace:

    parser = argparse.ArgumentParser()
    parent_parser = argparse.ArgumentParser(add_help=False)
    subparsers = parser.add_subparsers(dest="mode", required=True)

    parent_parser.add_argument(
        "-u",
        "--url",
        help="Target URL.",
        required=True,
        type=str,
    )
    parent_parser.add_argument(
        "-w",
        "--wordlist",
        help="Path to wordlist.",
        required=True,
        type=str,
    )
    parent_parser.add_argument(
        "--cookies",
        help="Expects dict as input.",
        default={},
        type=ast.literal_eval
    )
    parent_parser.add_argument(
        "--headers",
        help="Expects dict as input.",
        default={},
        type=ast.literal_eval
    )
    parent_parser.add_argument(
        "--workers",
        help="Amount of workers to use.",
        default=30,
        type=int
    )
    parent_parser.add_argument(
        "-s",
        "--status_codes",
        help="Disallowed status codes for directory enumeration. (Format:-s 200 300 303 405 500)",
        nargs='+',
        default=[404],
        type=int,
    )
    parent_parser.add_argument(
        "-f",
        "--fail_string",
        help="Fail message for matching with response.text",
        default="",
        type=str,
    )
    parent_parser.add_argument(
        "-p",
        "--password",
        type=list
        )

    # Allows handlers to be used with the parent parser args.
    for handler in REQUEST_HANDLERS.keys():
        handler = subparsers.add_parser(handler, parents=[parent_parser])

    # Add subparser or subparser args here if needed.

    args = parser.parse_args()
    return args
