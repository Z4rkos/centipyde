import argparse
import ast
from typing import Tuple, Dict

from request_handlers.request_handler_factory import REQUEST_HANDLERS


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
    ]
    # Mode is a string as there will always just be one (atleast as things are atm).
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
                wordlist_loader_args = opt

            elif arg in request_handler_arg_list:
                request_handler_args[arg] = opt

    return mode, executor_args, wordlist_loader_args, request_handler_args


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "mode",
        help="What type of mode to use.",
        choices=REQUEST_HANDLERS.keys(),
        default="dir",
        type=str,
    )
    parser.add_argument(
        "-u",
        "--url",
        help="Target URL.",
        type=str,
    )
    parser.add_argument(
        "-w",
        "--wordlist",
        help="Path to wordlist.",
        required=True,
        type=str,
    )
    parser.add_argument(
        "--cookies",
        help="Expects dict as input.",
        default={},
        type=ast.literal_eval
    )
    parser.add_argument(
        "--headers",
        help="Expects dict as input.",
        default={},
        type=ast.literal_eval
    )
    parser.add_argument(
        "--workers",
        help="Amount of workers to use.",
        default=30,
        type=int
    )
    parser.add_argument(
        "-s",
        "--status_codes",
        help="Allowed status codes for directory enumeration. (Format:-s 200 300 303 405 500)",
        default=[200, 300, 303],
        nargs='+',
        type=int,
    )
    parser.add_argument(
        "-f",
        "--fail_string",
        help="Fail message for matching with response.text",
        default="",
        type=str,
    )
    # try:
    #     # Conditionally required argumets.
    #     parser.add_argument(
    #         "--data",
    #         help="Data to use in post request (expects dict as input).",
    #         default={},
    #         required=sys.argv[(sys.argv.index("-m") + 1)] == "POST",
    #         type=ast.literal_eval,
    #     )
    # except:
    #     parser.print_help()
    #     sys.exit()

    args = parser.parse_args()
    return args





