import streamlit as st
st.title("🎈 Selamat Datang, Selamat menghitung")
st.write("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")

import streamlit as st
st.write("Fighting, *Semuanya!* :sunglasses:")

import streamlit as st
number = int(st.number_input("Insert a number",min_value=None, max_value=None,))
if number%2==1:
    st.write("Bilngan",number,"termasuk bilangan ganjil")
else:
    st.write("Bilngan",number,"termasuk bilangan genap")
