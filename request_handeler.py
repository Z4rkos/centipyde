import requests


class RequestHandeler:
    def __init__(self, args: dict):
        for key, value in args.items():
            setattr(self, key, value)

    def password(self, word: str):

        word = word.rstrip('\n')
        data = {
            'username': "test_user",
            'password': word
        }
        response = requests.post(self.url, headers=self.headers,
                                 data=data, cookies=self.cookies)

        if self.fail_string not in response.text:
            return f"Password found: {word}"

    def username(self, word: str):

        word = word.rstrip('\n')
        data = {
            'username': word,
            'password': "placeholder"
        }
        response = requests.post(self.url, headers=self.headers,
                                 data=data, cookies=self.cookies)

        if self.fail_string not in response.text:
            return f"Username found: {word}"

    def directory(self, word: str):

        word = word.rstrip('\n')
        okay_status_codes = [i for i in range(200, 310)]

        payload = f"{self.url}/{word}"
        response = requests.get(self.url, headers=self.headers,
                                data=data, cookies=self.cookies)

        if response.status_code not in okay_status_codes:
            return f"{response.status_code}: /{word}"
