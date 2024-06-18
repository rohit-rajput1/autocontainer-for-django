import toml
from pathlib import Path

def load_config():
    config_path = Path(__file__).resolve().parent / 'src/home/project.toml'
    return toml.load(config_path)

config = load_config()