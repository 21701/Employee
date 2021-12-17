import streamlit as st
import numpy as np
import pandas as pd

import joblib

def run_ml_app():
    classifier = joblib.load('data/best_modelX.pkl')
    scaler_X = joblib.load('data/scaler_XX.pkl')

    st.subheader('데이터를 입력하면 퇴사를 예측')

    
# PaymentTier	Age	Gender	EverBenched	ExperienceInCurrentDomain	Education_Masters	Education_PHD
# 월급: 1: 최고 2: 중간 수준 3: 최저
    PaymentTier = st.number_input('급여(1: 최고 2: 중간 수준 3: 최저)', min_value=1,max_value=3)
    Age = st.number_input('나이', min_value=0)
    menu = ['여자','남자']
    Gender = st.sidebar.selectbox('성별',menu)
    if Gender == '여자':
        return 0
    print(Gender)
    # skinthickness = st.number_input('SkinThickness', min_value=0)
    # insulin = st.number_input('Insulin', min_value=0)    
    # bmi = st.number_input('BMI', min_value=0.0, format='%.1f')
    # diabetesPedigreeFunction = st.number_input('DiabetesPedigreeFunction', min_value=0.0, format='%.2f')
    # age = st.number_input('AGE',min_value=0)

    # if st.button('결과 보기') :
    #     new_data = np.array([pregnancies,glucose,pressure,
    #                 skinthickness,insulin,bmi,
    #                 diabetesPedigreeFunction, age ])

    #     new_data = new_data.reshape(1, 8)

    #     new_data = scaler_X.transform(new_data)

    #     y_pred = classifier.predict(new_data)

    #     print(y_pred[0])
    #     if y_pred[0] == 0 :
    #         st.write('예측 결과는, 당뇨병이 아닙니다.')
    #     else :
    #         st.write('예측 결과는, 당뇨병입니다.')
