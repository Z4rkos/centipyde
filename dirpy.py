from executor import executor
from request_handler import RequestHandler, RequestHandlerFactory
from wordlist_loader import load_wordlist
from get_args import get_args


def main():

    executor_args, wordlist_args, request_handler_args = get_args()

    print("Loading wordlist...")
    
    print("Wordlist loaded.")

    request_handler_args = {"url": "test", "wordlist": "stuff", "abc": "shit"}
    mode = "dir"
    # RequestHandler(request_handler_args)
    request_handler = RequestHandlerFactory.get_request_handler(mode)
    request_handler = request_handler(request_handler_args)

    executor(wordlist_args, request_handler.run, executor_args)


if __name__ == '__main__':
    main()


# print(f"Loading wordlist...")
# wordlist_generator, wordlist_length = load_wordlist("~/Tools/wordlists/rockyou.txt")
# print(f"Wordlist of length {wordlist_length} loaded.")
