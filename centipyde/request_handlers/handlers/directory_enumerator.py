import requests

from ..request_handler import RequestHandler


class DirectoryEnumerator(RequestHandler):
    """
    Enumerates webpages for directoriesself.
    Arguments are handeled by the parrent class.
    """

    def run(self, word: str) -> str:
        """
        Runs the DirectoryEnumerator.
        The 'word' argument is passed by the executor from a wordlist.
        Checks the status codes in the response for a match against self.status_codes.
        """

        url: str = f"{self.url}/{word}"

        response = requests.get(
            url=url,
            cookies=self.cookies,
            headers=self.headers,
            allow_redirects=True
        )
        # print(response.status_code not in self.status_codes)
        if response.status_code not in self.status_codes:
            return f"/{word}: {response.status_code}"
        else:
            return
