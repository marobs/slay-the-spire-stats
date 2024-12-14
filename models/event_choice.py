from dataclasses import dataclass, field


@dataclass
class EventChoice:
    event_name: str
    player_choice: str
    floor: float
    damage_taken: float
    damage_healed: float
    max_hp_gain: float
    max_hp_loss: float
    gold_gain: float
    gold_loss: float
    relics_obtained: list[str] = field(default_factory=list)
    cards_obtained: list[str] = field(default_factory=list)
    relics_lost: list[str] = field(default_factory=list)
    cards_transformed: list[str] = field(default_factory=list)
    potions_obtained: list[str] = field(default_factory=list)
    cards_upgraded: list[str] | None = None
    cards_removed: list[str] | None = None
