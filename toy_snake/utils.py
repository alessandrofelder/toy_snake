from pathlib import Path
import datetime

def write_file(path: Path, params=""):
    with open(path, "a") as file:
        file.write(f"Writing this file at {datetime.datetime.now()}\n")
        file.write(f"Parameters: {params}")