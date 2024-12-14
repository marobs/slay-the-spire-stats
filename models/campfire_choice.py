from dataclasses import dataclass


@dataclass
class CampfireChoice:
    floor: float
    key: str
    data: str | None = None
