import pandas as pd
import streamlit as st

air =  pd.read_csv('ar-airports.csv')
st.title("Parte 1")
st.header("Datos que encontramos")
st.write("La información que encotramos en el dataset de aeropuertos Argentinos son:")
st.write("Los tipos de aeropuertos que hay en Argentina son: aeropuertos de globos, de helicópteros, grandes, medianos, pequeños y los aeropuertos que fueron cerrados. El dataset también muestra los nombres y la cantidad total de aeropuertos que hay. Además, se incluye la ubicación del aeropuerto según las coordenadas y su página web, si es que la tiene.")

with st.expander("¿Cuántas filas y columnas tiene el dataset?"):
    filas, columnas = air.shape
    st.write(f'Tiene { filas} filas y {columnas} columnas')
    
    
nombres_ubic = air['type'].unique()
type_air = len(air['type'].unique())

with st.expander("¿Cuántos son los valores únicos de la columna **type**?"):
    st.write(type_air)
with st.expander("¿Cuáles son los valores únicos de la columna **type**?"):
    st.write(nombres_ubic)
with st.expander("¿Cuales son los nombres de las columnas?"):
   
    st.write(air.columns)