from dataclasses import dataclass


@dataclass
class CardChoice:
    not_picked: list[str]
    picked: str
    floor: float
