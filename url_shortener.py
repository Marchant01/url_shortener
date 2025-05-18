import pyshorteners.exceptions
import streamlit as st
import pyshorteners

s = pyshorteners.Shortener()

st.header('URL Shortener')

# Initialize session state variables
if 'url_output' not in st.session_state:
    st.session_state.url_output = ''

if 'url_input' not in st.session_state:
    st.session_state.url_input = ''

# Text input for URL
url_input = st.text_input(label='Enter URL here:', 
                          value='', 
                          placeholder='http://example.url.com',
                          key='url_input')

# Shorten URL button
shorten_pressed = st.button('Shorten')

# Update session state if button is pressed
if shorten_pressed:
    # Try to shorten URL, changes the url_output session state and handles exceptions
    if st.session_state.url_input == '':
        st.text('Please enter a URL!')    
    try:
        st.session_state.url_output = s.tinyurl.short(st.session_state.url_input)
    except pyshorteners.exceptions.ShorteningErrorException:
        st.text('Bad URL, try another!')
    # The following usually occurs when an empty string is given
    except pyshorteners.exceptions.BadURLException:
        pass

# Code block for URL output
st.code(st.session_state.url_output)