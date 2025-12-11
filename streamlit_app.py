import streamlit as st
st.title("🎈 Selamat Datang, Selamat menghitung")
st.write("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")

import streamlit as st
st.write("Fighting, *Semuanya!* :sunglasses:")

import streamlit as st
st.title("This is a title")
st.title("_Streamlit_ is :blue[cool] ")

import streamlit as st
col1, col2, col3 = st.columns(3)
with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")
with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")
with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
