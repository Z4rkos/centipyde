import requests


class RequestHandeler:
    """
    ARGS:
    -----------------
    word: The word to use in the request.
    url: The target URL.
    fail_string: Something in the response that tells the script that the attempt was unsuccessfull (optional for dictionary).
    status_codes: A list of status codes that are acceptible when doing directory enumeration.
    username: The username to use when doing password attack. (optional)
    password: the password to use when doing username attack. (optional)
    headers: Hheaders to use in request (as a dict). (optional)
    cookies. cookies to use in the request (as a dict). (optional)
    """

    def __init__(self, args: dict):
        """
        I set the arguments like this to make it easy to vary the arguments given to the class.
        I might just drop this class at some point... Takes max 5 lines to make a request handeler.
        """
        for key, value in args.items():
            setattr(self, key, value)

    def password(self, word: str):

        username = "username" if not self.uername else self.username

        word = word.rstrip('\n')
        data = {
            'username': username,
            'password': word
        }
        response = requests.post(self.url, headers=self.headers,
                                 data=data, cookies=self.cookies)

        if self.fail_string not in response.text:
            return f"Password found: {word}"

    def username(self, word: str):

        password = "password" if not self.password else self.password

        word = word.rstrip('\n')
        data = {
            'username': word,
            'password': password
        }
        response = requests.post(self.url, headers=self.headers,
                                 data=data, cookies=self.cookies)

        if self.fail_string not in response.text:
            return f"Username found: {word}"

    def directory(self, word: str):

        word = word.rstrip('\n')
        status_codes = [i for i in range(200, 310)] if not self.status_codes else self.status_codes

        payload = f"{self.url}/{word}"
        response = requests.get(self.url, headers=self.headers,
                                data=data, cookies=self.cookies)

        if response.status_code not in status_codes:
            return f"{response.status_code}: /{word}"
