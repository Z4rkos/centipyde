import time
import concurrent.futures
import os
from typing import Callable, Iterator


start_time = time.time()
tries = 0
try_checker = 0


def executor(gen_wordlist: Iterator, request_handler: Callable, args: dict) -> None:
    """
    Takes cares of execution and timing.
    """
    global tries, try_checker, start_time
    workers = args["workers"]

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        future_to_url = (executor.submit(request_handler.run, word) for word in gen_wordlist())
        # print(request_handler)
        try:
            for future in concurrent.futures.as_completed(future_to_url):
                if tries % 22 == 0:
                    # Need to reformat, remake, and/or rethink this as it is not accurate atm.
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
                    # All the spaces makes the end="/r" thing above work.
                    print(f"[+] {data}                                    ")
        except KeyboardInterrupt:
            # Super sketchy stuff, but it makes it so I only have to do CTRL+c once to cancell.
            pid = os.getpid()
            # Should really do this with subprocess instead...
            os.kill(pid, 9)
