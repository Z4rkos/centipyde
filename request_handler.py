import requests


class RequestHandler:
    """
    ARGS:
    -----------------
    word: The word to use in the request.
    url: The target URL.
    fail_string: Something in the response that tells the script that the attempt was unsuccessfull (optional for directory).
    status_codes: A list of status codes that are acceptible when doing directory enumeration.
    username: The username to use when doing password attack. (optional)
    password: the password to use when doing username attack. (optional)
    headers: Hheaders to use in request (as a dict). (optional)
    cookies. cookies to use in the request (as a dict). (optional)
    """

    def __init__(self, args: dict):

        self.url = args["url"]
        self.fail_string = args["fail_string"]
        self.status_codes = args["status_codes"]
        self.username = args["username"]
        self.password = args["password"]
        self.headers = args["headers"]
        self.cookies = args["cookies"]

    def password_handler(self, word: str):
        data = {
            'username': self.username,
            'password': word
        }
        response = requests.post(self.url, headers=self.headers,
                                 data=data, cookies=self.cookies)

        if self.fail_string not in response.text:
            return f"Password found: {word}"

    def username_handler(self, word: str):
        data = {
            'username': word,
            'password': self.password
        }
        response = requests.post(self.url, headers=self.headers,
                                 data=data, cookies=self.cookies)

        if self.fail_string not in response.text:
            return f"Username found: {word}"

    def directory_handler(self, word: str):
        url = f"{self.url}/{word}"
        response = requests.get(
            url=url, headers=self.headers, cookies=self.cookies)

        if response.status_code in self.status_codes:
            return f"{response.status_code}: /{word}"
