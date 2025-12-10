import streamlit as st

st.set_page_config(page_title="My Streamlit Test", layout="centered")

st.title("My First Streamlit Webpage")
st.write("Hello — this is deployed from a fresh GitHub repo to Streamlit Cloud.")

st.write("Click the sidebar to navigate to Page 2 b, or use the external link below:")

st.markdown(
    '<a href="https://aravisg.github.io/test1/Page2.html" target="_blank">Open Page 2 in new tab</a>',
    unsafe_allow_html=True
)
