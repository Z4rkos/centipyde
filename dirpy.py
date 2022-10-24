from executor import executor
from request_handler import RequestHandler, RequestHandlerFactory
from wordlist_loader import load_wordlist
from get_args import get_args


def main():

    executor_args, wordlist_args, request_handler_args = get_args()

    wordlist_generator = load_wordlist(wordlist_args)

    # Need to implement this propperly in get_args with subparsers.
    mode = "dir"

    stuff = RequestHandlerFactory.get_request_handler(mode)
    request_handler = stuff(request_handler_args).run

    executor(wordlist_generator, request_handler, executor_args)


if __name__ == '__main__':
    main()


# print(f"Loading wordlist...")
# wordlist_generator, wordlist_length = load_wordlist("~/Tools/wordlists/rockyou.txt")
# print(f"Wordlist of length {wordlist_length} loaded.")
