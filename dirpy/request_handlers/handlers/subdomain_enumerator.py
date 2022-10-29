import requests

from ..request_handler import RequestHandler

class SubDomainEnumerator(RequestHandler):

    def run(self, word: str) -> str:
        """
        Runs the DirectoryEnumerator.
        The 'word' argument is passed by the executor from a wordlist.
        Checks the status codes in the response for a match against self.status_codes.
        """

        url: str = f"{word}.{self.url}"
        # print(url)
        response = requests.get(
            url=url,
            cookies=self.cookies,
            headers=self.headers
        )

        if response.status_code in self.status_codes:
            return f"/{word}: {response.status_code}"
        else:
            return ""
