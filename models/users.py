import json
from dataclasses import dataclass, asdict


@dataclass
class User:
    email: str
    password: str

    def __init__(self,
                 email="",
                 password=""):
        self.email = email
        self.password = password

    def __str__(self) -> str:
        return json.dumps(asdict(self), indent=4)
