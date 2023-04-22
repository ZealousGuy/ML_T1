import streamlit as st
import pandas as pd
import os
from PIL import Image

# TITLE
st.header("Pubs in the UK🍺")

#Load data
ABS = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(ABS,os.pardir) #Parent dir
RES_DIR = os.path.join(FILE_DIR, "resources")
CSV = os.path.join(RES_DIR,"data", "cleaned_open_pubs.csv")
df = pd.read_csv(CSV)


pub_img = os.path.join(RES_DIR,"image","PUB.jpg")
st.image(Image.open(pub_img))



#Display Pub Locations by Zip Code, Local Authority
unique=['All','Post Code', 'Local Authority','Pub Name']

option=st.radio(label="Select from below option to Search Pubs by...",
                options=unique, horizontal=False)

if option=='Post Code':
    selected=st.selectbox(label='Select the ZipCode',options=df['postcode'].unique())
    st.subheader(f"Total Pubs Found : {df[df['postcode']==selected].shape[0]}")
    st.map(data=df[df['postcode']==selected],  use_container_width=True)

elif option=='Pub Name':
    selected=st.selectbox(label='Select the Pub Name',options=df['name'].unique())
    st.subheader(f"Total Pubs Found : {df[df['name']==selected].shape[0]}")
    st.map(data=df[df['name']==selected],  use_container_width=True)

elif option=='Local Authority':
    selected=st.selectbox(label='Select Local Authority',options=df['local_authority'].unique())
    st.subheader(f"Total Pubs Found : {df[df['local_authority']==selected].shape[0]}")
    st.map(data=df[df['local_authority']==selected],  use_container_width=True)

else:
    st.subheader(f"Total Pubs Found : {df.shape[0]}")
    st.map(data=df,  use_container_width=True)