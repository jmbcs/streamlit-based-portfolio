import json
from pathlib import Path

from pydantic import BaseModel


def get_animation_json(path: Path) -> dict:
    with open(path, mode="r") as source:
        return json.load(source)


def get_html_string(path: Path) -> str:
    with open(path, "r") as source:
        return source.read()


class Animations(BaseModel):
    about: dict = get_animation_json(Path("portfolio/animation/about.json"))
    computer: dict = get_animation_json(Path("portfolio/animation/computer.json"))
    contact: dict = get_animation_json(Path("portfolio/animation/contact.json"))
    experience: dict = get_animation_json(Path("portfolio/animation/experience.json"))
    skills: dict = get_animation_json(Path("portfolio/animation/skills.json"))


class Htmltext(BaseModel):
    about: str = get_html_string(Path("portfolio/html/about.html"))
    style: str = get_html_string(Path("portfolio/html/style.html"))
    contact_form: str = get_html_string(Path("portfolio/html/contact.html"))
    experience: str = get_html_string(Path("portfolio/html/experience.html"))
    divider: str = get_html_string(Path("portfolio/html/divider.html"))
    subtitle: str = get_html_string(Path("portfolio/html/subtitle.html"))
    title: str = get_html_string(Path("portfolio/html/title.html"))
    footer: str = get_html_string(Path("portfolio/html/footer.html"))


class Styles(BaseModel):
    main: Path = Path("portfolio/styles/main.css")
    form: Path = Path("portfolio/styles/form.css")
