# CryptoPythia Yandex Dialogs Bot
This repository contains basic template for Yandex Alice's skill.

## Structure
- `pythia_bot/`. code is here
- `pictures/`. static files are here

## Test skill "CryptoPythia"
Ready-to-go example is in `pythia_bot` directory.
Yandex Alice Documentation was borrowed https://tech.yandex.ru/dialogs/alice/doc/quickstart-python-docpage/
- `main_logic.py` implements main logic (function `handle_dialog`), managing user's input.
- `alice_sdk.py` contains library for handling Yandex Alice's API.
- `alice_app.py` contains script which runs a server.
