import streamlit as st
import pyshorteners

s = pyshorteners.Shortener()

st.header('URL Shortener')

if "url_output" not in st.session_state:
    st.session_state.url_output = ''

def shorten_url(url: str) -> str:
    try:
        short_url = s.tinyurl.short(url)
        return short_url
    except Exception as e:
        return f'Error: {str(e)}'

def change_url_text(url):
    st.session_state

url_input = st.text_input(label='URL:', value='')

# Initiate a variable with a sessionstate
url_output = st.session_state.url_output
st.code(url_output)

if st.session_state.get('shorten'):
    st.session_state.url_output = shorten_url(url_input)
    st.rerun()

st.button('Shorten', key='shorten')
# url_output = st.text_input(label='Shortened URL: ', disabled=True, placeholder='Short URL', value=st.session_state.url_output)