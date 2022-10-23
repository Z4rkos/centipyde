from abc import ABC
import requests
from requests import Response
from dataclasses import dataclass


@dataclass
class Args:
    url: str
    data: dict
    fail_string: str
    status_codes: list
    headers: dict
    cookies: dict

class RequestHandler:

    def __init__(self, args: dict):
        self.url          = args["self.url"]
        self.data         = args["data"]
        self.fail_string  = args["fail_string"]
        self.status_codes = args["status_codes"]
        self.headers      = args["headers"]
        self.cookies      = args["cookies"]

    def get(self, url) -> Response:
        res = requests.get(url=url, cookies=self.cookies, headers=self.headers)
        return res





class RequestHandlerFactory(ABC):
    """
    Factory for request handlers.
    The factory does not maintain any of the instances it creates.
    """

    def get_request_handler(self) -> RequestHandler:
        """Returns a new request handler instance."""

class DirectoryEnumeratorFactory(RequestHandlerFactory) -> DirectoryEnumerator:
    pass

    


class DirectoryEnumerator(RequestHandler):
    def dir(self, word: str):
        self.url += word
        if not self.status_codes:
            self.status_codes = [200, 301, 302, 401, 403]
        response = requests.get(self.url=self.url, cookies=cookies, headers=headers)      

        if response.status_code in self.status_codes:
            return f"/{word}: {response.status_code}"

    def sub_domain(self, word: str):
        self.url = word + self.url

def _replace_word(some_dictionary: dict, word: str) -> dict:
    dictionary = some_dictionary.copy()
    try:
        dictionary[word] = dictionary.pop("FUZZ")
    except KeyError:
        pass
    for key, value in dictionary.items():
        if value == "FUZZ":
            dictionary[key] = word
    
    return dictionary


