from dataclasses import dataclass


@dataclass
class BossRelic:
    not_picked: list[str] | None = None
    picked: str | None = None
