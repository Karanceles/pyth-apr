import csv

def read_csv_chunks(file_name):
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        for i, chunk in enumerate(reader):
            print("Chunk {}".format(i))
            print(chunk)

read_csv_chunks("HEAVY_FILE.csv")