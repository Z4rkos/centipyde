from typing import Iterator


def load_wordlist(wordlist_path: str) -> Iterator[str]:
    def generator(wordlist_path=wordlist_path):
        # The default argument thing allows generator to be passed as an object/
        # to be used without arguments aslong as load_wordlist has the wordlist path when making generatorself.
        # Definatly refractor this comment lol.
        try:
            with open(wordlist_path) as file:
                for word in file:
                    yield word.strip()
        except FileNotFoundError:
            print(f"File '{wordlist_path}' not found.")

    return generator
