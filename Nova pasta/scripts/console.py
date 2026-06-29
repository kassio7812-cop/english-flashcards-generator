"""
console.py

Centraliza toda a saída no terminal.
"""

from __future__ import annotations


class Console:

    WIDTH = 60

    # ==================================================
    # Estrutura
    # ==================================================

    @classmethod
    def line(cls):

        print("=" * cls.WIDTH)

    @classmethod
    def separator(cls):

        print("-" * cls.WIDTH)

    @staticmethod
    def blank():

        print()

    # ==================================================
    # Títulos
    # ==================================================

    @classmethod
    def title(cls, text):

        cls.blank()

        cls.line()

        print(text)

        cls.line()

    # ==================================================
    # Mensagens
    # ==================================================

    @staticmethod
    def info(text):

        print(text)

    @staticmethod
    def success(text):

        print(f"✅ {text}")

    @staticmethod
    def warning(text):

        print(f"⚠️  {text}")

    @staticmethod
    def error(text):

        print(f"❌ {text}")

    # ==================================================
    # Lições
    # ==================================================

    @staticmethod
    def lesson(name):

        print()

        print(f"📚 {name}")

    # ==================================================
    # Áudios
    # ==================================================

    @staticmethod
    def generated(file):

        # Na V1.2.1 estas mensagens podem ser
        # desativadas quando usamos tqdm.
        print(f"   🎤 {file}")

    @staticmethod
    def skipped(file):

        print(f"   ✔ {file}")

    # ==================================================
    # Estatísticas
    # ==================================================

    @staticmethod
    def stat(label, value):

        print(f"{label:<22}: {value}")

    # ==================================================
    # Banner
    # ==================================================

    @classmethod
    def banner(cls, app_name, version):

        cls.title(app_name)

        cls.info(f"Version : {version}")

        cls.separator()