import pandas as pd #pd == pandas en lengua común
## print(type(pd)) pd is a module

# data frame (hoja de cálculo 2D fila columna)
df = pd.read_csv("Intermediate-Advanced\\Archivos\\dato.csv") #,names=["Name","2nd name","Age","Gender"])
df2 = pd.read_csv("Intermediate-Advanced\\Archivos\\dato.csv")
# nombre = df["Nombre"]

# slicing (pandas' one of the most used)
cadena = "0123456789"

# arrange df by age %% if not assigned, creates an anonymous value
df_ascend = df.sort_values("Edad") ## True == default
df_descend = df.sort_values("Edad", ascending=False)

# concatenar 2 data frames
df_concatenado = pd.concat([df,df2])

# head/tail (acceding firsts/lasts ones)
first_row = df.head(2)
last_row = df.tail(2)

# desencapsulando
# .shape ==> acceding to quantity of rows and columns
tot_rows, tot_columns = df.shape # [0]: rows // [1]: columns

# statistical numbers (data analysis) from data fram
df_info = df.describe()

# using loc: acceding to a specific df element aswell as iloc
spec_element_loc = df.loc[2,"Edad"] # 2D specific element
spec_element_iloc = df.iloc[2,2] # acceding through the index (iloc)

# acceding to the whole row array from a column
segundo_nombre = df.iloc[:,1] #
fila_3 = df.iloc[2,:] # read it as a vertical directory

# acceding to rows with an age boundary
age_gap_30 = df.loc[df["Edad"]>30,:]

print(age_gap_30)
## print(cadena[:]) ## ([:]) starts on the 1st term and ends with the last one