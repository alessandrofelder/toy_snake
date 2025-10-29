configfile: "config.yaml"

SAMPLES = ["sample_data1", "sample_data2"]


rule all:
    input:
        expand("data/derivatives/preprocessed/{sample}_preprocessed.csv", sample=SAMPLES),


rule ingest:
    input:
        expand("data/raw/{sample}.txt", sample=SAMPLES),
    output:
        "data/derivatives/ingested/{sample}_ingested.csv",
    log:
        "logs/toy_snake_ingest_{sample}.log",
    conda:
        config["ingest"]["env"]
    script:
        "toy_snake/ingest.py"


rule preprocess:
    input:
        expand("data/derivatives/ingested/{sample}_ingested.csv", sample=SAMPLES),
    output:
        "data/derivatives/preprocessed/{sample}_preprocessed.csv",
    log:
        "logs/toy_snake_preprocess_{sample}.log",
    script:
        "toy_snake/preprocess.py"
