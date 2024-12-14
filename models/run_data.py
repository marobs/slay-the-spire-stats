from dataclasses import dataclass
import json

from .boss_relic import BossRelic
from .campfire_choice import CampfireChoice
from .card_choice import CardChoice
from .damage_taken import DamageTaken
from .event_choice import EventChoice
from .item_purged import ItemPurged
from .potion_obtained import PotionObtained
from .relic_obtained import RelicObtained


def parse_run_data(run_data):
    """Parses the given JSON object into a RunData object."""
    # Convert lists to appropriate objects
    items_purged = [ItemPurged(card=item)
                    for item in run_data.get('items_purged', [])]
    campfire_choices = [CampfireChoice(
        **choice) for choice in run_data.get('campfire_choices', [])]
    potions_obtained = [PotionObtained(
        **potion) for potion in run_data.get('potions_obtained', [])]
    relics_obtained = [RelicObtained(**relic)
                       for relic in run_data.get('relics_obtained', [])]
    card_choices = [CardChoice(**choice)
                    for choice in run_data.get('card_choices', [])]
    damage_taken = [DamageTaken(**damage)
                    for damage in run_data.get('damage_taken', [])]
    event_choices = [EventChoice(**event)
                     for event in run_data.get('event_choices', [])]
    boss_relics = [BossRelic(**relic)
                   for relic in run_data.get('boss_relics', [])]

    return RunData(
        gold_per_floor=run_data.get('gold_per_floor', []),
        floor_reached=run_data.get('floor_reached', 0),
        playtime=run_data.get('playtime', 0),
        items_purged=items_purged,
        score=run_data.get('score', 0),
        play_id=run_data.get('play_id', ''),
        local_time=run_data.get('local_time', ''),
        is_ascension_mode=run_data.get('is_ascension_mode', False),
        campfire_choices=campfire_choices,
        neow_cost=run_data.get('neow_cost', ''),
        seed_source_timestamp=run_data.get('seed_source_timestamp', 0),
        circlet_count=run_data.get('circlet_count', 0),
        master_deck=run_data.get('master_deck', []),
        special_seed=run_data.get('special_seed', 0),
        relics=run_data.get('relics', []),
        potions_floor_usage=run_data.get('potions_floor_usage', []),
        damage_taken=damage_taken,
        seed_played=run_data.get('seed_played', ''),
        potions_obtained=potions_obtained,
        is_trial=run_data.get('is_trial', False),
        path_per_floor=run_data.get('path_per_floor', []),
        character_chosen=run_data.get('character_chosen', ''),
        items_purchased=run_data.get('items_purchased', []),
        campfire_rested=run_data.get('campfire_rested', 0),
        item_purchase_floors=run_data.get('item_purchase_floors', []),
        current_hp_per_floor=run_data.get('current_hp_per_floor', []),
        gold=run_data.get('gold', 0),
        neow_bonus=run_data.get('neow_bonus', ''),
        is_prod=run_data.get('is_prod', False),
        is_daily=run_data.get('is_daily', False),
        chose_seed=run_data.get('chose_seed', False),
        campfire_upgraded=run_data.get('campfire_upgraded', 0),
        win_rate=run_data.get('win_rate', 0.0),
        timestamp=run_data.get('timestamp', 0),
        path_taken=run_data.get('path_taken', []),
        build_version=run_data.get('build_version', ''),
        purchased_purges=run_data.get('purchased_purges', 0),
        victory=run_data.get('victory', False),
        max_hp_per_floor=run_data.get('max_hp_per_floor', []),
        card_choices=card_choices,
        player_experience=run_data.get('player_experience', 0),
        relics_obtained=relics_obtained,
        event_choices=event_choices,
        is_beta=run_data.get('is_beta', False),
        boss_relics=boss_relics,
        items_purged_floors=run_data.get('items_purged_floors', []),
        is_endless=run_data.get('is_endless', False),
        potions_floor_spawned=run_data.get('potions_floor_spawned', []),
        killed_by=run_data.get('killed_by', ''),
        ascension_level=run_data.get('ascension_level', 0),
    )


@dataclass
class RunData:
    gold_per_floor: list[int]
    floor_reached: int
    playtime: int
    items_purged: list[ItemPurged]
    score: int
    play_id: str
    local_time: str
    is_ascension_mode: bool
    campfire_choices: list[CampfireChoice]
    neow_cost: str
    seed_source_timestamp: int
    circlet_count: int
    master_deck: list[str]
    special_seed: int
    relics: list[str]
    potions_floor_usage: list[int]
    damage_taken: list[DamageTaken]
    seed_played: str
    potions_obtained: list[PotionObtained]
    is_trial: bool
    path_per_floor: list[str | None]
    character_chosen: str
    items_purchased: list[str]
    campfire_rested: int
    item_purchase_floors: list[int]
    current_hp_per_floor: list[int]
    gold: int
    neow_bonus: str
    is_prod: bool
    is_daily: bool
    chose_seed: bool
    campfire_upgraded: int
    win_rate: float
    timestamp: int
    path_taken: list[str]
    build_version: str
    purchased_purges: int
    victory: bool
    max_hp_per_floor: list[int]
    card_choices: list[CardChoice]
    player_experience: int
    relics_obtained: list[RelicObtained]
    event_choices: list[EventChoice]
    is_beta: bool
    boss_relics: list[BossRelic]
    items_purged_floors: list[int]
    is_endless: bool
    potions_floor_spawned: list[float]
    killed_by: str
    ascension_level: int
