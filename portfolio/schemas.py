import json
from pathlib import Path

from pydantic import BaseModel

HTML_PATH = "portfolio/html"
ANIMATION_PATH = "portfolio/animation"
STYLES_PATH = "portfolio/styles"


def get_animation_json(path: Path) -> dict:
    with open(path, mode="r") as source:
        return json.load(source)


def get_html_string(path: Path) -> str:
    with open(path, "r") as source:
        return source.read()


class Animations(BaseModel):
    about: dict = get_animation_json(Path(f"{ANIMATION_PATH}/about.json"))
    computer: dict = get_animation_json(Path(f"{ANIMATION_PATH}/computer.json"))
    contact: dict = get_animation_json(Path(f"{ANIMATION_PATH}/contact.json"))
    experience: dict = get_animation_json(Path(f"{ANIMATION_PATH}/experience.json"))
    skills: dict = get_animation_json(Path(f"{ANIMATION_PATH}/skills.json"))


class Htmltext(BaseModel):
    section_about: str = get_html_string(Path(f"{HTML_PATH}/section_about.html"))
    stucture_style: str = get_html_string(Path(f"{HTML_PATH}/stucture_style.html"))
    section_contact: str = get_html_string(Path(f"{HTML_PATH}/section_contact.html"))
    section_experience: str = get_html_string(
        Path(f"{HTML_PATH}/section_experience.html")
    )
    section_curriculum: str = get_html_string(
        Path(f"{HTML_PATH}/section_curriculum.html")
    )
    structure_divider: str = get_html_string(
        Path(f"{HTML_PATH}/structure_divider.html")
    )
    structure_subtitle: str = get_html_string(
        Path(f"{HTML_PATH}/structure_subtitle.html")
    )
    structure_title: str = get_html_string(Path(f"{HTML_PATH}/structure_title.html"))
    structure_footer: str = get_html_string(Path(f"{HTML_PATH}/structure_footer.html"))
    section_skills: str = get_html_string(Path(f"{HTML_PATH}/section_skills.html"))
    section_project_bighpc: str = get_html_string(
        Path(f"{HTML_PATH}/section_project_bighpc.html")
    )
    section_project_thesis: str = get_html_string(
        Path(f"{HTML_PATH}/section_project_thesis.html")
    )
    section_project_portfolio: str = get_html_string(
        Path(f"{HTML_PATH}/section_project_portfolio.html")
    )
    project_bighpc_video: str = get_html_string(Path(f"{HTML_PATH}/video_bighpc.html"))

    structure_tech_stack: str = get_html_string(
        Path(f"{HTML_PATH}/structure_tech_stack.html")
    )


class Styles(BaseModel):
    form: Path = Path(f"{STYLES_PATH}/form.css")
    lottie: Path = Path(f"{STYLES_PATH}/lottie.css")
    main: Path = Path(f"{STYLES_PATH}/main.css")
