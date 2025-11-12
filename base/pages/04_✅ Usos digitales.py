import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
fig,ax = plt.subplots()
dig = pd.read_csv("uso_digitales_FINAL.csv")
st.title("Uso de redes sociales de los jovenes")
st.write("Los datos surgen de una encuesta que se hizo a los jovenes de la tecnica 9 sobre el tiempo de uso de las redes sociales. Esta encuesta se reealizo en los años 2024/25")
st.write("En este grafico se muestra la cantidad de edades que se recopiló en la encuesta, en esta encuesta la edad de 18 años es la que mayor cantidad tiene")


fig1,ax = plt.subplots()
# Crear el gráfico de barras
conteo_edad = dig['Edad'].value_counts()
conteo_edad.plot(kind='pie', ax=ax)

ax.set_label('Edad')
ax.set_title('Edades de los jóvenes que usan las redes sociales')

with st.expander("En este grafico vemos las edades de los jovenes que usan las redes sociales"):
     st.pyplot(fig)

fig,ax = plt.subplots()
genv = dig[dig["Género"]== "Varón"]
vi = genv["youtube"].value_counts()
vi.plot(kind='pie', ax=ax)

ax.set_title('Uso de la app de youtube en los chicos')

with st.expander("Grafico de Youtube en los chicos de la encuesta"):
     st.pyplot(fig)

fig,ax = plt.subplots()
genv = dig[dig["Género"]== "Varón"]
vi = genv["twiter"].value_counts()
vi.plot(kind='pie', ax=ax)

ax.set_title('Uso de la app de twiter en los chicos')

with st.expander("Grafico de twiter en los chicos de la encuesta"):
     st.pyplot(fig)
     
fig,ax = plt.subplots()
genv = dig[dig["Género"]== "Varón"]
vi = genv["tiktok"].value_counts()
vi.plot(kind='pie', ax=ax)

ax.set_title('Uso de la app de tiktok en los chicos')

with st.expander("Grafico de tiktok en los chicos de la encuesta"):
     st.pyplot(fig)
     
