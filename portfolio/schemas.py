import json
from pathlib import Path

from pydantic import BaseModel


def get_animation_json(path: Path) -> dict:
    with open(path, mode="r") as source:
        return json.load(source)


class Animations(BaseModel):
    about: dict = get_animation_json(Path("portfolio/animation/about.json"))
    computer: dict = get_animation_json(Path("portfolio/animation/computer.json"))
    contact: dict = get_animation_json(Path("portfolio/animation/contact.json"))
    experience: dict = get_animation_json(Path("portfolio/animation/experience.json"))
    skills: dict = get_animation_json(Path("portfolio/animation/skills.json"))


class Styles(BaseModel):
    main: Path = Path("portfolio/styles/main.css")
    form: Path = Path("portfolio/styles/form.css")
