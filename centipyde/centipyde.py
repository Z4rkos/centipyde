#!/bin/python
"""
A little program that is ment to simplify the process of writing web
'hacking' tools for me.
"""

from executor import executor
from request_handlers.request_handler_factory import RequestHandlerFactory
from wordlist_loader import load_wordlist
from get_args import get_args


def main():

    mode, executor_args, wordlist_args, request_handler_args = get_args()

    wordlist_generator = load_wordlist(wordlist_args)

    stuff = RequestHandlerFactory.get_request_handler(mode)

    request_handler = stuff(request_handler_args)

    executor(wordlist_generator, request_handler, executor_args)


if __name__ == '__main__':
    main()
