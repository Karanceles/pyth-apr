import pandas as pd
import matplotlib.pyplot as plt ## graphical visualizer
import seaborn as sns # data visualization library

df = pd.read_csv("Intermediate-Advanced\\Problemas gráficos\\cofla_ingresos.csv")
sns.barplot(x="fuente",y="ingresos",data=df)

# function sum() --> total sumado
total_ingresos = df["ingresos"].sum()
print(f"El total de ingresos de Cofla es: CLP {total_ingresos} ")

plt.show()