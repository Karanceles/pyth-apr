import pandas as pd
import matplotlib.pyplot as plt ## graphical visualizer
import seaborn as sns # data visualization library

df = pd.read_csv("Intermediate-Advanced\\Problemas gráficos\\bigotes_nums.csv")
# ploteo de cajas --> toma rango de valores
sns.boxplot(x="categoria",y="valor",data=df)
plt.show()