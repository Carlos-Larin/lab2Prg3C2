"""
https://www.kaggle.com/datasets/surajjha101/top-youtube-channels-data


segun este archivo Csv el canal de Tseries es quien posee el mayor numero de suscriptores
"""
import pandas as pd
import matplotlib.pyplot as plt

#Llamar el CSV a trabajar
FrananCrack = pd.read_csv("youtuber.csv")

#Eliminar las comas en la columna 'subscribers' y convertir a números porque sino no saldran datos (error que nos tomo 30 minutos resolver)
FrananCrack['subscribers'] = FrananCrack['subscribers'].str.replace(',', '').astype(float)

#Verificar los datos procesados
print(FrananCrack[['Youtuber', 'subscribers']])

#Ordenar por número de suscriptores
FrananCrack_sorted = FrananCrack.sort_values(by='subscribers', ascending=False).head(10)

#Graficar los datos con un gráfico de líneas
plt.figure(figsize=(10, 6))
plt.plot(FrananCrack_sorted['Youtuber'], FrananCrack_sorted['subscribers'], marker='o', color='skyblue', linestyle='-')

plt.xlabel('Youtuber')
plt.ylabel('Suscriptores')
plt.title('Top 10 Youtubers por número de suscriptores')
plt.xticks(rotation=45, ha='right')  # Rotar los nombres de los Youtubers para mejor legibilidad
plt.tight_layout()  # Ajustar el layout para evitar que se corte el texto

plt.show()
