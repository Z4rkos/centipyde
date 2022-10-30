#!/bin/python
"""
A little program that is ment to simplify the process of writing web
'hacking' tools for me.
"""

from executor import executor
from request_handlers.request_handler_factory import RequestHandlerFactory
from wordlist_loader import load_wordlist
from get_args import get_args
from banner import print_banner


def main() -> None:

    mode, executor_args, wordlist_args, request_handler_args = get_args()

    print_banner(mode, executor_args, wordlist_args, request_handler_args)

    wordlist_generator = load_wordlist(wordlist_args)

    request_handler = RequestHandlerFactory.get_request_handler(mode)
    request_handler = request_handler(request_handler_args)
    # print(vars(request_handler))

    executor(wordlist_generator, request_handler, executor_args)


if __name__ == '__main__':
    main()
