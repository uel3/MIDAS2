# These are the "raw" inputs to the MIDAS DB construction subcommands.
# See https://github.com/czbiohub/MIDAS2.0/wiki/MIDAS-DB#inputs

igg = "s3://microbiome-pollardlab"
server="https://microbiome-pollardlab.s3.us-west-2.amazonaws.com"

MIDASDB_DICT = {
    "uhgg": f"{server}/uhgg",
    "gtdb": f"{server}/gtdb",
    "newdb": f"{server}/newdb", # reserved for building new MIDASDB locally
    "s3db": f"{igg}/testdb", # reserved for building new MIDASDB and upload to S3
}

MIDASDB_VERSION = {
    "uhgg": f"version 1.0",
    "gtdb": f"version r202",
}
MIDASDB_NAMES = list(MIDASDB_DICT.keys())


marker_set = "phyeco"
MARKER_FILE_EXTS = ["fa", "fa.bwt", "fa.header", "fa.sa", "fa.sequence", "map"]
hmmsearch_max_evalue = 1e-5
hmmsearch_min_cov = 0.00
