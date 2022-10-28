import requests

class RequestHandler():
    """
    Base class for request handlers.
    This allows all request handlers to set arguments the same way,
    only set the required ones and to take new arguments without having to
    rewrite anything.
    """

    # Currently it will set anything as args. Not sure if this is a prblem or not, but if I keep it like this
    # I will need to implement checks in get_args.

    def __init__(self, *args: dict, **kwargs: any):
        for dictionary in args:
            for key in dictionary:
                setattr(self, key, dictionary[key])
            for key in kwargs:
                setattr(self, key, kwargs[key])


    # This is from when this was an ABC. I will let it chill her for now though as I do want to do something like that.
    def run(self, *args) -> str:
        """The method that starts the request handler"""


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


class SubDomainEnumerator(RequestHandler):

    def run(self, word: str) -> str:
        """
        Runs the DirectoryEnumerator.
        The 'word' argument is passed by the executor from a wordlist.
        Checks the status codes in the response for a match against self.status_codes.
        """

        url: str = f"{word}.{self.url}"

        response = requests.get(
            url=url,
            cookies=self.cookies,
            headers=self.headers
        )

        if response.status_code in self.status_codes:
            return f"/{word}: {response.status_code}"
        else:
            return ""


# Should put this in a place for globals and stuffsself.
REQUEST_HANDLERS = {
    "dir": DirectoryEnumerator,
    "dns": SubDomainEnumerator,
}

class RequestHandlerFactory:
    """
    Factory for request handlers.
    Makes it easier to get the right handler without loads of if statements.
    """

    def get_request_handler(handler: str) -> RequestHandler:
        """Returns a request handler object."""
        try:
            if handler in REQUEST_HANDLERS:
                return REQUEST_HANDLERS[handler]
        except KeyError:
            print(f"Unkown mode: {handler}")
            return
