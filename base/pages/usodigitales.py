import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
fig,ax = plt.subplots()
dig = pd.read_csv("uso_digitales_FINAL.csv")
st.title("Uso de redes sociales de los jovenes")



fig,ax = plt.subplots()
# Crear el gráfico de barras
conteo_tipos = dig['Edad'].value_counts()
conteo_tipos.plot(kind='pie', ax=ax, color='skyblue')

with st.expander("En este graficos vemos las edades de los jovenes que usan las redes sociales"):
     st.pyplot(fig)