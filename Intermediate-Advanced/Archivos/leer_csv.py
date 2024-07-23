import csv # importo csv
# archivo CSV , comas son espacios

with open("Intermediate-Advanced\\Archivos\\dato.csv",encoding="UTF-8") as archivo:
    reader = csv.reader(archivo) ## iterable
    for row in reader:
        print(row)

