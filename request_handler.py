from typing import Protocol
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

# class RequestHandler:

#     def __init__(self, args: dict):
#         self.url          = args["self.url"]
#         self.data         = args["data"]
#         self.fail_string  = args["fail_string"]
#         self.status_codes = args["status_codes"]
#         self.headers      = args["headers"]
#         self.cookies      = args["cookies"]

#     def get(self, url) -> Response:
#         res = requests.get(url=url, cookies=self.cookies, headers=self.headers)
#         return res

@dataclass
class RequestHandler(Protocol):

    url: str
    data: dict
    fail_string: str
    status_codes: list
    headers: dict
    cookies: dict

    mode: str

    def run(self, *args) -> Response:


class DirectoryEnumerator(RequestHandler):

    def run(self, word: str):
        self.url += word
        if not self.status_codes:
            self.status_codes = [200, 301, 302, 401, 403]
        response = requests.get(url=self.url, cookies=self.cookies, headers=self.headers)      

        if response.status_code in self.status_codes:
            return f"/{word}: {response.status_code}"

class Dns:
    pass


REQUEST_HANDLERS = {
        "dir": DirectoryEnumerator,
        "dns": Dns,
        }

class RequestHandlerFactory:
    """
    Factory for request handlers.
    The factory does not maintain any of the instances it creates.
    """

    def get_request_handler(self, handler: str) -> RequestHandler:
        """Returns a new request handler instance."""
        try:
            if handler in REQUEST_HANDLERS:
                return handler
        except KeyError:
            print(f"Unkown mode: {handler}")


class DirectoryEnumeratorFactory(RequestHandlerFactory):
    
    def get_request_handler(self):
        pass

    


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

