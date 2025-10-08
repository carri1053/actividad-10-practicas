import pandas as pd
import streamlit as st

air =  pd.read_csv('ar-airports.csv')
st.title("Parte 1")
st.header("Datos que encontraron")
st.write("La información que encotramos en el dataset de aeropuertos Argentinos:")
st.write("Los tipos de aeropuertos que tiene son: aeropuertos de globos, helicopteros, grandes, medianos, pequeños y cerrados." \
" El dataset tambien te muestra los Nombres y la cantidad aerpuertos que hay en total . " \
" Esta muestra la ubicacion del aeropuerto según las cordenadas" \
"y su pagina web si es que esta la tiene")

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