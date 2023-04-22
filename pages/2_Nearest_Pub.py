import streamlit as st
import pandas as pd
import numpy as np
import os

# Title
st.header("Find Your Local Pub🍸")


ABS = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(ABS,os.pardir) #Parent dir
RES_DIR = os.path.join(FILE_DIR, "resources")
CSV = os.path.join(RES_DIR,"data", "cleaned_open_pubs.csv")
df = pd.read_csv(CSV)




if st.button('Note(Range)'): 
    st.markdown('''
                    Latitude: (49.892485, 60.764969) \n
                    Longitude: (-7.384525, 1.757763) 
                ''')
    
# LAT and LONG Input
c1,c2=st.columns(2)
with c1:
    lat=st.number_input(label="Latitude", min_value=49.892485, max_value=60.764969)
with c2:
    long=st.number_input(label="Longitude", min_value=-7.384525, max_value=1.757763)


findLoc=np.array((lat,long))

og_loc=np.array([df['latitude'],df['longitude']]).T #transposes the 2D array


# Now to Find Euclidean dist and save it as a new feature in df
dist=np.sum((og_loc-findLoc)**2, axis=1)
df['dist']=dist

# Now to find nearest 5 PUBS
data=df.sort_values(by='dist', ascending=True)[:5]

#List of Bar Names
st.subheader(f":Blue[Pubs Found more details below :point_down:]")

#Show Nearest Pubs on Map
st.map(data=data, zoom=None, use_container_width=True)

#Name and Address of Nearby Pubs
st.table(data[['fsa_id','name','address','dist']])