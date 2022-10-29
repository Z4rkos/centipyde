from abc import ABC, abstractmethod


class RequestHandler(ABC):
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
    @abstractmethod
    def run(self, *args) -> str:
        """The method that starts the request handler"""



