import pickle
import streamlit as st
import pandas as pd
import numpy as np
st.title("Diamond Price Predicter")
model=pickle.load(open("./diamond.pkl",'rb'))
data = pd.read_csv("./diamonds.csv")
carat = st.selectbox("Carat",data['carat'].unique(),index=None)
cut= st.selectbox("cut",data['cut'].unique(),index=None)
length = st.selectbox("length",data['x'].unique().astype(float),index=None)
width = st.selectbox("width",data['y'].unique().astype(float),index=None)
depth = st.selectbox("depth",data['z'].unique().astype(float),index=None)
result=''
if st.button('Predict'):
    result=model.predict([[carat,cut,length,width,depth]])
st.success(result)
