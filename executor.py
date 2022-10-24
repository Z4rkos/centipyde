import time
import concurrent.futures
import os
from typing import Callable, Iterator

from wordlist_loader import load_wordlist
start_time = time.time()
tries = 0
try_checker = 0

def executor(gen_wordlist: Iterator[str], request_handler: Callable, args: dict):
    global tries, try_checker, start_time
    workers = args["workers"]

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        future_to_url = (executor.submit(request_handler, word) for word in gen_wordlist())
        try:
            for future in concurrent.futures.as_completed(future_to_url):
                if tries % 33 == 0:
                    # Need to reformat, remake, and/or rethink this.
                    tries_per_sec = int(
                        tries // (time.time() - start_time))
                    print(f"[+] {try_checker} words tried ({tries_per_sec}/s)", end="\r")
                    start_time = time.time()
                    tries = 0
                data = future.result()
                tries += 1
                try_checker += 1
                if data:
                    tries += 1
                    print(f"[+] {data}                                    \n")
        except KeyboardInterrupt:
            # Super sketchy stuff, but it works.
            pid = os.getpid()
            os.kill(pid, 9)
