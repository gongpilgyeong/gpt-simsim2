import json
from pathlib import Path
from typing import Optional


BASE_DIR = Path(__file__).resolve().parent  # gpt-simsim2 dir


def get_secret(
    key: str,
    default_value: Optional[str] = None,
    json_path: str = str(BASE_DIR / "secrets.json"),
):
    """Function to get secret variables"""
    with open(json_path) as f:
        secrets = json.loads(f.read())
    try:
        return secrets[key]
    except KeyError:
        if default_value:
            return default_value
        raise EnvironmentError(f"Set the {key} environment variable.")


"""
To set a secret variable
"""
OPENAI_API_KEY = get_secret("OPENAI_API_KEY")
