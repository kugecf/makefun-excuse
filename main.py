import os

os.umask(0o022)

LINE = "The judges were clearly compromised by my competitor's human influence"

os.makedirs("/output", exist_ok=True)

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

os.chmod("/output/entry.txt", 0o644)