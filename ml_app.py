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
    paymenttier = st.selectbox('지불계층',('최고','중간','최저'))
    if paymenttier == '최고':
        paymenttier = 1
    elif paymenttier == '중간':
        paymenttier = 2
    elif paymenttier == '최저':
        paymenttier = 3

    # paymenttier = st.number_input('PaymentTier', min_value=1,max_value=3)

    age = st.number_input('나이 ( 22 ~ 41 )', min_value=22, max_value=41)
    
    # gender = st.number_input('성별',min_value=0)
    gender = st.selectbox('성별',('여자','남자'))
    if gender == '여자':
        gender = 0
    elif gender == '남자':
        gender = 1
    # 1개월 이상 프로젝트에 참여하지 않음
    everbenched = st.selectbox('1 개월 이상 프로젝트에 참여하지 않음',('그렇다','그렇지않다'))
    if everbenched == '그렇다':
        everbenched = 1
    elif everbenched == '그렇지않다':
        everbenched = 0
    # everbenched = st.number_input('1개월 이상 프로젝트에 참여하지 않음', min_value=0)

    experienceincurrentdomain = st.number_input('경력 년차( 0 ~7 )', min_value=0, max_value=7)    

    education = st.selectbox('학력',('학사','석사','기타'))
    if education == '학사':
        education_bachelors = 1 
        education_masters = 0
        education_phd = 0

    elif education == '석사':
        education_masters = 1
        education_bachelors = 0
        education_phd = 0
        
    elif education == '기타':
        education_phd = 1
        education_bachelors = 0
        education_masters = 0

   

    if st.button('결과 보기') :
        new_data = np.array([paymenttier,age,gender,
                    everbenched,experienceincurrentdomain,education_bachelors,education_masters,
                    education_phd])

        new_data = new_data.reshape(1, 8)

        new_data = scaler_X.transform(new_data)

        y_pred = classifier.predict(new_data)

        print(y_pred[0])
        if y_pred[0] == 1 :
            st.write('당신은 퇴사할 것입니다.')
        else :
            st.write('당신은 퇴사 안 합니다.')
