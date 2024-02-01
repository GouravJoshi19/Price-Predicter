import pickle
import streamlit as st
import pandas as pd
import numpy as np
primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"
st.title("Diamond Price Predicter")
model=pickle.load(open("./diamond.pkl",'rb'))
data = pd.read_csv("./diamonds.csv")
carat = st.selectbox("Carat",options=data['carat'].sort_values().unique(),index=None)
length = st.selectbox("length",data['x'].sort_values().unique().astype(float),index=None)
width = st.selectbox("width",data['y'].sort_values().unique().astype(float),index=None)
depth = st.selectbox("depth",data['z'].sort_values().unique().astype(float),index=None)
result=''
input_features=[carat,length,width,depth]
if st.button('Predict'):
           for i in input_features:
             if(i==None):
              st.write("please select all the features")
              break
           else:
              result=model.predict([[carat,length,width,depth]])
              st.write('price is:') 
              st.success(result)
              
     
