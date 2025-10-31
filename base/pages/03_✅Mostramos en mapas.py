import folium
import streamlit as st
from streamlit_folium import folium_static, st_folium
import pandas as pd

def generar_mapa():
    attr = (
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
        'contributors, &copy; <a href="https://cartodb.com/attributions">CartoDB</a>'
    )
    
    tiles = 'https://wms.ign.gob.ar/geoserver/gwc/service/tms/1.0.0/capabaseargenmap@EPSG%3A3857@png/{z}/{x}/{-y}.png'
    m = folium.Map(
        location=(-33.457606, -65.346857),
        control_scale=True,
        zoom_start=5,
        name='es',
        tiles=tiles,
        attr=attr
    )
    return m


air = pd.read_csv('ar-airports.csv')
st.title("Mapa")
st.write("En el mapa se puede ver los tipos de aeropuertos ")
mapa = generar_mapa()

def agregar_marca_aerop(row):
    
    #st.write(color)
    folium.Marker(
        [row['latitude_deg'], row['longitude_deg']],
        popup=row['name'],
        icon=folium.Icon()
        ).add_to(mapa)

ac1,ac2 = st.columns([0.3, 0.7])
air_lar = ac1.checkbox("Grandes")
if air_lar:
    a_larg = air[air['type']=='large_airport']
    a_larg.apply(agregar_marca_aerop, axis=1)
air_mid = ac1.checkbox("Medianos")
if air_mid:
    a_med = air[air['type']=='medium_airport']
    a_med.apply(agregar_marca_aerop, axis=1)
air_small = ac1.checkbox("Pequeños")
if air_small:
    a_small = air[air['type']=='small_airport']
    a_small.apply(agregar_marca_aerop, axis=1)
with ac2:
    st_folium(mapa, key='air')
