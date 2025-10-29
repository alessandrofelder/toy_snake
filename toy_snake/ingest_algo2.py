import sys
from toy_snake.utils import write_file

sys.stderr = open(snakemake.log[0], "a")
sys.stdout = open(snakemake.log[0], "a")

def ingest_data_algo2():
    print("ingest_algo_2")
    import numpy as np
    print(sys.executable)
    print(np.__version__)
    print(snakemake.config["ingest"].keys())
    write_file(f"{snakemake.output[0]}")    

if __name__ == "__main__":
    ingest_data_algo2()