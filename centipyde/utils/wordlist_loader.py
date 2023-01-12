import os
from typing import Iterator


def load_wordlist(wordlist_args: dict) -> Iterator[str]:
    """
    Returns a generator that can iterate over the provided wordlist.
    If the wordlist is not found, print a message and exit.
    """
    wordlist_path = wordlist_args["wordlist"]

    if not os.path.isfile(wordlist_path):
        print(f"File '{wordlist_path}' not found.")

    def wordlist_generator(wordlist_path=wordlist_path) -> str:
        with open(wordlist_path) as file:
            for word in file:
                yield word.strip()

    return wordlist_generator
