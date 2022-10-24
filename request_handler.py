from abc import ABC, abstractmethod
from concurrent.futures import wait
from typing import Protocol
import requests
from requests import Response
from dataclasses import dataclass


class RequestHandler():
    """
    Base class for request handlers.
    This allows all request handlers to set arguments the same way, only set the required ones
    and to take new arguments without having to rewrite anything.
    """

    # Currently it will set anything as args. Not sure if this is a prblem or not, but if I keep it like this
    # I will need to implement checks in get_args.

    def __init__(self, *args: dict, **kwargs: any):
        # print(hasattr(RequestHandler, "url"))
        for dictionary in args:
            for key in dictionary:
                # if key in dir(self):
                setattr(self.__class__, key, dictionary[key])
            for key in kwargs:
                setattr(self.__class__, key, kwargs[key])


    @abstractmethod
    def run(self, *args) -> Response:
        """The method that starts the request handler"""


class DirectoryEnumerator(RequestHandler):
    """
    Enumerates webpages for directories.
    Arguments are handeled by the parrent class.
    """

    def test(self):
        print(self.url, self.wordlist, self.abc)

    def run(self, word: str):
        """
        Runs the DirectoryEnumerator.
        The 'word' argument is passed by the executor from a wordlist.
        """
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
    """

    def get_request_handler(handler: str) -> RequestHandler:
        """Returns a request handler object."""
        try:
            if handler in REQUEST_HANDLERS:
                return REQUEST_HANDLERS[handler]
        except KeyError:
            print(f"Unkown mode: {handler}")
            return


# class DirectoryEnumeratorFactory(RequestHandlerFactory):
    
#     def get_request_handler(self):
#         pass

    
# def _replace_word(some_dictionary: dict, word: str) -> dict:
#     dictionary = some_dictionary.copy()
#     try:
#         dictionary[word] = dictionary.pop("FUZZ")
#     except KeyError:
#         pass
#     for key, value in dictionary.items():
#         if value == "FUZZ":
#             dictionary[key] = word
    
#     return dictionary


# def set_args(self, *args: dict, **kwargs):
#     for dictionary in args:
#         for key in dictionary:
#             setattr(self, key, dictionary[key])
#         for key in kwargs:
#             setattr(self, key, kwargs[key])

mode = "dir"
request_handler = RequestHandlerFactory.get_request_handler(mode)

