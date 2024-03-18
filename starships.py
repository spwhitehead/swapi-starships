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


def print_starships(starships: list) -> None:
    for starship in starships:
        print(starship["name"])


url = "https://swapi.dev/api/starships"
response = requests.get(url)
results = response.json()
print_starships(results["results"])

while results["next"] is not None:
    url = results["next"]
    response = requests.get(url)
    results = response.json()
    print_starships(results["results"])


print("Done")
