""" Main Streamlit Module """
# import module
import streamlit as st
import time

def goes_wild():
    # Sidebar
    with st.sidebar:
        st.sidebar.header("this is a sidebar")
        st.divider()
        st.subheader("My sub")
        st.code("for i in range(8): foo()")
        st.html("<p>Hi!</p>")

        teks2 = st.text_input('Isi String :')
        # st.write(f'isian input :{teks2}')
        st.divider()


    # Body
    st.title("Hello GeeksForGeeks !!!")
    st.header('ini adalah HEADER')
    st.markdown('## ini adalah h2 Header')

    st.divider()
    st.caption('Ini adalah Caption')

    # Input
    st.write('st.text_input')
    teks1 = st.text_input('Tulis isian teks ke dalam inputan di bawah ini :')
    st.write(f'disini mirror isian dari input :{teks1}') 
    st.divider()

    st.write("Most objects") # df, err, func, keras!
    st.text("Fixed width text")
    st.markdown("_Markdown_") # see *
    st.latex(r""" e^{i\pi} + 1 = 0 """)
    st.title(teks2)

    col1, col2 = st.columns(2)

    with col1:
        with st.spinner(text="In progress"):
            time.sleep(3)
            st.success("Done")

        # Show and update progress bar
        bar = st.progress(10)
        time.sleep(3)
        bar.progress(100)

        with st.status("Authenticating...") as s:
            time.sleep(2)
            st.write("Some long response.")
            s.update(label="Response")

        st.balloons()
        st.snow()
        st.toast("Warming up...")
        st.error("Error message")
        st.warning("Warning message")
        st.info("Info message")
        st.success("Success message")
        # st.exception(e)

    with col2:
        st.button("Click me")
        # st.download_button("Download file", data)
        st.feedback("thumbs")
        # st.link_button("Go to gallery", url)
        # st.page_link("app.py", label="Home")
        # st.data_editor("Edit data", data)
        st.checkbox("I agree")
        st.toggle("Enable")
        st.radio("Pick one", ["cats", "dogs"])
        st.selectbox("Pick one", ["cats", "dogs"])
        st.multiselect("Buy", ["milk", "apples", "potatoes"])
        st.slider("Pick a number", 0, 100)
        st.select_slider("Pick a size", ["S", "M", "L"])
        st.text_input("First name")
        st.number_input("Pick a number", 0, 10)
        st.text_area("Text to translate")
        st.date_input("Your birthday")
        st.time_input("Meeting time")
        st.file_uploader("Upload a CSV")
        st.camera_input("Take a picture")
        st.color_picker("Pick a color")

        # Use widgets' returned values in variables:
        # for i in range(int(st.number_input("Num:"))):
        #     foo()
        # if st.sidebar.selectbox("I:",["f"]) == "f":
        #     b()
        slider_val = st.slider("Quinn Mallory", 1, 88)
        st.write(slider_val)

        # # Disable widgets to remove interactivity:
        # st.slider("Pick a number", 0, 100, disabled=True)



def main() -> None:
    goes_wild()
    

if __name__ == "__main__":
    main()