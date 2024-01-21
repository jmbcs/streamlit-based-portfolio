from pathlib import Path
from typing import Tuple, Type

# from pydantic import field_validator
from pydantic_settings import (
    BaseSettings,
    EnvSettingsSource,
    PydanticBaseSettingsSource,
)

from portfolio.schemas import Animations, Htmltext, Styles

# from yaml import safe_load

# __PATH_TO_CONFIG = "config/config.yml"


# def _load_yaml(file_path: Path, encoding: str = "utf8") -> dict[str, Any]:
#     with open(file_path, encoding=encoding) as reader:
#         config: dict[str, Any] = safe_load(reader)
#     return config


# def yaml_config_settings_source() -> dict[str, Any]:
#     """
#     A simple settings source that loads variables from a YAML file named
#     "inventory.yml" at <project_root>/config.`
#     """

#     config = _load_yaml(Path(__PATH_TO_CONFIG))
#     return config

_Config__SERVICE_PREFIX = "PORTFOLIO_"


class Settings(BaseSettings):
    animations: Animations = Animations()
    styles: Styles = Styles()
    html: Htmltext = Htmltext()
    profile_image_path: Path = Path("portfolio/docs/profile.jpg")
    curriculum_path: Path = Path("portfolio/docs/cv_julio_silva.pdf")

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: EnvSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        return (
            env_settings,
            dotenv_settings,
            init_settings,
            # yaml_config_settings_source,
            file_secret_settings,
        )

    class Config:
        env_file = (".env", ".prod.env")
        env_nested_delimiter = "__"
        env_file_encoding = "utf-8"
        env_prefix = _Config__SERVICE_PREFIX


config = Settings()
