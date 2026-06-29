"""
settings.py

Carrega as configurações do programa.
"""

from __future__ import annotations

import json

from scripts.config import SETTINGS_FILE


class Settings:

    def __init__(self):

        self.reload()

    def reload(self):

        with open(
            SETTINGS_FILE,
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        self.voice_lang = data.get(
            "voice_lang",
            "en"
        )

        self.voice_slow = data.get(
            "voice_slow",
            False
        )

        self.skip_existing_audio = data.get(
            "skip_existing_audio",
            True
        )

        self.create_backup = data.get(
            "create_backup",
            True
        )

        self.keep_backups = data.get(
            "keep_backups",
            10
        )

        self.show_progress = data.get(
            "show_progress",
            True
        )

        self.anki_separator = data.get(
            "anki_separator",
            ","
        )

        self.log_level = data.get(
            "log_level",
            "INFO"
        )

    def save(self):

        data = {

            "voice_lang": self.voice_lang,

            "voice_slow": self.voice_slow,

            "skip_existing_audio": self.skip_existing_audio,

            "create_backup": self.create_backup,

            "keep_backups": self.keep_backups,

            "show_progress": self.show_progress,

            "anki_separator": self.anki_separator,

            "log_level": self.log_level,

        }

        with open(
            SETTINGS_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )