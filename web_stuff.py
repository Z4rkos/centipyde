import concurrent.futures
import time
import subprocess
import sys
import json
import argparse

from executor import executor
from request_handeler import RequestHandeler
from wordlist_loader import load_wordlist


class WebStuff:

    def __init__(self, args: dict, req_args: dict):

        for key, value in args.items():
            print(key, value)
            setattr(self, key, value)

        print(req_args["request_handeler"])
        request_handeler = RequestHandeler(
            req_args).eval(req_args.request_handeler)

        print(self.chunk_size)
        self.tries = 0

    def start(self):
        start_time = time.time()
        print(
            "-----------------------------------------------------------------------------")
        wordlist_s, preserve_ram = load_wordlist(
            self.chunk_size, self.wordlist)
        print("-----------------------------------------------------------------------------\n")

        if preserve_ram:
            for wordlist in wordlist_s:
                with concurrent.futures.ThreadPoolExecutor(max_workers=self.workers) as executor:
                    future_to_url = (executor.submit(
                        self.request_handeler, word) for word in wordlist)

                    for future in concurrent.futures.as_completed(future_to_url):
                        self.tries += 1
                        tries_per_sec = int(
                            self.tries // (time.time() - start_time))
                        print(
                            f"[-] {self.tries} words tried ({tries_per_sec}/s)", end="\r")
                        data = future.result()
                        if data:
                            print(
                                f"[+] {data}                                              \n")

        else:
            with concurrent.futures.ThreadPoolExecutor(max_workers=self.workers) as executor:
                future_to_url = (executor.submit(self.request_handeler, word)
                                 for word in wordlist_s)
                for future in concurrent.futures.as_completed(future_to_url):
                    tries_per_sec = int(
                        self.tries // (time.time() - start_time))
                    print(
                        f"[-] {self.tries} words tried ({tries_per_sec}/s)", end="\r")
                    data = future.result()
                    if data:
                        print(
                            f"[+] {data}                                              \n")


def get_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    parser.add_argument(
        "-u",
        "--url",
        help="Target URL.",
        type=str,
        required=True
        )
    parser.add_argument(
        "-r",
        "--request_handeler",
        help="What type of request_handeler to use (username, password, directory)", 
        required=True
        )
    parser.add_argument(
        "--password",
        help="Password used when enumerating usernames (default = password)"
        )
    parser.add_argument(
        "--cookies",
        help="Cooooookies. Expects dictionary as input.",
        type=json.loads
        )
    parser.add_argument(
        "--headers", 
        help="Heaaaaaders. Expects dictionary as input.",
        type=json.loads
        )
    parser.add_argument(
        "--workers", 
        help="Amount of workers to use (default = 30)",
        type=int)

    try:
        # Need to change this, too messy.
        parser.add_argument(
            "--username", 
            help="Username used when bute forcing password.",
            type=str,
            required=sys.argv[(sys.argv.index("-r") + 1)] == "username"
            )
        parser.add_argument(
            "-f",
            "--fail_string", 
            help="Fail message used when using username or password handeler.",
            required=sys.argv[(sys.argv.index("-r") + 1)] != "directory"
            )
        parser.add_argument(
            "-s", 
            "--status_codes",
            help="Allowed status codes for directory enumeration.",
            type=int,
            nargs='+',
            required=sys.argv[(sys.argv.index("-r") + 1)] == "directory"
            )
    except:
        parser.print_help()
        sys.exit()

    parser.add_argument(
        "--chunk_size", 
        help="Size of chunk the wordlist should be split into (default = 100000). If len(wordlist) * 2 < chunk size it will not be split.",
        default=100000,
        type=int
        )
    parser.add_argument(
        "-w",
        "--wordlist",
        type=str,
        help="Path to wordlist.",
        required=True
        )

    args = parser.parse_args()
    return args


def main():
    args = get_args()

    req_args = {}
    wordlist_args = {}
    main_args = {}
    for arg in vars(args):
        opt = getattr(args, arg)
        if opt != None:
            if arg == "chunk_size" or arg == "wordlist" or arg == "workers":
                main_args[arg] = opt
            else:
                req_args[arg] = opt

    WebStuff(main_args, req_args).start()


if __name__ == '__main__':
    main()
