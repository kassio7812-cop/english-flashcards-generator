"""
csv_reader.py

Leitura dos arquivos CSV das lições.

Suporta dois formatos:

1)
english,portuguese

2)
id,english,portuguese
"""

from pathlib import Path

import pandas as pd


class CsvReader:

    REQUIRED_COLUMNS = (
        "english",
        "portuguese",
    )

    def read(self, csv_file: Path):

        df = pd.read_csv(
            csv_file,
            encoding="utf-8"
        )

        df.columns = [
            c.strip().lower()
            for c in df.columns
        ]

        for column in self.REQUIRED_COLUMNS:

            if column not in df.columns:

                raise ValueError(
                    f"Coluna obrigatória ausente: {column}"
                )

        rows = []

        for index, row in df.iterrows():

            rows.append(
                {
                    "id": index + 1,
                    "english": str(
                        row["english"]
                    ).strip(),
                    "portuguese": str(
                        row["portuguese"]
                    ).strip(),
                }
            )

        return rows