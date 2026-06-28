"""
Application settings.
"""

import json
from scripts.config import SETTINGS_FILE


class Settings:

    def __init__(self):

        with open(SETTINGS_FILE, encoding="utf-8") as f:
            self.data = json.load(f)

    def get(self, key, default=None):
        return self.data.get(key, default)

    @property
    def voice(self):
        return self.get("voice")

    @property
    def rate(self):
        return self.get("rate")

    @property
    def volume(self):
        return self.get("volume")

    @property
    def skip_existing(self):
        return self.get("skip_existing", True)