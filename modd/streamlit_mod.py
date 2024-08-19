""" Main Streamlit Module """
# import module
import time
import streamlit as st

from PIL import Image
from streamlit_folium import st_folium

import modd.folium_mod as folmap
# Wide Layout dipanggil di halaman MAIN.py

def goes_wild():
    ''' Running Streamlit fuction '''
    # # Sidebar
    # with st.sidebar:
    #     st.sidebar.header("this is a sidebar")
    #     st.divider()
    #     st.subheader("My sub")
    #     st.code("for i in range(8): foo()")
    #     st.html("<p>Hi!</p>")

    #     teks2 = st.text_input('Isi String :')
    #     # st.write(f'isian input :{teks2}')
    #     st.divider()

    # Body
    st.title("Monitoring Sistem MMU")
    st.write('Dashboard ini menyajikan informasi terkini mengenai status kesehatan aset, ' +\
             'pemeliharaan, dan kinerja sistem kelistrikan PLN UIW MMU')

    box_map = st.container(border=True, height=500)
    with box_map :
        st_folium(folmap.map, height= 470, use_container_width=True)

def main() -> None:
    ''' Running Lokal di Modul ini '''
    goes_wild()


if __name__ == "__main__":
    main()
