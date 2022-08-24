import time


def executor(wordlist: list, request_handeler: func, workers=30):
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        future_to_url = (executor.submit(request_handeler, word)
                         for word in wordlist_s)
        for future in concurrent.futures.as_completed(future_to_url):
            tries_per_sec = int(
                tries // (time.time() - start_time))
            print(
                f"[-] {tries} words tried ({tries_per_sec}/s)", end="\r")
            data = future.result()
            if data:
                print(
                    f"[+] {data}                                              \n")
