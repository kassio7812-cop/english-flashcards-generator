"""
backup.py

Sistema de backup automático das lições.

Responsabilidade:
- Criar a pasta de backup caso não exista.
- Gerar uma cópia completa da pasta lessons.
- Organizar os backups por data e hora.
"""

from __future__ import annotations

import shutil
from datetime import datetime
from pathlib import Path


class BackupManager:
    """
    Gerencia os backups automáticos do projeto.
    """

    def __init__(
        self,
        source: str | Path = "lessons",
        backup_root: str | Path = "backup",
    ) -> None:

        self.source = Path(source)
        self.backup_root = Path(backup_root)

        self.backup_root.mkdir(
            parents=True,
            exist_ok=True,
        )

    def create(self) -> Path | None:
        """
        Cria um backup completo da pasta lessons.

        Returns
        -------
        Path | None
            Caminho do backup criado ou None caso
            a pasta de origem não exista.
        """

        if not self.source.exists():
            return None

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        destination = self.backup_root / timestamp

        shutil.copytree(
            src=self.source,
            dst=destination,
            dirs_exist_ok=True,
        )

        return destination

    def list_backups(self) -> list[Path]:
        """
        Lista todos os backups disponíveis.
        """

        return sorted(
            self.backup_root.iterdir(),
            reverse=True,
        )

    def latest_backup(self) -> Path | None:
        """
        Retorna o backup mais recente.
        """

        backups = self.list_backups()

        if not backups:
            return None

        return backups[0]

    def remove_old(
        self,
        keep: int = 10,
    ) -> None:
        """
        Remove backups antigos.

        Parameters
        ----------
        keep:
            Quantidade máxima de backups
            que serão mantidos.
        """

        backups = self.list_backups()

        if len(backups) <= keep:
            return

        for folder in backups[keep:]:

            shutil.rmtree(folder)

    def restore(
        self,
        backup: Path,
    ) -> None:
        """
        Restaura um backup.

        Parameters
        ----------
        backup:
            Caminho do backup.
        """

        if not backup.exists():
            raise FileNotFoundError(backup)

        if self.source.exists():
            shutil.rmtree(self.source)

        shutil.copytree(
            backup,
            self.source,
        )