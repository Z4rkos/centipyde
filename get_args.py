import argparse
import ast
import sys


def get_args():
    args = parse_args()

    # Everything here will be passed to the right classes/functions.
    # Just have to do the self.foo shizzle.
    main_arg_list = ["workers"]
    wordlist_arg_list = ["wordlist", "chunk_size"]
    fuzzer_arg_list = [
        "url", "fail_string", "status_codes", "data", "headers", "cookies", "mode"]

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

            elif arg in fuzzer_arg_list:
                req_args[arg] = opt

            elif arg == "request_handler":
                handler = opt

    return main_args, wordlist_args, req_args


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
        "-m",
        "--mode",
        help="What type of mode to use (GET, POST)",
        choices=["GET", "POST"],
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
        "--chunk_size",
        help="Size of chunk the wordlist should be split into (default = 100000). If len(wordlist) * 2 < chunk size it will not be split.",
        default=100000,
        type=int
    )
    parser.add_argument(
        "-s",
        "--status_codes",
        help="Allowed status codes for directory enumeration. (format: 200 300 303 405 500)",
        default=[],
        type=int,
        nargs='+',
    )
    parser.add_argument(
        "-f",
        "--fail_string",
        help="Fail message used when using username or password handler.",
        default="",
    )
    try:
        # Conditionally required argumets.
        parser.add_argument(
            "--data",
            help="Data to use in post request (expects dict as input).",
            type=ast.literal_eval,
            default={},
            required=sys.argv[(sys.argv.index("-m") + 1)] == "POST"
        )
    except:
        parser.print_help()
        sys.exit()



    args = parser.parse_args()
    return args
