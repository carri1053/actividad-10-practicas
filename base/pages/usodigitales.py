import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
fig,ax = plt.subplots()
dig = pd.read_csv("uso_digitales_FINAL.csv")
st.title("Uso de redes sociales de los jovenes")
st.write("Los datos surgen de una encuesta que se hizo a los jovenes de la tecnica 9 sobre el tiempo de uso de las redes sociales. Esta encuesta se reealizo en los años 2024/25")
st.write("En este grafico se muestra la cantidad de edades que se recopiló en la encuesta, en esta encuesta la edad de 18 años es la que mayor cantidad tiene")


fig,ax = plt.subplots()
# Crear el gráfico de barras
conteo_edad = dig['Edad'].value_counts()
conteo_edad.plot(kind='pie', ax=ax)

ax.set_label('Edad')
ax.set_title('Edades de los jovenes que usan las redes sociales')

with st.expander("En este grafico vemos las edades de los jovenes que usan las redes sociales"):
     st.pyplot(fig)

varon = dig[dig["instagram"]== "Varón"]
varon.plot(kind='pie', ax=ax, color='skyblue')

ax.set_xlabel('var')
ax.set_ylabel('var')
ax.set_title('Cantidad de aerpuertos por provincia')

with st.expander("A"):
     st.pyplot(fig)