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
st.title(":orange[Diamond Price Predicter]")
st.subheader("This is a machine learning model That predicts the price of a Diamond.")
st.header(":orange[Description about the input features]")
st.markdown("""1.**Carat** -> Weight of the diamond, a significant factor in determining its value. \n\n
2.**Cut(Quality)** -> Quality of cut(Fair, Good, Very Good, Premium, Ideal).\n\n
3.**Color** -> Grading of the diamond's color, ranging from D (colorless) to Z (light yellow or brown).\n\n
4.**Clarity** -> Measurement of Transparency(how clear the Diamond is)\n\n
                Sequence of clarity ( I1 (worst quality), SI2, SI1, VS2, VS1, VVS2, VVS1, IF(best quality) ).\n\n
5.**Length** -> Length of Diamond in mm. \n\n
6.**Width** -> Width of Diamond in mm. \n\n
7.**Depth** -> Depth of Diamond in mm.\n\n
""")
model=pickle.load(open("./diamond.pkl",'rb'))
data = pd.read_csv("./diamonds.csv")
st.sidebar.title("Input Features")
carat = st.sidebar.selectbox("Carat",options=data['carat'].sort_values().unique(),index=None)
cut = st.sidebar.selectbox("Cut",options=data['cut'].unique(),index=None)
color = st.sidebar.selectbox("Color",options=data['color'].unique(),index=None)
clarity = st.sidebar.selectbox("Clarity",options=data['clarity'].unique(),index=None)
Length = st.sidebar.slider("Length(in mm)",float(data['x'].min()),float(data['x'].max()),float(data['x'].mean()))
Width = st.sidebar.slider("Width(in mm)",float(data['y'].min()),float(data['y'].max()),float(data['y'].mean()))
Depth = st.sidebar.slider("Depth(in mm)",float(data['z'].min()),float(data['z'].max()),float(data['z'].mean()))
result=''
input_features=[carat,cut,color,clarity,Length,Width,Depth]
st.header(":orange[Values  of the selected Features:]")
st.dataframe(input_features)
if st.button('Predict'):
       if any(Value is None for Value in input_features):
           st.warning("Please Select All The Features")
       else:
            result=model.predict([[carat,cut,color,clarity,Length,Width,Depth]])
            if (result<0):
                 st.warning(f'${result[0]:.2f} OOPS!.. That is Something Unusual  \n\n please try again')
            else:
                st.success(f'the price of the diamond is:${result[0]:.2f}')
st.markdown("""----""")              
st.markdown("""Made by :heart: Gourav Joshi""")
     
