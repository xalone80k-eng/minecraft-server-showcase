# Minecraft Server Showcase

A responsive Flask website for showing your Minecraft server details, ranks, player showcase, features, and community links.

## Requirements
- Python 3.10+
- pip

## Setup

Create and activate a virtual environment.

Windows:
```powershell
py -m venv .venv
.venv\Scripts\activate
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install packages:
```bash
python -m pip install -r requirements.txt
```

Edit `SERVER` and `RANKS` in `app.py` with your server address, version, community invite, rank names, perks, and consenting player display names.

Run locally:
```bash
python app.py
```
Open http://127.0.0.1:5000

## Pages
- `/` home page and rank preview
- `/ranks` rank descriptions and public player showcase
- `/about` server connection information

## Notes
This is a public information site. It does not connect to the Minecraft permissions database; rank/player listings are manually maintained in `app.py`. Do not publish passwords, RCON credentials, API tokens, or other secrets. `debug=True` is for local development only. For public hosting, disable debug mode, use a production WSGI server, and enable HTTPS.

Minecraft is a trademark of Mojang Studios. This independent fan project is not affiliated with Mojang or Microsoft.
