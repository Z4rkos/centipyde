from abc import ABC, abstractmethod

# Not sure if ABC is the right thing for this, but I want it to have an abstract method as all RequestHandler classes needs a run method.
class RequestHandler(ABC):
    """
    Base class for request handlers.
    This allows all request handlers to set arguments the same way,
    only set the required ones and to take new arguments without having to
    rewrite anything.
    """
    # Currently it will set anything as args. Not sure if this is a prblem or not as the args are limited by get_args.

    def __init__(self, *args: dict, **kwargs: any):
        for dictionary in args:
            for key in dictionary:
                setattr(self, key, dictionary[key])
            for key in kwargs:
                setattr(self, key, kwargs[key])

    @abstractmethod
    def run(self, *args) -> str:
        """The method that starts the request handler"""



