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

        url: str = self.url + word

        if not self.status_codes:
            # This should not be implemented here. Maybe a config file or something?
            self.status_codes = [200, 301, 302, 401, 403]

        response = requests.get(
            url=url,
            cookies=self.cookies,
            headers=self.headers
        )

        if response.status_code in self.status_codes:
            return f"/{word}: {response.status_code}"
        else:
            return ""
