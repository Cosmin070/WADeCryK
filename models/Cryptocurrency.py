import json
from dataclasses import dataclass, asdict


@dataclass
class Cryptocurrency:
    name: str
    crypto_id: str
    description: str
    block_time: int
    date_founded: str
    incept: str
    proof_of_work: str
    premine: int
    protection_scheme: str
    protocol: str
    retarget_time: int
    source: str
    symbol: str
    total_coins: int
    website: str

    def __init__(self, name="",
                 crypto_id="",
                 description="",
                 block_time=0,
                 date_founded="",
                 incept="",
                 proof_of_work="",
                 premine=0,
                 protection_scheme="",
                 protocol="",
                 retarget_time=0,
                 source="",
                 symbol="",
                 total_coins=0,
                 website=""):
        self.website = website
        self.total_coins = total_coins
        self.symbol = symbol
        self.source = source
        self.retarget_time = retarget_time
        self.protocol = protocol
        self.protection_scheme = protection_scheme
        self.premine = premine
        self.proof_of_work = proof_of_work
        self.incept = incept
        self.date_founded = date_founded
        self.block_time = block_time
        self.description = description
        self.name = name
        self.crypto_id = crypto_id

    def __str__(self) -> str:
        return json.dumps(asdict(self), indent=4)