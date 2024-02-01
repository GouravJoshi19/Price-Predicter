import pickle
import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(
    page_title="Diamond Price Predictor",
    page_icon="💎",
    layout="centered",
    initial_sidebar_state="collapsed"
)
st.title("Diamond Price Predicter")
st.markdown("""This is a machine learning model which predicts the price of a diamond.
            The features used here are **Carat** **Length** **Width** and **Depth** of the Diamond""")
model=pickle.load(open("./diamond.pkl",'rb'))
data = pd.read_csv("./diamonds.csv")
st.sidebar.title("Input Features")
carat = st.sidebar.selectbox("Carat",options=data['carat'].sort_values().unique(),index=None)
length = st.sidebar.slider("Length(in mm)",float(data['x'].min()),float(data['x'].max()),float(data['x'].mean()))
width = st.sidebar.slider("Width(in mm)",float(data['y'].min()),float(data['y'].max()),float(data['y'].mean()))
depth = st.sidebar.slider("Depth(in mm)",float(data['z'].min()),float(data['z'].max()),float(data['z'].mean()))
result=''
input_features=[carat,length,width,depth]
st.header("The features selected are:")
st.write(pd.DataFrame(input_features))
if st.button('Predict'):
       if any(Value is None for Value in input_features):
           st.warning("Please Select All The Features")
       else:
            result=model.predict([[carat,length,width,depth]])
            st.success(f'the price of the diamond is:${result[0]:.2f}')
st.markdown("""----""")              
st.markdown("""Made by :heart: Gourav Joshi""")
     
