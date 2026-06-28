"""
tts.py

Responsável por gerar arquivos MP3 usando edge-tts.
"""

from __future__ import annotations

import asyncio
from pathlib import Path

import edge_tts


class TTS:

    def __init__(
        self,
        voice: str,
        rate: str = "+0%",
        volume: str = "+0%",
    ) -> None:

        self.voice = voice
        self.rate = rate
        self.volume = volume

    async def _save(
        self,
        text: str,
        output: Path,
    ) -> None:

        communicate = edge_tts.Communicate(
            text=text,
            voice=self.voice,
            rate=self.rate,
            volume=self.volume,
        )

        await communicate.save(str(output))

    def generate(
        self,
        text: str,
        output: Path,
    ) -> None:

        output.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        asyncio.run(
            self._save(
                text=text,
                output=output,
            )
        )