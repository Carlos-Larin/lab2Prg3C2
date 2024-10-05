#aqui le tiramos la call a las librerias
import pandas as pd
import matplotlib as plt


cancerbero = pd.read_csv("")
frecuencia=cancerbero[""].value_counts()
plt.pie(frecuencia.values,labels=frecuencia.index.autopat="%1.1f%%")
plt.show()