import sys
from toy_snake.utils import write_file

sys.stderr = open(snakemake.log[0], "a")
sys.stdout = open(snakemake.log[0], "a")

def preprocess_algo1():
    print("preprocess_algo_1")
    write_file(snakemake.output[0])  

def preprocess_algo2():
    print("preprocess_algo_2")
    write_file(snakemake.output[0])  

preprocess_algo1()