import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib




def main():
    menu = ['홈','데이터분석','인공지능']

    choice = st.sidebar.selectbox('메뉴',menu)
    
    if choice == '홈' :
        st.subheader('직원 퇴사 예측')

    elif choice == '데이터분석':
        pass

    elif choice == '인공지능' :
        pass




if __name__ == '__main__' :
    main()