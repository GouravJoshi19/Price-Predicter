import pickle
import streamlit_app as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Loading the Data set and pickle model
model=pickle.load(open("./diamond.pkl",'rb'))
data = pd.read_csv("./diamonds.csv")



st.set_page_config(
    page_title="Diamond Price Predictor",
    page_icon="💎",
    layout="centered",
    initial_sidebar_state="collapsed"
)


st.title(":orange[Diamond Price Predicter]")
st.subheader("This is a machine learning model That predicts the price of a Diamond.")
st.header(":orange[Description about the Dataset]")
st.write("## Features ")
st.markdown("""1.**Carat** -> Weight of the diamond, a significant factor in determining its value. \n\n
2.**Cut(Quality)** -> Quality of cut(Fair, Good, Very Good, Premium, Ideal).\n\n
3.**Color** -> Grading of the diamond's color, ranging from D (colorless) to Z (light yellow or brown).\n\n
4.**Clarity** -> Measurement of Transparency(how clear the Diamond is).\n\n
                Sequence of clarity ( I1 (worst quality), SI2, SI1, VS2, VS1, VVS2, VVS1, IF(best quality) ).\n\n
5.**Depth**(total depth percentage) -> can be calculated using the formula below:- \n\n
             z / mean(x, y) = 2 * z / (x + y)     \n\n
6.**Length** -> Length of Diamond in mm. \n\n
7.**Width** -> Width of Diamond in mm. \n\n
8.**Depth** -> Depth of Diamond in mm.\n\n
""")

#Histogram
st.write("## Carat distribution within the Data")
sns.histplot(Data=data,x=data['carat'],bins=20,color='Green',kde=True)
plt.title('Carat Distribution')
st.pyplot()

#Relation of Carat with the Target Feature
st.write("## Relation between Carat and Price")
sns.scatterplot(Data=data,x=data['carat'],y=data['price'],color='Yellow')
plt.title('Carat-Price')
st.pyplot()

#Relation of various Parameters with Target Fetaure
parameter=st.selectbox("Parameter",options=['Length','Width','Depth'])
def name(string):
     if(string=='Length'):
          sns.scatterplot(Data=data,x=data['x'],y=data['price'],hue=data['y'])
          plt.title('Length-Price')
          st.pyplot()
     elif(string=='width'):
          sns.scatterplot(Data=data,x=data['y'],y=data['price'],hue=data['z'])
          plt.title('Width-Price')
          st.pyplot()
     elif(string=='Depth'):
          sns.scatterplot(Data=data,x=data['z'],y=data['price'],hue=data['x'])
          plt.title('Depth-Price')
          st.pyplot()

name(parameter)

st.sidebar.title("Input Features")
cut_label={'Fair':0, 'Good':1, 'Very Good':2, 'Premium':3, 'Ideal':4}
color_label={'J':0, 'I':1, 'H':2, 'G':3, 'F':4, 'E':5, 'D':6}
clarity_label={'I1':0, 'SI2':1, 'SI1':2, 'VS2':3, 'VS1':4, 'VVS2':5, 'VVS1':6, 'IF':7}
carat = st.sidebar.selectbox("Carat",options=data['carat'].sort_values().unique(),index=None)
cut = st.sidebar.selectbox("Cut",tuple(cut_label.keys()),index=None)
color =st.sidebar.selectbox("Color",tuple(color_label.keys()),index=None)
clarity = st.sidebar.selectbox("Clarity",tuple(clarity_label.keys()),index=None)
Depth_ratio = st.sidebar.slider("Depth Ratio",float(data['depth'].min()),float(data['depth'].max()),float(data['depth'].mean()))
Length = st.sidebar.slider("Length(in mm)",3.73,10.74,float(data['x'].mean()))
Width = st.sidebar.slider("Width(in mm)",3.68,10.54,float(data['y'].mean()))
Depth = st.sidebar.slider("Depth(in mm)",1.07,6.98,float(data['z'].mean()))
features=[carat,cut,color,clarity,Depth_ratio,Length,Width,Depth]
Data={
     'carat':carat,
     'cut':cut,
     'color':color,
     'clarity':clarity,
     'depth_ratio':Depth_ratio,
     'length':Length,
     'width':Width,
     'depth':Depth
}
result=''
input_feature=pd.DataFrame(Data,index=[0])
st.header(":orange[Values  of the selected Features:]")
st.write(input_feature)
value=''

def get_keys(val,my_dict):
     for key,value in my_dict.items():
          if val==value:
               return key

def get_value(val,my_dict):
     for key,value in my_dict.items():
          if val==key:
               return value
new_cut=get_value(cut,cut_label)
new_color=get_value(color,color_label)
new_clarity=get_value(clarity,clarity_label)
final_data=[carat,new_cut,new_color,new_clarity,Depth_ratio,Length,Width,Depth]                 
if st.button('Predict'):
       if any(Value is None for Value in features):
           st.warning("Please Select All The Features")
       else:
            result=model.predict([final_data])
            if (result<0):
                 st.warning(f'${result[0]:.2f} OOPS!.. This is Something Unusual  \n\n please try again')
            else:
                st.success(f'the price of the diamond is:${result[0]:.2f}')
st.markdown("""----""")              
st.markdown("""💎 Made by  Gourav Joshi💎 """)
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
     
