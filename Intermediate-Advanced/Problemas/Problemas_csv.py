# cambiar el tipo de dato en una columna
import pandas as pd
df = pd.read_csv("Intermediate-Advanced\\Archivos\\dato.csv")

# converted as string data from a column
df["Edad"] = df["Edad"].astype(str)

# show data type // show 1st element of "age" column
print(type(df["Edad"][0]))

# replacing data "Bicha" to "Ladrona"
df["Segundo nombre"].replace("Bicha","Ladrona",inplace=True)

# deletes void/missing data lines
df = df.dropna()

# deletes repeated files
df = df.drop_duplicates()

## creando un data frame limpio // sin void data
# df.to_csv("Intermediate-Advanced\\Archivos\\datos_limpios.csv")