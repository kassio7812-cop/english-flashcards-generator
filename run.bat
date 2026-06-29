@echo off
title English Flashcards Generator v1.3.1
color 0A

cd /d "%~dp0"

if exist ".venv\Scripts\activate.bat" (
    call ".venv\Scripts\activate.bat"
)

echo.
echo ============================================================
echo              English Flashcards Generator
echo                     Version 1.3.1
echo ============================================================
echo.

python main.py --all

echo.
echo ============================================================
echo Processo finalizado.
echo ============================================================
echo.

pause