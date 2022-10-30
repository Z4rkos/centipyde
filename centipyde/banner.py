from termcolor import colored

title = """
 __                    
/   _  _ |_o _    _| _ 
\__(-`| )|_||_)\/(_|(-`
            |  /       
"""

title = colored(title, 'blue')
line = colored("-----------------------", "blue")

def print_banner(mode: str, executor_args: dict, wordlist_args: dict, request_handler_args: dict):
    print(title)
    print(line)
    print(colored(f"[?] Mode: {mode}", 'red'))
    print(colored(f"[?] url: {request_handler_args['url']}", 'red'))
    print(colored(f"[?] Wordlist: {wordlist_args}", 'red'))
    print(colored(f"[?] Workers: {executor_args['workers']}", 'red'))

    print(line)
    print()
