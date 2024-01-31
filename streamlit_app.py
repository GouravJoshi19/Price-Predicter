import pickle
import streamlit as st
import pandas as pd
st.title("Diamond Price Predicter")
model=pickle.load(open("E:\deployment\diamond.pkl",'rb'))
data = pd.read_csv("./diamonds.csv")
carat=st.text_input("Carat")
cut=st.text_input("cut")
length=st.text_input("length")
width=st.text_input("width")
depth=st.text_input("depth")
result=''
if st.button('Predict'):
    result=model.predict([[carat,cut,length,width,depth]])[0]
st.success(result)
