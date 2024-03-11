import pandas as pd
import streamlit as st
from streamlit_chat import message
import random
import time
import re


st.set_page_config(page_title="Medical Insurace Prediction", layout="wide")
left, center, right = st.columns([2,5,1.75])
with left:
    st.title("")
    #add image
    st.header("IMAGE")
with center:
    st.header("")
    st.header("")
    st.header("")
    st.markdown("<h1 style='text-align:center;color:#E2A3F3'>MEDICAL INSURANCE PREDICTIONS</h1>", unsafe_allow_html=True)
with right:
    #filler *DELETE*
    st.header("IMAGE")
    #add image

left,center,right = st.columns([1, 5, 1])
with left:
    visual = st.radio('**INFORMATION**', options=['**ABOUT**','**DATA**','**ML MODEL**','**PREDICTION FORM**', '**CONCLUSION**'], index=0)
with center:
    if visual == '**ABOUT**':
        st.header("INTRO FOR OUR PRESENTATION")
    if visual == '**DATA**':
        st.header("DATASET FOR PRESENTATION GOES HERE")
    if visual == '**ML MODEL**':
        st.header("ML MODEL CODE FOR PRESENTATION GOES HERE")
    if visual == '**PREDICTION FORM**':
        st.markdown("<h2 style='text-align:center'>MEDICAL INSURANCE PREDICTING FORM</h2>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align:center'>Please answer the following questions to get your medical insurance prediction: </h3>", unsafe_allow_html=True)

        st.markdown("<h4>How old are you?</h4>", unsafe_allow_html=True)
        age = st.text_input(label="age", label_visibility="collapsed",placeholder="Please enter your age")
        if re.search('[a-zA-Z]', age):
            st.error('ERROR: Enter numerical value!', icon="🚨")
        elif '.' in age:
            st.error('ERROR: Enter whole number!', icon="🚨")

        st.markdown("<h4>What is your gender?</h4>", unsafe_allow_html=True)
        gender = st.radio(label='gender', label_visibility="collapsed", options=['**female**', '**male**'], index=None)

        st.markdown("<h4>What is your BMI (Body Mass Index)?</h4>", unsafe_allow_html=True)
        bmi = st.text_input(label="bmi", label_visibility="collapsed",placeholder="Please enter your BMI")
        if re.search('[a-zA-Z]', bmi):
            st.error('ERROR: Enter numerical value!', icon="🚨")

        st.markdown("<h4>How many children do you have?</h4>", unsafe_allow_html=True)
        children = st.text_input(label="children", label_visibility="collapsed",placeholder="Please enter the number of children you have")
        if re.search('[a-zA-Z]', children):
            st.error('ERROR: Enter numerical value!', icon="🚨")
        elif '.' in children:
            st.error('ERROR: Enter whole number!', icon="🚨")

        st.markdown("<h4>Do you smoke?</h4>", unsafe_allow_html=True)
        smoker = st.radio(label='smoker', label_visibility="collapsed", options=['**yes**', '**no**'], index=None)

        st.markdown("<h4>Which US region do you live in?</h4>", unsafe_allow_html=True)
        region = st.radio(label='region', label_visibility="collapsed", options=['**northeast**', '**northwest**', '**southeast**', '**southwest**'], index=None)

        output_cost = st.button("PREDICT COST", type="primary")
        if output_cost and (age == '' or gender == None or bmi == '' or children == '' or smoker == None or region == None):
            st.error('ERROR: Please answer all the above fields to get your medical insurance prediction!', icon="🚨")
        predict = []
        if age != '' and gender != None and bmi != '' and children != '' and smoker != None and region != None:
            predict.extend([int(age), str(gender).replace('*', ''), float(bmi), int(children), str(smoker).replace('*', ''), str(region).replace('*', '')])
            if output_cost:
                cost = 1000
                st.markdown(f"<h1>Your Medical Insurance Prediction: ${cost}</h1>", unsafe_allow_html=True)

with right:
    st.write("")
        