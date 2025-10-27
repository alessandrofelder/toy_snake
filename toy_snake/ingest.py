from pathlib import Path
from toy_snake.utils import write_file

def ingest_data_algo1(path: Path):
    print("ingest_algo_1")
    write_file(f"{path}_ingested1")    

def ingest_data_algo2(path: Path):
    print("ingest_algo_2")
    write_file(f"{path}_ingested2")



    