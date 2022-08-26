def load_wordlist(args: dict):
    wordlist_path: str = args["wordlist"]
    chunk_size: int = args["chunk_size"]

    wordlist = list()
    nested_wordlists = list()

    preserve_ram = True

    try:
        with open(wordlist_path) as f:
            for line in f:
                wordlist.append(line.rstrip('\n'))
    except Exception as ex:
        print(ex)

    print(f"[-] {len(wordlist)} words loaded from {wordlist_path}.")

    if len(wordlist) > chunk_size * 2:
        for i in range(0, len(wordlist), chunk_size):
            nested_wordlists.append(wordlist[i:i+chunk_size])
        print(
            f"[-] Wordlist split into {len(nested_wordlists)} lists of size {chunk_size}.")
        return nested_wordlists, preserve_ram

    preserve_ram = False
    return wordlist, preserve_ram
