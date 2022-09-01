from os import replace
import requests


class Fuzzer:

    def __init__(self, args: dict):
        args = {} if args is None else args
        self.url          = args["url"]
        self.data         = args["data"]
        self.fail_string  = args["fail_string"]
        self.status_codes = args["status_codes"]
        self.headers      = args["headers"]
        self.cookies      = args["cookies"]
        self.mode         = args["mode"]


    def fuzz(self, word: str):
        url, data, cookies, headers, mode = self.url, self.data, self.cookies, self.headers, self.mode

        if cookies:
            cookies = _replace_word(cookies, word)
        if headers:
            headers = _replace_word(headers, word)

        if mode == "GET":
            if "FUZZ" in url:
                url = url.replace("FUZZ", word)
            response = requests.get(url=url, cookies=cookies, headers=headers)      

        elif mode == "POST":
            data = _replace_word(data, word)

            response = requests.post(url=url, data=data, cookies=cookies, headers=headers)

        if self.status_codes:
            if response.status_code in self.status_codes:
                return f"{response.status_code}: {word}"

        if self.fail_string:
            if self.fail_string not in response.text:
                return f"FOUND: {word}"


def _replace_word(some_dictionary, test):
    dictionary = some_dictionary.copy()
    try:
        dictionary[test] = dictionary.pop("FUZZ")
    except KeyError:
        pass
    for key, value in dictionary.items():
        if value == "FUZZ":
            dictionary[key] = test
    
    return dictionary


