import pyshorteners.exceptions
import streamlit as st
import pyshorteners
import qrcode
from io import BytesIO

s = pyshorteners.Shortener()

st.header('URL Shortener')

# Initialize session state variables
if 'url_output' not in st.session_state:
    st.session_state.url_output = ''

if 'url_input' not in st.session_state:
    st.session_state.url_input = ''

if 'qr_code_img' not in st.session_state:
    st.session_state.qr_code_img = ''

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
        # Generate qr code from the shortened url
        qr_image = qrcode.make(st.session_state.url_output)
        img_bytes = BytesIO()
        # Store the image as a png
        qr_image.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        # Set the session state of the image widget
        st.session_state.qr_code_img = img_bytes
    except pyshorteners.exceptions.ShorteningErrorException:
        st.text('Bad URL, try another!')
    # The following usually occurs when an empty string is given
    except pyshorteners.exceptions.BadURLException:
        pass

# Display code block and image for URL output when url is generated
if st.session_state.url_output:
    st.code(st.session_state.url_output)
    st.image(st.session_state.qr_code_img, 
            caption=st.session_state.url_output)