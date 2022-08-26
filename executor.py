import time
import concurrent.futures

start_time = time.time()
tries = 0


def executor(wordlist: list, request_handler: object, args: dict):
    global tries, start_time
    workers = args["workers"]

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        future_to_url = (executor.submit(request_handler, word)
                         for word in wordlist)
        for future in concurrent.futures.as_completed(future_to_url):
            tries_per_sec = int(
                tries // (time.time() - start_time))
            print(
                f"[+] {tries} words tried ({tries_per_sec}/s)", end="\r")
            data = future.result()
            if data:
                print(
                    f"[+] {data}                                              \n")
            tries += 1
