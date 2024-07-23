import pandas as pd
import matplotlib.pyplot as plt ## graphical visualizer
import seaborn as sns # data visualization library

df = pd.read_csv("Intermediate-Advanced\\Problemas gráficos\\pasos_moca.csv")

# ploting a graph
sns.lineplot(x="fecha",y="pasos",data=df)

# creating a point in a determined day or data
plt.plot("10-10",14100,"o")

plt.show()