import pandas as pd
import streamlit as st
import plotly as px
import matplotlib.pyplot as plt
dig = pd.read_csv("uso_digitales_FINAL.csv")

dig["Marca temporal"]=pd.to_datetime(dig["Marca temporal"])

marca=dig.groupby(dig["Marca temporal"].dt.to_period("M")).size().reset_index(name="cantidad")
st.write(marca)

fig = plt.plot(marca["Marca temporal"], marca["cantidad"])
fig.show()

