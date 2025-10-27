from pathlib import Path
import datetime

def write_file(path: Path):
    with open(path, "a") as file:
        file.write(f"Writing this file at {datetime.datetime.now()}\n")