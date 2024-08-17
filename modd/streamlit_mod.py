""" Main Streamlit Module """
# import module
import streamlit as st
from streamlit_folium import st_folium
import time
import modd.folium_mod as folmap

# Wide Layout dipanggil di halaman MAIN.py

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

    col1, col2 = st.columns([1,4])

    with col1:
        st.markdown('# Selamat Datang di WebApp ini..')
        st.write('ini adalah kolom 1')
        st.image("docs/inu.png")

    with col2 :
        container1 = st.container(border=True, height=500)
        with container1:
            # st_data = st_folium(folmap.map, width=720, height=300)
            st_data = st_folium(folmap.map, height= 450, use_container_width=True)
            st.write('ini adalah kolom 2')


def main() -> None:
    goes_wild()


if __name__ == "__main__":
    main()
