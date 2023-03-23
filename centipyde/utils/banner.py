from termcolor import colored


title = """
 __                    
/   _  _ |_o _    _| _ 
\__(-`| )|_||_)\/(_|(-`
            |  /       
"""

title = colored(title, "blue")
line = colored("-----------------------", "blue")


def print_banner(mode: str, executor_args: dict, wordlist_args: dict, request_handler_args: dict) -> None:
    """
    Prints the banner with some information about the current settings.
    """

    def print_banner_item(title: str, setting: str) -> None:
        print(colored(f"[?] {title}: {setting}", "green"))

    print(title)
    print(line)
    print_banner_item("Mode", mode)
    print_banner_item("URL", request_handler_args["url"])
    print_banner_item("Wordlist", wordlist_args["wordlist"])
    print_banner_item("Workers", executor_args["workers"])


    # Conditional banner items
    match mode:
        case "dir":
            print_banner_item("Status Codes", request_handler_args["status_codes"])
        case "dns":
            print_banner_item("Status Codes", request_handler_args["status_codes"])
        case "post":
            print_banner_item("Fail String", request_handler_args["fail_string"])
        case "pwd":
            print_banner_item("Fail String", request_handler_args["fail_string"])

    print(line)
    print()
