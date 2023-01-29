import json
from dataclasses import dataclass, asdict


@dataclass
class Portfolio:
    user_id: str
    coins: dict[str, int]

    def __init__(self, user_id="",
                 coins=None):
        self.coins = {} if coins is None else coins
        self.user_id = user_id

    def __str__(self) -> str:
        return json.dumps(asdict(self), indent=4, default=str)
