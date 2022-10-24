import time
import concurrent.futures
import os
from typing import Callable, Iterator

from wordlist_loader import load_wordlist
start_time = time.time()
tries = 0


def executor(wordlist_generator: Iterator[str], request_handler: Callable, args: dict):
    global tries, start_time
    workers = args["workers"]
    wordlist_generator = load_wordlist(wordlist_args)

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        future_to_url = (executor.submit(request_handler, word) for word in wordlist_generator())
        try:
            for future in concurrent.futures.as_completed(future_to_url):
                tries_per_sec = int(
                    tries // (time.time() - start_time))
                print(f"[+] {tries} words tried ({tries_per_sec}/s)", end="\r")
                data = future.result()
                if data:
                    tries += 1
                    print(f"[+] {data}                                    \n")
        except KeyboardInterrupt:
            # Super scetchy stuff, but it works.
            pid = os.getpid()
            os.kill(pid, 9)
