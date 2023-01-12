import datetime
import concurrent.futures
import os
from typing import Callable, Iterator

from termcolor import colored


def executor(gen_wordlist: Iterator, request_handler: Callable, args: dict) -> None:
    """
    Takes cares of execution and timing.
    """
    current_tries = 0
    update_time = 0.2
    total_tries = 0

    workers = args["workers"]
    start_thing = colored('[+]', 'blue')

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        future_to_url = (executor.submit(request_handler.run, word) for word in gen_wordlist())

        next_time = datetime.datetime.now()
        delta = datetime.timedelta(seconds=update_time)

        try:
            for future in concurrent.futures.as_completed(future_to_url):
                period = datetime.datetime.now()

                if period >= next_time:
                    # print(period)
                    next_time += delta
                    # print(tries)
                    tries_per_sec = current_tries
                    current_tries = 0
                    print(f"{start_thing} {total_tries} words tried ({tries_per_sec * 5}/s)", end="\r")

                data = future.result()
                total_tries += 1
                if data:
                    # All the spaces makes the end="/r" thing above work.
                    data = colored(data, 'green')
                    print(f"{start_thing} {data}                                    ")
                current_tries += 1
        except KeyboardInterrupt:
            # Super sketchy stuff, but it makes it so I only have to do CTRL+c once to cancell.
            pid = os.getpid()
            # Should do this with subprocess instead...
            os.kill(pid, 9)
