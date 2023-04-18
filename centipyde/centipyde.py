#!/usr/bin/env python

"""
A little program that is ment to simplify the process of writing web
enumeration tools for me.
"""

import test
from .utils.check_host import host_is_up
from .utils.executor import executor
from .utils.wordlist_loader import load_wordlist
from .utils.get_args import get_args
from .utils.banner import print_banner
from .request_handlers.request_handler_factory import RequestHandlerFactory


def main() -> None:

    mode, executor_args, wordlist_args, request_handler_args = get_args()

    gen_wordlist = load_wordlist(wordlist_args)

    print_banner(mode, executor_args, wordlist_args, request_handler_args)

    if not host_is_up(request_handler_args["url"]):
        return
    print()

    request_handler = RequestHandlerFactory.get_request_handler(mode)
    request_handler = request_handler(request_handler_args)

    executor(gen_wordlist, request_handler, executor_args)


if __name__ == '__main__':
    main()
