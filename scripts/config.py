"""
config.py

Centraliza caminhos do projeto.
"""

from pathlib import Path

# Diretório raiz do projeto
ROOT_DIR = Path(__file__).resolve().parent.parent

# Pastas do projeto
LESSONS_DIR = ROOT_DIR / "lessons"
AUDIO_DIR = ROOT_DIR / "audios"
ANKI_DIR = ROOT_DIR / "anki"
LOG_DIR = ROOT_DIR / "logs"
BACKUP_DIR = ROOT_DIR / "backup"
EXPORT_DIR = ROOT_DIR / "exports"
SETTINGS_DIR = ROOT_DIR / "settings"
IMPORTS_DIR = ROOT_DIR / "imports"

# Arquivo de configurações
SETTINGS_FILE = SETTINGS_DIR / "settings.json"

# Criar automaticamente as pastas do projeto
for directory in (
    LESSONS_DIR,
    AUDIO_DIR,
    ANKI_DIR,
    LOG_DIR,
    BACKUP_DIR,
    EXPORT_DIR,
    SETTINGS_DIR,
    IMPORTS_DIR,
):
    directory.mkdir(
        parents=True,
        exist_ok=True,
    )