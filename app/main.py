import tempfile
import streamlit as st

st.write("""
    # Bad Boy Records V2
""")


uploaded_file = st.file_uploader("Upload an song", type=['wav','mp3'])
if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/wav")

    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())