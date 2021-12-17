import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda_app():
    st.subheader('데이터분석')

    df = pd.read_csv('data/Employee.csv')

    st.dataframe(df)

    st.subheader('Nan 데이터 확인')

    st.dataframe( df.isna().sum())

    st.subheader('각 컬럼별 히스토그램 확인')

    selected_column = st.selectbox('컬럼을 선택하세요', df.columns)

    bins = st.slider('bin의 갯수 조절', min_value=10, max_value=50)

    fig1 = plt.figure()
    df[selected_column].hist(bins= bins)
    st.pyplot(fig1)

    st.subheader('각 컬럼별 통계치')
    st.dataframe(df.describe())
