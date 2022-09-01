from executor import executor
from request_handler import Fuzzer
from wordlist_loader import load_wordlist
from get_args import get_args


def main():

    main_args, wordlist_args, fuzz_args = get_args()

    print("-----------------------------------------------------------------------------")
    wordlist_s, preserve_ram = load_wordlist(wordlist_args)
    print("-----------------------------------------------------------------------------\n")

    fuzzer = Fuzzer(fuzz_args).fuzz

    if preserve_ram:
        for wordlist in wordlist_s:
            executor(wordlist, fuzzer, main_args)
    else:
        executor(wordlist_s, fuzzer, main_args)
 

if __name__ == '__main__':
    main()
