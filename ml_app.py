import streamlit as st
import numpy as np
import pandas as pd

import joblib

def run_ml_app():
    classifier = joblib.load('data/best_model.pkl')
    scaler_X = joblib.load('data/scaler_X.pkl')

    st.subheader('데이터를 입력하면 퇴사를 예측')

    
# PaymentTier	Age	Gender	EverBenched	ExperienceInCurrentDomain,Education_Bachelors,Education_Masters	Education_PHD
# 월급: 1: 최고 2: 중간 수준 3: 최저
    paymenttier = st.number_input('PaymentTier', min_value=1,max_value=3)
    age = st.number_input('나이', min_value=0)
    
    gender = st.number_input('Gender',min_value=0)
    
    everbenched = st.number_input('EverBenched', min_value=0)

    experienceincurrentdomain = st.number_input('ExperienceInCurrentDomain', min_value=0)    

    education_bachelors = st.number_input('Education_Bachelors', min_value=0 )

    education_masters = st.number_input('Education_Masters', min_value=0 )

    education_phd = st.number_input('Education_PHD', min_value=0 )


    if st.button('결과 보기') :
        new_data = np.array([paymenttier,age,gender,
                    everbenched,experienceincurrentdomain,education_masters,education_masters,
                    education_phd])

        new_data = new_data.reshape(1, 8)

        new_data = scaler_X.transform(new_data)

        y_pred = classifier.predict(new_data)

        print(y_pred[0])
        if y_pred[0] == 1 :
            st.write('당신은, 퇴사할 것 입니다.')
        else :
            st.write('당신은, 퇴사 안 합니다.')
