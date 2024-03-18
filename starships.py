import requests
from dataclasses import dataclass


@dataclass
class Film:
    title: str
    episode_id: int


@dataclass
class Pilot:
    name: str
    films: list[Film]


@dataclass
class Starship:
    name: str
    model: str
    cost_in_credits: int
    pilots: list[Pilot]


response = requests.get("https://swapi.dev/api/starships")
response.json()
print()
