import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
import pickle

st.set_page_config(
    page_title="Decision making about the model to be deployed to production",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.set_option('deprecation.showPyplotGlobalUse', False)

st.markdown(
    """
    <style>
        .css-hby737, .css-17eq0hr, .css-qbe2hs {
            background-color:    #154360    !important;
            color: black !important;
        }
        div[role="radiogroup"] {
            color:black !important;
            margin-left:8%;
        }
        div[data-baseweb="select"] > div {
            
            color: black;
        }
        div[data-baseweb="base-input"] > div {
            background-color: #aab7b8 !important;
            color: black;
        }
        
        .st-cb, .st-bq, .st-aj, .st-c0{
            color: black !important;
        }
        .st-bs, .st-ez, .st-eq, .st-ep, .st-bd, .st-e2, .st-ea, .st-g9, .st-g8, .st-dh, .st-c0 {
            color: black !important;
        }
        .st-fg, .st-fi {
            background-color: #c6703b !important;
            color: black !important;
        }
        
        .st-g0 {
            border-bottom-color: #c6703b !important;
        }
        .st-fz {
            border-top-color: #c6703b !important;
        }
        .st-fy {
            border-right-color: #c6703b !important;
        }
        .st-fx {
            border-left-color: #c6703b !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)


st.sidebar.markdown('<h1 style="margin-left:8%; color:#FA8072">Machine Learning Model Selection</h1>', unsafe_allow_html=True)

add_selectbox = st.sidebar.radio(
    "",
    ("About", "Model selection")
)

if add_selectbox == 'About':
    
    st.subheader('ABOUT THE PROJECT')
    st.markdown('Here are some important considerations while choosing an algorithm.',unsafe_allow_html=True)
    st.markdown('1. Accuracy and/or Interpretability of the Output \n 2. Speed of output or Training Time \n 4. Linearity \n 5. Number of Features',unsafe_allow_html=True)
    st.markdown('In this tool we use size of training data, Accuracy and Speed of output to select the algorithm to deploy',unsafe_allow_html=True)
    
elif add_selectbox == 'Model selection':
	
      st.subheader('MODEL SELECTION')
      name1 = st.text_input("Name of first model:")
      accuracy1 = st.number_input("Enter the accuracy of first model:", min_value=0.00, max_value=100.00, step=0.001)
      latency1 = st.number_input("Enter the latency in ms of first model", min_value=0.00, max_value=50.00, step=0.001)
      name2 = st.text_input("Name of second model:")
      accuracy2 = st.number_input("Enter the accuracy of second model:", min_value=0.00, max_value=100.00, step=0.001)
      latency2 = st.number_input("Enter the latency in ms of second model", min_value=0.00, max_value=30.00, step=0.001)
      submit = st.button('Predict')

      if submit:
            score1 = 1.2*0.01*accuracy1 - 0.6*0.02*latency1
            score2 = 1.2*0.01*accuracy2 - 0.6*0.02*latency2
            st.write('Score 1 ',score1)
            st.write('Score 2 ',score2)
            if score1>=score2:
                prediction = name1
            else:
                prediction = name2
            st.write('Hi, ','The best model is ',prediction)

