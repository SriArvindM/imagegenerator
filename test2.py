import streamlit as st
import requests
import io
from PIL import Image

# API details
API_URL = "https://api-inference.huggingface.co/models/stabilityai/sdxl-turbo"
headers = {"Authorization": "Bearer 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"}
import base64

def get_img_as_base64(file):
    with open(file,"rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
img = get_img_as_base64("man.avif")

page_bg_img = f"""

<style>
[data-testid="stAppViewContainer"] > .main {{
background-image :url("data:image/avif;base64,{img}");
background-size : cover;
}}
[data-testid="stHeader"]{{
background:rgba(0,0,0,0);
}}
</style>

"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Function to make a request to the API
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# Streamlit app
st.title(":red[AI Image Generator]")

# Get user input for the image description
user_input = st.text_input(":red[Enter a description for the image]")

# Generate the image when the user clicks the button
if st.button("Generate Image"):
    image_bytes = query({"inputs": user_input})
    
    # Display the generated image
    image = Image.open(io.BytesIO(image_bytes))
    st.image(image, caption=f"Generated Image: {user_input}")
