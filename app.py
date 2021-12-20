import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from eda_app import run_eda_app
from ml_app import run_ml_app
from PIL import Image





def main():
    menu = ['홈','데이터분석','인공지능']

    choice = st.sidebar.selectbox('메뉴',menu)
    
    if choice == '홈' :
        st.title('직원의 정보를 입력하면 퇴사를 예측')
        st.image('https://blog.kakaocdn.net/dn/m14u3/btq0dohqHsv/RgkaxYBBXp7cQsDw1bsug1/img.jpg',use_column_width=True)

    elif choice == '데이터분석':
        run_eda_app()

    elif choice == '인공지능' :
        run_ml_app()
        
        
        
        





if __name__ == '__main__' :
    main()
