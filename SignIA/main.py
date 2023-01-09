import streamlit as st
from PIL import Image
import cv2
import torch
import numpy as np


def main():
    st.title('YOLOv5 detection panneaux de signalisation')
    image_file = st.file_uploader("choisir une Image", type='png')
    if image_file is not None:
        myImage = Image.open(image_file)
        col1, col2 = st.columns(2)
        with col1:
            st.text("Input : ")
            st.image(myImage)
        if st.button('Analyse'):
            new_img=np. array(myImage.convert('RGB' ))
            img = cv2. cvtColor(new_img,1)
            results = model(img)
            with col2:
                st.text("Output : ")
                st.image(results.render())

if __name__ == '__main__':
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='myYOLO/best.pt', force_reload=True)
    main()
