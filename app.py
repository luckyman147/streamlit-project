import streamlit as st 

import pandas as pd  
import numpy as np
import plost 
from PIL import Image

st.set_page_config(layout="wide")
with open("style.css") as f:

    st.markdown('<style>{}</style>'.format(f.read()),unsafe_allow_html=True)
#data 
seattle_weather=pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')

#Row A
a1,a2=st.columns(2)

a1.metric("Wind","9mph","-8%")
a2.metric("Humidity","86%","4%")
#Row B
b1,b2,b3=st.columns(3)
b1.metric("Pressure","29.9","-2%")
b2.metric("Temp","54F","-2%")
b3.metric("Visibility","10mi","-2%")
#Row C
c1,c2=st.columns((7,3))

with c1:
    st.markdown("### Heatmap ")
    plost.time_hist(data=seattle_weather,
    date='date',
        x_unit="week",
        y_unit='day',
        color='temp_max',
        aggregate='median',legend=None )
with c2:
    st.markdown("### Bar chart")
    plost.donut_chart(data=stocks,theta='q2',color='company')    
