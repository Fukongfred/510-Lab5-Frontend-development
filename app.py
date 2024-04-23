import os
import streamlit as st
import google.generativeai as genai  # Assuming you renamed the library for brevity
from dotenv import load_dotenv
import io
import PIL.Image
import google.ai.generativelanguage as glm

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro-vision')

extracted_results = []  

def prepare_image(uploaded_file):
    image = Image.open(uploaded_file)
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')  # Adjust format as needed
    img_byte_arr = img_byte_arr.getvalue()
    return img_byte_arr

def upload_image():
    uploaded_file = st.file_uploader("Upload Your Cloud Photo", type=["jpg", "jpeg", "png"], key="image_uploader")
    return uploaded_file

uploaded_image = upload_image()

if uploaded_image is not None:
    user_response = st.text_input("What do you think the cloud looks like?")

if uploaded_image is not None:
    try:
        # Prepare the image data
        img = PIL.Image.open(uploaded_image)
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')  # Adjust the format if necessary
        img_byte_arr = img_byte_arr.getvalue()
        def process_analysis_text(text):
            # Implement the logic to process the analysis text and extract top 5 items and similarities
            pass
        
        # Create the content object
        content = glm.Content(parts=[
            glm.Part(text="What top 5 things does this cloud resemble?"),  # Your text input
            glm.Part(inline_data=glm.Blob(mime_type='image/png', data=img_byte_arr)),  # Image data
        ])
        
        # Call the generate_content method with the content object
        response = model.generate_content(content)
        analysis_text = response.text
        st.write(analysis_text)

        # Further processing based on your existing code
        extracted_results = process_analysis_text(analysis_text)
        
    except Exception as e:
        st.error(f"An error occurred: {e}")

if extracted_results:
    st.subheader("Top 5 Similarities:")
    for item, similarity in extracted_results:
        st.write(f"- {item}: {similarity}%")