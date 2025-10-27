from pathlib import Path
from toy_snake.utils import write_file

def preprocess_algo1(path: Path):
    print("preprocess_algo_1")
    write_file(f"{path}_preprocessed1")  

def ingest_data_algo2(path: Path):
    print("preprocess_algo_2")
    write_file(f"{path}_preprocessed2")  