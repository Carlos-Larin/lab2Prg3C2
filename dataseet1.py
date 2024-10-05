#aqui le tiramos la call a las librerias
import pandas as pd
import matplotlib.pyplot as plt

#aqui leemos el dataseet
cancerbero = pd.read_csv("valorant-stats.csv")
data = cancerbero.groupby("Name")["HDMG_0"].mean().sort_values()
#para que se muestre el daño a la cabeza que provoca por arma
plt.bar(data.index, data.values)
#los label de las orillas para identificar
plt.ylabel('Daño a la cabeza(HDMG_0)')
plt.xlabel('Arma')
plt.title('Daño por Arma')
#algunos names son largos asi que toca rotar
plt.xticks(rotation=90)
#para que se imprima
plt.tight_layout()
plt.show()

#plt.bar(frecuencia.values,labels=frecuencia.index,autopct="%1.1f%%",)