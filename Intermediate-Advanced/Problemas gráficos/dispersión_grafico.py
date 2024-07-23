import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Intermediate-Advanced\\Problemas gráficos\\dispersión_numeros.csv")

# vastly used by AI and Machine learning giving the fact that throws out lines
sns.scatterplot(x="tiempo",y="dinero",data=df) # relation btwn 2 lines or smtn
plt.show()