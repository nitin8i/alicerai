@echo off
TITLE alice bot
:: Enables virtual env mode and then starts Telegram bot
env\scripts\activate.bat && py -m alice
