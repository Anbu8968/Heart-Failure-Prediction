import pickle
import streamlit as st

from PIL import Image


with open('Heart_failure_pickle_model', 'rb') as file:
    loaded_model = pickle.load(file)
#print(loaded_model.predict([[75.0,0,582,0,20,1,26500,1.9,130,0]]))
st.title("HEART FAILURE PREDICTION")

#st.image("heart_background.png",width=1000,use_column_width=20000)

st.sidebar.subheader("PARAMETERS")

age=st.sidebar.slider("Age",1,100)

anaemi=st.sidebar.radio("Anaemia",("Yes","No"))
anaemia=0
if anaemi=="Yes":
    anaemia=1
    
creatine_phosphokinase=st.sidebar.number_input("Creatine Phosphokinase")

diabete=st.sidebar.radio("diabetes",("Yes","No"))
diabetes=0
if diabete=="Yes":
    diabetes=1
    
ejection_fraction=st.sidebar.number_input("Ejection Fraction")

high_bp=st.sidebar.radio("BP",("Yes","No"))
high_BP=0
if high_bp=="Yes":
    high_BP=1

platelets=st.sidebar.number_input("Platelets")

serum_creatinine=st.sidebar.number_input("Serum_Creatinine")

serumsodium=st.sidebar.number_input("Serumsodium")

smokin=st.sidebar.radio("Smoking",("Yes","No"))
smoking=0
if smokin=="Yes":
    smoking=1


output=loaded_model.predict([[age,anaemia,creatine_phosphokinase,diabetes,ejection_fraction,high_BP,platelets,serum_creatinine,serumsodium,smoking]])

if st.sidebar.button("Predict"):
    if output==[1]:
        st.image("heart-failure.jpg",width=400,use_column_width=300)
        st.subheader("...........................Death conform da Sambu Mavanae!!!! ")
    else:
        st.image("heart_fail.jpg",width=400,use_column_width=300)
        st.subheader("...............You are safe da Sambu Mavanae............")


import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('13up.png')    



hide="""
<style>
#MaimMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}
</style>
"""
st.markdown(hide,unsafe_allow_html=True)