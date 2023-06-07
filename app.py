import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from app_home import run_app_home
from app_eda import run_app_eda
from app_ml import run_app_ml
from streamlit_option_menu import option_menu

def main():


    st.title('KLPGA 상금 예측 앱')

    menu = ['홈', '탐색적 데이터분석', '머신러닝']

    with st.sidebar:
        choice = option_menu("메뉴", menu, 
            icons=['house', 'graph-up-arrow','file-bar-graph'], menu_icon="cast", default_index=0)
        

    if choice == menu[0]:
        run_app_home()
    elif choice == menu[1]:
        run_app_eda()
    else:
        run_app_ml()

    




if __name__=='__main__':
    main()