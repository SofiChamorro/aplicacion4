import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image


st.title("Reconocimiento óptico de Caracteres")
st.image(
    "https://www.adobe.com/es/acrobat/resources/media_1e63dcac97bdfbfd1991836a2fb31d4fba4312d83.png?width=1200&format=pjpg&optimize=medium",
    caption="Ejemplo de extracción de texto con OCR",
    use_column_width=True
)

img_file_buffer = st.camera_input("Toma una Foto")

with st.sidebar:
      filtro = st.radio("Aplicar Filtro",('Con Filtro', 'Sin Filtro'))


if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    
    if filtro == 'Con Filtro':
         cv2_img=cv2.bitwise_not(cv2_img)
    else:
         cv2_img= cv2_img
    
        
    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    text=pytesseract.image_to_string(img_rgb)
    st.write(text) 
    

