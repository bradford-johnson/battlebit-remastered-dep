# Battlebit Remastered
Data analysis project that collects game server data via the server status API and explores the findings.

## Getting the data

This project uses GitHub Actions to pull in data with Python.

### Hourly server pull | [![Hourly game server data pull](https://github.com/bradfordjohnson/battlebit-remastered/actions/workflows/server_api.yml/badge.svg)](https://github.com/bradfordjohnson/battlebit-remastered/actions/workflows/server_api.yml)

Pulls the server data in each hour as `JSON` and converts to `CSV`. 

### Daily CSV Combination | [![Combine server data](https://github.com/bradfordjohnson/battlebit-remastered/actions/workflows/combine_server_data.yml/badge.svg)](https://github.com/bradfordjohnson/battlebit-remastered/actions/workflows/combine_server_data.yml)

Combines all `CSV` files into one, and clears the "data staging" directory when done.

### Load combined data into my Postgres database

[`03-load_into_postgres.py`](scripts/03-load_into_postgres.py) uses `creds.json` for secret environmental variables

## Disclaimer
Just a quick heads-up – this project is a **personal endeavor** and not affiliated with or endorsed by the creators of [BattleBit Remastered](https://joinbattlebit.com/). I enjoy the game and thought it would be fun to work on this project in my spare time.
