import os
from flask import Flask, render_template

app = Flask(__name__)

# Customize these values for your server.
SERVER = {IGNITEMC
    "name": "IgniteMc",
    "ip": "play.ignitemc.net",
    "port": 25565,
    "edition": "Java Edition Bedrock",
    "version": "1.21.x",
    "description": "A friendly community with survival, events, and player-built worlds.",
    "discord_url": "https://discord.gg/FMTS9NDzP",
}

# Example public showcase data. Only list players who agree to be featured.
RANKS = [
    {"name": "Owner", "color": "gold", "description": "Leads the server and community.",
     "perks": ["Community leadership", "Event planning"], "players": ["ExampleOwner"]},
    {"name": "Admin", "color": "red", "description": "Helps manage the server.",
     "perks": ["Staff tools", "Player support"], "players": ["ExampleAdmin"]},
    {"name": "Moderator", "color": "green", "description": "Keeps gameplay welcoming.",
     "perks": ["Chat moderation", "Player assistance"], "players": ["ExampleMod"]},
    {"name": "VIP", "color": "purple", "description": "A supporter rank with cosmetic extras.",
     "perks": ["Cosmetic tag", "Lobby effects"], "players": ["ExampleVIP"]},
]

FEATURES = [
    {"icon": "🌲", "title": "Survival", "text": "Build, explore, and create with friends."},
    {"icon": "⚔️", "title": "Community events", "text": "Join friendly events and challenges."},
    {"icon": "🏡", "title": "Player builds", "text": "Showcase your creativity and projects."},
]

@app.get("/")
def home():
    return render_template("index.html", server=SERVER, ranks=RANKS, features=FEATURES)

@app.get("/ranks")
def ranks():
    return render_template("ranks.html", server=SERVER, ranks=RANKS)

@app.get("/about")
def about():
    return render_template("about.html", server=SERVER)

@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html", server=SERVER), 404

if __name__ == "__main__":
    # Local development only. Use a production WSGI server when hosting publicly.
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", "5000")), debug=True)
