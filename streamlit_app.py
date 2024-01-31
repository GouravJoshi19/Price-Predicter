import pickle
import streamlit as st
import pandas as pd
st.title("Diamond Price Predicter")
model=pickle.load(open('E:\deployment\diamond.pkl','rb'))
data = pd.read_csv("./diamonds.csv")
carat=st.selectbox("Carat",data["carat"],index=None)
cut=st.selectbox("cut",data["cut"],index=None)
color=st.selectbox("color",data["color"],index=None)
clarity=st.selectbox("clarity",data["clarity"],index=None)
length=st.selectbox("length",data["x"],index=None)
width=st.selectbox("width",data["y"],index=None)
depth=st.selectbox("depth",data["z"],index=None)
result=''
if st.button('Predict'):
    result=model.predict([[carat,cut,color,clarity,length,width,depth]])[0]
st.success(result)
