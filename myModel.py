import streamlit as st
st.title("first render plateform model")
tv_input = st.number_input("TV",min_value=0,max_value = 1000, step = 1)
radio_input =st.number_input("Radio",min_value=0,max_value = 1000, step = 1)
newpaper_input =st.number_input("newPaper",min_value=0,max_value = 1000, step = 1)
import pickle as pkl
file1=open("preprocessor_1.pkl","rb")
sc = pkl.load(file1)
file2=open("model.pkl","rb")
model_1 = pkl.load(file2)
input1 = sc.transform([[tv_input,radio_input,newpaper_input]])

if st.button("Predict"):
    pred = model_1.predict(input1)
    st.text(pred)