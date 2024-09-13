import streamlit as st
import google.generativeai as genai
from PIL import Image

st.title("Hello")
st.subheader(" ",divider='rainbow')

uploaded_file = st.file_uploader("Upload Files", type=["jpg", "jpeg", "png"])
genai.configure(api_key=st.secrets.GOOGLE_API_KEY)

image = Image.open(uploaded_file)
# st.image(image, caption='Uploaded Image', use_column_width=True)
col1, col2, col3 = st.columns([1, 2, 1])  # Adjust the width ratio as needed
with col2:
    st.image(image, use_column_width=True)

# Generate a prompt for the generative model
pmt = """ Analyze the image and determine if it shows a part of a mobile tower. If it does, provide a descriptive name for the component. If not, respond with 'Not a part of a mobile tower.'
circular antenna - are circular in nature also known as microwave dish

"""

# Initialize and use the generative model for the image
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# btn = st.button("PREDICT")

if uploaded_file:
    response = model.generate_content([pmt, image])
    st.write(response.text)