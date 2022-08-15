class Arguments:

    @dataclass
    class RequestArgs:
        url: str
        username: str = ""
        password: str = ""
        fail_string: str = ""
        status_codes: list = field(default_factory=list)
        headers: dict = field(default_factory=dict)
        cookies: dict = field(default_factory=dict)

    @dataclass
    class WebArgs:
        wordlist_path: str
        request_handeler: object
        workers: int = 30
        chunk_size: int = 100000
