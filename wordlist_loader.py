from typing import Iterator


def load_wordlist(wordlist_path: str) -> Iterator[str]:
    print(wordlist_path)
    def generator(wordlist_path):
        print(wordlist_path)
        with open(wordlist_path) as file:
            for word in file:
                yield word
    return generator
