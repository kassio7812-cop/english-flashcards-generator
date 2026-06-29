"""
logger.py

Sistema de logs do projeto.
"""

from __future__ import annotations

import logging

from scripts.config import LOG_DIR


class Logger:

    _started = False

    @classmethod
    def setup(cls):

        if cls._started:
            return

        logfile = LOG_DIR / "latest.log"

        logging.basicConfig(

            level=logging.INFO,

            format="%(asctime)s | %(levelname)s | %(message)s",

            handlers=[

                logging.FileHandler(
                    logfile,
                    encoding="utf-8"
                ),

                logging.StreamHandler()

            ]

        )

        cls._started = True

    @staticmethod
    def info(message):

        logging.info(message)

    @staticmethod
    def warning(message):

        logging.warning(message)

    @staticmethod
    def error(message):

        logging.error(message)

    @staticmethod
    def exception(message):

        logging.exception(message)