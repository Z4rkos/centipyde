from .handlers import subdomain_enumerator, directory_enumerator
from .request_handler import RequestHandler

# Should put this in a place for globals and stuffsself.
REQUEST_HANDLERS = {
    "dir": directory_enumerator.DirectoryEnumerator,
    "dns": subdomain_enumerator.SubDomainEnumerator,
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
