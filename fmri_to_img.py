import streamlit as st
from st_clickable_images import clickable_images
from PIL import Image

import base64
import urllib.request


with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


st.markdown("<h1 style='text-align: center; color: white;'>Deep Image Reconstruction of Human Brain Activity</h1>", unsafe_allow_html=True)

def img_to_64(im_path):
    with open(im_path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read())
    return b64_string


st.markdown("<h2 style='text-align: center; color: grey;'>Select Stimulus Image </h2>", unsafe_allow_html=True)

CLICKED = 0
INT_TO_CONSTRUCTED = {0:'Surfing', 1:'Bathroom', 2:'Pizza'}
INT_TO_IMNAME = {0:'surf', 1:'bathroom', 2:'pizza'}

LINKS = {'Surfing':'https://github.com/connor11son/tmp_sl_data/blob/main/sl_data/18374_generated.jpg',
        'Bathroom':'https://github.com/connor11son/tmp_sl_data/blob/main/sl_data/18487_generated.jpg',
        'Pizza':'https://github.com/connor11son/tmp_sl_data/blob/main/sl_data/18659_generated.jpg'}

clicked = clickable_images(
    [
        "https://github.com/connor11son/tmp_sl_data/blob/main/sl_data/surf.jpg?raw=true",
        "https://github.com/connor11son/tmp_sl_data/blob/main/sl_data/bathroom.jpg?raw=true",
        "https://github.com/connor11son/tmp_sl_data/blob/main/sl_data/pizza.jpg?raw=true",
    ],
    titles=[['Surfing', 'Bathroom', 'Pizza']],
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "5px", "height": "200px"},
)


if clicked < 0:
    st.markdown("<h2 style='text-align: center; color: grey;'>Model's Reconstruction of {} </h2>".format(INT_TO_CONSTRUCTED[CLICKED]), unsafe_allow_html=True)
    img = Image.open('sl_data/{}_gen.jpg'.format(INT_TO_IMNAME[CLICKED]))
    #st.image(img, caption = 'Recreated Image')
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        st.write("")

    with col2:
        st.image(img)

    with col3:
        st.write("")
else:
    st.markdown("<h2 style='text-align: center; color: grey;'>Model's Reconstruction of {} </h2>".format(INT_TO_CONSTRUCTED[clicked]), unsafe_allow_html=True)
    img = Image.open('sl_data/{}_gen.jpg'.format(INT_TO_IMNAME[clicked]))
    #st.image(img, caption = 'Recreated Image')
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        st.write("")

    with col2:
        st.image(img)

    with col3:
        st.write("")