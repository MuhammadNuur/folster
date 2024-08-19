""" Main Module for main App """
# import time
import streamlit as st
from streamlit_folium import st_folium
from PIL import Image

import modd.folium_mod as folmap
import modd.streamlit_mod as stmod





img = Image.open('docs/inu.png')
st.set_page_config(page_title="Simulasi Doang",
        page_icon=img,
        layout="wide",
        menu_items=None)



stmod.goes_wild()
