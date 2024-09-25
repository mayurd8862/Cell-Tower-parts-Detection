import streamlit as st
import cv2
from ultralytics import YOLO
import numpy as np
from PIL import Image

# Load the trained model
model = YOLO('./runs/detect/train/weights/last.pt')  # Path to your trained model

# Streamlit app
st.title('🗼 Mobile Tower Components Detection')

st.write('Upload an image to perform object detection.')

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

btn = st.button("Analyze")
if btn and uploaded_file is not None:
    # Read the image file
    with st.spinner("Please wait analyzing Image"):
        image = Image.open(uploaded_file).convert("RGB")
        # Convert image to a format that OpenCV can handle
        img_np = np.array(image)
        img = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

        # Run detection
        results = model(img)

        # Draw bounding boxes on the image
        annotated_img = results[0].plot()
        annotated_img_rgb = cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB)
        st.image(annotated_img_rgb, caption='Detected Image', use_column_width=True)

