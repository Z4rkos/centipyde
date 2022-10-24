from typing import Iterator


def load_wordlist(wordlist_path: str) -> Iterator[str]:
    def generator(wordlist_path):
        with open(wordlist_path) as file:
            for word in file:
                yield word
    return generator
