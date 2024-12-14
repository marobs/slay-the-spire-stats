from dataclasses import dataclass


@dataclass
class DamageTaken:
    damage: float
    enemies: str
    floor: float
    turns: float
