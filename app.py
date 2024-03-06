import pandas as pd
import streamlit as st


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
    st.markdown("<h1 style='text-align:center;color:#29FFC6'>MEDICAL INSURANCE PREDICTIONS</h1>", unsafe_allow_html=True)
with right:
    #filler *DELETE*
    st.header("IMAGE")
    #add image

left,right = st.columns([1, 5])
with left:
    visual = st.radio('**INFORMATION**', options=['**ABOUT**','**DATA**','**ML MODEL**','**CHATBOT**'], index=0)
with right:
    if visual == '**ABOUT**':
        st.header("INTRO FOR OUR PRESENTATION")
    if visual == '**DATA**':
        st.header("DATASET FOR PRESENTATION GOES HERE")
    if visual == '**ML MODEL**':
        st.header("ML MODEL CODE FOR PRESENTATION GOES HERE")
    if visual == '**CHATBOT**':
        st.header("CHATBOT FOR PRESENTATION GOES HERE")