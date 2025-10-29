import sys
from toy_snake.utils import write_file
import importlib

if __name__ == "__main__":
    sys.stderr = open(snakemake.log[0], "a")
    sys.stdout = open(snakemake.log[0], "a")


    params = snakemake.config["ingest"]["params"]
    spec = importlib.util.spec_from_file_location("ingest_algo_module", snakemake.config["ingest"]["script"])
    ingest_module = importlib.util.module_from_spec(spec)
    print(ingest_module.__name__)
    spec.loader.exec_module(ingest_module)

    result = ingest_module.ingest(params)
    write_file(f"{snakemake.output[0]}", params=result)    
