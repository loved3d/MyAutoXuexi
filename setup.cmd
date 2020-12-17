@echo off
cd /d %~dp0
echo %cd%
echo first, confirm python3.7+ installed?
echo install venv...
python -m venv venv
echo venv installed OK.
echo install packages...
pip install -r requirements.txt
echo packages installed OK.
pause