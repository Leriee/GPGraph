
import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import base64

import streamlit.components.v1 as components

st.set_page_config(layout='wide')
c_left, c_right = st.columns(2)
with c_left:
    HtmlFile = open("Graph.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code, height= 600, width=650)


dff = pd.read_csv('applied.csv')


with c_right:
    dff = pd.read_csv('applied.csv')
    
    st.write(dff, unsafe_allow_html=True)