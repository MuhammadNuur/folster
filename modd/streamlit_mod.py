""" Main Streamlit Module """
# import module
import streamlit as st
from streamlit_folium import st_folium
import time
import folium_mod as folmap

st.set_page_config(layout="wide")

def goes_wild():
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
    st.title("Hello GeeksForGeeks !!!")
    st.header('ini adalah HEADER')


    # st_data = st_folium(folmap.map, width=500)

    col1, col2, col3 = st.columns([1,2,1])

    with col1:
        st.markdown('# Selamat Datang di WebApp ini..')
        st.write('ini adalah kolom 1')

    with col2 :
        container1 = st.container(border=True)
        with container1:
            st_data = st_folium(folmap.map, width=640)

    with col3 :
        container = st.container(border=True)
        container.write("This is inside the container")


def main() -> None:
    goes_wild()


if __name__ == "__main__":
    main()
