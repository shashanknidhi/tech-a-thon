import streamlit as st
import os
from PIL import Image
st.write(""" # Dashboard 
Displays Threats 
""")



def display_images(images):
    # st.write(
    #     """
    #     <style>
    #     .row-container {
    #         display: flex;
    #         flex-wrap: wrap;
    #         justify-content: center;
    #         margin-bottom: 20px;
    #     }
    #     .column-container {
    #         flex-basis: 30%;
    #         margin-right: 10px;
    #         margin-bottom: 10px;
    #     }
    #     .column-container:last-child {
    #         margin-right: 0;
    #     }
    #     .column-container img {
    #         width: 100%;
    #         height: auto;
    #     }
    #     </style>
    #     """
    # )

    # st.write('<div class="row-container">')

    for image in images:
        # st.write('<div class="column-container">')
        st.image(image, use_column_width="auto")
        # st.write('</div>')

    # st.write('</div>')

# Specify the folder path containing the images
folder_path = "output"

# Get the list of image files in the folder
image_files = [f for f in os.listdir(folder_path) if f.endswith((".jpg", ".jpeg", ".png"))]

# Read and store the images
images = [Image.open(os.path.join(folder_path, image_file)) for image_file in image_files]

# Display the images
display_images(images)

import streamlit as st
import pandas as pd
tab1, tab2 = st.tabs(['tab1',"tab2"])
with tab1:
    display_images(images)
with tab2:
    df = pd.read_csv('blocked.csv')
    st.dataframe(df['ip.src']) 