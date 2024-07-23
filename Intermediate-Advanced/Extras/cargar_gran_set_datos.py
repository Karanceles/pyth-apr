import pandas as pd

def read_csv_chunks(file_name):
    for i,chunk in enumerate(pd.read_csv(file_name,chunksize=1000)):
        print("Chunk #{}".format(i))
        print(chunk)

read_csv_chunks("HEAVY_FILE.csv")