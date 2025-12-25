# import yaml
# import os
# from logger.custom_logger import CustomLogger


# def load_config(config_path: str = "config\config.yaml") -> dict:
#     logger = CustomLogger().get_logger(__name__)
#     logger.info(f'Inside config loader {os.getcwd()}')
#     with open(config_path, "r") as file:
#         config=yaml.safe_load(file)
#     return config


from pathlib import Path
import yaml
from logger.custom_logger import CustomLogger


def load_config(config_path: str | None = None) -> dict:
    logger = CustomLogger().get_logger(__name__)

    # Project root = where test.py is executed
    project_root = Path.cwd()

    # Default config path
    if config_path is None:
        config_path = project_root / "config" / "config.yaml"
    else:
        config_path = Path(config_path)

    logger.info(
        event="Loading config",
        config_path=str(config_path),
        cwd=str(project_root),
    )

    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path, "r") as file:
        return yaml.safe_load(file)
