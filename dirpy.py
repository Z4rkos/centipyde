from executor import executor
from request_handler import RequestHandler
from wordlist_loader import load_wordlist
from get_args import get_args


def main():

    main_args, wordlist_args, handler_args = get_args()

    print("Loading wordlist...")
    wordlist_generator = load_wordlist(wordlist_args)
    print(f"Wordlis loaded.")

    request_handler = RequestHandler(handler_args).dir

    executor(wordlist_generator, request_handler, main_args)


if __name__ == '__main__':
    main()


# print(f"Loading wordlist...")
# wordlist_generator, wordlist_length = load_wordlist("~/Tools/wordlists/rockyou.txt")
# print(f"Wordlist of length {wordlist_length} loaded.")
