import requests
from termcolor import colored


def host_is_up(host: str) -> bool:
    print(colored("[?] Checking if the target is up...", "blue"))
    try:
        response = requests.get(host, timeout=5)
        if response.status_code == 200:
            print(colored("[?] Got response from target.", "green"))
            print()
            return True
    except requests.exceptions.ConnectionError:
        print(colored("[X] The target is not responding.", "red"))
        return False
