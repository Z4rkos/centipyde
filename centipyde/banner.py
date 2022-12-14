from termcolor import colored

title = """
 __                    
/   _  _ |_o _    _| _ 
\__(-`| )|_||_)\/(_|(-`
            |  /       
"""

title = colored(title, 'blue')
line = colored("-----------------------", "blue")

def print_banner(mode: str, executor_args: dict, wordlist_args: dict, request_handler_args: dict) -> None:
    """
    Prints the banner with some information about the current settings.

    """
    print(title)
    print(line)
    print(colored(f"[?] Mode: {mode}", 'red'))
    print(colored(f"[?] url: {request_handler_args['url']}", 'red'))
    print(colored(f"[?] Wordlist: {wordlist_args}", 'red')) # Not sure why wordlist is not in a dict.
    print(colored(f"[?] Workers: {executor_args['workers']}", 'red'))
    
    try:
        print(colored(f"[?] Status Codes: {request_handler_args['status_codes']}", "red"))
    except KeyError:
        pass

    print(line)
    print()

    """
    Need to find a bit cleaner way to do coloring so it works more seamlessly
    with the output produced by executor.

    Should also really just do the banner things in a loop. Could just have a
    list with things that I want to display.
    """
