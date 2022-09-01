import requests


class Fuzzer:

    def __init__(self, args: dict):

        self.url          = args["url"]
        self.data         = args["data"]
        self.fail_string  = args["fail_string"]
        self.status_codes = args["status_codes"]
        self.headers      = args["headers"]
        self.cookies      = args["cookies"]
        self.mode         = args["mode"]


    def fuzz(self, word: str):
        url, data, cookies, headers, mode = self.url, self.data, self.cookies, self.headers, self.mode

        if "FUZZ" in url:
            url = url.replace("FUZZ", word)

        if cookies:
            try:
                cookies[word] = cookies.pop("FUZZ")
            except KeyError:
                pass
            for key, value in cookies.items():
                if value == "FUZZ":
                    cookies[key] = word

        if headers:
            try:
                headers[word] = headers.pop("FUZZ")
            except KeyError:
                pass
            for key, value in headers.items():
                if value == "FUZZ":
                    headers[key] = word

        if mode == "GET":
            response = requests.get(url=url, cookies=cookies, headers=headers)      

        elif mode == "POST":
            try:
                data[word] = data.pop("FUZZ")
            except KeyError:
                pass
            for key, value in data.items():
                if value == "FUZZ":
                    data[key] = word
            response = requests.post(url=url, data=data, cookies=cookies, headers=headers)
            print(response.text)
        if self.status_codes:
            if response.status_code in self.status_codes:
                return f"{response.status_code}: {word}"

        if self.fail_string:
            if self.fail_string not in response.text:
                return f"FOUND: {word}"


