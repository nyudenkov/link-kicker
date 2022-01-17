from pathlib import Path

from app.misc import parse_config

# Project directory
ROOT_DIRECTORY = Path(__file__).parent.parent

# Bot Commands description dictionary
commands = parse_config(ROOT_DIRECTORY / "commands.yaml")
