from executor import executor
from request_handler import RequestHandler
from wordlist_loader import load_wordlist
from get_args import get_args


def main():

    main_args, wordlist_args, req_args, handler = get_args()

    print("-----------------------------------------------------------------------------")
    wordlist_s, preserve_ram = load_wordlist(wordlist_args)
    print("-----------------------------------------------------------------------------\n")

    match handler:
        case "username":
            request_handler = RequestHandler(req_args).username_handler
        case "password":
            request_handler = RequestHandler(req_args).password_handler
        case "directory":
            request_handler = RequestHandler(req_args).directory_handler

    if preserve_ram:
        for wordlist in wordlist_s:
            executor(wordlist, request_handler, main_args)
    else:
        executor(wordlist_s, request_handler, main_args)
 

if __name__ == '__main__':
    main()
