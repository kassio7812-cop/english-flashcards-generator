"""
Project paths.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FRASES_DIR = ROOT / "frases"
AUDIOS_DIR = ROOT / "audios"
ANKI_DIR = ROOT / "anki"
EXPORTS_DIR = ROOT / "exports"
LOGS_DIR = ROOT / "logs"

SETTINGS_DIR = ROOT / "settings"
SETTINGS_FILE = SETTINGS_DIR / "settings.json"

for folder in (
    FRASES_DIR,
    AUDIOS_DIR,
    ANKI_DIR,
    EXPORTS_DIR,
    LOGS_DIR,
    SETTINGS_DIR,
):
    folder.mkdir(exist_ok=True)