# Imports
import streamlit as st
import os
import pandas as pd
from PIL import Image

# Load data paths
ABS = os.path.dirname(os.path.abspath("__file__"))
CSV = os.path.join(ABS,"resources","data","cleaned_open_pubs.csv")
pub_img = os.path.join(ABS,"resources","image","BestPub.jpg")
df = pd.read_csv(CSV)


# TITLE
st.title(':white[Cheers!🥂 UK Pubs🍺]')


#Page Heading
# st.header("")
st.image(Image.open(pub_img))




#Unique Bars and Local Authorities
bt_lables=['Number of Pubs', 'Number of Local Authorities','Number of Postal Code']

st.subheader("This app will help you find the best PUB for you in UK🍸")


left,right=st.columns(2,gap='small')
with left:
    option=st.radio(label="We have...",
                options=bt_lables, horizontal=False)
    if option=='Number of Pubs':
        right.subheader(f":blue[{df['fsa_id'].nunique()}] Total Pubs")
    elif option=='Number of Local Authorities':
        right.subheader(f":blue[{df['local_authority'].nunique()}] Local Authorities")
    else:
        right.subheader(f":blue[{df['postcode'].nunique()}] Unique Post Codes")

st.subheader(":red[Discover the UK's Pub Culture🥂, Have a great time!🍻]")

# Entire dataset
with st.expander(label='View the data',expanded=False):
     st.dataframe(df)


######################### Links ##########################
st.subheader("Get in touch :point_down:")

c1,c2=st.columns(2,gap='small')
with c1:
    st.subheader("[LinkedIn](https://www.linkedin.com/in/shubhammyadav/)") 
with c2:
    st.subheader("[Github](https://github.com/ZealousGuy)")
