import json
from dataclasses import dataclass, asdict


@dataclass
class Profile:
    user_id: str
    firstname: str
    lastname: str
    email: str
    address: str
    country: str
    city: str
    about: str

    def __init__(self, user_id="",
                 firstname="",
                 lastname="",
                 email="",
                 address="",
                 country="",
                 city="",
                 about=""
                 ):
        self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.address = address
        self.country = country
        self.city = city
        self.about = about

    def __str__(self) -> str:
        return json.dumps(asdict(self), indent=4, default=str)