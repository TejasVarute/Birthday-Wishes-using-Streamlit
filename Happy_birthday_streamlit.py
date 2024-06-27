import streamlit as st
import time

def wish(name):
    st.set_page_config(page_title="Happy Birthday Wisher", layout="centered")
    if name:
        img = "./data/img.jpg"

        _,col2,_ = st.columns(3)

        with col2:
            st.image(img, width=250)

        st.subheader('', divider='rainbow')
        st.markdown(f"<h1 style='text-align: center; color: red'>HAPPY BIRTHDAY {name}</h1>", unsafe_allow_html=True)
        st.subheader('', divider='rainbow')

        st.audio("./data/song.mp3", format="audio/wav", start_time=0, autoplay=True, loop=True)

        image_style = '''
            <style>
                h1 {
                    font-size: 3rem;
                    background: linear-gradient(to right, #ef5350, #f48fb1, #7e57c2, #2196f3, #26c6da, #43a047, #eeff41, #f9a825, #ff5722);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                }
                img{
                    border-radius: 20%;
                }
                audio{
                }
            </style>
            '''
        st.html(image_style)
        while(True):
            time.sleep(1.7)
            st.balloons()
wish("SHRIPAD")
