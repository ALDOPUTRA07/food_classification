import streamlit as st

from streamlit_app.utils.ui import header_description, result, sidebar
from streamlit_app.utils.utils import process

# fastapi endpoint
url = "http://127.0.0.1:8000"
endpoint = "/predict"

# Sidebar
sidebar()

# UI
header_description()

st.divider()

image = st.sidebar.file_uploader(
    "insert image", type=["png", "jpg"]
)  # image upload widget

if image is not None:
    button_classification = st.sidebar.button("Classify image", type="primary")

    col1, col2 = st.columns([3, 2])

    with col1:
        st.subheader("Image")
        st.image(image)

    if button_classification:
        segments = process(image, url + endpoint)

        with col2:
            results = result(segments)
