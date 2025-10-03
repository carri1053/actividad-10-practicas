import streamlit as st
import pandas as pd

import streamlit as st
import matplotlib.pyplot as plt


lagos = pd.read_csv('ar-airports.csv')
st.title("Gráfico")
fig,ax = plt.subplots()
# Crear el gráfico de barras
conteo_tipos = lagos['type'].value_counts()
conteo_tipos.plot(kind='bar', ax=ax, color='skyblue')
# Agregar etiquetas y título
ax.set_xlabel('Tipos de aeropuertos')
ax.set_ylabel('Cantidad')
ax.set_title('Cantidad de aerpuertos por provincia')

# Mostrar el gráfico
st.pyplot(fig)
